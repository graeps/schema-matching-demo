# Demonstrator for Schema Matching approach in project AMPL

## Quick start

Install [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/).
Move to the project directory

```
cd .../schema-matching
```

#### Run production mode

```
docker compose up
```

The application runs on [http://localhost:6060/](http://localhost:80/).

#### Run development mode

```
docker compose -f docker-compose.dev.yml up
```

Frontend runs on [http://localhost:9000/](http://localhost:9000/).\
Backend runs on [http://localhost:5000/](http://localhost:5000/).

```
# Start in the background
docker compose -f docker-compose.dev.yml up -d
# Start with rebuild
docker compose -f docker-compose.dev.yml up --build
# Stop running container
docker compose down
# remove ALL containers (careful!)
docker rm -fv $(docker ps -aq)
```

---
___

## Start frontend and backend manually

```
sudo apt update
```

#### Start Flask backend server in dev mode

##### Create and activate conda environment

Install [Miniconda](https://docs.anaconda.com/miniconda/)

```
cd .../schema-matching/server
conda env create -f conda-env.yml
conda activate smd-env
```

##### Install Java11 if not installed already

```
java -version
sudo apt install openjdk-11-jre #if not installed
java -version #check if installation succesful
```

##### Run Flask server

```
flask run --port=5000 --debug
```

#### Run Quasar/vue frontend server in dev mode

##### Install Node.js 20

```
cd .../schema-matching/webapp/
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
nvm install 20
node -v
npm -v
```

##### Install Quasar-CLI and node dependencies

```
npm install-g @quasar/cli
npm install
```

##### Run the app in dev mode

```
quasar dev
```
