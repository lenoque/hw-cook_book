from pprint import pprint

cook_book = {}

with open ('recipes.txt', encoding='utf-8') as f:
    dishes = []
    buffer = []
    for line in f.readlines():
        if line := line.strip():
            buffer.append(line)
        else:
            dishes.append(buffer)
            buffer = []
for dish in dishes:
    dish_name = dish[0]
    recipe_list = []
    for line in dish[2:]:
        ingredient_name, quantity, measure = line.split(" | ")
        recipe_list.append({"name": ingredient_name, "quantity": quantity, "measure": measure})
    cook_book[dish_name] = recipe_list

pprint(cook_book, indent=4)


def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['name'] not in ingredients:
                    ingredients[ingredient['name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity']}
    return ingredients



res = get_shop_list_by_dishes(['Омлет'],2)
pprint(res, indent=4)


