import os

def read_file_info(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return file_path, len(lines), lines

def main():


    file_paths = ['1.txt', '2.txt', '3.txt']  
    all_file_info = []

    # Считываем информацию о каждом файле
    for file_path in file_paths:
        file_info = read_file_info(file_path)
        all_file_info.append(file_info)
    
    # Сортируем по количеству строк
    all_file_info.sort(key=lambda x: x[1])  # Сортировка по количеству строк
    
    
    # Записываем в итоговый файл
    output_file_path = 'Результат объединения.txt'
    with open(output_file_path, 'w', encoding='utf-8') as f_out:
        for file_name, line_count, lines in all_file_info:
            f_out.write(f"{file_name}\n{line_count}\n")
            f_out.writelines(lines)
            f_out.write("\n") 
    
    print(f"Объединение файлов завершено. Результат сохранен в {output_file_path}")

if __name__ == '__main__':
    main()