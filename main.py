import random
import pandas as pd

ids = []
# dicionario com os dados dos professores e dos alunos
informacoes_gerais = {}

class Sistema:
  def __init__(self, classificacao):
    self.classificacao = classificacao
    # classificacao dita se é professor ou aluno, entra 1 ou 2
    # inputa 1 ou 2
    if self.classificacao == 2:
      self.classificacao = "professor"
    elif self.classificacao == 1:
      self.classificacao = "aluno"

  def gerar_id(self):
    while True:
        id = "".join(random.choices("0123456789", k=3))
        if id not in ids:
            ids.append(id)
            break



  def cadastrar_pessoa(self):
    if self.classificacao == "professor":

    #while true c var do qual em baixo do while tem um bgl q faz repetir ou nao o programa
