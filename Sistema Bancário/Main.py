from Cliente import Cliente # Isso importa a classe Cliente do arquivo Cliente.py
from Conta import Conta, ContaCorrente, ContaPoupanca # Isso importa as classes Conta do arquivo Conta.py.

if __name__ == "__main__": # Isso garante que o código seja executado apenas se este arquivo for executado diretamente.
    Cliente1 = Cliente("João Silva", "123.456.789-00") # Isso cria um objeto Cliente1 da classe Cliente.
    Conta_corrente1 = Cliente1.Abrir_Conta("Corrente", 1000) # Isso chama o método Abrir_Conta do objeto Cliente1.
    Conta_poupanca1 = Cliente1.Abrir_Conta("Poupança", 5000) # Isso chama o método Abrir_Conta do objeto Cliente1.

    Cliente2 = Cliente("Maria Santos", "987.654.321-00") # Isso cria um objeto Cliente2 da classe Cliente.
    Conta_corrente2 = Cliente2.Abrir_Conta("Corrente", 2000) # Isso chama o método Abrir_Conta do objeto Cliente2.

    # Realizar operações
    Conta_corrente1.depositar(500) # Isso chama o método depositar do objeto Conta_corrente1 para depositar 500 na conta.
    print("1")

    Conta_poupanca1.sacar(1000) # Isso chama o método sacar do objeto Conta_poupanca1 para sacar 1000 da conta.
    print("2")

    Conta_poupanca1.calcular_juros() # Isso chama o método calcular_juros do objeto Conta_poupanca1 para calcular e adicionar os juros ao saldo da conta.
    print("3")

    # Essas linhas chamam o método extrato dos respectivos objetos de conta para imprimir o extrato da conta.
    Conta_corrente1.extrato()
    print("4")

    Conta_poupanca1.extrato()
    print("5")

    Conta_corrente2.extrato()
    print("6")