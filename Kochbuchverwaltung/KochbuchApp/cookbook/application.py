
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.exceptions import ExceptionMiddleware

from cookbook.config import ISDEBUG
from cookbook.endpoints import app_endpoints
from cookbook.httpexceptions import exception_handlers

APPLICATION = Starlette(debug=ISDEBUG, routes=app_endpoints)
APPLICATION.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])
APPLICATION.add_middleware(ExceptionMiddleware, handlers=exception_handlers)
