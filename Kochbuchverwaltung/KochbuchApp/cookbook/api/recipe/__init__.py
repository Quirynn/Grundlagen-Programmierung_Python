from starlette.routing import Mount, Route
from .views import *

def include():
    return Mount('/recipe', routes=[
        Route('/', views.recipe_list_handler, methods=['GET']),
        Route('/', views.recipe_create_handler, methods=['POST']),
        Route('/{recipeID:int}', views.recipe_read_handler, methods=['GET']),
        Route('/{recipeID:int}', views.recipe_update_handler, methods=['PUT']),
        Route('/{recipeID:int}', views.recipe_delete_handler, methods=['DELETE'])
    ])
