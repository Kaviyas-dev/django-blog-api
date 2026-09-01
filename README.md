# Blog Project

A blog application built with Django, featuring user authentication, user profiles, post management, and a REST API built with Django REST Framework.

## Features

- **User authentication** — register, login, logout
- **User profiles** — profile image, phone, address, bio
- **Blog posts** — create, view, update, delete posts
- **REST API** — list/create and retrieve/update/delete posts via a JSON API, with ownership-based permissions (only the author can edit or delete their own post; anyone can read)

## Tech stack

- Python / Django
- Django REST Framework
- SQLite (development database)
- python-decouple (environment variable management)

## Project structure

```
blogproject/
├── blogapp/          # Core web app: posts, profiles, auth, templates
├── api/               # REST API app (DRF serializers, views, permissions)
├── blogproject/       # Project settings, URLs, WSGI/ASGI entry points
└── manage.py
```

## Setup

1. **Clone the repo and create a virtual environment**

   ```bash
   git clone <your-repo-url>
   cd blogproject
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Copy `.env.example` to `.env` and fill in your own values:

   ```bash
   cp .env.example .env
   ```

   Generate a secret key, for example:

   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for /admin access)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/`.

## Routes

| Path | Description |
|---|---|
| `/` | Post list (home) |
| `/post/<id>/` | Post detail |
| `/blogapp/add/` | Add a new post |
| `/blogapp/update/<id>/` | Update a post |
| `/blogapp/delete/<id>/` | Delete a post |
| `/login/`, `/register/`, `/logout/` | Authentication |
| `/profile/`, `/profile/edit/` | View and edit user profile |
| `/admin/` | Django admin |

## API Endpoints

| Method | Endpoint | Description | Auth required |
|---|---|---|---|
| GET | `/api/posts/` | List all posts | No |
| POST | `/api/posts/` | Create a new post | Yes |
| GET | `/api/posts/<id>/` | Retrieve a single post | No |
| PUT/PATCH | `/api/posts/<id>/` | Update a post | Yes (author only) |
| DELETE | `/api/posts/<id>/` | Delete a post | Yes (author only) |

## Notes

- `DEBUG` should always be `False` in production.
- The SQLite database and uploaded media files are not tracked in version control (see `.gitignore`); each environment should run its own migrations.

## License

MIT (or your preferred license)
