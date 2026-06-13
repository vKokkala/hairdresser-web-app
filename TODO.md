# Production TODO

## Django
- [ ] Set `DEBUG=False`
- [ ] Set `SECRET_KEY` to a real random value
- [ ] Configure `ALLOWED_HOSTS` with your actual domain
- [ ] Set up HTTPS (SSL certificate via Let's Encrypt)
- [ ] Configure static file serving (whitenoise or CDN)
- [ ] Replace `runserver` with Gunicorn
- [ ] Run `python manage.py check --deploy` and fix all warnings

## Docker / Infrastructure
- [ ] Add Nginx as a reverse proxy in front of Gunicorn
- [ ] Add a health check to `depends_on` so `web` waits for Postgres to be ready
- [ ] Add `.env` to `.gitignore`
- [ ] Store secrets securely (not in a committed `.env`)
