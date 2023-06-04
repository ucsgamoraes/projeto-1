import json

receitas_global = {}

try:
    f = open("receitas.json", "r", encoding="utf-8")
    text = f.read()
    receitas_global = json.loads(text)
except:
    print("error")

def buscar_receitas_for (ingr_list, max_time):
    result = []

    for index, receita in enumerate(receitas_global):
        ingredientes = [e['name'].strip().lower() for e in receita['ingredients']]
        time = sum(receita['timers'])
        matches = 0
        percentage = 0.0
        for ingr in ingr_list:
            if ingr in ingredientes:
                matches += 1

        percentage = matches/len(ingredientes)


        if matches > 0:
            result.append({
                'match': percentage,
                'in_time': time < max_time,
                'recipe': index
            })

    sorted_results = sorted(result, key=lambda x: x['match'], reverse=True)

    return sorted_results