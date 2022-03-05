cookbook = {
	"sandwich" : {
		"ingredients" : ["ham", "bread", "cheese", "tomatoes"],
		"meal" : "lunch",
		"prep_time" : "10 min"
	},
	"cake" : {
		"ingredients" : ["flour", "sugar", "eggs", "dessert"],
		"meal" : "dessert",
		"prep_time" : "60 min"
	},
	"salad" : {
		"ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
		"meal" : "lunch",
		"prep_time" : "15 min"
	}
}

def display_recipe(name):
	if not name in cookbook:
		print("invalid recipe")
		return
	for key, value in cookbook.items():
		if key == name:
			print(f"the ingredients of {key} are {cookbook[key]['ingredients']}")
			print(f"the meal type of a {key} is {cookbook[key]['meal']}")
			print(f"preparation time of the {key} is {cookbook[key]['prep_time']}")

def pop_recipe(name):
	if not name in cookbook:
		print('recipe does not exist')
		return 
	for key, value in cookbook.items():
		if key == name:
			cookbook.pop(key)
			print("recipe deleted succefully")
			return ;

def add_recipe(name,ingredients, meal_type, prep_time):
	assert type(ingredients) is list, "ingredients must be on a list"
	assert type(meal_type) is str, "meal type must be a string"
	assert type(prep_time) is str, "prep_time must be a string"
	cookbook[name] = {"ingredients" : ingredients, "meal":meal_type, "prep_time":prep_time}

def display_recipe_names():
	for key in cookbook:
		print(f"{key}")

is_on = True
while is_on:
	print("1: Add a recipe")
	print("2: Delete a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit")
	choise = int(input(">>"))
	if choise == 5:
		is_on = False
	elif choise == 1:
		name = input("enter the name of the recipe\n")
		ingredients = []
		done = False
		print("insert done to end the ingredients insertion")
		while not done:
			item = input("enter ingredients\n")
			ingredients.append(item)
			if item == 'done':
				done = True
		meal_type = input("insert the meal type\n")
		prep_time = input("insert the preparation time of the meal\n")
		add_recipe(name, ingredients, meal_type, prep_time)
	elif choise == 2:
		name = input("insert the name of the recipe\n")
		pop_recipe(name)
	elif choise == 3:
		name = input("insert the name of the recipe you want to display\n")
		display_recipe(name)
	elif choise == 4:
		display_recipe_names()
	else :
		print("This option does not exist, please type the corresponding number. To exit, enter 5.")
		
