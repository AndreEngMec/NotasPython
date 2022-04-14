# Aspectos iniciais de dicionários

a = dict()
a = {'nome': 'João', 'idade': 25}
a['nome'] = "André Sant'ana"
a['idade'] = 31
print(a)
print(a['nome'])
a['profissão'] = 'Engenheiro Mecânico'

a['nome'] = 'Claudia Dias'

# os dicionários não são ordenados (diferente de uma lista),não importa em que
# ordem os pares chave-valor são digitados em um dicionário

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
eggs == ham #Verdadeiro

# Laços com dicionários
for v in ham.values():
    print(v)
for k in ham.keys():
    print(k)
for i in ham.items():
    print(i) #retorna uma tupla
for k,v in a.items():
    print(f'k é {k} e V é {v}')

# Transformção das chaves, valores e par chave-valores em uma lista
print(a.values())
print(list(a.values()))
print(a.keys())
print(list(a.keys()))
print(a.items())
print(list(a.items()))

# Verificando se uma chave ou um valor estão presentes em um dicionário

spam = {'name': 'Zophie', 'age': 7}
'name' in spam.keys() #Verdadeiro
'Zophie' in spam.values() #Verdadeiro
'color' in spam.keys() # Falso
'color' not in spam.keys() # Verdadeiro
'color' in spam # Quando não tem o método, o python consegue reconhecer uma chave porém os valores não

# método get() # que aceita dois argumentos: a chave do valor a ser obtido e um valor alternativo a ser retornado se essa chave não existir.
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.') #'I am bringing 2 cups.'
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.') #'I am bringing 0 eggs.'

# método setdefault() O primeiro argumento passado para o método é a chave a ser verificada e o segundo argumento é o valor a ser definido nessa chave caso
# ela não exista. Se a chave existir, o método setdefault() retornará o valor da chave.

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')#'black'
#spam = {'color': 'black', 'age': 5, 'name': 'Pooka'}
spam.setdefault('color', 'white') #'black'
# spam#{'color': 'black', 'age': 5, 'name': 'Pooka'}

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)

# Dicionários e listas aninhados

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
'Bob': {'ham sandwiches': 3, 'apples': 2},
'Carol': {'cups': 3, 'apple pies': 1}}
def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought
print('Number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))