def count_letter():
    c = input("Введите букву: ")
    b = 0
    for i in ['python', 'c++', 'c', 'scala', 'java']:
        if c in i:
            b +=1
    print(f"Букв {c} = {b}")

count_letter()









