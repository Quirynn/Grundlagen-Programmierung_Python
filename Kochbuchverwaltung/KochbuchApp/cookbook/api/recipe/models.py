
import datetime
from sqlalchemy import Column, BigInteger, String, Text, DateTime
from sqlalchemy.orm import relationship

from cookbook.config import ModelBaseObject, dbsession
from ..ingredient.models import Ingredient


class Recipe(ModelBaseObject):
    __tablename__ = 'recipe'

    # Attributes:
    recipeID = Column(BigInteger, primary_key=True)
    title = Column(String(120))
    prepareTimeMinutes = Column(BigInteger)
    prepareInstructions = Column(Text)

    # Relationships:
    ingredients = relationship('Ingredient', cascade='all, delete, delete-orphan',
                               primaryjoin='foreign(Ingredient.recipeID) == Recipe.recipeID')

    @classmethod
    def byRecipeID(cls, recipeID):
        return dbsession.query(Recipe).filter_by(recipeID=recipeID).first()

    @classmethod
    def create(cls, data):
        isCreate = False

        if 'recipeDetail' in data and \
            'title' in data.get('recipeDetail') and \
            'prepareTimeMinutes' in data.get('recipeDetail') and \
            'prepareInstructions' in data.get('recipeDetail'):
            r = Recipe(
                title=data.get('recipeDetail').get('title'),
                prepareTimeMinutes=data.get('recipeDetail').get('prepareTimeMinutes'),
                prepareInstructions=data.get('recipeDetail').get('prepareInstructions'))
            dbsession.add(r)
            dbsession.commit()

            if 'ingredients' in data:
                for ingredient in data.get('ingredients'):
                    i = Ingredient(
                        recipeID=r.recipeID,
                        title=ingredient.get('title'),
                        amount=ingredient.get('amount'),
                        amountUnit=ingredient.get('amountUnit'),
                        calories=ingredient.get('calories'))
                    dbsession.add(i)
                    dbsession.commit()
            isCreate = True
        return isCreate

    def delete(self):
        dbsession.delete(self)
        dbsession.commit()

    @classmethod
    def getRecipeList(cls):
        db_recipes = dbsession.query(Recipe).order_by(Recipe.recipeID)
        recipeList = list()
        for recipe in db_recipes:
            recipeList.append(recipe.getData())

        return recipeList

    def getData(self):
        ingredientList = list()
        for ingredient in self.ingredients:
            ingredientList.append(ingredient.getData())

        return dict(
            recipeID=self.recipeID,
            title=self.title,
            prepareTimeMinutes=self.prepareTimeMinutes,
            prepareInstructions=self.prepareInstructions,
            ingredients=ingredientList)

    def setData(self, data):
        if 'recipeDetail' in data:
            if 'title' in data.get('recipeDetail'):
                self.title = data.get('recipeDetail').get('title')
            if 'prepareTimeMinutes' in data.get('recipeDetail'):
                self.prepareTimeMinutes = data.get('recipeDetail').get('prepareTimeMinutes')
            if 'prepareInstructions' in data.get('recipeDetail'):
                self.prepareInstructions = data.get('recipeDetail').get('prepareInstructions')
            dbsession.commit()
        if 'ingredients' in data:
            for ingredient in self.ingredients:
                dbsession.delete(ingredient)
                dbsession.commit()
            for ingredient in data.get('ingredients'):
                i = Ingredient(
                    recipeID=self.recipeID,
                    title=ingredient.get('title'),
                    amount=ingredient.get('amount'),
                    amountUnit=ingredient.get('amountUnit'),
                    calories=ingredient.get('calories'))
                dbsession.add(i)
                dbsession.commit()

sampledata_recipe = [
    dict(
        title="Apfelkuchen",
        prepareTimeMinutes=30,
        prepareInstructions="Einen Apfel Schälen<br/><br/>Apfelkuchen daraus backen"),
    dict(
        title="Müsli",
        prepareTimeMinutes=5,
        prepareInstructions="Müsli in Schüssel kippen,<br/><br/>Milch hinterher,<br/><br/>Auf keinen Fall andersrum."
    )
]
