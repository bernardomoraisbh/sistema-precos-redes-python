# sistema-precos-redes-python
Criar um socket UDP para enviar preços.

Sistema de Preços 
 
O principal objetivo do trabalho é praticar a programação com a biblioteca Socket e utilizando o protocolo UCP. O trabalho consiste em desenvolver um sistema para enviar o preço de vários postos de combustíveis e requisitar o preço mais barato em uma dada região. Você deverá criar um programa cliente e outro programa servidor. Os programas irão funcionar utilizando o UDP. 
 
O trabalho prático consistirá na implementação de dois programas, o cliente e o servidor. Ambos vão receber parâmetros de entrada como explicado a seguir:  
 
cliente <ip/nome> <porta>  servidor <porta>  
 
O primeiro programa, o cliente, irá conectar no servidor definido pelo endereço IP e porta passados por parâmetro. Já o servidor irá executar um serviço, que irá tratar uma comunicação por vez, mas que poderá comunicar com vários clientes. A porta a ser escutada é dada pelo parâmetro único do programa. 
 
O cliente poderá enviar dois tipos de mensagens ao servidor: dados (D) e pesquisa (P). Como o UDP não garante a entrega de mensagens, o cliente deve implementar pelo menos uma retransmissão, caso a mensagem não seja recebida a primeira vez, para tentar garantir a entrega de mensagens. O servidor deve confirmar a recepção de mensagens. As mensagens de dados começam com a letra D seguida de um inteiro identificador da mensagem, um inteiro que indica o tipo de combustível ( 0 - diesel, 1 - álcool, 2- gasolina), um inteiro com o preço x 1000 (ex: R$3,299 fica 3299 ) e as coordenadas do posto de combustível (latitude e longitude). O servidor deverá confirmar a recepção da mensagem e adicionar a informação em um arquivo. Vários clientes podem enviar dados e mesmo com o término da comunicação entre um cliente e um servidor os dados enviados devem ser salvos no arquivo para consultas de outros clientes. As mensagens de pesquisa começam com a letra P seguida de um inteiro identificador da mensagem, um inteiro que indica o tipo de combustível ( 0 - diesel, 1 - álcool, 2- gasolina), um inteiro com o raio de busca e as coordenadas do centro de busca (latitude e longitude). O servidor deverá responder com o menor preço para aquele combustível para postos de combustível que estejam no centro de busca mais raio de busca. Para verificar o correto funcionamento dos programas, o cliente e o servidor devem imprimir na tela o conteúdo das mensagens que eles receberem. 
