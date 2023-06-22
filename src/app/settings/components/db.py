from app.settings import env

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DATABASE_NAME'),
        'USER': env.str('DATABASE_USER'),
        'PASSWORD': env.str('DATABASE_PASS'),
        'HOST': env.str('DATABASE_HOST'),
        'PORT': '5432',
    },
}
