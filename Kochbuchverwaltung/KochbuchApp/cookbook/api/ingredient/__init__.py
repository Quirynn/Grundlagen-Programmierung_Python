# from starlette.routing import Mount, Route
# from .views import *

# def include():
#     return Mount('/ingredient', routes=[
#         Route('/', views.ingredient_list_handler, methods=['GET']),
#         Route('/', views.ingredient_create_handler, methods=['POST']),
#         Route('/{ingredientID:int}', views.ingredient_read_handler, methods=['GET']),
#         Route('/{ingredientID:int}', views.ingredient_update_handler, methods=['PUT']),
#         Route('/{ingredientID:int}', views.ingredient_delete_handler, methods=['DELETE'])
#     ])
