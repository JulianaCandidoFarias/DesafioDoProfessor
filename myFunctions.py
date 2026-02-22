
""" Exercicio N°1 """
def OlaMundo():
    return print("Ola Mundo!")

""" Exercicio N°2 """
def InformaNumero():
    numero = int(input("Insira um numero inteiro: "))
    return print("O numero informado foi:", numero)

""" Exercicio N°3 """
def SomaDeDois():
    num1 = int(input("Informe um primeiro numero: "))
    num2 = int(input("Agora Informe o segundo numero: "))

    return print("A soma dos dois numero é:", num1 + num2)

""" Exercicio N°4 """
def MediaBimestral():
    media = 0
    for i in range(4):
        nota = int(input(f"Insira sua {i + 1}º, nota: "))
        media += nota

    return print(f"Sua média bimestral foi de: {media / 4:.2f}")

""" Exercicio N°5 """
def MetroEmCentimetro():
    metro = int(input("Insira, em metros, um valor: "))
    return print(f"{metro}m equivale á {metro * 100}cm")
    
""" Exercicio N°6 """
def AreaDoCirculo():
    raio = int(input("Insira o raio de um circulo: "))
    return print(f"{raio} de raio equivale a um circulo de: {3.14 * (raio ** 2)} de area")

""" Exercicio N°7 """
def CalculaQuadrado():
    lado = int(input("Insira o perimetro do lado de um quadrado: "))
    area = lado * lado
    return print(f"A area do teu quadrado é de: {area} \nE o dobro da area é de: {area * 2}")

""" Exercicio N°8 """
def CalculaSalario():
    hora = float(input("Insira a quantia que voce recebe por hora trabalhada: "))
    dia = hora * 8
    return print(f"Por mês voce recebe: {dia * 26:.2f}")

""" Exercicio N°9 """
def CalculaCelcius():
    fahrenheit = int(input("Insira em fahrenheit uma temperatura qualquer:"))
    celcius = (fahrenheit - 32) / 1.8
    return print(f"Tua temperatura em fahrenheit equivale á {celcius:.2f}° celcius")

""" Exercicio N°10 """
def CalculaFahrenheit():
    celcius = int(input("Insira em celcius uma temperatura qualquer:"))
    fahrenheit = (celcius * 1.8) + 32
    return print(f"Tua temperatura em celcius equivale á {fahrenheit:.2f}° fahrenheit")

""" Exercicio N°11 """
def CalculaNumeros():
    intNum1 = int(input("Insira um numero inteiro: "))
    intNum2 = int(input("Insira agora um segundo numero inteiro: "))

    floatNum = float(input("Insira um numero real, ou seja, quebrado: "))

    operacao1 = (intNum1 * 2) + (intNum2 / 2)
    operacao2 = (3 * intNum1) + floatNum
    operacao3 = floatNum ** 3

    def Mensagens():
        print(f"O produto do dobro da primeira com a metade do segundo é: {operacao1}")
        print(f"A soma do triplo do primeiro com o terceiro é: {operacao2:.2f}")
        print(f"O terceiro elevado ao cubo é: {operacao3:.2f}")
    
    return Mensagens()

