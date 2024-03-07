
dicionario = dict()
print(dicionario)

dicionario = {

    'A': {'a': 10,
          'b': 20,
          'c': 30, },

    2 : {'d': 40,
        'e': 50,
        'f': 60, },

}

dicionario['A']['a'] = dicionario.get('A', 'Não encontrado').get('a', 0) + 1

print(dicionario.get('A'))
