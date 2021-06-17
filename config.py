# coding = utf-8
import os

DEBUG = True

SECRET_KEY = os.urandom(24)
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# mysql配置
DIALECT = "mysql"
DRIVER = "pymysql"
USERNAME = "root"
PASSWORD = "Welcome_800jm"
HOST = "cd-cdb-jdvqs5zi.sql.tencentcdb.com"
# HOST="localhost"
PORT = "62054"
# PORT="3306"
AUTOCOMMIT=True
DATABASE = "new_shop"

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE,autocommit=AUTOCOMMIT)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# qq邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PROT = 25
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = "654510629@qq.com"
MAIL_DEFAULT_SENDER = "654510629@qq.com"
MAIL_PASSWORD = "adqaumondrphbaia"
MAIL_DEBUG = True

# redis配置
REDIS_HOST = "localhost"
REDIS_PORT = 6379

# 七牛云配置
ALLOWED_EXT = set(['png', 'jpg', 'jpeg', 'bmp', 'gif'])
QINIU_ACCESS_KEY = "sdUGq7V5JzVEIgVOkplMYwOSIiQ4BoDIEFFBaqL8"
QINIU_SECRET_KEY = "x5Jrnk457Umh5Yp6BT8KN0ivVHUEdWdGN4da6yVr"
QINIU_BUCKET_NAME = 'nexuswebsite'
QINIU_URL = "http://qusmjq524.hb-bkt.clouddn.com/"
