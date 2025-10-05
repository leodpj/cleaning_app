import os
from pathlib import Path
from decouple import config, RepositoryEnv, Csv
from datetime import timedelta

# ================================
# 🔧 PATHS
# ================================
BASE_DIR = Path(__file__).resolve().parent.parent

# ================================
# 🔄 AMBIENTE (dev/prod)
# ================================
ENV = config('ENV', default='devopment')
#config = Config(repository=RepositoryEnv(BASE_DIR / ENV_FILE))

# ================================
# ⚙️ CONFIGURAÇÕES BÁSICAS
# ================================
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)
ENV = config("ENV", default="development")

if DEBUG:
    ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
else:
    ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="", cast=Csv())

# ================================
# 📦 APLICAÇÕES
# ================================
INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Terceiros
    "rest_framework",
    "corsheaders",

    # Apps do projeto
    "users",
    "clients",
    "services",
    "finance",
    "quotes",
    "communication",
]

AUTH_USER_MODEL = "users.User"

# ================================
# ⚙️ MIDDLEWARE
# ================================
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "cleaning_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "cleaning_app.wsgi.application"

# ================================
# 🗄️ BANCO DE DADOS
# ================================
DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", default="django.db.backends.mysql"),
        "NAME": config("DB_NAME", default="cleaning_app"),
        "USER": config("DB_USER", default="root"),
        "PASSWORD": config("DB_PASS", default=""),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", default="3306"),
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# ================================
# 🕒 TIMEZONE / LOCALIZAÇÃO
# ================================
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# ================================
# 🧾 STATIC / MEDIA FILES
# ================================
STATIC_URL = config("STATIC_URL", default="/static/")
MEDIA_URL = config("MEDIA_URL", default="/media/")
STATIC_ROOT = config("STATIC_ROOT", default=str(BASE_DIR / "staticfiles"))
MEDIA_ROOT = config("MEDIA_ROOT", default=str(BASE_DIR / "media"))

# ================================
# 🌐 CORS / CSRF
# ================================
CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", default="http://localhost:3000", cast=Csv())
CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", default="http://localhost:3000", cast=Csv())

# ================================
# 📧 E-MAIL
# ================================
EMAIL_BACKEND = config("EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")
EMAIL_HOST = config("EMAIL_HOST", default="localhost")
EMAIL_PORT = config("EMAIL_PORT", default=1025, cast=int)
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=False, cast=bool)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="Cleaning App <noreply@cleaningapp.local>")

# ================================
# 🔒 SEGURANÇA (modo produção)
# ================================
if not DEBUG:
    SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", default=True, cast=bool)
    SESSION_COOKIE_SECURE = config("SESSION_COOKIE_SECURE", default=True, cast=bool)
    CSRF_COOKIE_SECURE = config("CSRF_COOKIE_SECURE", default=True, cast=bool)
    SECURE_HSTS_SECONDS = config("SECURE_HSTS_SECONDS", default=31536000, cast=int)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = config("SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True, cast=bool)
    SECURE_HSTS_PRELOAD = config("SECURE_HSTS_PRELOAD", default=True, cast=bool)

# ================================
# ⚙️ DJANGO REST FRAMEWORK
# ================================
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),      # Token válido por 1h
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),         # Token de refresh válido por 7 dias
    "ROTATE_REFRESH_TOKENS": True,                       # Gera novo refresh a cada login
    "BLACKLIST_AFTER_ROTATION": True,                    # Invalida o refresh antigo
    "UPDATE_LAST_LOGIN": True,                           # Atualiza último login no modelo User

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,                           # usa a mesma SECRET_KEY do settings
    "AUTH_HEADER_TYPES": ("Bearer",),                    # formato do header: Authorization: Bearer <token>
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",

    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=60),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=7),
}

# ================================
# 📄 PADRÕES
# ================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ================================
# 🪵 LOGGING CONFIGURATION
# ================================
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_LEVEL = "DEBUG" if DEBUG else "INFO"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{asctime}] {levelname} {name} - {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "debug_file": {
            "class": "logging.FileHandler",
            "filename": LOG_DIR / "debug.log",
            "formatter": "verbose",
        },
        "error_file": {
            "class": "logging.FileHandler",
            "filename": LOG_DIR / "errors.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "debug_file"],
            "level": LOG_LEVEL,
        },
        "django.request": {
            "handlers": ["error_file"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.security": {
            "handlers": ["error_file"],
            "level": "ERROR",
            "propagate": False,
        },
        "cleaning_app": {
            "handlers": ["console", "debug_file"],
            "level": LOG_LEVEL,
            "propagate": True,
        },
    },
}

