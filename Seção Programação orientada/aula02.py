import json

class Pessoa:
    def __init__(self, name, idade):
        self.name = name
        self.idade = idade

    def __str__(self):
        return f'{self.name},{self.idade}'  
    
    def save_json(self, filename):
        data = {
            'name': self.name, 
            'idade': self.idade
        }

        with open(filename, mode='w') as json_file:
            json.dump(data, json_file, indent=2)
            print('Arquivo criado com sucesso.')

pessoa = Pessoa('Diego', 29)
#pessoa.save_json('Diego.json')

pessoa.name = 'Mayara'
pessoa.idade = 28
pessoa.save_json('Mayara.json')