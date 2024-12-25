

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



def main():
    file_path = 'Рецепты.json'
    cook_book = read_recipes(file_path)


    for dish, ingredients in cook_book.items():
        print(f"  '{dish}': [")
        for ingredient in ingredients:
            print(f"    {{'ingredient_name': '{ingredient['ingredient_name']}', 'quantity': {ingredient['quantity']}, 'measure': '{ingredient['measure']}'}}")

                
if __name__ == '__main__':
    main()




