def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mErro: Por favor, digite um valor válido\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mEntrada de dados interrompida pelo usuário\033[m")
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mErro: Por favor, digite um valor válido\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mEntrada de dados interrompida pelo usuário\033[m")
            return 0
        else:
            return n


num = leiaInt('Digite um valor inteiro: ')
print(f'O valor digitado foi {num}')
num2 = leiaFloat('Digite um valor Real: ')
print(f'O valor digitado foi {num2}')