import random
import datetime
import pandas as pd


control_sys = "roda"

while control_sys == "roda": # while que sempre reinicia o sistema e age em conjunto com o while da classe
  ids = [] # ids dos profs e alunos
  informacoes_gerais = {} # dicionario com os dados dos professores e dos alunos
  control_class = "roda" # faz com que a classe reinicie a cada iteração
  
  
  while control_class == "roda": # while que roda a classe e permite o controle de reinicio com entradas invalidas
    class Sistema:
      def __init__(self, classificacao):
        self.id = "" # constroi a variavel id com self para ser acessivel facilmente
        self.classificacao = classificacao # diz que classificacao é igual ao valor inputado pelo usuario (1 ou 2)

        if self.classificacao == 2:
          self.classificacao = "professor" 
        elif self.classificacao == 1:
          self.classificacao = "aluno"
        else: 
          print("mds veyr")
          control_class = "não roda" # dá break fazendo a classe reiniciar, uma vez 

      def gerar_id(self): # define a função que vai gerar id's e herda self p lidar com a variavel self.id
        while True: # while que faz repetir até a primeira condicional ser valida
            self.id = "".join(random.choices("0123456789", k=3)) # gera um id com 3 digitos aleatorios no intervalo de [0, 9]
            if id not in ids: # se o id gerado não estiver em ids, 
              ids.append(id) # adiciona id a ids (considera que id é um id totalmente novo, ele vem p cadastro/matricula)
              break # para o loop, ja que conseguiu gerar o id novo
            else:
              self.id = "" # redefine a variavel self.id para começar uma nova iteração limpa

      def cadastrar_pessoa(self): # função que cadastra/matricula
        if self.classificacao == "professor":
          self.gerar_id()
          self.nome_prof = input("Digite o seu nome: ")
          while True: # faz o usuario inserir a data de nascimento corretamente
            self.nascimento = input("Digite sua data de nascimento (xx/xx/xxxx): ")
            if len(self.nascimento) != 10: # se a data de nascimento for menor q 10 digitos (n seguindo o padrao estabelecido) ele  insere dnv
              print("Insira corretamente sua data de nascimento.")
              print("") # /n elegante
            else:
              subsequencia = self.nascimento[-4:]
              if subsequencia < 1924:
                da_continuidade = input("Você é um vampiro???")
                if da_continuidade.upper() in ["SIM.", "SIM"]:
                  print("socororrorr..")
                  pass
                else:
                  print("Você é um abobalhado veyr")
                  control_class = "não roda"
              break
          self.disciplina = input("Digite a disciplina que você leciona: ")
          informacoes_gerais[self.id] = {'NASCIMENTO' : self.nascimento, 'NOME' : self.nome_prof, 'DISCIPLINA' : self.disciplina}
          print(f"Esse é o seu ID: {self.id}")
          
        elif self.classificacao == "aluno":
          self.gerar_id()
          self.nome_aluno = input("Digite o seu nome: ")
          if datetime.datetime.now().year - self.nascimento[-4:] == 12:
            self.turma = "sexto"
          elif datetime.datetime.now().year - self.nascimento[-4:] == 13:
            self.turma = "sétimo"
          elif datetime.datetime.now().year - self.nascimento[-4:] == 14:
            self.turma = "oitavo"
          elif datetime.datetime.now().year - self.nascimento[-4:] == 15:
            self.turma = "nono"
          elif datetime.datetime.now().year - self.nascimento[-4:] == 11:
            self.turma == "quinto"
          elif datetime.datetime.now().year - self.nascimento[-4:] == 10:
            self.turma == "quarto"
          elif datetime.datetime.now().year - self.nascimento[-4:] == 9:
            self.turma == "terceiro"
          elif datetime.datetime.now().year - self.nascimento[-4:] == 8:
            self.turma == "segundo"
          elif datetime.datetime.now().year - self.nascimento[-4:] == 7:
            self.turma == "primeiro"
          elif datetime.datetime.now().year - self.nascimento[-4:] in [6, 5]:
            self.turma == "maternal"
          elif datetime.datetime.now().year - self.nascimento[-4:] > 19:
            self.turma == "EJA"
          elif datetime.datetime.now().year - self.nascimento[-4:] == 16:
            self.turma == "primeiro - médio"
          elif datetime.datetime.now().year - self.nascimento[-4:] == 17:
            self.turma == "segundo - médio"
          elif datetime.datetime.now().year - self.nascimento[-4:] in [19, 18]:
            self.turma == "terceiro - médio"
          informacoes_gerais[self.id] = {'NASCIMENTO' : self.nascimento, 'NOME' : self.nome_aluno, 'TURMA' : self.turma}
          print(f"Esse é o seu ID: {self.id}")

      def consultar_pessoa(self):
        df = pd.DataFrame(informacoes_gerais).T
        seu_id = input("Digite o seu ID: ")
        print("Aqui estão seus dados: ")
        print("")
        print(df.loc[seu_id])

parametro_init = input("Se você for professor, digite 2; se for aluno, digite 1: ") # dita a classificacao
obj = Sistema(parametro_init)
print("Bem vindo(a) ao Catálogo Escolar!")
print("")
consulta_ou_cadastro = input("Se você deseja se cadastrar no sistema, digite 1; caso queira consultar dados, digite 2")
if consulta_ou_cadastro == 1:
  obj.cadastrar_pessoa()

    dados = {
        'Alice': {'idade': 25, 'altura': 1.70, 'cidade': 'São Paulo', 'profissão': 'Engenheira'},
        'Paulo': {'idade': 30, 'altura': 1.75, 'cidade': 'Rio de Janeiro', 'profissão': 'Médico'}
    }

    # Adicionando os dados de Roberta
    dados['Roberta'] = {'idade': 22, 'altura': 1.65, 'cidade': 'Belo Horizonte', 'profissão': 'Designer'}

    import pandas as pd

    # Estrutura de dados inicial
    dados = {
        'Alice': {'idade': 25, 'altura': 1.70, 'cidade': 'São Paulo', 'profissão': 'Engenheira'},
        'Paulo': {'idade': 30, 'altura': 1.75, 'cidade': 'Rio de Janeiro', 'profissão': 'Médico'}
    }

    # Adicionando os dados de Roberta
    dados['Roberta'] = {'idade': 22, 'altura': 1.65, 'cidade': 'Belo Horizonte', 'profissão': 'Designer'}

    # Convertendo o dicionário em um DataFrame
    df = pd.DataFrame(dados).T  # Transpõe o DataFrame para que os nomes sejam as linhas

    # Exibindo apenas as informações de Paulo
    print(df.loc['Paulo'])

