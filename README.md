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
