import shutil

from crudlfap.settings import autosettings, basedir

INSTALLED_APPS = [
    'person',
    'transport',
    'pmt',
    'mrs',
    'mrsrequest',
    'mrsattachment',

    'material',
    'webpack_loader' if shutil.which('npm') else 'webpack_mock',
    'crudlfap',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TEMPLATE_CONSTANTS = {
    'settings': dict(
        SITE_NAME='Mes remboursements simplifiés',
        SITE_TITLE='MRS',
    )
}

LANGUAGE_CODE = 'fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True

OPTIONAL_APPS = [
    {'dbdiff': {'after': 'crudlfap'}},
]

autosettings(globals(), basedir(__file__, '..', '..'))
