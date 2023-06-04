import tkinter as tk
import buscar_functions

def buscar_button_action():
    ingredientes = ingredientes_entry.get()
    tempo = int(tempo_entry.get())

    ingr_list_input = ingredientes.split(',')
    ingr_list_input = [e.strip() for e in ingr_list_input]

    results = buscar_functions.buscar_receitas_for(ingr_list_input, tempo)

    #Limpar caixa de resultados
    result_text.configure(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)

    print(len(results))

    for result in results:
        receita_index = result['recipe']
        receita = buscar_functions.receitas_global[receita_index]

        tempo = sum(receita['timers'])
        ingr_list = receita['ingredients']
        passos = receita['steps']

        #Titulo
        result_text.insert(tk.END, f"Receita: {receita['name']}\n", 'bold2')

        #Tempo
        result_text.insert(tk.END, f"Tempó : ")
        result_text.insert(tk.END, f"{tempo} minutos \n", 'ok' if result['in_time'] else 'warning')

        result_text.insert(tk.END, "-----------------\n")

        #Ingredientes
        result_text.insert(tk.END, f"Ingredientes: \n", 'bold2')

        for index, ingr in enumerate(ingr_list):
            result_text.insert(tk.END, f"Ingrediente {index+1}: ", 'bold')
            result_text.insert(tk.END, f"{ingr['quantity']} de ")
            result_text.insert(tk.END, f"{ingr['name']} \n", 'ok' if  ingr['name'].strip().lower() in ingr_list_input else 'warning')

        result_text.insert(tk.END, "\n")

        #Passo a Passo
        
        result_text.insert(tk.END, f"Passo a Passo: \n", 'bold2')

        for passo_i, passo_text in enumerate(passos):
            result_text.insert(tk.END, f"Passo {passo_i+1}:", 'bold')
            result_text.insert(tk.END, f" {passo_text} \n")

        #Separador
        result_text.insert(tk.END, "-----------------\n")
        result_text.insert(tk.END, "\n")
        result_text.insert(tk.END, "\n")


    result_text.configure(state=tk.DISABLED)


#Janela principal
window = tk.Tk()
window.title("Search")

#Ingredientes input
ingredientes_label = tk.Label(window, text="Ingredientes:")
ingredientes_label.pack(pady=5)
ingredientes_entry = tk.Entry(window)
ingredientes_entry.pack(pady=5)

#Tempo input
tempo_label = tk.Label(window, text="Tempo:")
tempo_label.pack(pady=5)
tempo_entry = tk.Entry(window)
tempo_entry.pack(pady=5)

#Botao de buscar
buscar_button = tk.Button(window, text="Buscar", command=buscar_button_action)
buscar_button.pack(pady=5)

#Caixa de texto dos resultados
result_text = tk.Text(window, height=10, width=40)
result_text.pack(pady=5, fill='both',expand=True)
result_text.configure(state=tk.DISABLED)

#Estilos
result_text.tag_config('warning', foreground="red")
result_text.tag_config('ok', foreground="green")
result_text.tag_config('bold', font=('Helvetica', 10, 'bold'))
result_text.tag_config('bold2', font=('Helvetica', 11, 'bold'))


window.mainloop()