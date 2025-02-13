def get_cats_info(path: str):

    cats_info_list = []
    cat_info = {}

    try:

        with open(path, "r", encoding='utf-8') as file:

            read_file = file.readlines()

            for line in read_file:

                info = (line.strip('\n').split(','))
                cat_info.update(
                    {"id": info[0], "name": info[1], "age": info[2]})
                cats_info_list.append(cat_info)
                cat_info = {}

        return cats_info_list

    except FileNotFoundError:

        print("Файл не знайдено! Переконайтесь, що шлях правильний.")


if __name__ == '__main__':
    print(get_cats_info('files/cats_info.txt'))
