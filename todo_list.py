 
guardar_tarefas = []

while True: 
  print("1 - Adicionar tarefas") 
  print("2 - Ver total de tarefas adicionada")
  print("3 - Listar tarefas")
  print("4 - Excluir tarefa da lista")
  print("5 - Sair")
  opcao = input("Escolha uma opção:")
    
    
  if opcao  == "1":
       tarefa = input("Digite a tarefa: ")
       guardar_tarefas.append(tarefa)

  elif opcao == "2":
       print(len(guardar_tarefas))

  elif opcao == "3":
       for número, tarefa in enumerate(guardar_tarefas, 1):   
            print(número, "-" ,tarefa)

  elif opcao == "4":  
       número = input("Qual número deseja excluir? ") 
       del  guardar_tarefas[int(número) - 1]
             
  elif opcao == "5":
       print("Até logo!")
       break
      
  else : 
       print("Opção inválida,tente novamente.")
                       