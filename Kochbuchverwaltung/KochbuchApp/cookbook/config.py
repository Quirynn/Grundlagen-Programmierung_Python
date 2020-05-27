import sys

# APPLICATION CONFIGURATION:
from starlette.config import Config

config = Config(sys.argv[1])
HOST = config('APP_HOST', cast=str, default='127.0.0.1')
PORT = config('APP_PORT', cast=int, default=8080)
ISDEBUG = config('DEBUG', cast=bool, default=False)
LOG_LEVEL = config('LOG_LEVEL')
DATABASE_URL = config('DATABASE_URL')
DEFAULT_LOCALE = config('DEFAULT_LOCALE', cast=str, default='de_DE')

# SET LOCALE
import locale
locale.setlocale(locale.LC_ALL, DEFAULT_LOCALE)

# DATABASE INITIALIZATION
import pymysql
pymysql.install_as_MySQLdb()

from sqlalchemy.ext.declarative import declarative_base
ModelBaseObject = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session

dbengine = create_engine(DATABASE_URL)
dbsession = Session(bind=dbengine)
