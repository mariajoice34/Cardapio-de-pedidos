O código desenvolvido em Python simula um sistema simples de pedidos de uma lanchonete utilizando o terminal. O objetivo do programa é permitir que o usuário escolha itens de um cardápio, adicione ao pedido, visualize os itens selecionados, remova itens e finalize a compra, mostrando o valor total.

No início do programa é criada uma lista chamada **pedidos**, que será responsável por armazenar todos os itens escolhidos pelo usuário. Cada item é guardado como uma tupla contendo o nome do produto e o seu preço.

Em seguida, o programa entra em um **laço de repetição `while True`**, que mantém o sistema funcionando continuamente até que o usuário finalize o pedido. Dentro desse laço é exibido um menu principal com as seguintes opções: comida, bebida, doces, visualizar pedidos, finalizar o pedido e remover item do pedido.

Para evitar erros quando o usuário digita algo que não seja número, o programa utiliza **`try` e `except`**, garantindo que apenas valores numéricos sejam aceitos na escolha das opções.

Quando o usuário escolhe a opção **1 (Comida)**, é apresentado um cardápio com diferentes alimentos como hambúrguer, pizza, empada, torta, pão de queijo e coxinha. Ao selecionar um item, ele é adicionado à lista **pedidos** utilizando o método **`append()`**, que insere o nome do produto e o preço na lista.

Na opção **2 (Bebida)** ocorre o mesmo processo, mostrando bebidas disponíveis como refrigerantes e sucos. O item escolhido também é armazenado na lista de pedidos.

Na opção **3 (Doces)** o usuário pode escolher sobremesas como brigadeiro, beijinho, pudim e bolo de chocolate, que também são adicionadas à lista.

A opção **4 (Ver pedidos)** permite visualizar todos os itens já selecionados. O programa percorre a lista **pedidos** utilizando um laço **`for`**, exibindo o nome de cada produto e seu preço. Durante esse processo, o programa também soma os valores para mostrar o **total parcial do pedido**.

Na opção **5 (Finalizar pedido)** o sistema mostra todos os itens escolhidos e calcula o **valor total a pagar**. Após exibir o total e uma mensagem de agradecimento, o programa é encerrado utilizando o comando **`break`**.

A opção **6 (Remover item do pedido)** permite excluir algum produto escolhido. O programa usa a função **`enumerate()`** para mostrar os itens numerados. O usuário digita o número do item que deseja remover e o programa utiliza o método **`pop()`** para retirar o elemento da lista.

Dessa forma, o código simula o funcionamento básico de um sistema de pedidos, permitindo adicionar, visualizar, remover itens e calcular o valor final da compra.

