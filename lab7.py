# Словник для збереження даних про поїзди
schedule = {
    1: {"route": "Київ – Харків", "arrival": (10, 30), "departure": (10, 50)},
    2: {"route": "Львів – Одеса", "arrival": (12, 15), "departure": (12, 45)},
    3: {"route": "Дніпро – Київ", "arrival": (14, 20), "departure": (14, 35)},
    4: {"route": "Харків – Львів", "arrival": (16, 40), "departure": (17, 0)},
    5: {"route": "Одеса – Дніпро", "arrival": (18, 10), "departure": (18, 25)},
    6: {"route": "Київ – Одеса", "arrival": (19, 50), "departure": (20, 10)},
    7: {"route": "Львів – Київ", "arrival": (21, 15), "departure": (21, 35)},
    8: {"route": "Харків – Одеса", "arrival": (22, 5), "departure": (22, 20)},
    9: {"route": "Одеса – Львів", "arrival": (23, 0), "departure": (23, 20)},
    10: {"route": "Дніпро – Харків", "arrival": (9, 10), "departure": (9, 30)}
}

# Функція для виведення всіх значень словника
def print_all_trains():
    print("\nРозклад поїздів:")
    for train_num, details in schedule.items():
        print(f"Поїзд №{train_num}: {details['route']}, Прибуття: {details['arrival'][0]:02}:{details['arrival'][1]:02}, "
              f"Відправлення: {details['departure'][0]:02}:{details['departure'][1]:02}")

# Функція для додавання нового запису до словника
def add_train(train_num, from_city, to_city, arrival_hour, arrival_min, departure_hour, departure_min):
    route = f"{from_city} – {to_city}"
    
    # Перевірка на дублювання за маршрутом, часом прибуття та відправлення
    for num, details in schedule.items():
        if details["route"] == route and \
           details["arrival"] == (arrival_hour, arrival_min) and \
           details["departure"] == (departure_hour, departure_min):
            # Якщо номери поїздів різні, але інші деталі співпадають
            if num != train_num:
                overwrite = input(f"Поїзд з маршрутом '{route}', прибуттям о {arrival_hour:02}:{arrival_min:02} та відправленням о {departure_hour:02}:{departure_min:02} вже існує під номером {num}. Бажаєте перезаписати його під новим номером {train_num}? (так/ні): ").lower()
                if overwrite == 'так':
                    # Видаляємо старий запис і додаємо новий під новим номером
                    del schedule[num]
                    schedule[train_num] = {
                        "route": route,
                        "arrival": (arrival_hour, arrival_min),
                        "departure": (departure_hour, departure_min)
                    }
                    print(f"Поїзд під новим номером {train_num} додано до розкладу.")
                else:
                    print("Зміни не було здійснено.")
                return  # Завершуємо роб
    
    # Якщо поїзд з таким номером вже існує, запитуємо, чи потрібно його перезаписати
    if train_num in schedule:
        overwrite = input(f"Поїзд №{train_num} вже існує. Переписати його? (так/ні): ").lower()
        if overwrite == 'так':
            schedule[train_num] = {
                "route": route,
                "arrival": (arrival_hour, arrival_min),
                "departure": (departure_hour, departure_min)
            }
            print(f"Поїзд №{train_num} було оновлено.")
        else:
            print(f"Поїзд №{train_num} не було змінено.")
    else:
        # Додаємо новий запис, якщо не було дублювання і не існує поїзда під цим номером
        schedule[train_num] = {
            "route": route,
            "arrival": (arrival_hour, arrival_min),
            "departure": (departure_hour, departure_min)
        }
        print(f"Поїзд №{train_num} додано до розкладу.")

# Функція для видалення запису зі словника
def remove_train(train_num):
    try:
        del schedule[train_num]
        print(f"Поїзд №{train_num} видалено з розкладу.")
    except KeyError:
        print(f"Помилка: Поїзд №{train_num} не знайдено у розкладі.")

# Функція для виведення словника, відсортованого за часом прибуття
def print_sorted_schedule_by_arrival():
    print("\nРозклад поїздів за часом прибуття (відсортовано):")
    
    # Сортуємо словник за часом прибуття
    sorted_trains = sorted(schedule.items(), key=lambda x: x[1]['arrival'])
    
    for train_num, details in sorted_trains:
        print(f"Поїзд №{train_num}: {details['route']}, Прибуття: {details['arrival'][0]:02}:{details['arrival'][1]:02}, "
              f"Відправлення: {details['departure'][0]:02}:{details['departure'][1]:02}")

# Функція для визначення, які поїзди стоять на станції у визначений момент часу
def trains_at_station(current_hour, current_min):
    print(f"Поїзди, що стоять на станції о {current_hour:02}:{current_min:02}:")
    found = False
    for train_num, details in schedule.items():
        arrival_hour, arrival_min = details["arrival"]
        departure_hour, departure_min = details["departure"]

        # Перевірка, чи перебуває поїзд на станції в даний час
        if (arrival_hour < current_hour or (arrival_hour == current_hour and arrival_min <= current_min)) and \
           (departure_hour > current_hour or (departure_hour == current_hour and departure_min >= current_min)):
            print(f"Поїзд №{train_num}: {details['route']}")
            found = True

    if not found:
        print("Немає поїздів на станції у цей момент.")

# Основна функція для взаємодії з користувачем
def main():
    while True:
        print("\nМеню:")
        print("1. Показати всі поїзди")
        print("2. Додати новий поїзд")
        print("3. Видалити поїзд")
        print("4. Показати розклад поїздів (відсортовано за номерами)")
        print("5. Перевірити, які поїзди стоять на станції у визначений час")
        print("6. Вийти")

        choice = input("Оберіть дію: ")

        if choice == '1':
            print_all_trains()
            
        elif choice == '2':
            try:
                train_num = int(input("\nВведіть номер поїзда: "))
                from_city = input("Введіть місто відправлення: ")
                to_city = input("Введіть місто прибуття: ")
                arrival_hour = int(input("Введіть годину прибуття: "))
                arrival_min = int(input("Введіть хвилини прибуття: "))
                departure_hour = int(input("Введіть годину відправлення: "))
                departure_min = int(input("Введіть хвилини відправлення: "))
                add_train(train_num, from_city, to_city, arrival_hour, arrival_min, departure_hour, departure_min)
            except ValueError:
                print("Помилка вводу! Години та хвилини мають бути цілими числами.")

        elif choice == '3':
            try:
                train_num = int(input("\nВведіть номер поїзда для видалення: "))
                remove_train(train_num)
            except ValueError:
                print("Помилка: номер поїзда має бути цілим числом.")
                
        elif choice == '4':
            print_sorted_schedule_by_arrival()
            
        elif choice == '5':
            try:
                current_hour = int(input("\nВведіть годину: "))
                current_min = int(input("Введіть хвилини: "))
                trains_at_station(current_hour, current_min)
            except ValueError:
                print("Помилка вводу! Години та хвилини мають бути цілими числами.")
                
        elif choice == '6':
            print("\nДо побачення!")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
