from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.orm import Session, relationship, validates, declarative_base

Base = declarative_base()

class Meal(Base):
    __tablename__ = "meals"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    temp = Column(Integer, nullable=False)
    calories = Column(Integer, nullable=False)
    ingredients = relationship("Ingredient", secondary="recipies", back_populates="meals")

class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    meals = relationship("Meal", secondary="recipies", back_populates="ingredients")

class Recipie(Base):
    __tablename__ = "recipies"
    id = Column(Integer, primary_key=True)
    meal_id = Column(Integer, ForeignKey("meals.id"))
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"))

if __name__ == "__main__":
    engine = create_engine("sqlite:///many_to_many.db")
    # DROP TABLES TO REFRESH TABLES
    Meal.__table__.drop(engine)
    Ingredient.__table__.drop(engine)
    Recipie.__table__.drop(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        pasta = Meal(name="Meat Pasta", temp=150, calories=250)
        pizza = Meal(name="Cheese Pizza", temp=175, calories=300)
        tacos = Meal(name="Steak Tacos", temp=200, calories=100)
        session.add_all([pasta, pizza, tacos])
        session.commit()

        ingredient1 = Ingredient(name="Sauce")
        ingredient2 = Ingredient(name="Pasta")
        ingredient3 = Ingredient(name="Sausage")
        ingredient4 = Ingredient(name="Dough")
        ingredient5 = Ingredient(name="Shredded Cheese")
        ingredient6 = Ingredient(name="Taco Shells")
        ingredient7 = Ingredient(name="Carne Asada")
        session.add_all([ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7])

        recipie1 = Recipie(meal_id = pasta.id, ingredient_id= ingredient1.id)
        recipie2 = Recipie(meal_id = pizza.id, ingredient_id= ingredient4.id)
        session.add_all([recipie1, recipie2])
        session.commit()

        # name = input("Enter a meal name: ")
        # temp = int(input("Enter a temperature: "))
        # calories = int(input("Enter the calories: "))
        
        # # create
        # new_meal = Meal(name=name, temp=temp, calories=calories)
        # session.add(new_meal)
        # session.commit()
        # print("Added new meal")

        # # update        
        # update_meal = int(input("Enter the meal ID: "))
        # new_name = input("Enter meal name: ")
        # meal_to_update = session.query(Meal).filter_by(id = update_meal).first()
        # meal_to_update.name = new_name
        # session.commit()

        # # delete
        # delete_meal = int(input("Enter the meal ID to delete: "))
        # deleted_meal = session.query(Meal).filter_by(id = delete_meal).first()
        # session.delete(deleted_meal)
        # session.commit()

        # all_meals = session.query(Meal).all()
        # for meals in all_meals:
        #     print(f"{meals.name}")

        # find_id = int(input("Enter the id to find the meal: "))
        # found = session.query(Meal).filter_by(id = find_id).first()
        # print(f"Found: {found.name}")

        find_recipie = int(input("Enter id for the recipie: "))
        search_recipie = session.query(Recipie).filter_by(meal_id = find_recipie).first
        find_meal = session.query(Meal).filter_by(id = search_recipie.id).first()
        print(f"Meal is {find_meal.name}")



