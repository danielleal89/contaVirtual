# contaVirtual com Python e Django

Projeto de um banco virtual feito com Python e Django.
https://app-contavirtual.herokuapp.com/index/

O projeto consiste na criação de um sistema de banco virtual, o qual pode-se cadastrar novas contas e fazer operações de depósito, saque e consultar extrato.
Não é necessário login para entrar nas contas. *O mesmo será implementado posteriormente.

1 - Ao acessa o link acima, será direcionado a página inicial, a qual tem a opção de cadastrar uma conta ou entrar na lista de contas já cadastradas.
2.1 - Cadastrar: precisará informar o nome e o cpf(será implementado mascará), necessário para criação da conta.
2.2 - Entrar: irá para página com todas contas cadastradas. Em cada linha mostrará o Nº da conta, Nome, CPF, saldo (começa zerado) e o botão para entrar na conta.
3 - Entrar/conta: entrando na conta temos as opções de Depositar, Sacar, Extrato, Editar e Sair.
3.1 - Depositar (Débito): insira um valor maior que 0 para acrescentar a conta. O valor irá aumentar ao saldo.
3.2 - Sacar (Crédito): insira um valor maior que 0 e menor ou igual ao saldo da conta. O valor irá diminuir do saldo.
3.3 - Extrato: mostrará todos os depositos e saques feito na conta, assim como o saldo.
*Falta implementar o filtro de depósito e saque, assim como a data das transações e o saldo anterior.
3.4 - Editar: retorna os campos nome e o cpf para alterar os dados conta.
3.5 - Sair: retorna a página inicial.


Obs: é um sistema básico que ainda falta algumas implementações. Qualquer sugestão, fique a vontade.
