# mail

This is a super app

## Installation

Install ``pipenv``:

```
pip install pipenv
```

Install all dependencies:

```
pipenv install
```

## SMTP Server

Run local SMTP server

```
python -m smtpd -c DebuggingServer -d -n
```

## Development

For local development, all configurations must be saved in `app/settings/local.py`.

Run the development server:

```
uvicorn app.main:app --reload
```

## Production

For production, all configurations must be saved in `app/settings/production.py`.

Set ``APP_ENV`` environment to select configuration file:

```
export APP_ENV=production
```

Run the production server:

```
uvicorn app.main:app
```
