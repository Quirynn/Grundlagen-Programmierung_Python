
import datetime
from sqlalchemy import Column, BigInteger, String, Text, DateTime
from sqlalchemy.orm import relationship
from cookbook.config import ModelBaseObject, dbsession

class Ingredient(ModelBaseObject):
    __tablename__ = 'ingredient'

    # Attributes:
    ingredientID = Column(BigInteger, primary_key=True)
    recipeID = Column(BigInteger)
    title = Column(String(120))
    amount = Column(BigInteger)
    amountUnit = Column(String(120))
    calories = Column(BigInteger)

    # Relationships:
    recipe = relationship('Recipe', foreign_keys=[recipeID], primaryjoin='Recipe.recipeID == Ingredient.recipeID')

    @classmethod
    def create(cls, data):
        isCreate = False
        if 'recipeID' in data and 'title' in data and 'amount' in data and 'amountUnit' in data and 'calories' in data:

            ingredient = Ingredient(
                recipeID=data.get('recipeID'),
                title=data.get('title'),
                amount=data.get('amount'),
                amountUnit=data.get('amountUnit'),
                calories=data.get('calories'))

            dbsession.add(ingredient)
            dbsession.commit()
            isCreate = True

        return isCreate

    @classmethod
    def delete(cls):
        dbsession.delete(self)
        dbsession.commit()
    
    def getData(self):
        return dict(
            ingredientID=self.ingredientID,
            recipeID=self.recipeID,
            title=self.title,
            amount=self.amount,
            amountUnit=self.amountUnit,
            calories=self.calories)


sampledata_ingredients = [
    dict(
        recipeID=1,
        title="Äpfel",
        amount=1000,
        amountUnit="gramm",
        calories=10),
    dict(
        recipeID=1,
        title="Teig",
        amount=2250,
        amountUnit="gramm",
        calories=2250),
    dict(
        recipeID=2,
        title="Zerealienmischung",
        amount=200,
        amountUnit="gramm",
        calories=1000),
    dict(
        recipeID=2,
        title="Milch",
        amount=400,
        amountUnit="ml",
        calories=400)
]
