# Dockerized Python Flask App

A minimal, production-ready setup for containerizing a Flask application with Gunicorn.

## Features

-   **Multi-Stage Build**: Optimized image size using a builder pattern.
-   **Production Server**: Runs with Gunicorn instead of the dev server.
-   **Non-Root User**: Runs as a secure user for better security.

## Installation

1.  **Clone the repository**.
2.  **Build and Run**:
    ```bash
    docker build -t my-flask-app .
    docker run -p 5000:5000 my-flask-app
    ```

## Usage

Visit `http://localhost:5000` to see the "Hello World" message.

## Contact

Developed for Anunzio International by Anzul Aqeel.
Contact +971545822608 or +971585515742.

## License

MIT


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
