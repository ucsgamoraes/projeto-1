import json

receitas = {}

try:
    f = open("receitas.json", "r")
    text = f.read()
    receitas = json.loads(text)
except:
    print("error")

#ingredientes_input = input("Digite os ingrediente separados por virgulas: ")
ingredientes_input = "water"
ingr_list = ingredientes_input.split(',')
ingr_list = [e.strip() for e in ingr_list]
#data.list.find( record => record.name === "my Name")

result = []

for index, receita in enumerate(receitas):
    receita_ingr = [e['name'].strip().lower() for e in receita['ingredients']]
    matches = 0
    percentage = 0.0
    for ingr in ingr_list:
        if ingr in receita_ingr:
            matches += 1
    percentage = matches/len(receita_ingr)

    if percentage >= 0.2:
        result.append({
            'match': percentage, 
            'recipe': index
        })

print(result)