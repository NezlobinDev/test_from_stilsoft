from pathlib import PurePath

import environ
from split_settings.tools import include

ENVFILE_PATH = PurePath.joinpath(PurePath(__file__).parent, '../../../.env')

env = environ.Env(
    DEBUG=(bool, False),
    DJANGO_ENV=(str, 'development'),
)
environ.Env.read_env(str(ENVFILE_PATH))

ENV = env.str('DJANGO_ENV')

include(
    'components/db.py',
    'components/installed_apps.py',
    'components/middlewares.py',
    'components/rest_framework.py',
    'components/settings.py',
)
