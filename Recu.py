# COPIE E COLE ESTE ENUNCIADO NO TERMINAL EM UM ARQUIVO .py. 
# Para executar no terminal use "python3 nome_arquivo.py"
# Use somente o Classroom e o GitHub. Uso do Google ou qualquer tipo de IA = zero!
# Link GitHub professor: https://github.com/profpatrickoli/1TRI-DesSistemas
# 1) (0,5 p) Crie variáveis para armazenar seu nome, nota da prova escrita, série e turma. Após isso, mostre no terminal uma mensagem personalizada se apresentando.

nome = "Nicolas"
NOTAescrita = 3
serie = "3"
turma =  "DS c"


print ('ola meu nome é', nome,'da turma do', serie, turma)

# 2) (0,5 p) Crie uma lista com 3 atividades que você gosta de fazer no final de semana.

atividades = ["dormir", "churrasco", "estudar"]

# 3) (1,0 p) Crie uma condição que verifica se sua nota da prova é maior que a média 1,8.


print ('ola meu nome é', nome,'da turma do', serie, turma)

if ( NOTAescrita <= 1,8 ) :
    print ("finalmente venceu na vida")
else : 
    print ("você é um falido")

# 4) (1,0 p) Crie uma função mostra no terminal a quantidade de litros de água que devem ser consumidos diariamente por uma pessoa. Depois execute a função colocando um peso como parâmetro.
# Para calcular, siga a fórmula: qtd_litros = 0,035 * peso.

peso = 60 

def aguaBEBER() :
    qtd_litros = 0.035 * peso 
    print ("vocẽ deve beber", qtd_litros,"litros de agua")


aguaBEBER()

# 5) (1,0 p) Crie um código que verifica se "estudar" existe na lista criada da questão 2. Use o laço de repetição que preferir.

for atividade in atividades : 
    if  (atividade == "estudar"):
        print('essa atividade é estudar')
    else :
        print('essa atividade não é estudar')


# 6) (1,0 p) Crie um laço de repetição que conta de 1 a 128, mas ao invés de somar 1 no contador, multiplique-o por 2.


contador = 1
while contador <= 128:
    print(contador)
    contador = contador * 2



