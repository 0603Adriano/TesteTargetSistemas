"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule
a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
"""

num = int(input("Digite um número para verificar se este pertence a sequência fibonacci: "))
a, b = 0, 1
fibonacci = []

while a <= num:
        fibonacci.append(a)
        a, b = b, a+b

print(fibonacci)

if (num in fibonacci):
    print("O número pertence a sequência Fibonacci")
else:
    print("O número NÃO pertence a sequência Fibonacci")