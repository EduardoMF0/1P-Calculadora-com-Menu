resultado = 0;

print("Bem vindo a Calculadora!");
print();

print("Escreva o calculo com esses sinais, 1- Soma: +, 2- Subtração: -, 3- Multiplicação: *, 4- Divisão: / e 5- Porcentagem: %");
print ("--- Para %, escreve primeiro o valor que será a porcentagem.");
print();

print("Atenção!");
print();

print("Separe os valores do sinal com espaço, EX: 10 + 20 ou 10 % 100.");
print();

print("Começe os calculos:");

calculo = input();

numero1, sinal, numero2 = calculo.split();

try:
    numero1 = int(numero1)
except ValueError:
    print(f"Erro, o primeiro valor não é um número válido: {numero1}. Tente Novamente!");

try:
    numero2 = int(numero2)
except ValueError:
    print(f"Erro, o segundo valor não é um número válido: {numero2}. Tente Novamente!");


if sinal == "+":
    resultado = numero1 + numero2;

    print(f"{calculo} = {resultado}");

elif sinal == "-":
    resultado = numero1 - numero2;

    print(f"{calculo} = {resultado}");

elif sinal == "*" or sinal == "x":
    resultado = numero1 * numero2;

    print(f"{calculo} = {resultado}");

elif sinal == "/":
    resultado = numero1 / numero2;

    print(f"{calculo} = {resultado}");

elif sinal == "%":
    valor_decimal = numero1 / 100
    resultado = valor_decimal * numero2;

    print(f"{calculo} = {resultado}");





# elif == "%":