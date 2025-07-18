from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Rutas de media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configuración del dominio
BASE_DOMAIN = os.environ.get('BASE_DOMAIN', 'http://localhost:8000')  # Reemplaza con tu dominio de producción en Render

# Seguridad: Mantén la clave secreta en producción secreta
SECRET_KEY = os.environ.get('SECRET_KEY')

# No ejecutar con debug en producción
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Permitir solo tu dominio o el de Render
ALLOWED_HOSTS = ['localhost']

# Add RENDER_EXTERNAL_HOSTNAME (the .onrender.com domain)
render_external_hostname = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if render_external_hostname:
    ALLOWED_HOSTS.append(render_external_hostname)
else:
    # Fallback to your specific domain if RENDER_EXTERNAL_HOSTNAME is not available
    # (e.g. local environment or if something is unusual with Render's env vars)
    ALLOWED_HOSTS.append('desploy-7.onrender.com')

# Add BASE_DOMAIN (for custom domains), stripping any scheme
base_domain_env = os.environ.get('BASE_DOMAIN')
if base_domain_env:
    processed_base_domain = base_domain_env.replace('https://', '').replace('http://', '').split('/')[0]
    if processed_base_domain and processed_base_domain not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(processed_base_domain)

# Ensure uniqueness
ALLOWED_HOSTS = list(set(ALLOWED_HOSTS))

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'adminuser.apps.AdminuserConfig',
    'home.apps.HomeConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # Para plantillas globales
            os.path.join(BASE_DIR, 'home/templates'),  # Para plantillas de la app 'home'
            os.path.join(BASE_DIR, 'shop/templates'),  # Para plantillas de la app 'shop'
            os.path.join(BASE_DIR, 'cart/templates'),  # Para plantillas de la app 'cart'
            # Agregar más rutas si es necesario
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'

# Configuración de base de datos
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Directorios de archivos estáticos de las apps
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'home/static'),  # Static files de la app 'home'
    os.path.join(BASE_DIR, 'shop/static'),  # Static files de la app 'shop'
    # Agregar otras rutas de apps si es necesario
]

# Definir STATIC_ROOT en producción para almacenar los archivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Definir campo primario
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Rutas de media
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'china-prototipo/media')
MEDIA_URL = '/media/'

# Sesión del carrito
CART_SESSION_ID = 'cart'
