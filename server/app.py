import json
import os
from flask import Flask, request, session, jsonify
from flask_cors import CORS
from flask_session import Session
from werkzeug.middleware.proxy_fix import ProxyFix

from data_gen.data_generation_for_demo import (
    gen_matching_from_request,
    gen_data_from_request,
)
from utils.utils import delete_old_files

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

# enable CORS
CORS(app, resources={r"/*": {"origins": ["http://quasar-webapp","http://localhost:9000"]}}, supports_credentials=True)


# Session configuration
app.config["SECRET_KEY"] = os.urandom(24)  # Replace with a strong secret key
app.config["SESSION_TYPE"] = "filesystem"  # Store sessions in the filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_FILE_DIR"] = "./.flask_session/"  # Path to store session files
Session(app)

TEMP_DIR = "./temp_json_files"
os.makedirs(TEMP_DIR, exist_ok=True)


@app.before_request
def before_request():
    """Deletes generated temporary files older than one hour."""
    delete_old_files(TEMP_DIR, 3600)

@app.route("/generateData", methods=["GET"])
def send_data():
    """Responds to a GET request from the data generator.

    Returns:
    dict: containing the demanded schemas.
    """
    session_id = session.get("session_id")
    if not session_id:
        session["session_id"] = os.urandom(16).hex()
        session_id = session["session_id"]

    file_path = os.path.join(TEMP_DIR, f"schemas_{session_id}.json")

    option_choice = json.loads(request.args.get("options"))
    return gen_data_from_request(option_choice, file_path)


@app.route("/generateMatching", methods=["GET"])
def send_matching():
    """Responds to a GET request from the schema matching generator.

    Returns:
        array: containing the matching of the schemas which where generated before via /generateData route.
    """
    session_id = session.get("session_id")

    if not session_id:
        return jsonify({"error": "No session found"}), 403

    # Path to the session-specific JSON file
    file_path = os.path.join(TEMP_DIR, f"schemas_{session_id}.json")
    config_choice = request.args.get("config")
    return gen_matching_from_request(config_choice, file_path)


if __name__ == "__main__":
    app.run()
