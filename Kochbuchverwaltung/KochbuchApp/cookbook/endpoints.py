# REGISTERED ENDPOINTS
from starlette.routing import Route, Mount
from .api import recipe, ingredient


app_endpoints = [
    Mount('/api', routes=[
        recipe.include()
    ])
]
