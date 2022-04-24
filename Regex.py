import re

# MATERIAL E EXEMPLO DO YOUTUBE

#Caracteres:

# . - Entende qualquer valor exceto uma nova linha
# \. - Para buscar o caracter "."
texto = 'arara'
t = re.compile(r'a...a')
check = t.findall(texto)
print(check)

# ^ - Irá testar o início da string
# [^] -Irá considerar todos os caracteres EXCETO o indicado
texto = 'arara'
t = re.compile(r'[^a]')
q = re.compile(r'^a')
check = t.findall(texto)
check1 = q.findall(texto)
print(check, '\n', check1)

# \d - Qualquer caracter que SEJA um algarismo  de 0 a 9
# \D - Qualquer caracter que NÃO SEJA um algarismo de 0 a 9
texto = 'arara1992'
t = re.compile(r'\d')
q = re.compile(r'\D')
check = t.findall(texto)
check1 = q.findall(texto)
print(check, '\n', check1)

# \s - Qualquer caracter que SEJA vazio
# \S - Qualquer caracter que NÃO SEJA vazio
texto = '''

arara 1992

'''
t = re.compile(r'\s')
q = re.compile(r'\S')
check = t.findall(texto)
check1 = q.findall(texto)
print(check, '\n', check1)

# \w - Qualquer caracter que SEJA alfanumérico
# \W - Qualquer caracter que NÃO SEJA Alfanumérico
texto = '''

_arara@ 1992_

'''
t = re.compile(r'\w')
q = re.compile(r'\W')
check = t.findall(texto)
check1 = q.findall(texto)
print(check, '\n', check1)

#Métodos para checagem:

texto = 'arara'
t = re.compile(r'a')
check_findall = t.findall(texto)
check_match = t.match(texto)
check_search = t.search(texto)
check_finditer = t.finditer(texto)
print(check_findall)
print(check_match)
print(check_search)
print(check_finditer)

correspondencias = check_finditer
for correspondencia in correspondencias:
    print(correspondencia)

texto = '''
Arara 1992
'''
t = re.compile(r'[a-zA-Z0-9]')
correspondencias = t.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)

texto = '''
Arara 1992
'''
t = re.compile(r'[a-zA-Z] [0-9]')
correspondencias = t.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)

texto = '''
Arara 1992
'''
t = re.compile(r'[a-zA-Z]+ [0-9]+')
correspondencias = t.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)


#Quantificadores:

# * - 0 ou mais
texto = '''
Arara
'''
t = re.compile(r'[ra]*')
correspondencias = t.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)

# + - 1 ou mais
texto = '''
Arara
'''
t = re.compile(r'[ra]+')
correspondencias = t.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)

# ? - 0 ou um
texto = '''
Arara
'''
t = re.compile(r'[ra]?')
correspondencias = t.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)

# {3} - número exato de repetições
texto = '''
Arara
'''
t = re.compile(r'[ra]{2}')
correspondencias = t.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)

# {3,4} - de 3 a 4 min e max
texto = '''
Arara
'''
t = re.compile(r'[ra]{2,4}')
correspondencias = t.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)

#Grupos

texto = '''
Arara 1992
arara 1993
'''
t = re.compile(r'(A|a)?[a-z]{4} [0-9]+')
correspondencias = t.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)
    print(correspondencia.group(0))
    print(correspondencia.group(1))

#Textos:

texto1 = '''
Sites diversos:
https://google.com/
https://www.gov.br/
https://www.kaiamba.com.br/
http://www.faetec.rj.gov.br/
'''
t = re.compile(r'https?://(www\.)?([a-zA-Z0-9]+\.)+(com.br|gov.br|com)')
correspondencias = t.finditer(texto1)
for correspondencia in correspondencias:
    print(correspondencia)
    print(correspondencia.group(1))
    print(correspondencia.group(2))
    print(correspondencia.group(3))

emails = '''
Vários e-mails:
daniel@dominio.com
daniel.candiotto@dominio.com.br
DANIEL@dominio.br
DANIEL.CANDIOTTO@gov.br
danielcandiotto1@dominio1.co
daniel_candiotto_1@dominio-dominio.net
'''

t = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
correspondencias = t.finditer(emails)
for correspondencia in correspondencias:
    print(correspondencia)

# MATERIAL E EXEMLPOS DO  LIVRO 'aUTMOATIZA tAREFAS mAÇANTES'

#Embora haja diversos passos para usar expressões regulares em Python, cada
#passo é bem simples.
#1. Importe o módulo de regex usando import re.
#2. Crie um objeto Regex usando a função re.compile(). (Lembre-se de usar uma
#string pura.)
#3. Passe a string que você quer pesquisar ao método search() do objeto Regex.
#Isso fará um objeto Match ser retornado.
#4. Chame o método group() do objeto Match para retornar uma string com o
#texto correspondente


# Criando objeto REGEX - Criação de Padrão
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

#Agrupando com paranteses

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
#'415'
mo.group(2)
#'555-4242'
mo.group(0)
#'415-555-4242'
mo.group()
#'415-555-4242
areaCode, mainNumber = mo.groups()
print(areaCode)
#415
print(mainNumber)

#Caracteres de escape \( e \)
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1)
#'(415)'
mo.group(2)
#'555-4242'

#Fazendo a correspondência de vários grupos com pipe
#O caractere | é chamado de pipe

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group()
#'Batman'
mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group()
# 'Tina Fey'

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
#'Batmobile'
mo.group(1)

