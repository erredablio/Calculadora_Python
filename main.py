def decisor():
    decisor = int(input("\nDeseja realizar uma nova operação? [1 - Sim] [2 - Não]: "))
    match decisor:
        case 1:
            calculadora()
        case _:
            exit

def somar(n1, n2):
    equacao = n1 + n2
    print(f"\n{n1} + {n2} = {equacao}")

def subtrair(n1, n2):
    equacao = n1 - n2
    print(f"\n{n1} - {n2} = {equacao}")

def multiplicar(n1, n2):
    equacao = n1 * n2
    print(f"\n{n1} * {n2} = {equacao}")

def dividir(n1, n2):
    equacao = n1 / n2
    print(f"\n{n1} / {n2} = {equacao:.2f}")

def calculadora():
    n1 = float(input("Informe o primeiro valor: "))
    n2 = float(input("Informe o segundo valor: "))
    operador = input("Selecione o operador [+] [-] [*] [/]: ")
    match operador:
        case "+":
            somar(n1, n2)
            decisor()
        case "-":
            subtrair(n1, n2)
            decisor()
        case "*":
            multiplicar(n1, n2)
            decisor()
        case "/":
            dividir(n1, n2)
            decisor()
        case _:
            print("Operador inválido")
            decisor()

if __name__ == "__main__":
    calculadora()
