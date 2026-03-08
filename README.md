# Schema Matching Demonstrator

### Overview

This repository contains an educational demonstrator application for a schema matching approach developed
at [ScaDS.AI Leipzig/Dresden](https://scads.ai/).

It provides a full-stack web application that offers a short interactive introduction
to [schema matching](https://en.wikipedia.org/wiki/Schema_matching) and allows users to experiment with automated schema
matching between heterogeneous data schemas.

### Included Demonstrator Content

The frontend includes several interactive and explanatory elements, such as:

- introductory explanations of schema matching
- visual diagrams illustrating preprocessing and matching workflows
- interactive demonstrations of preprocessing and matching techniques
- puzzle- and game-like UI components for illustrating matching concepts
- example data schemas used throughout the demonstrator

Note: The original research prototype for schema matching is not included in this public repository.
This version only contains the demonstrator interface and example data used for the interactive tutorial.

---

### Architecture & Infrastructure

The system follows a client–server architecture.

- Frontend framework: **Vue.js with Quasar**
- Backend Framework: **Flask**
- **Docker / Docker Compose** for containerized execution
- Separate configurations for **production** and **development**

Many of the interactive visualizations rely on the great
[VueFlow](https://github.com/bcakmakoglu/vue-flow) library.

---

### Repository Structure

```text
schema-matching-demo/
├── server/                  # Flask backend and demo data generation
│   ├── app.py               # Backend entry point
│   ├── data_gen/            # Demo data generation and preprocessing logic
│   ├── utils/               # Backend utility functions
│   ├── env.yaml             # Conda environment definition
│   └── pyproject.toml       # Python project metadata
│
├── webapp/                  # Quasar/Vue frontend
│   ├── src/
│   │   ├── pages/           # Main application pages
│   │   ├── components/      # Reusable UI components
│   │   ├── layouts/         # Application layouts
│   │   ├── router/          # Frontend routing
│   │   └── assets/          # Images and visual assets for the demonstrator
│   └── nginx/               # Nginx configuration for containerized deployment
│
├── docker-compose.yml       # Production setup
├── docker-compose.dev.yml   # Development setup
├── LICENSE
└── README.md
```

---

### Prerequisites

#### For Docker-based execution

- Docker
- Docker Compose

#### For manual development setup

- Python (via Conda)
- Miniconda
- Node.js 20
- npm
- Java 11
- Quasar CLI

---

### Quick Start (Docker)

Install:

- https://docs.docker.com/engine/install/
- https://docs.docker.com/compose/install/

Move to the project directory:

```bash
cd .../schema-matching
```

---

#### Run production mode

```bash
docker compose up
```

The application runs on:

```bash
http://localhost:6060/
```

---

#### Run development mode

```bash
docker compose -f docker-compose.dev.yml up
```

Services:

Frontend

```bash
http://localhost:9000/
```

Backend

```bash
http://localhost:5000/
```

### Additional commands

```bash
# Start in background
docker compose -f docker-compose.dev.yml up -d

# Start with rebuild
docker compose -f docker-compose.dev.yml up --build

#Stop containers
docker compose -f docker-compose.dev.yml down

# Remove all containers
docker rm -fv $(docker ps -aq)
```

---

### Manual Development Setup

#### System update

```bash
sudo apt update
```

---

### Backend (Flask)

#### Create Conda environment

Install Miniconda:

https://docs.anaconda.com/miniconda/

```bash
cd .../schema-matching/server

conda env create -f env.yml
conda activate smd-env
```

---

#### Install Java 11 (required)

Check installation:

```bash
java -version
```

Install if necessary:

```bash
sudo apt install openjdk-11-jre
```

Verify installation:

```bash
java -version
```

---

#### Start Flask server

```bash
flask run --port=5000 --debug
```

Backend endpoint:

```bash
Backend endpoint:
```

---

### Frontend (Vue / Quasar)

#### Install Node.js 20

```bash
cd .../schema-matching/webapp/

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh
 | bash
nvm install 20

node -v
npm -v
```

---

#### Install dependencies

Install Quasar CLI:

```bash
npm install -g @quasar/cli
```

Install project dependencies:

```bash
npm install
```

---

#### Start development server

```bash
quasar dev
```

Frontend endpoint:

```bash
Frontend endpoint:
```

---

### Configuration

Container configuration is managed through Docker Compose and the corresponding Dockerfiles.

- `docker-compose.yml` – production setup
- `docker-compose.dev.yml` – development setup

The container images are defined in the following Dockerfiles:

- `server/Dockerfile_prod` – backend production image
- `server/Dockerfile_dev` – backend development image
- `webapp/Dockerfile` – frontend image


---

## License
BSD 3-Clause License
