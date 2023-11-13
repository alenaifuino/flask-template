# Flask Application Template

This is a base template for Flask web applications. It provides a structured starting point for new projects, adhering to best practices in Flask development and project organization.

## Features

- Modular design using Blueprints.
- Error handling for HTTP status codes 400, 403, 404, and 500.
- Template rendering using Jinja2.
- Environment-based configuration via `.env` file.
- Basic file upload handling and static file serving.
- Pre-configured logging.

## Quick Start

1. Clone the repository.
2. Copy `.env.example` to `.env` and set your environment variables.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the application: `flask run`.

## Project Structure

- `app/`: Application package containing the Blueprints, static files, templates, and routes.
- `app/static/`: Directory for CSS, JavaScript, and image files.
- `app/templates/`: Jinja2 templates for the application.
- `app/main/`: Blueprint for the main application routes.
- `instance/`: Folder for instance-specific configurations (not under version control).
- `.flaskenv`: Flask-specific environment variables.
- `.env`: General environment variables (not to be committed).
- `application.py`: Entry point for the Flask application.

## Configuration

Configure the application using the `.env` file. Reference `.env.example` for required variables.

## Usage

To create a new project:

1. Clone this repository.
2. Rename the project folder.
3. Initialize a new git repository.
4. Customize the Blueprints and templates as needed.


## Contributing

Contributions to the template are welcome. Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

Special thanks to all the contributors and maintainers of Flask and its extensions.
