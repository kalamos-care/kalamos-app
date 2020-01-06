# Kalamos Care

## Basic Usage
1. Run **`make build`** inside root directory.
2. Then run **`make up`** to start up the project for first time.
3. In a new terminal window, run **`make adminuser`** and enter information in the prompt to create the first super user.
4. Open your browser to <a href="http://0.0.0.0:8000">http://0.0.0.0:8000/admin</a> and log in with your new credentials to begin managing the app.

## Commands
1. `make up` to build the project and starting containers.
2. `make build` to build the project.
3. `make start` to start containers if project has been up already.
4. `make stop` to stop containers.
5. `make shell-web` to shell access web container.
6. `make shell-db` to shell access db container.
7. `make shell-nginx` to shell access nginx container.
8. `make logs-web` to log access web container.
9. `make logs-db` to log access db container.
10. `make logs-nginx` to log access nginx container.
11. `make collectstatic` to put static files in static directory.
12. `make log-web` to log access web container.
13. `make log-db` to log access db container.
14. `make log-nginx` to log access nginx container.
15. `make restart` to restart containers.
16. `make adminuser` to create a new admin super user.
