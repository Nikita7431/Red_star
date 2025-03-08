# def generate_print_layout(pages, drops):
#     layout = []
#
#     # Определяем количество разворотов
#     sheet_count = pages // (drops // 2)
#
#     for i in range(sheet_count):
#         # Пары страниц для текущего разворота
#         layout.append((i * 2 + 1, pages - i * 2))
#         layout.append((pages - i * 2 - 1, i * 2 + 2))
#
#     return layout
#
# # Пример использования
# pages = 16
# drops = 8
#
# result = generate_print_layout(pages, drops)
#
# # Вывод результата
# for pair in result:
#     print(pair[0], pair[1])
#

# def print_sheet_numbering(all_pages=32, part=3, with_cover=False):
   

# ################ подсчёт для одной книги 

#     book_pages = pow(2, part + 1)
#     if book_pages < 4:
#         raise ValueError("Формат слишком мал для создания разворотов. Увеличьте количество страниц.")

#     book_drops = book_pages // 2
#     if book_drops < 2:
#         raise ValueError("Количество полос спуска слишком мало. Увеличьте количество страниц или часть.")

#     pairs = []
#     sheet_count = (book_pages + book_drops - 1) // book_drops  

#     start_page = 1 if with_cover else 3
    
#     final_page = 0

#     for i in range(sheet_count):
#         for j in range(book_drops // 2):
#             left_top = (i * book_drops) + (j + start_page)  # Номер страницы сверху слева
#             right_top = (i * book_drops) + (book_drops - j + start_page - 1)  # Номер страницы сверху справа
#             left_bottom = book_pages - (i * book_drops) - j  # Номер страницы снизу слева
#             right_bottom = book_pages - (i * book_drops) - (book_drops - j - 1)  # Номер страницы снизу справа

#             # Добавляем проверку на выход за пределы страниц
#             if left_top <= book_pages:
#                 pairs.append((left_top, right_top, left_bottom, right_bottom))

#     final_page = book_pages
#     return pairs
def print_sheet_numbering(all_pages=32, part=3, first_number=1):

    pairs_2 = [4,1,2,3]
    pairs_4 = [1,8,4,5,7,2,6,3]
    pairs_8 = [1,8,16,9,13,12,4,5,7,2,10,15,11,14,6,3]
    pairs_16 = [16,17,24,9,1,32,25,8,4,29,28,5,13,20,21,12,10,23,18,15,7,26,30,2,6,27,31,3,11,22,19,14]

    book_pages = pow(2, part)
    
    if book_pages < 4:
        print("Страниц слигком мало")
        raise ValueError("Формат слишком мал ")

    book_drops = book_pages // 2
    
    if book_drops < 2:
        print("Количество полос спуска мало")
        raise ValueError("Количество полос спуска мало")
    
    pairs =[]

    match part:
        case 1:
            pairs = pairs_2 
        case 2 : 
            pairs = pairs_4
        case 3 : 
            pairs = pairs_8
        case 4 :
            pairs = pairs_16

    
    
    # pairs_16 = []
    # pairs_32 = []  

    # sheet_count = (book_pages + book_drops - 1) // book_drops  

    # start_page = 1 if with_cover else 3
    
    # final_page = 0

    # final_page = book_pages
    
    return [x+(first_number-1) for x in pairs]

#def print_sheet_numbering(pages, drops):
#    # Развороты
#    pairs = []
#
#    # Определяем количество разворотов
#    sheet_count = (pages + drops - 1) // drops  # Учитываем, если есть дополнительные страницы
#
#    for i in range(sheet_count):
#        # Номера страниц для текущего разворота
#        for j in range(drops // 2):
#            left_top = (i * drops) + (j + 1)  # Номер страницы сверху слева
#            right_top = (i * drops) + (drops - j)  # Номер страницы сверху справа
#            left_bottom = pages - (i * drops) - j  # Номер страницы снизу слева
#            right_bottom = pages - (i * drops) - (drops - j - 1)  # Номер страницы снизу справа
#
#            # Добавляем проверку на выход за пределы страниц
#            if left_top <= pages:
#                pairs.append((left_top, right_top, left_bottom, right_bottom))
#    # попадать в кратность определенную ( если 1/4 или 3/4 будут проблемы.
#    # давать сообщение - "давайте доп.страницы" в общем выдавать ошибку.
#    # с обложкой от 1
#    # без обложки от 3
#    return pairs




