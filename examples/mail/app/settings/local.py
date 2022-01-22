DEBUG = True
PLUGINS = ["fastack_mail"]

COMMANDS = []
EMAIL_BACKEND = "fastack_mail.backend.EmailBackend"
EMAIL_HOSTNAME = "localhost"
EMAIL_PORT = 8025
# EMAIL_USERNAME = None
# EMAIL_PASSWORD = None
# EMAIL_TIMEOUT = 60
# EMAIL_USE_TLS = False
# EMAIL_START_TLS = False
# EMAIL_VALIDATE_CERTS = True
# EMAIL_CLIENT_CERT = None
# EMAIL_CLIENT_KEY = None
# EMAIL_CERT_BUNDLE = None
EMAIL_ASYNC_MODE = True
DEFAULT_FROM_EMAIL = "Local <noreply@localhost>"
