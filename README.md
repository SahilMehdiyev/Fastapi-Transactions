# FastAPI Transaction Project

This project is a **FastAPI**-based transaction management system. It leverages **SQLite** as the database, **SQLAlchemy** ORM for database interactions, **Celery** for asynchronous task processing, and **Alembic** for database migrations. The API provides CRUD operations for managing transactions and storing transaction data efficiently.

---

## 🚀 **Features**

- **CRUD API**: Create, Read, Update, and Delete operations for transactions.
- **SQLite Database**: Lightweight and easy-to-setup database.
- **Alembic Migrations**: Manage database schema with migrations.
- **Celery**: Asynchronous task processing for background operations.
- **Swagger UI**: Built-in API documentation for easy testing and exploration.

---

## 🛠️ **Setup and Run**

### Install Dependencies
Clone the repository and install dependencies using Poetry:

```bash
git clone <repository-url>
cd fastapi_transaction
poetry install

```


## 🧰 Makefile Commands

The project includes a Makefile for commonly used commands:

| Command                | Description                                           |
|------------------------|-------------------------------------------------------|
| `make run_server`      | Start the FastAPI server.                             |
| `make install`         | Install dependencies using Poetry.                    |
| `make run_migrations`  | Apply database migrations.                            |
| `make makemigrations`  | Generate new migration files with Alembic.            |
| `make run_celery_worker` | Start Celery worker process.                        |
| `make run_celery_beat`   | Start Celery beat process.                          |
| `make pre_commit_run`  | Run pre-commit checks.                                |
| `make test`            | Run tests using pytest.                               |
| `make lint`            | Check code with Flake8.                               |
| `make format`          | Format code with Black.                               |




📂 Project Structure
```bash
fastapi_transaction/
├── fastapi_transaction/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   ├── config.py
├── tests/
│   ├── __init__.py
│   ├── test_transactions.py
├── pyproject.toml
├── Makefile


```

🧪 Testing

Run tests using pytest:
```bash
make test


```



