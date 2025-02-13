def total_salary(path: str):

    total = 0
    count = 0

    try:

        with open(path, "r", encoding='utf-8') as file:

            read_file = file.readlines()

            for line in read_file:

                total += float(line.strip('\n').split(',')[1])
                count += 1

            return (total, total/count)

    except FileNotFoundError:

        print("Файл не знайдено! Переконайтесь, що шлях правильний.")


if __name__ == '__main__':
    total, average = total_salary('files/salary.txt')
    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
