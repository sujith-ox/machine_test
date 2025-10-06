# Python Machine Test - Django REST API Project

The project includes:  
1. User registration with validation.  
2. REST API to manage users.  
3. Expense tracker with category-wise summary.

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/sujith-ox/machine_test.git
cd machine_test
````

### 2. Set up a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

* **PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

* **CMD:**

```cmd
venv\Scripts\activate.bat
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Server will run at `http://127.0.0.1:8000/`

---

## API Endpoints

### 1. User Registration

* **POST** `/register/`
* **Request Body:**

```json
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "pass1234"
}
```

* **Response:**

```json
{
    "id": 1,
    "username": "testuser",
    "email": "test@example.com"
}
```

> Password is not returned for security reasons.
> The API validates username (min 5 chars), email format, and password (min 8 chars, must include a number).

---

### 2. Users API

* **GET /users/** → List all users
* **GET /users/<id>/** → Get a user by ID
* **DELETE /users/<id>/** → Delete a user by ID

No authentication is implemented as it was not required for this test.

---

### 3. Expense Tracker

I created two models:

* `Category` (name)

* `Expense` (title, amount, category, date)

* **GET /expenses/summary/** → Returns total expenses grouped by category

* **Example Response:**

```json
{
    "Food": 1200,
    "Travel": 3000,
    "Entertainment": 800
}
```

I used Django ORM aggregation (`Sum`) to calculate totals.

---

## Git Workflow

* Initialized the repository locally: `git init`
* Added a `.gitignore` to exclude `venv/`, compiled files, and SQLite database
* Committed my changes: `git commit -m "Initial commit: Django REST API project"`
* Pushed to GitHub using HTTPS with a personal access token

---

## Notes

* I included a `requirements.txt` for dependencies.
* The project uses SQLite by default, but PostgreSQL can be used if needed.
* Virtual environment (`venv/`) is not included in the repo.
