# --------------------------------
# Nutrition Tracking for Children
# --------------------------------

# Step 1: Initialising the variables and the data structures
child_profiles = {}
meal_logs = {}

# Step 2: Defining the food groups
food_nutrition = {
    "Breastmilk": {"calories": 170, "protein": 2, "vitamin A": 100},
    "Rice": {"calories": 200, "protein": 4, "vitamin A": 0},
    "Wheat": {"calories": 180, "protein": 5, "vitamin A": 0},
    "Lentils": {"calories": 230, "protein": 9, "vitamin A": 10},
    "Chickpeas": {"calories": 270, "protein": 15, "vitamin A": 8},
    "Milk": {"calories": 150, "protein": 8, "vitamin A": 100},
    "Cheese": {"calories": 400, "protein": 25, "vitamin A": 200},
    "Chicken": {"calories": 300, "protein": 20, "vitamin A": 10},
    "Fish": {"calories": 250, "protein": 22, "vitamin A": 15},
    "Eggs": {"calories": 70, "protein": 6, "vitamin A": 75},
    "Carrots": {"calories": 50, "protein": 1, "vitamin A": 300},
    "Pumpkin": {"calories": 45, "protein": 2, "vitamin A": 400},
    "Banana": {"calories": 100, "protein": 1, "vitamin A": 50},
    "Apple": {"calories": 90, "protein": 1, "vitamin A": 5},
}

# Step 3: User input for children data
child_id = int(input("Enter child ID: ")) 
child_name = input("Enter child's name: ").upper()
child_age = int(input("Enter child's age: "))
child_weight = float(input("Enter child's weight (kg): "))
first_name = child_name.split()[0] 

child_profiles[child_id] = (child_name, child_age, child_weight, first_name)
meal_logs[child_id] = {"Breakfast": [], "Lunch": [], "Dinner": []}

# Step 4: Logging the food intake through user input
print("\nAvailable food items:")
print("Breastmilk, Rice, Wheat, Lentils, Chickpeas, Milk, Cheese, Chicken, Fish, Eggs, Carrots, Pumpkin, Banana, Apple")

# Breakfast
print("\nEnter Breakfast details: ")
food_item = input("Enter food item: ").capitalize()
quantity = float(input("Enter quantity in grams for " + food_item + ": "))  

if food_item in food_nutrition:
    meal_logs[child_id]["Breakfast"].append({
        "food": food_item,
        "calories": (food_nutrition[food_item]["calories"] / 100) * quantity,
        "protein": (food_nutrition[food_item]["protein"] / 100) * quantity,
        "vitamin A": (food_nutrition[food_item]["vitamin A"] / 100) * quantity
    })
else:
    print("\nFood item unavailable.")

# Lunch
print("\nEnter Lunch details: ")
food_item = input("Enter food item: ").capitalize()
quantity = float(input("Enter quantity in grams for " + food_item + ": "))  

if food_item in food_nutrition:
    meal_logs[child_id]["Lunch"].append({
        "food": food_item,
        "calories": (food_nutrition[food_item]["calories"] / 100) * quantity,
        "protein": (food_nutrition[food_item]["protein"] / 100) * quantity,
        "vitamin A": (food_nutrition[food_item]["vitamin A"] / 100) * quantity
    })
else:
    print("\nFood item unavailable.")

# Dinner
print("\nEnter Dinner details: ")
food_item = input("Enter food item: ").capitalize()
quantity = float(input("Enter quantity in grams for " + food_item + ": "))  

if food_item in food_nutrition:
    meal_logs[child_id]["Dinner"].append({
        "food": food_item,
        "calories": (food_nutrition[food_item]["calories"] / 100) * quantity,
        "protein": (food_nutrition[food_item]["protein"] / 100) * quantity,
        "vitamin A": (food_nutrition[food_item]["vitamin A"] / 100) * quantity
    })
else:
    print("\nFood item unavailable.")

# Step 5: Calculating the overall nutrients: 
recommended_nutrients = {"calories": 1500, "protein": 50, "vitamin A": 400}
total_nutrients = {"calories": 0, "protein": 0, "vitamin A": 0}

if meal_logs[child_id]["Breakfast"]:
    meal = meal_logs[child_id]["Breakfast"][0]
    total_nutrients["calories"] += meal["calories"]
    total_nutrients["protein"] += meal["protein"]
    total_nutrients["vitamin A"] += meal["vitamin A"]

if meal_logs[child_id]["Lunch"]:
    meal = meal_logs[child_id]["Lunch"][0]
    total_nutrients["calories"] += meal["calories"]
    total_nutrients["protein"] += meal["protein"]
    total_nutrients["vitamin A"] += meal["vitamin A"]

if meal_logs[child_id]["Dinner"]:
    meal = meal_logs[child_id]["Dinner"][0]
    total_nutrients["calories"] += meal["calories"]
    total_nutrients["protein"] += meal["protein"]
    total_nutrients["vitamin A"] += meal["vitamin A"]

# Step 6: Analysing the nutritions with the standard levels
# Step 7: Presenting the compared data to the user
print("\nSummary")
print("\nTotal children records: ", len(child_profiles))

print("\nMeal logs of the child: ")
print(meal_logs[child_id].items())

print("Child Details: ", child_profiles[child_id])
print("Total Nutrients Intake: ", total_nutrients)

# Comparison
match (
    total_nutrients["calories"] >= recommended_nutrients["calories"],
    total_nutrients["protein"] >= recommended_nutrients["protein"],
    total_nutrients["vitamin A"] >= recommended_nutrients["vitamin A"],
):
    case (True, True, True):
        print(child_profiles[child_id][3] + " has met the required nutrition levels.")
    case (False, _, _):
        print("Alert! " + child_profiles[child_id][3] + " is undernourished in calories.")
    case (_, False, _):
         print("Alert! " + child_profiles[child_id][3] + " lacks sufficient protein.")
    case (_, _, False):
        print("Alert! " + child_profiles[child_id][3] + " needs more Vitamin A-rich foods.")
    case _:
        print("Error. Try again")
