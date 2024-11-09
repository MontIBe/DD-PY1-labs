# TODO Найдите количество книг, которое можно разместить на дискете
# Исходные данные:

disk_size = 1.44 #Мб
pages = 100
lines = 50
symbols = 25
symbol_weight = 4 #байт
one_Kb = 1024 #байт
one_Mb = 1024 * one_Kb #байт

disk_size_byte = disk_size * one_Mb
book_size = pages * lines * symbols * symbol_weight
books_amount = disk_size_byte // book_size

print("Количество книг, помещающихся на дискету:", int(books_amount))
