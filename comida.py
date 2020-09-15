import random

ALVARO = "ALVARO"
LUCIA = "LUCIA"
BOTH = "BOTH"


class Food:
    def __init__(self, name, category, subcategory, complement, consumer):
        self.name = name
        self.category = category
        self.subcategory = subcategory
        self.complement = complement
        self.consumer = consumer

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


Carne = ["Croquetas",
         "Pollo al ras el hanout",
         "Filetes de cerdo con salsas (gaucha, roquefort, ketchup+mayonesa+mostaza)",
         "Filetes de pollo con salsas",
         "Fajitas",
         "Bocadillo de lomo",
         "Pollo panko teriyaki marinado",
         "Pollo al horno",
         "Estofado de ternera",
         "Estofado de cerdo",
         "Empanadillas chinas",
         "Empanadas",
         "Empanadillas",
         "Hamburguesas",
         "Perritos",
         "Salchichas",
         "Albondigas con tomate",
         "Kofta marroqui",
         "Pastel de patata y carne",
         "Alitas de pollo",
         "Filetes empanados",
         "Pollo al curry",
         "Chuletas de aguja",
         "Conejo al ajillo",
         "Entrecot"]

Pescado = ["Merluza a la plancha",
           "Merluza en salsa verde",
           "Rosada a la plancha",
           "Salmon a la plancha",
           "Atun encebollado",
           "Salmon con brocoli",
           "Lubina al microondas con soja y jengibre",
           "Embutido de pescado",
           "Palitos de merluza empanados",
           "Ceviche a la acapulqueña",
           "Ceviche de corvina",
           "Bacalao gratinado con patatas",
           "Merluza a la gallega"]

Verduras = ["Ensalada cesar",
            "Ensalada murciana",
            "Ensalada normal",
            "Ensalada Waldorf",
            "Ensaladilla rusa",
            "Salteado de verduras",
            "Crepes de verduras"]

Pasta = ["Espaguetis carbonara",
         "Ensalada de pasta",
         "Pasta con salsa pesto",
         "Pasta con salsa de tomate (arrabiata, napolitana, boloñesa, etc)",
         "Couscous",
         "Lasaña La Cocinera",
         "Ramen",
         "Pasta de arroz con verduras y carne"]

Arroz = ["Paella marinera",
         "Arroz a la cubana",
         "Ensalada de arroz",
         "Risotto de setas",
         "Arroz frito tres delicias"]

Huevos = ["Huevo con patatas",
          "Huevos rellenos"]

Patatas = ["Tortilla"]

Sopas = ["Lentejas",
         "Vichyssoise",
         "Gazpacho",
         "Porra"]

Masas = ["Sandwiches",
         "Croque Madame",
         "Croissants de jamon y queso",
         "Quiche lorraine",
         "Pizza"]


def selectFood(food, cat, already):
    foodList = [x for x in food if x.category == cat]
    selectedFood = foodList[random.randint(0, len(foodList)) - 1]
    print("First option: " + selectedFood.name)

    while selectedFood.name in already[-14:]:
        selectedFood = foodList[random.randint(0, len(foodList) - 1)]
        print("Next: " + selectedFood.name)

    return selectedFood.name


def prepareFoodList():
    food_list = list()
    for meal in Carne:
        food_list.append(Food(meal, "Meat", "Meat", False, BOTH))
    for meal in Pescado:
        food_list.append(Food(meal, "Fish", "Fish", False, BOTH))
    for meal in Verduras:
        food_list.append(Food(meal, "Vegs", "Vegs", False, BOTH))
    for meal in Pasta:
        food_list.append(Food(meal, "Pasta", "Pasta", False, BOTH))
    for meal in Sopas:
        food_list.append(Food(meal, "Others", "Soups", False, BOTH))
    for meal in Masas:
        food_list.append(Food(meal, "Others", "Doughs", False, BOTH))
    for meal in Arroz:
        food_list.append(Food(meal, "Pasta", "Rice", False, BOTH))
    for meal in Huevos:
        food_list.append(Food(meal, "Others", "Eggs", False, BOTH))
    for meal in Patatas:
        food_list.append(Food(meal, "Others", "Potatoes", False, BOTH))
    return food_list


if __name__ == "__main__":

    food_list = prepareFoodList()
    print(food_list)

    # One week: meat, fish, vegs, meat, pasta, others, fish

    week = ["Meat", "Meat", "Fish", "Vegs", "Pasta", "Others", "Others"]

    food = []

    day = 1
    for i in range(1, 5):
        print("Week " + str(i))
        random.shuffle(week)

        for cat in week:
            print("Day " + str(day))
            print("Category: " + cat)
            selectedFood = selectFood(food_list, cat, food)
            food.append(selectedFood)

            day += 1
        print()