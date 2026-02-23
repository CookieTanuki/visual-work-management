# Visual Work Management

A modern, fast, and responsive work management platform designed to be a lightweight, open-source alternative to tools like Monday.com or Asana. Built specifically for simplicity, performance, and real-time feel using Server-Side Rendering augmented with HTMX.

![Project Status](https://img.shields.io/badge/Status-Ready%20to%20use-blue)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Django](https://img.shields.io/badge/Django-6.x%2B-green.svg)

## 📌 Project Overview
**Visual Work Management** allows teams to efficiently organize their workflow. It provides intuitive Kanban-style task boards, project grouping, and team coordination.
The core goal is to deliver an extremely fast and reactive user experience while keeping the JavaScript payload functionally at zero, handled primarily by Django and HTMX.

**Link to deployed webservice:** https://visual-work-management.onrender.com/
*(Test credentials - Login: `admin`, Password: `1qazcde3`)*

## 🚀 Key Features
- **Task Management**: Create, view, update, and manage the statuses of tasks.
- **Project Structure**: Group tasks naturally into broader "Projects".
- **Team Management**: Create teams and seamlessly assign workers to them.
- **Dynamic UI**: Tasks visually move between status columns instantly without page reloads (via HTMX).
- **Simple Interface**: Modern styling built rapidly using TailwindCSS styling primitives.

## 🛠️ Tech Stack
- **Backend Framework**: Python (Django)
- **Frontend / Reactivity**: HTMX
- **Styling**: Tailwind CSS (via CDN)
- **Database**: SQLite (Development) / PostgreSQL (Production ready)

## 📦 Project Structure
```text
visual-work-management/
├── core/                   # Main Django application logic
│   ├── forms.py            # ModelForms including Task, Project, Team & User Registration
│   ├── models.py           # Database Schema definitions
│   ├── urls.py             # Route definitions mapped to views
│   └── views.py            # Handle HttpRequests & return server-rendered HTML
├── templates/              # Directory for all HTML files
│   ├── base.html           # Main structural DOM wrapper and navigation
│   ├── projects/           # Templates specific to project viewing/creation
│   ├── registration/       # Templates for login and user registration
│   ├── tasks/              # Main Task board, row logic, and HTMX partials
│   └── teams/              # Templates specific to team managing
├── visual-work-management/ # Top-level Django project settings/urls
└── manage.py               # Django development utility script
```

## 🗄️ Database Structure (Schema)
The core database models powering the platform:

- **Worker (Custom User)**: Inherits from Django's `AbstractUser`. Includes a ForeignKey to `Position`.
- **Position**: Stores distinct job titles (e.g., "Developer", "Manager").
- **Team**: Represents a working group of multiple 'Workers'.
- **Project**: High-level goal. Linked directly to a `Team`.
- **TaskType**: Classification category (e.g., "Bug", "Feature").
- **Tag**: Color-coded label mapped dynamically to Tasks.
- **Task**: The primary moving structure. Contains:
  - Inherits descriptions, dates, and strict deadlines.
  - State tracking via `Status` (To Do, In Progress, Stuck, Done) and `Priority`.
  - Links securely to its `creator`, multiple `assignees`, its parent `project`, and related `tags`.

## 💻 Local Start of the Project

Follow these instructions to quickly boot the project on your local machine:

1. **Clone the repository**
   ```bash
   git clone <repository_url>
   cd visual-work-management
   ```

2. **Set up a Virtual Environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On MacOS/Linux
   # or .venv\Scripts\activate on Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables (.env)**
   Create a `.env` file in the root directory mirroring the configuration below with your local or production database credentials and an appropriate Django Secret Key:
   ```env
   # Database Configuration
   POSTGRES_DB=<db_name>
   POSTGRES_DB_PORT=<db_port>
   POSTGRES_USER=<db_user>
   POSTGRES_PASSWORD=<db_password>
   POSTGRES_HOST=<db_host>
   
   # Django Configuration
   SECRET_KEY=<your_secret_key>
   DJANGO_SETTINGS_MODULE=visual_work_management.settings.dev
   RENDER_EXTERNAL_HOSTNAME=<host_name>
   ```

5. **Initialize the Database**
   Apply Django's schema migrations down to your local SQLite file:
   ```bash
   python manage.py migrate
   ```

6. **Load Example Data (Optional)**
   If you wish to populate the database with initial testing data (users/positions/task types):
   ```bash
   python manage.py loaddata initial_data.json
   ```

7. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```
   Open `http://localhost:8000` in your browser. You can register an entirely new account via `/accounts/register` or create a superuser using `python manage.py createsuperuser` via the terminal.
