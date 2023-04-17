import json

with open('data.json', 'r') as arquivo:
    dados = json.load(arquivo)

meuarray = []    
   
for lista in dados:
    meuarray.append(lista) 

for item in meuarray:
    if item[2].isdigit():
        item[2],item[3] = item[3], item[2]
        if item[2].isdigit():
            item[2] = 'NULL'
               
for item in meuarray:        
    if item[3].isalpha():
        item[3] = 'NULL'

for item in meuarray:
    ano, mes, dia = item[5].split("-")
    item[5] = dia + "-" + mes + "-" + ano

meuarray = list(set(tuple(item) for item in meuarray))

meuarray = [list(item) for item in meuarray]

meuarray.sort(key=lambda x: x[4], reverse=True)

with open('resultado.json', 'w') as f:
    json.dump(meuarray, f)


















