
#definindo um dicionário:

dicionario = { 
    'cat':'chat', # conteúdo que tem em um dicionário
    'dog':'chien', # conteúdo que tem em um dicionário, lembrando que o : é para indicar que o que tem a esquerda é a chave e a direita é o valor: chave : valor
    'horse':'cheval' # conteúdo que tem em um dicionário
}

#Fazendo um loop dentro de um dicionário:

for chave in dicionario.keys():
    print(chave, '->', dicionario[chave])s