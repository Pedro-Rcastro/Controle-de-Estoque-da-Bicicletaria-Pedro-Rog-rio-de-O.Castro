#exercício 4 de 4
listaPecas = [] #
def cadastrarPeca(codigo): # FUNÇÃO CADASTRAR PEÇAS
  print('Selecionada a opção "Cadastrar Peça"')
  print('O código da peça é: {:0>3}'.format(codigo))
  nome = input('Entre com o nome da peça:')
  fabricante = input('Entre com o fabricante da peça:')
  valor = float(input('Entre com o valor R$ da peça:'))
  dicionarioPecas = {'codigo' : codigo,
                     'nome' : nome,
                     'fabricante': fabricante,
                     'valor': valor}
  listaPecas.append(dicionarioPecas.copy())
def consultarPeca(): # FUNÇÃO COSULTAR PEÇAS
  while True:
    try:
      print('Você Selecionou a Opção de Consultar Peças')
      opConsultar = int(input('Entre com a opção desejada\n'
                                 '1- Consultar Todas as Peças\n'
                                 '2- Consultar Peças por Código\n'
                                 '3- Consultar Peças por Fabricante\n'
                                 '4- Retornar\n-->'))
      if opConsultar == 1:
          print('-' * 20)
          for pecas in listaPecas:
              for key, value in pecas.items(): print('{} : {}'.format(key,value))
              print('-' * 20)
      elif opConsultar == 2:
            print('Você Selecionou a Opção Peças por Código')
            entrada = int(input('Digite o Código: '))
            print('-' * 20)
            for pecas in listaPecas:
             if(pecas['codigo'] == entrada):
              for key, value in pecas.items():
                print('{} : {}'.format(key,value))
              print('-' * 20)
      elif opConsultar == 3:
              print('Você Selecionou a Opção Peças por Fabricante')
              entrada = input('Digite o Fabricante: ')
              print('-' * 20)
              for pecas in listaPecas:
                    if(pecas['fabricante'] == entrada):
                      for key, value in pecas.items():
                        print('{} : {}'.format(key,value))
                      print('-' * 20)
      elif opConsultar == 4:
                   break
      else:
                print('Por favor digite somente o que pede')
                continue
    except ValueError:
            print('Por Favor pare de digitar números que não existe...')
            continue
def removerPeca(): # FUNÇÃO REMOVER PEÇAS
    print('Você Selecionou o Remover Peça')
    entrada = int(input('Digite o Código da peça que irá remover: '))
    for pecas in listaPecas:
      if(pecas['codigo'] == entrada):
        listaPecas.remove(pecas)
      else:
          print('Você removeu o código.')
print('***Controle de Estoque da Bicicletaria Pedro Rogério de O.Castro RU 4505802')
registroPecas = 0
while True:
    try:
      opcao = int(input('Digite a opção desejada:\n'
                                  '1- Cadastrar Peças\n'
                                  '2- Consultar Peças\n'
                                  '3- Remover Peças\n'
                                  '4- Sair\n-->'))
      if opcao == 1:
        registroPecas = registroPecas + 1
        cadastrarPeca(registroPecas)
      elif opcao == 2: consultarPeca()
      elif opcao == 3: removerPeca()
      elif opcao == 4:
        print('*Programa finalizado pelo operador*')
        break
      else:
        print('Digite somente as opções do MENU')
        continue
    except ValueError:
        print('*Numeração inexistente...')




