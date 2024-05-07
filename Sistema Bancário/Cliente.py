# Isso importa os módulos random e datetime do Python, que são usados para gerar números aleatórios e trabalhar com datas e horas, respectivamente.
import random
import datetime

# Isso importa as classes Conta, ContaCorrente e ContaPoupanca do arquivo Conta.py.
from Conta import Conta, ContaCorrente, ContaPoupanca

# Atributos de proteção:

# Public
# _Protected - Pode ser chamada, mas não se deve
# __Private - Não pode ser chamada fora da classe

class Cliente:
    def __init__(self, nome, cpf) -> None: # Coisas comuns de todos os clientess
        self.nome = nome
        self.cpf = cpf
        self._contas = [] #Lista de contas privadas
    
    def Abrir_Conta(self, tipo_conta, saldo_inicial): # Este é um método que permite ao cliente abrir uma nova conta.
        if tipo_conta == "Corrente": # Se o tipo_conta for “Corrente”, ele cria uma nova conta corrente com o saldo_inicial
            conta = ContaCorrente(saldo_inicial)
        elif tipo_conta == "Poupança": # Se o tipo_conta for “Poupança”, ele cria uma nova conta poupança.
            conta = ContaPoupanca(saldo_inicial)
        else: # Se o tipo_conta não for nem “Corrente” nem “Poupança”, ele levanta um erro.
            raise ValueError("Tipo de conta inválido")

        self._contas.append(conta) # Isso adiciona a nova conta à lista de contas do cliente.
        return conta # Isso retorna a nova conta.
    
    def __str__(self) -> str: # Este é o método __str__ da classe Cliente. Ele retorna uma representação em string Cliente.
        return f"Cliente: {self.nome}, de CPF: {self.cpf}" # Isso retorna uma string formatada que inclui o nome e o CPF.