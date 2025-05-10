#Primeira questão
#Observe o trecho de código abaixo: 
#int INDICE = 13, SOMA = 0, K = 0; 
#Enquanto K < INDICE faça 
# { K = K + 1; SOMA = SOMA + K; }
#Imprimir(SOMA); 
#Ao final do processamento, qual será o valor da variável SOMA? 

indice = 13
soma = 0
k = 0

def imprimirSoma(indice, soma, k):
    while(k < indice):
        k = k +1
        soma = soma + k
    return soma

##O print de soma será 91
print(imprimirSoma(indice, soma, k))     