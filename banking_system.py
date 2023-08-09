from abc import ABC, abstractmethod

class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta):
        self.conta = conta

class Deposito(Transacao):
    _valor = float

class Saque(Transacao):
    _valor = float

class Cliente:

    def __init__(self, endereco, contas):
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(self):
        pass

    def adicionar_conta(self):
        pass
class PessoaFisica(Cliente):

    def __init__(self, cpf, nome, data_nascimento):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

class Conta:

    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self.agencia = agencia
        self._cliente = cliente
        self._historico = historico

    def saldo(self):
        pass

    def nova_conta(self, _cliente, _numero):
        pass

    def sacar(self, valor):
        pass

    def depositar(self, valor):
        pass

class ContaCorrente(Conta):

    def __init__(self, limite, limite_saques):
        self._limite = limite
        self._limite_saques = limite_saques

class Historico:

    def adicionar_transacao(self):
        pass

