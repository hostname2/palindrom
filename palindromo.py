def es_palindromo(word):
    if word == word[::-1]: #se imvierte la palabra con [::-1] y se compara con la palabra normal
        return True
    else:
        return False


def es_palindromo2(word):
    return word == word[::-1] #buenas practicas



flag = True
while flag:
    print('Digite palindromo')
    pal=input()
    print(es_palindromo(pal))
    print('deseae otra palabra? ')
    opc=input()
    if opc == 'si':
        flag = True
    else :
        flag = False