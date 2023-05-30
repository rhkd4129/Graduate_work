from .common import *

# DEBUG = os.environ.get("DEBUG") in ["1", "t", "true", "T", "True"]
DEBUG=False
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")
# CORS_ORIGIN_WHITELIST = os.environ.get("CORS_ORIGIN_WHITELIST", "").split(",")




# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {"console": {"level": "ERROR", "class": "logging.StreamHandler",},},
#     "loggers": {"django": {"handlers": ["console"], "level": "ERROR",},},
# }




STATICFILES_STORAGE = "graduation_work_site.storage.S3StaticStorage"
DEFAULT_FILE_STORAGE  = "graduation_work_site.storage.S3MediaStorage"



ALLOWED_HOSTS = ['.elasticbeanstalk.com','192.168.56.101','127.0.0.1']

import os
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME':os.environ['DATABASE_NAME'],
#         'USER':os.environ['DATABASE_USER'],
#         'PASSWORD':os.environ['DATABASE_PASSWORD'],
#         'HOST':'django-project.c41emichhaxf.ap-northeast-2.rds.amazonaws.com',
#         'PORT':'3306',
#         'OPTIONS':{
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",        
#             }
#     },

# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'',
        'USER':'',
        'PASSWORD':'',
        'HOST':'django-project.c41emichhaxf.ap-northeast-2.rds.amazonaws.com',
        'PORT':'3306',
        'OPTIONS':{
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",        
            }
    },

}


AWS_S3_REGION_NAME='ap-northeast-2'
AWS_STORAGE_BUCKET_NAME ='django-project-buckets'
# AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME)
AWS_DEFAULT_ACL = None