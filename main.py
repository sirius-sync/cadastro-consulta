import random
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

        while True:
          self.nascimento = input("Digite sua data de nascimento (xx/xx/xxxx)")
          if len(self.nascimento) != 10:
            print("Insira corretamente sua data de nascimento.")
            print("")
          else:
            subsequencia = self.nascimento[-4:]
            if self.nascimento < 1924:
              da_continuidade = input("Você é um vampiro???")
              if da_continuidade.upper() in ["SIM.", "SIM"]:
                pass
              else:
                print("Você é um abobalhado veyr")
                control_class = "não roda"
            break

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
          informacoes_gerais[self.id] = {'NASCIMENTO' : self.nascimento}


dados = {
    'Alice': {'idade': 25, 'altura': 1.70, 'cidade': 'São Paulo', 'profissão': 'Engenheira'},
    'Paulo': {'idade': 30, 'altura': 1.75, 'cidade': 'Rio de Janeiro', 'profissão': 'Médico'}
}

# Adicionando os dados de Roberta
dados['Roberta'] = {'idade': 22, 'altura': 1.65, 'cidade': 'Belo Horizonte', 'profissão': 'Designer'}
