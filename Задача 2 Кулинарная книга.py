import json
from pprint import pprint

def read_recipes(file_path):

    cook_book = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            while True:
                name = f.readline().strip()
                if not name:
                    break

                ingredient_count = int(f.readline().strip())
                ingredients = []
                for _ in range(ingredient_count):
                    ingredient_data = f.readline().strip().split(' | ')
                    ingredients.append({
                        'ingredient_name': ingredient_data[0],
                        'quantity': int(ingredient_data[1]),
                        'measure': ingredient_data[2]
                    })

                cook_book[name] = ingredients
                f.readline()  

    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_recipes('Рецепты.json') 
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
                else:
                    shop_list[ingredient_name] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
    
    return shop_list

file_path = 'Рецепты.json'

def main(): 
    result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    pprint(result)

if __name__ == '__main__':
    main()