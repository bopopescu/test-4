import mysql.connector as mysql # Импортируем нужные библиотеки

db = mysql.connect(             # подключениие к бд
    host = "localhost",         # ip адрес или адрес хоста
    user = "root",              # пользователь базы данных
    passwd = "",                # пароль пользователя базы данных
    database = "gmap_bd"        # имя базы данных
)

cursor = db.cursor()            # указываем курсору что ему нужно открыть базу данных

masiv = ["Дозиметрические_измерения", "Заключение_РПН", "Лицензия", "Кабинет_открыт", "Сведения_подтверждаю_Главный_врач"] # масив названий столбцов

# print(masiv)                                                                                # выводил масив для проверки
# print(len(masiv))                                                                           # выводил длину масива

for nac_str in range(149, 2, -1):                                                             # задал переменую начальной строки и поставил ее в цикл в котором она долна пройти от 149 строки до 3-ей с шагом -1
    q = 0                                                                                     # обнуляем счетчик q
    for i in range(len(masiv)):                                                               # цикл для прохода по всем элементам масива (для выборки по какому столбцу произойдет запрос)
        zapros = "SELECT " + str(masiv[i]) + " FROM sheet WHERE id = " + str(nac_str)         # запрос для выборки из базы данных по строке с айди
        ++i                                                                                   # поднимаем счетчик на 1 каждую итерацию

        cursor.execute(zapros)                                                                # получать записи из таблицы
        records = cursor.fetchall()                                                           # fetching all records from the 'cursor' object

        for record in records:                                                                # Необходимо для выдачи запроса из бд
            # print(record.__getitem__(0))                                                    # Использовал для отладки
            proverka = "да"                                                                   # Присвоил переменной проверочное значение
            if record.__getitem__(0) == proverka:                                             # Проверил итем зависи рекорд на наличие значения "да"
                q = q + 1                                                                     # Сделал ход итерации на + 1
                # print("zawli syda, q= ", q)                                                 # Использовал для отладки
    # print(q)                                                                                # Использовал для отладки

    vstavka = "UPDATE sheet SET ввод = '" + str(q) + "' WHERE id = '" + str(nac_str) + "'"    # Сделал запрос на вставку в бд в строку столбца "ввод"
    # print("moi zapros", vstavka)                                                            # Использовал для отладки
                                                                                              # storing values in a variable
    values = q
                                                                                              # executing the query with values
    cursor.execute(vstavka)                                                                   # Необходимый параметр для работы запроса

    db.commit()                                                                               # to make final output we have to run the 'commit()' method of the database object

    # print(cursor.rowcount, "record inserted")                                               # использовал для отладки
else:
    print("vse vedeno")