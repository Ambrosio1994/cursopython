list_tasks = []
comandos = ['listar', 'desfazer', 'refazer']
descarte = []

while True:
    print()
    print(f'Comandos: listar, desfazer, refazer')

    task = input('Digite uma tarefa ou comando: ')

    if task == "sair":
        print('Saindo do sitema')
        break

    if task.isdigit():
        print('Você não digitou um comando ou tarefa, tente novamente.')

    elif task not in comandos:
        if task not in list_tasks:
            list_tasks.append(task)
            print()
            print('TAREFAS:')
            for task in list_tasks:
                print(task)

        else:
            print(f'A tarefa "{task}" já está na lista.')

    elif task == 'listar':
        print(list_tasks)
        print()

    elif task == 'desfazer':
        if list_tasks:
            descarte.append(list_tasks[-1])
            print()
            list_tasks.pop()
            print(f'Tarefa "{descarte[-1]}" excluída com sucesso da lista!')
            print()
            print('TAREFAS:')
            for task in list_tasks:
                print(task)

        else:
            print('Não há tarefas para desfazer.')

    elif task == 'refazer':
        if list_tasks:
            list_tasks.append(descarte[-1])
            descarte.pop()
            print(f'Tarefa "{list_tasks[-1]}" reincluída com sucesso na lista!')
            print()
            print('TAREFAS:')
            for task in list_tasks:
                print(task)

        else:
            print('Não há tarefas para refazer.')