# django-ws-demo

## setup

backend
```sh
cd backend
# enter ur venv, then run the next command
pip install django celery channels[daphne] channels-redis celery[redis]
```

frontend
```sh
cd frontend
npm i -D
```

## starting

1. start redis (configured as `redis://localhost:6379`)

2. start django and celery
   - `cd backend/root && celery -A root worker -P solo` (solo for testing)
   - `cd backend/root && celery -A root beat`
   - `cd backend/root && python manage.py runserver`

3. start vite dev server
   - `cd frontend && npm run dev`

4. visit `http://localhost:5173`
