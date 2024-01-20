lista = []

while True:
    print('[1] Para inserir novo produto\n'
                    '[2] Para apagar algum produto\n'
                    '[3] Para ver os produtos da lista\n')

    opcoes = int(input('O que deseja fazer? '))

    if opcoes == 1:
        inserir = input('O que deseja inserir na lista? ').capitalize()
        lista.append(inserir)
        print('Produto inserido com sucesso!')
        print('*'*30)

    elif opcoes == 2:
        deletar = input('O que deseja apagar da sua lista? ').capitalize()
        if deletar in lista:
             lista.remove(deletar)
             print(f'{deletar} removido da lista com sucesso!')
             print('*' * 30)
        else:
            print(f'{deletar} não encontrado na lista.')
    
    elif opcoes == 3:
            print(f'Sua lista tem {len(lista)} produtos e os produtos nela são: ')
            for produto in lista:
                print(produto)
            break
    else:
         print('Opção inválida. Tente novamente.')