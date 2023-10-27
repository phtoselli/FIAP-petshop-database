import os
import cx_Oracle
import pandas as pd

# -- Database connection -- #
try:
  dsnStr = cx_Oracle.makedsn("?????", "?????", "?????")
  conn   = cx_Oracle.connect(user='?????', password="?????", dsn="?????")

  #Module instructions
  inst_create = conn.cursor()
  inst_read   = conn.cursor()
  inst_update = conn.cursor()
  inst_delete = conn.cursor()
except Exception:
  print("Error: ", Exception)
  connection = False
else:
  connection = True

# -- Program -- #
while connection:
  os.system('cls') #clean terminal

  print("---- PET SHOP ----")
  print("""
    1 - Cadastrar Pet
    2 - Listar Pets
    3 - Editar Pet
    4 - Excluir Pet
    5 - EXCLUIR TODOS OS PETS
    6 - SAIR
  """)

  user_entry = int(input("Escolha uma opção do menu -> "))

  if user_entry.isdigit():
    user_entry = int(user_entry)
  else:
    user_entry = 6
    print("Escolha inválida, por favor digite um número válido.")
  os.system('cls')

  match user_entry:
    case 1:
      try:
        print("---- CADASTRAR PET ----")
        pet_type = input("Digite o tipo : ")
        pet_name = input("Digite o nome : ")
        pet_age  = input("Digite a idade : ")

        register_query = f""" INSERT INTO pets (pet_type, pet_name, pet_age) VALUES ('{pet_type}', '{pet_name}', {pet_age}) """

        inst_create.execute(register_query)
        conn.commit()

      except ValueError:
        print("O valor 'idade' precisa ser um número")
      except:
        print("Erro ao inserir novo valor no Banco de dados")
      else:
        print("Pet cadastrado com sucesso!")
      input("Presione ENTER")

    case 2:
      print("---- CADASTRAR PET ----")
      data_list = []
      inst_read.execute('SELECT * FROM pets')
      data = inst_read.fetchall()

      for pet in data:
        data_list.append(pet)

      data_list = sorted(data_list)
      data_df = pd.DataFrame.from_records(data_list, columns=['Id', 'Tipo', 'Nome', 'Idade'], index='Id')

      if data_df.empty:
        print(f"Não há um Pets cadastrados!")
      else:
        print(data_df)
      print("Pets listados com sucesso!")
      input("Pressione ENTER")

    case 3:
      try:
        print("---- ALTERAR PET ----")
        data_list = []
        pet_id = int(input("Digite um id: "))
        search_query = f""" SELECT * FROM pets WHERE {pet_id}"""

        inst_read.execute(search_query)
        data = inst_read.fetchall()

        for pet in data:
          data_list.append(pet)

        if len(data_list) == 0:
          print(f"Não há nenhum pet cadastrado com o ID = {pet_id}")
          input("Pressione ENTER")
        else:
          new_type = input("Digite um novo tipo : ")
          new_name = input("Digite um novo nome : ")
          new_age  = input("Digite uma nova idade : ")

          change_query = f""" UPDATE pets SET pet_type='{new_type}', pet_name='{new_name}', pet_age='{new_age}' WHERE id={pet_id}"""

          inst_update.execute(change_query)
          conn.commit()
      except ValueError:
        print("O valor 'idade' precisa ser um número")
      except:
        print("Erro ao editar valor no Banco de dados")
      else:
        print("Dados atualizados com sucesso!")
        input("Presione ENTER")

    case 4:
      print("---- DELETAR PET ----")
      data_list = []
      pet_id = input("Digite um id: ")

      if pet_id.isdigit():
        pet_id = int(pet_id)
        search_query = f""" SELECT * FROM pets WHERE {pet_id}"""

        inst_read.execute(search_query)
        data = inst_read.fetchall()

        for pet in data:
          data_list.append(pet)

        if len(data_list) == 0:
          print(f"Não há nenhum pet cadastrado com o ID = {pet_id}")
        else:
          delete_query = f"DELETE FROM pets WHERE id={pet_id}"
          inst_delete.execute(delete_query)
          conn.commit()
          print("Pet deletado com sucesso!")
      else:
        print("O id não é numérico!")
      input("Pressione ENTER")

    case 5:
      print("---- DELETAR TODOS OS DADOS DA TABELA DE PETS ----")
      confirm = input("CONFIRMAR A EXCLUSÃO DE TODOS OS PETS? [S]sim ou [N]ão ?")
      if confirm.upper() == "S":
        inst_delete.execute("DELETE FROM pets")
        conn.commit()

        data_reset_ids = """ALTER TABLE pets MODIFY(ID GENERATED AS IDENTITY (STARTS WITH 1)) """
        inst_delete.execute(data_reset_ids)
        conn.commit()

        print("Todos os registros foram excluidos!")
      else:
        print("Operação cancelada pelo usuário!")
      input("Pressione ENTER")

    case 6:
      connection = False
    case _:
      input("Digite um número entre 0 e 6.")
else:
  print("Obrigado!")
cl