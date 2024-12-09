# Fundamentals of Operating Systems - Module Assignment

## Task 1: Website Availability Checker

### Objective

Write a Bash script to check the availability of specific websites and log the results.

### Implementation

- **Website List**: Defined an array with URLs (`https://google.com`, `https://facebook.com`, `https://twitter.com`).
- **Availability Check**: Used the `curl` command to send HTTP GET requests and verified responses with status code 200.
- **Logging**: Results are saved in a file named `website_status.log` with a clear format (e.g., "https://google.com is UP").
- **Redirection Handling**: Configured `curl` to follow URL redirections.
- **Output Message**: Displayed a message confirming that results were logged.

### Outcome

The script successfully:

- Checked website availability.
- Logged results in `website_status.log`.
- Provided clear feedback after execution.

---

## Task 2: FastAPI Application in Docker

### Objective

Set up a FastAPI application in Docker, integrated with a PostgreSQL database.

### Implementation

- **Dockerfile**: Created to build the Docker image for the FastAPI application.
- **docker-compose.yaml**: Configured to deploy the FastAPI app and PostgreSQL as separate services.
- **Database Connection**: Updated `SQLALCHEMY_DATABASE_URL` to use the PostgreSQL service name from `docker-compose.yaml` for seamless connectivity.
- **Environment Setup**: Used `docker-compose up` to build and start the environment.

### Outcome

- Successfully deployed the FastAPI application in a Docker container.
- Verified database connectivity using the "Check DB" button in the FastAPI interface.
- Ensured full functionality of the application and database.
