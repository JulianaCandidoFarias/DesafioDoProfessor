
import myFunctions, os

AllFunctions = [
    myFunctions.OlaMundo,
    myFunctions.InformaNumero,
    myFunctions.SomaDeDois,
    myFunctions.MediaBimestral,
    myFunctions.MetroEmCentimetro,
    myFunctions.AreaDoCirculo,
    myFunctions.CalculaQuadrado,
    myFunctions.CalculaSalario,
    myFunctions.CalculaCelcius,
    myFunctions.CalculaFahrenheit,
    myFunctions.CalculaNumeros
]

def CarregaNomes():
    for i in range(11):
        print(f"{i + 1}. {AllFunctions[i].__name__}")

def EscolhePrograma():
    programa = int(input("\nInsira um numero entre 1 ao 11 para\na execução do programa --> "))
    return programa - 1

def ExecutaFuncao(numero):
    print("\n ")
    print(f"---> {AllFunctions[numero].__name__}")
    AllFunctions[numero]()
    print("\n ")

os.system('cls' if os.name == 'nt' else 'clear')

print("-----------------------------------")
print("------[ Desafio Valendo 100 ]------")
print("-----------------------------------")

print("Neste Programa voce podera escolher\nentre 11 programas diferente para á\nexecução!\n")

CarregaNomes()
programNumber = EscolhePrograma()
ExecutaFuncao(programNumber)

escolha = str(input("Deseja execeutar outro programa?\n'S' para sim 'N' para não --> "))
while escolha == "S" or escolha == "s":
    os.system('cls' if os.name == 'nt' else 'clear')

    CarregaNomes()
    programNumber = EscolhePrograma()
    ExecutaFuncao(programNumber)

    escolha = str(input("Deseja executar outro programa?\n'S' para sim 'N' para não --> "))