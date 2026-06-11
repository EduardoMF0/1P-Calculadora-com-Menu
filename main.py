resultado = 0;
calculo = "";
historico_de_contas = [];
sinais_operacao = ["+", "-", "*", "x", "/", "%"];
numero1 = 0;
numero2 = 0;
sinal = "";


def adicionar_historico(resultado):
    para_historico = f"{calculo}  = {resultado}";
    historico_de_contas.append(para_historico);


def mostrar_historico():
    global numero1, numero2, sinal; # Coloquei o reset das variáveis aqui por ser mais fácil.

    print();
    print("Histórico:", end=" ");
    for calculo in historico_de_contas:
        print(f"{calculo}, ", end=" ");
    print();
    print()

    calculo = "";
    numero1 = 0;
    numero2 = 0;
    sinal = "";

print("Bem vindo a Calculadora!");
print();

print("Escreva o calculo com esses sinais, 1- Soma: +, 2- Subtração: -, 3- Multiplicação: *, 4- Divisão: / e 5- Porcentagem: %");
print ("--- Para %, escreve primeiro o valor que será a porcentagem.");
print();

print("Atenção!");
print();

print("Separe os valores do sinal com espaço, EX: 10 + 20 ou 10 % 100.");
print();
print("Caso deseje finalizar as operações escreva: SAIR")
print("---------------------------------------------------");

print("Começe os calculos:");

while True:

    while True:

        calculo = input().lower().strip();

        if calculo == "sair":
            muda = False
            break;
        
        try:
            numero1, sinal, numero2 = calculo.split();
        
            numero1 = numero1.replace(",", ".");
            numero2 = numero2.replace(",", ".");
        except ValueError:
            print("Erro! Inserção de valores inválida! A conta deve ser formatada como mostrado nos exemplos.");

        try:
            numero1 = float(numero1);
        except ValueError:
            print(f"Erro! 1º valor não é um número válido: {numero1}. Tente Novamente!");

        if sinal not in sinais_operacao:
            print("Erro! Sinal inválido, Tente Novamente!")

        try:
            numero2 = float(numero2);
        except ValueError:
            print(f"Erro! 2º valor não é um número válido: {numero2}. Tente Novamente!");

        if isinstance(numero1, float) and isinstance(numero2, float):
            break;

    if calculo == "sair":
        break;

    inputs = [numero1, sinal, numero2];

    if sinal == "+":
        resultado = numero1 + numero2;

        adicionar_historico(resultado);

        print(f"--- {calculo}= {resultado:.3f}");
        mostrar_historico();

    elif sinal == "-":
        resultado = numero1 - numero2;

        adicionar_historico(resultado);

        print(f"--- {calculo}= {resultado:.3f}");
        mostrar_historico();


    elif sinal == "*" or sinal == "x":
        resultado = numero1 * numero2;

        adicionar_historico(resultado);

        print(f"--- {calculo}= {resultado:.3f}");
        mostrar_historico();

    elif sinal == "/":
        resultado = numero1 / numero2;

        adicionar_historico(resultado);

        print(f"--- {calculo}= {resultado:.3f}");    
        mostrar_historico();

    elif sinal == "%":
        valor_decimal = numero1 / 100
        resultado = valor_decimal * numero2;

        adicionar_historico(resultado);

        print(f"--- {calculo}= {resultado:.3f}");    
        mostrar_historico();



    
    