#Correspondência opcional usando ponto de interrogação

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
#'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
#'Batwoman

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()
#'415-555-4242'
mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()
#'555-4242'

#Correspondendo a zero ou mais ocorrências usando asterisco

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
#'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
#'Batwoman'
mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
#'Batwowowowoman

#Correspondendo a uma ou mais ocorrências usando o sinal de adição

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()
#'Batwoman'
mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()
#'Batwowowowoman'
mo3 = batRegex.search('The Adventures of Batman')
mo3 == None
#True

#Correspondendo a repetições específicas usando chaves

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()
#'HaHaHa'
mo2 = haRegex.search('Ha')
mo2 == None
#True

#Correspondências greedy (gulosa) e nongreedy (não gulosa)

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()
#'HaHaHaHaHa'
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()
#'HaHaHa'

# Método findall()

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()
#'415-555-9999

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # não tem nenhum grupo
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
#['415-555-9999', '212-555-0000']

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # tem grupos
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
#[('415', '555', '9999'), ('212', '555', '0000')]

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall(r'12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
#['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4
# birds', '3 hens', '2 doves', '1 partridge']

# Criando suas próprias classes de caracteres

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
#['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

#Observe que, nos colchetes, os símbolos normais de expressão regular não
#são interpretados. Isso quer dizer que não é necessário escapar os caracteres
#.., *, ? ou () com uma barra invertida na frente.

consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
#['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

#Acento circunflexo e o sinal de dólar
# ^ é usado quando uma correspondencia deve ocorrer no início da string
# $ é usado qunado uma correspondência deve ocorrer no final da sting


beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search(r'Hello world!')
#<_sre.SRE_Match object; span=(0, 5), match='Hello'>
beginsWithHello.search(r'He said hello.') == None
#True

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
#<_sre.SRE_Match object; span=(16, 17), match='2'>
endsWithNumber.search('Your number is forty two.') == None
#True

wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
#<_sre.SRE_Match object; span=(0, 10), match='1234567890'>
wholeStringIsNum.search('12345xyz67890') == None
#True
wholeStringIsNum.search('12 34567890') == None
#True

#Caractere-curinga - O caractere . (ou ponto) em uma expressão regular é chamado de caracterecuringa e corresponde a
# qualquer caractere, exceto uma quebra de linha.

atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
#['cat', 'hat', 'sat', 'lat', 'mat']

#Correspondendo a tudo usando ponto-asterisco

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1)
#'Al'
mo.group(2)
#'Sweigart'

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group()
#'<To serve man>'

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()
#'<To serve man> for dinner.>'

#Correspondendo a quebras de linha com o caractere ponto

noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.
\nUphold the law.').group()
#'Serve the public trust.'

newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.
\nUphold the law.').group()
#'Serve the public trust.\nProtect the innocent.\nUphold the law.'

#Revisão dos símbolos de regex
#Este capítulo discutiu bastante a notação; sendo assim, apresentaremos uma
#revisão rápida do que aprendemos:
#• ? corresponde a zero ou uma ocorrência do grupo anterior.
#• * corresponde a zero ou mais ocorrências do grupo anterior.
#• + corresponde a uma ou mais ocorrências do grupo anterior.
#• {n} corresponde a exatamente n ocorrências do grupo anterior.
#• {n,} corresponde a n ou mais ocorrências do grupo anterior.
#• {,m} corresponde a zero até m ocorrências do grupo anterior.
#• {n,m} corresponde a no mínimo n e no máximo m ocorrências do grupo
#anterior.
#• {n,m}? ou *? ou +? faz uma correspondência nongreedy do grupo anterior.
#• ^spam quer dizer que a string deve começar com spam.
#• spam$ quer dizer que a string dever terminar com spam.
#• . corresponde a qualquer caractere, exceto os caracteres de quebra de linha.
#• \d, \w e \s correspondem a um dígito, um caractere de palavra ou um
#caractere de espaço, respectivamente.
#• \D, \W e \S correspondem a qualquer caractere, exceto um dígito, um
#caractere de palavra ou um caractere de espaço, respectivamente.
#• [abc] corresponde a qualquer caractere que estiver entre os colchetes (por
#exemplo, a, b ou c).
#• [^abc] corresponde a qualquer caractere que não esteja entre os colchetes

#Correspondências sem diferenciar letras maiúsculas de minúsculas

regex1 = re.compile('RoboCop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('robOcop')
regex4 = re.compile('RobocOp')

robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()
#'RoboCop'
robocop.search('ROBOCOP protects the innocent.').group()
#'ROBOCOP'
robocop.search('Al, why does your programming book talk about robocop somuch?').group()
#'robocop'

# Substituindo strings com o método sub()
namesRegex = re.compile(r'Agent \w+')
>>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
#'CENSORED gave the secret documents to CENSORED.'

agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
#A**** told C**** that E**** knew B**** was a double agent.'

#Administrando regexes complexas

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # código de área
(\s|-|\.)? # separador
\d{3} # primeiros 3 dígitos
(\s|-|\.) # separador
\d{4} # últimos 4 dígitos
(\s*(ext|x|ext.)\s*\d{2,5})? # extensão
)''', re.VERBOSE)

#Combinando re.IGNORECASE, re.DOTALL e re.VERBOSE
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL |re.VERBOSE)

