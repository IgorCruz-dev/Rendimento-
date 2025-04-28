while True:
    try:
        rendimento = float(input('Digite o rendimento da lata em M²: '))

        if rendimento > 0:
            altura = float(input('Digite a altura da parede em M²: '))
            largura = float(input('Digite a largura da parede em M²: '))
            qnt_latas = round((largura * altura) / rendimento)

            print(f'A quantidade necessária é de aproximadamente {qnt_latas} latas')
            while True:
                saida = input('Deseja sair do sistema? \n Digite sim ou não: ').lower()
                if saida in ['não', 'nao', 'Não', 'Nao']:
                    break
                elif saida == 'sim':
                    print('Até logo!')
                    break
                else:
                    print('Digite uma resposta válida!')
        else:
            print('Digite um valor válido!')
            var = input('Aperte ENTER para digitar novamente...')
            continue

    except ValueError:
        print('Digite um valor válido!')
        var = input('Aperte ENTER para digitar novamente...')
        continue

    if saida == 'sim':
        print('Volte sempre!')
        break
