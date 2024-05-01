import random
import datetime

# Atributos de proteção:

# Public
# _Protected - Pode ser chamada, mas não se deve
# __Private - Não pode ser chamada fora da classe

class Conta:
    def __init__(self, saldo_inicial=0) -> None:
        self._numero_conta = random.randint(10000, 100000) # Número da conta privado
        self._saldo = saldo_inicial
        self._transacoes = [] # Lista de transações privada
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._registrar_transacao(f"Depósito de R${valor}")

    
    def sacar(self, valor):
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            self._registrar_transacao(f"Saque de R${valor}")

    # Método privado para registrar transições
    def _registrar_transacao(self, descricao):
        data_hora = datetime.datetime.now()
        self._transacoes.append((data_hora, descricao))

    def extrato(self):
        print(f"Extrato da conta{self._numero_conta}")
        for data_hora, descricao in self._transacoes:
            print(f"{data_hora}: {descricao}")
        print(f"Saldo atual: R${self._saldo}")

class ContaCorrente(Conta):
    def __init__(self, saldo_inicial=0) -> None:
        super().__init__(saldo_inicial)
        self._tipo = "Corrente"

    def __str__(self) -> str:
        return f"Conta corrente número: {self._numero_conta}, saldo: {self._saldo})"

class ContaPoupanca(Conta):
    def __init__(self, saldo_inicial=0) -> None:
        super().__init__(saldo_inicial)
        self._tipo = "Poupança"
        self._taxa_juros = 0.03
    
    def calcular_juros(self):
        juros = self._saldo * self._taxa_juros
        self._saldo += juros
        self._registrar_transacao(f"Crédito de juros de R${juros}")
        
    def __str__(self) -> str:
        return f"Conta poupança - número: {self._numero_conta}, Saldo: {self._saldo}"