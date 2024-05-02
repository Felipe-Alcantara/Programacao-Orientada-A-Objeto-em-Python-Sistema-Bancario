# Isso importa os módulos random e datetime do Python, que são usados para gerar números aleatórios e trabalhar com datas e horas, respectivamente.
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
    
    def depositar(self, valor): # Este é um método que permite depositar um valor na conta. Ele aceita um parâmetro valor.
        if valor > 0: # Se o valor for maior que 0, ele adiciona o valor ao saldo da conta.
            self._saldo += valor
            self._registrar_transacao(f"Depósito de R${valor}") # Isso chama o método _registrar_transacao para registrar a transação de depósito.

    
    def sacar(self, valor): # Este é um método que permite sacar um valor da conta. Ele aceita um parâmetro valor.
        if valor > 0 and self._saldo >= valor: # Se o valor for maior que 0 e o saldo da conta for maior ou igual ao valor, ele subtrai o valor do saldo da conta.
            self._saldo -= valor 
            self._registrar_transacao(f"Saque de R${valor}") # Isso chama o método _registrar_transacao para registrar a transação de saque.

    # Método privado para registrar transições
    def _registrar_transacao(self, descricao): # Este é um método privado que registra uma transação. Ele aceita um parâmetro descricao que descreve a transação.
        data_hora = datetime.datetime.now() # Isso obtém a data e hora atuais.
        self._transacoes.append((data_hora, descricao)) # Isso adiciona a data e hora e a descrição da transação à lista de transações.

    def extrato(self): # Este é um método que imprime o extrato da conta.
        print(f"Extrato da conta{self._numero_conta}") # Isso imprime o número da conta.
        for data_hora, descricao in self._transacoes:
            print(f"{data_hora}: {descricao}") # Isso percorre a lista de transações e imprime a data e hora e a descrição de cada transação.
        print(f"Saldo atual: R${self._saldo}") # Isso imprime o saldo atual da conta.

class ContaCorrente(Conta): # Isso define uma nova classe chamada ContaCorrente que herda da classe Conta.
    def __init__(self, saldo_inicial=0) -> None: 
        super().__init__(saldo_inicial) # Este é o método construtor da classe ContaCorrente. Ele chama o método construtor da classe pai Conta com o parâmetro saldo_inicial.
        self._tipo = "Corrente" # Isso define o atributo _tipo do objeto ContaCorrente para “Corrente”.

    def __str__(self) -> str:
        return f"Conta corrente número: {self._numero_conta}, saldo: {self._saldo})" # Este é o método __str__ da classe ContaCorrente. Ele retorna uma representação em string do objeto ContaCorrente.

class ContaPoupanca(Conta): # Isso define uma nova classe chamada ContaPoupanca que herda da classe Conta.
    def __init__(self, saldo_inicial=0) -> None: # Este é o método construtor da classe ContaPoupanca. Ele chama o método construtor da classe pai Conta com o parâmetro saldo_inicial.
        self._tipo = "Poupança" # Isso define o atributo _tipo do objeto ContaPoupanca para “Poupança”.
        self._taxa_juros = 0.03 # Isso define o atributo _taxa_juros do objeto ContaPoupanca para 0.03.
    
    def calcular_juros(self): # Este é um método que calcula os juros da conta poupança.
        juros = self._saldo * self._taxa_juros # Isso calcula os juros multiplicando o saldo da conta pela taxa de juros.
        self._saldo += juros # Isso adiciona os juros ao saldo da conta.
        self._registrar_transacao(f"Crédito de juros de R${juros}") # Isso chama o método _registrar_transacao para registrar a transação de crédito de juros.
        
    def __str__(self) -> str:
        return f"Conta poupança - número: {self._numero_conta}, Saldo: {self._saldo}" # Este é o método __str__ da classe ContaPoupanca. Ele retorna uma representação em string do objeto ContaPoupanca.