"""

Curso de Python Completo - Code Academy BR - 13 horas
Aula 02 - VS Code, terminal, variáveis e erros (00:20:10 - 00:47:08)
Conceitos e Boas práticas com variáveis; Ordem de execução e Lidando com erros.

"""

#Variáveis
#O exemplo abaixo mostra como criar uma variável e atribuir um valor a ela.
#Além de mostrar que justamente devido ao significado da palavra variável, o valor de uma variável pode ser alterado a qualquer momento.
#Basta atribuir um novo valor a ela, como no exemplo abaixo. Chamando o nome da variável e atribuindo um novo valor a ela.
#Os dois prints abaixo mostram o valor da variável antes e depois de ser alterado.

#Ordem de Execução: 
#O Python lê o código de cima para baixo, então a variável precisa ser criada antes de ser usada.
#Se eu apagar o primeiro print, o valor da variável será alterado, mas o print não mostrará o valor antigo, apenas o novo.

#NameError e Traceback:
#Se eu tentar usar uma variável que não foi criada, o Python vai me dar um erro chamado NameError, e vai mostrar um Traceback,
#que é uma lista de chamadas de funções que levaram ao erro.
#No caso abaixo, se eu tirar a primeira declaração de "texto", o erro acontecerá porque eu tentei usar a variável texto antes 
#de ela ser criada.

#Regras para nomear variáveis:
#1. O nome da variável pode conter letras, números e underscores (_), mas deve começar com uma letra ou um underscore (_)
#2. O nome da variável não pode começar com um número
#3. O nome da variável não pode conter espaços, mas pode conter underscores (_)
#4. O nome da variável não pode ser uma palavra reservada do Python, como "print", "if", "else", etc.
#5. O nome da variável deve ser curto, mas descritivo, ou seja, deve indicar o que a variável representa.
#6. O nome da variável deve ser escrito em letras minúsculas, e se for composto por mais de uma palavra,
#   as palavras devem ser separadas por underscores (_), como "nome_da_variavel".


texto = "Seu destino está a 5km"

print(texto)

texto = "Seu destino está a 4km"

print(texto)