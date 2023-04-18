from .common import *

# DEBUG = os.environ.get("DEBUG") in ["1", "t", "true", "T", "True"]
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

# STATICFILES_STORAGE = "backend.storages.StaticAzureStorage"
# DEFAULT_FILE_STORAGE = "backend.storages.MediaAzureStorage"

# AZURE_ACCOUNT_NAME = os.environ["AZURE_ACCOUNT_NAME"]
# AZURE_ACCOUNT_KEY = os.environ["AZURE_ACCOUNT_KEY"]

# CORS_ORIGIN_WHITELIST = os.environ.get("CORS_ORIGIN_WHITELIST", "").split(",")

# # 절대 이렇게 소스코드에 키를 넣지 마세요.
# # 아래 키는 예제로 넣었으며, 동작하지 않는 키입니다.
# # AZURE_ACCOUNT_NAME = ""
# # AZURE_ACCOUNT_KEY = ""

# DATABASES = {
#     "default": {
#         "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.postgresql"),
#         "HOST": os.environ["DB_HOST"],
#         "USER": os.environ["DB_USER"],
#         "PASSWORD": os.environ["DB_PASSWORD"],
#         "NAME": os.environ.get("DB_NAME", "postgres"),
#     },
# }

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {"console": {"level": "ERROR", "class": "logging.StreamHandler",},},
#     "loggers": {"django": {"handlers": ["console"], "level": "ERROR",},},
# }



# AKIA3S4HJGLOEFYJD6AW
# uqjbQijxsLhJITEaZmmLwjtgQZ7yJmodx/tjJK/P




ALLOWED_HOSTS = ['.blasticbeanstalk.com','192.168.56.101','127.0.0.1']
# 

import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':os.environ['DATABASE_NAME'],
        'USER':os.environ['DATABASE_USER'],
        'PASSWORD':os.environ['DATABASE_PASSWORD'],
        'HOST':'django.c41emichhaxf.ap-northeast-2.rds.amazonaws.com',
        'PORT':'3306',
        'OPTIONS':{
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",        
            }
    },

}


