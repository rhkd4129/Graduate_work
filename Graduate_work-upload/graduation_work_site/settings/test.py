from pathlib import Path
# from django.urls import reverse, reverse_lazy

import os
from os.path import abspath,dirname,join
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent



print(BASE_DIR)


STATIC_URL = '/static/'

# STATICFILES_DIRS = [ os.path.join(BASE_DIR,'graduation_work_site','static')]
STATIC_ROOT = os.path.join(BASE_DIR,'graduation_work_site','static')
print(STATIC_ROOT)


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
print(MEDIA_ROOT)