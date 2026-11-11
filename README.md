# Ultimate FastAPI Recipe App

A recipe web application and REST API built with FastAPI. It uses SQLAlchemy to store recipes and users in SQLite, Alembic to manage database migrations, and Jinja templates to render a recipe page.

This project is a learning project based on [The Ultimate FastAPI Tutorial, Part 7: Database Setup with SQLAlchemy and Alembic](https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-7-sqlalchemy-database-setup/).

## Features

- FastAPI REST API for recipe data
- Request and response validation with Pydantic
- SQLAlchemy models and CRUD utilities
- SQLite database persistence
- Alembic database migrations
- Initial database data
- Jinja-templated recipe page
- Uvicorn development server with automatic reload

## Tech stack

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- Alembic
- Pydantic
- SQLite
- Jinja2
- Tailwind CSS

## Project structure

```text
.
├── alembic/                 # Alembic configuration and migration versions
├── alembic.ini
├── app/
│   ├── crud/                # Database CRUD operations
│   ├── db/                  # SQLAlchemy base, session, and database setup
│   ├── models/              # SQLAlchemy ORM models
│   ├── schemas/             # Pydantic request and response schemas
│   ├── templates/           # Jinja2 HTML templates
│   ├── backend_pre_start.py # Database connectivity check
│   ├── initial_data.py      # Initial database data setup
│   └── main.py              # FastAPI application and routes
├── prestart.sh              # Database startup and migration script, if present
├── run.sh                   # Development server script
└── requirements.txt         # Python dependencies
```

## Requirements

- Python 3.10 or newer
- `pip`
- Git

## Set up locally

Clone the repository and enter its root directory:

```bash
git clone <https://github.com/udhayanagaraj/ultimate-fastapi-tutorial-examples>
cd <ultimate-fastapi-tutorial-examples>
```

Create and activate a virtual environment:

```bash
python3 -m venv app/venv
source app/venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r app/requirements.txt
```

If your `requirements.txt` is in the project root instead, use:

```bash
pip install -r requirements.txt
```

## Database setup

The project uses SQLite. The configured database URL is:

```text
sqlite:///example.db
```

Run the startup script from the project root to check the database, apply existing migrations, and initialize data:

```bash
bash prestart.sh
```

If your project does not have `prestart.sh`, run the steps individually:

```bash
python -m app.backend_pre_start
python -m alembic upgrade head
python -m app.initial_data
```

Alembic applies migration files already present in `alembic/versions/`. When you change a database model, generate a migration, review it, and then apply it:

```bash
python -m alembic revision --autogenerate -m "describe your database change"
python -m alembic upgrade head
```

Commit migration files to Git so other developers and deployments can apply the same database changes.

## Run the application

From the project root, with the virtual environment activated:

```bash
bash run.sh
```

The development server should be available at:

- Web page: <http://127.0.0.1:8001>
- Interactive API documentation: <http://127.0.0.1:8001/docs>
- Alternative API documentation: <http://127.0.0.1:8001/redoc>

To start the server directly instead:

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
```

`--reload` restarts the development server when Python files change. It is intended for development.

## API

The application provides recipe endpoints for working with recipe data. Open the interactive API documentation at <http://127.0.0.1:8001/docs> to see the routes, required request fields, and response formats available in your version.

Examples discussed in the project:

- `GET /recipe/{recipe_id}` — retrieve a recipe by ID
- `POST /recipe/` — create a recipe

A recipe includes fields such as `label`, `source`, and `url`. The create request may also require `submitter_id`, depending on the current schema.

## Database models

The project uses SQLAlchemy models for database tables and Pydantic schemas for validating API input and output.

- `Recipe` stores recipe information and may reference a submitting user.
- `User` stores user information and can be related to submitted recipes.
- Alembic migrations track changes to the database schema.

## Development notes

- Run commands from the project root so Python can import the `app` package and the SQLite database is created in the expected location.
- Keep the virtual environment active when installing dependencies or running the app.
- If a database check uses raw SQL with SQLAlchemy 2, wrap the statement with `text()`:

  ```python
  from sqlalchemy import text

  db.execute(text("SELECT 1"))
  ```

- Don’t generate a new Alembic migration every time the app starts. Generate migrations when models change, review them, and apply them with `upgrade head`.
- Avoid committing your virtual environment, local database, or secrets. Add them to `.gitignore`.

## License

Add a license before distributing or reusing this project. For example, you can choose the MIT License and include its text in a `LICENSE` file.
