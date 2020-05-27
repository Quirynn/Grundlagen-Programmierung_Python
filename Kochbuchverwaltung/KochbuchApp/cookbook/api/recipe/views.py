from .models import Recipe
from starlette.responses import JSONResponse


async def recipe_list_handler(request):
    return JSONResponse(dict(
        recipeList=Recipe.getRecipeList()
    ))


async def recipe_read_handler(request):
    recipeID = request.path_params['recipeID']
    recipe = Recipe.byRecipeID(recipeID)
    return JSONResponse(dict(
        recipeDetail=recipe.getData()
    ))


async def recipe_create_handler(request):
    recipeDetail = await request.json()
    return JSONResponse(dict(
        isCreate=Recipe.create(recipeDetail)
    ))


async def recipe_update_handler(request):
    isUpdate = False
    recipeID = request.path_params['recipeID']

    recipe = Recipe.byRecipeID(recipeID)
    if recipe:
        recipeDetail = await request.json()
        recipe.setData(recipeDetail)
        isUpdate=True

    return JSONResponse(dict(
        isUpdate=isUpdate
    ))


async def recipe_delete_handler(request):
    recipeID = request.path_params['recipeID']
    isDelete = False
    recipe = Recipe.byRecipeID(recipeID)
    if recipe:
        recipe.delete()
        isDelete = True

    return JSONResponse(dict(
        isDelete=isDelete
    ))
