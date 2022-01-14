# numbers = [1, 2, 3, 4]
# def addition(num):
#     return num + num

# result = map(addition, numbers)
# print(result)

# result2 = map(lambda x: x + x, numbers)
# print(list(result2))

# result3 = map(lambda y: y * y, numbers)
# print(list(result3))

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
  
# result4 = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result4))


# a list contains both even and odd numbers. 
# seq = [0, 1, 2, 3, 5, 8, 13]
  
# result contains odd numbers of the list
# result5 = filter(lambda x: x % 2 != 0, seq)
# print(list(result5)) # [1, 3, 5, 13]
  
# result contains even numbers of the list
# result6 = filter(lambda x: x % 2 == 0, seq)
# print(list(result6)) # [0, 2, 8]

books = ['Harry Potter', 'Twilight', 'Cat in the Hat, Dr Sues', 'Twilight: new moon', 'Harry Potter: Sorcerers Stone', 'Harry Potter: Order of the Pheonix',  'One fish Two Fish, Dr Sues',  'Twilight: Breaking Dawn part 1', 'The Lorax, Dr Sues',  'Harry Potter: Prisoner of Askaban']

harry_potter_books = list(filter(lambda title_book: 'Harry' in title_book , books))

print("Potter Books", harry_potter_books)

twilight_books = list(filter(lambda title_books: 'Twi' in title_books , books))

print("Bella Books", twilight_books)

good_books = list(filter(lambda title_books: 'Sues' in title_books , books))

print("Good Books", good_books)



wgi2020 = ['']