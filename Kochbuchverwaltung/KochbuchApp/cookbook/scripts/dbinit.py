import sys

from starlette.config import Config

from ..api.recipe.models import Recipe, sampledata_recipe
from ..api.ingredient.models import Ingredient, sampledata_ingredients

from sqlalchemy import create_engine
from cookbook.config import ModelBaseObject, Session

# Console-Script: Erstellung der Datenbanktabellen mit Beispieldaten

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: {} <config_uri>\n(example: "{} dev.env"'.format(cmd, cmd))
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2: usage(argv)

    DATABASE_URL = Config(argv[1]).get('DATABASE_URL')

    dbengine = create_engine(DATABASE_URL)
    ModelBaseObject.metadata.create_all(dbengine)

    dbsession = Session(bind=dbengine)

    # Internationalization:
    for recipe in sampledata_recipe:
        r = Recipe(
            title=recipe['title'],
            prepareTimeMinutes=recipe['prepareTimeMinutes'],
            prepareInstructions=recipe['prepareInstructions'])
        dbsession.add(r)
    
    for ingredient in sampledata_ingredients:
        i = Ingredient(
            recipeID=ingredient['recipeID'],
            title=ingredient['title'],
            amount=ingredient['amount'],
            amountUnit=ingredient['amountUnit'],
            calories=ingredient['calories'])
        dbsession.add(i)

    dbsession.commit()