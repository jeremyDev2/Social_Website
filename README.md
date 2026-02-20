# Social Website (test project)
Test Django project for practicing authentication, social login, and image bookmarking.
## Features
- User registration, login/logout, password reset, and profile editing
- Google OAuth2 social authentication
- Image bookmarking with previews and thumbnails
- Likes and user following
- Activity feed based on user actions
- Image ranking using Redis
## Tech stack
- Django
- Redis (ranking)
- social-auth-app-django (Google OAuth2)
- easy-thumbnails + Pillow
## Setup
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
3. Create a `.env` file with OAuth keys:
   ```env
   GOOGLE_OAUTH2_KEY=your_key
   GOOGLE_OAUTH2_SECRET=your_secret
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the server:
   ```bash
   python manage.py runserver
   ```
## Redis
Image ranking uses Redis. Make sure Redis is running locally:
```bash
redis-server
```
## Notes
- Media files are stored under `media/`.
- Social auth URLs are under `/social-auth/`.
