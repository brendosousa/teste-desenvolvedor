# Segunda questão
#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 
    
def fibonacci(n):
    a = 0 
    b = 1
    while a < n:
        a = b
        b = a + b
    return a == n

def pertence_fibonacci(n):
    if fibonacci(n):
        return f"O número {n} está sequência de Fibonacci."
    else:
        return f"O número {n} não está na sequência de Fibonacci."
    
input_numero = int(input("Digite um número: "))
print(pertence_fibonacci(input_numero)) 