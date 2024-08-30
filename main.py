
#Exercício 1
def fibonacci():
    try:
        valor = int(input("Informe um número: "))

        checagem = 1
        i = 0
        while checagem < valor:
            auxiliar = checagem
            checagem = checagem + i
            i = auxiliar

        if checagem == valor:
            print("O valor informado, está presente na sequência de Fibonacci!")
        else:
            print("O valor informado, não está presente na sequência de Fibonacci!")
    except ValueError:
        print("Você informou um valor não numérico!")


#Exercício 2
def checarA():
    texto = input("Informe uma texto: ")
    contador = 0
    for caracter in texto:
        if (caracter == "a" or caracter == "A"):
            contador += 1

    if contador == 0:
        print("Não há nenhuma letra A nesse texto!")
    else:
        print(f"Há {contador} letra(s) A nesse texto!")


#Exercício 3
"""
Como a sequência descrita no exercício é 'K = K + 1; SOMA = SOMA + K;', o resultado é 77. 
Se fosse invertido, ou seja, primeiro a soma e depois o incremento, seria 66.
"""
def calcula():
    INDICE = 12
    SOMA = 0
    K = 1

    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K

    print(SOMA)


if __name__ == '__main__':
    fibonacci()
    checarA()
    calcula()