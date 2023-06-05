# Documentação

# Programa de Busca de Receitas
Este programa é uma interface gráfica desenvolvida em Python utilizando a biblioteca Tkinter. Ele permite que o usuário informe uma lista de ingredientes e um tempo de preparo desejado para buscar por receitas que atendam a esses critérios.

## Funcionamento do Programa
O usuário insere os ingredientes desejados no campo de entrada "Ingredientes", separados por vírgulas 
e o tempo de preparo no campo de entrada "Tempo".

Ao clicar no botão "Buscar", o programa chama a função buscar_button_action(). A função buscar_button_action() busca os ingredientes e o tempo informados pelo usuário chamando função buscar_functions.buscar_receitas_for() para buscar as receitas que atendam aos critérios no arquivo receitas.json.

A função buscar_receitas_for(ingr_list, max_time) recebe uma lista de ingredientes (ingr_list) e um tempo máximo de preparo (max_time). Ela busca as receitas existentes e retorna uma lista de resultados, classificada de acordo com a correspondência de ingredientes. Cada resultado contém o valor de correspondência, se a receita pode ser preparada dentro do tempo máximo e o índice da receita correspondente.

Os resultados das receitas são exibidos na caixa de texto abaixo do botão de busca.

Cada resultado exibe o nome da receita, o tempo de preparo, a lista de ingredientes necessários e o passo a passo de preparo.

Os ingredientes que estão presentes na lista informada pelo usuário são destacados em verde, enquanto os ingredientes ausentes são destacados em vermelho.

A interface é atualizada em tempo real conforme o usuário interage com o programa.


## Requisitos
Python 3.6 ou superior

Biblioteca Tkinter (já inclusa na maioria das instalações Python)
