# Sistema Bancário Simples em Python

Este código implementa um sistema bancário simples em Python. Ele contém várias classes que representam diferentes componentes de um sistema bancário.

## Classes

### Classe Cliente

A classe `Cliente` representa um cliente do banco. Cada cliente tem um nome e um CPF. Além disso, cada cliente tem uma lista de contas que ele possui.

Métodos da classe `Cliente`:

- `__init__(self, nome, cpf)`: Este é o construtor da classe. Ele inicializa um novo objeto `Cliente` com um nome e um CPF.
- `Abrir_Conta(self, tipo_conta, saldo_inicial)`: Este método permite ao cliente abrir uma nova conta. O tipo de conta e o saldo inicial são fornecidos como argumentos. A nova conta é adicionada à lista de contas do cliente.
- `__str__(self)`: Este método retorna uma representação em string do objeto `Cliente`.

### Classe Conta

A classe `Conta` é uma classe abstrata que representa uma conta bancária genérica. Cada conta tem um número de conta, um saldo e uma lista de transações.

Métodos da classe `Conta`:

- `__init__(self, saldo_inicial=0)`: Este é o construtor da classe. Ele inicializa um novo objeto `Conta` com um saldo inicial.
- `depositar(self, valor)`: Este método permite depositar um valor na conta.
- `sacar(self, valor)`: Este método permite sacar um valor da conta.
- `_registrar_transacao(self, descricao)`: Este é um método privado que registra uma transação na conta.
- `extrato(self)`: Este método imprime o extrato da conta.

### Classe ContaCorrente

A classe `ContaCorrente` é uma subclasse da classe `Conta` que representa uma conta corrente.

Métodos da classe `ContaCorrente`:

- `__init__(self, saldo_inicial=0)`: Este é o construtor da classe. Ele inicializa um novo objeto `ContaCorrente` com um saldo inicial.
- `__str__(self)`: Este método retorna uma representação em string do objeto `ContaCorrente`.

### Classe ContaPoupanca

A classe `ContaPoupanca` é uma subclasse da classe `Conta` que representa uma conta poupança. Além dos atributos de uma conta, uma conta poupança também tem uma taxa de juros.

Métodos da classe `ContaPoupanca`:

- `__init__(self, saldo_inicial=0)`: Este é o construtor da classe. Ele inicializa um novo objeto `ContaPoupanca` com um saldo inicial.
- `calcular_juros(self)`: Este método calcula os juros da conta poupança.
- `__str__(self)`: Este método retorna uma representação em string do objeto `ContaPoupanca`.

## Exemplo de Uso

O código também inclui um exemplo de uso dessas classes. Ele cria dois clientes, abre contas para eles e realiza algumas operações. Finalmente, ele exibe os extratos das contas.