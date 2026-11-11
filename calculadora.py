def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2

def ler_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero

        except ValueError:
            print('Digite um número válido!')


def ler_numeros():
    n1 = ler_numero('1º número: ')
    n2 = ler_numero('2º número: ')
    return(n1, n2)



while True:
    print('=' * 25)

    print('1. Adição          [+]')
    print('2. Subtração       [-]')
    print('3. Multiplicação   [*]')
    print('4. Divisão         [/]')
    print('5. Sair')

    print('=' * 25)

    try :
        opcao = int(input('Escolha um número: '))

    except ValueError:
        print('Digite apenas números!')
        continue
    
    if opcao == 1:
        print('Adição')
        n1, n2 = ler_numeros()

        total = somar(n1, n2)
        print(f'Resultado: {total}')
      

    elif opcao == 2:
        print('Subtração')
        n1, n2 = ler_numeros()

        total = subtrair(n1, n2)
        print(f'Resultado: {total}')
           
    elif opcao == 3:
        print('Multiplicação')
        n1, n2 = ler_numeros()

        total = multiplicar(n1, n2)
        print(f'Resultado: {total}')
        
    elif opcao == 4:
        print('Divisão')
        n1 = ler_numero('1º número: ')

        while True:
            n2 = ler_numero('2º número: ')
            if n2 != 0:
                total = dividir(n1, n2)
                print(f'Resultado: {total}')
                break
            else:
                print('Segundo valor não pode ser ZERO!')
                      

    elif opcao == 5:
        print('Até depois...')
        break
    else:
        print('Não tem essa opção! Tente novamente.')

    

    
    