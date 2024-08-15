# Flask Logging App

## Instructions

### For local setup

1. Create a virtual environment

```bash
python3 -m venv .venv
sourece .venv/bin/activate
```

2. Run the application using gunicorn

```bash
gunicorn --workers 4 --bind 0.0.0.0:8000 app:app
```