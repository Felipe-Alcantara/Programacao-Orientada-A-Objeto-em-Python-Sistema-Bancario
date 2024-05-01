import random
import datetime
from Conta import Conta, ContaCorrente, ContaPoupanca

# Atributos de proteção:

# Public
# _Protected - Pode ser chamada, mas não se deve
# __Private - Não pode ser chamada fora da classe

class Cliente:
    def __init__(self, nome, cpf) -> None:
        self.nome = nome
        self.cpf = cpf
        self._contas = [] #Lista de contas privadas
    
    def Abrir_Conta(self, tipo_conta, saldo_inicial):
        if tipo_conta == "Corrente":
            conta = ContaCorrente(saldo_inicial)
        elif tipo_conta == "Poupança":
            conta = ContaPoupanca(saldo_inicial)
        else:
            raise ValueError("Tipo de conta inválido")

        self._contas.append(conta)
        return conta
    
    def __str__(self) -> str:
        return f"Cliente {self.nome}, de CPF {self.cpf}"