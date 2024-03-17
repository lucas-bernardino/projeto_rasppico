# Iniciação Científica - UFSC 
## Esse repósitorio possui o código que desenvolvi para a bolsa de iniciação científica sobre o tema ***Desenvolvimento de atenuador de vibração para motocicletas***

## Objetivo
Esse projeto busca integrar diversos sensores instalados na motocicleta, realizar medições experimentais, analisar os dados coletados e utilizá-los para verificar o desempenho dos atenuadores.

## Estrutura do projeto
Para aquisição de dados, foram utilizados os seguintes sensores:

* WitMotion WTGAHRS1
    * Esse sensor é capaz de disponibilizar aceleração nos três eixos, velocidade angular nos três eixos, orientação angular nos três eixos, campo magnético nos três eixos, latitude e longitude,
    velocidade de acordo com o GPS e pressão atmosférica. Sua comunicação foi feita via UART.
* Sensor de Àngulo Magnético AS5600
    * Através desse sensor é possivel obter o esterçamento do guidão da motocicleta. Ele possui 12 bits de resolução e comunicação I2C.
* Sensor de Efeito Hall
    * Localizado na roda traseira, ele foi utilizado em junto com um imã para obter a velocidade e rotação da roda. A sua leitura é feita de modo digital.

Para a comunicação com esses sensores, inicialmente foi utilizado a Raspberry Pi Pico. Porém, foi verificada a necessidade de maior processamento de dados, assim passou-se a utilizar a Raspberry
Pi 4.

Antes de iniciar a acquisição, deve-se ter disponibilidade de Wi-Fi e um dispositivo que tenha a capacidade de se comunicar por Secure Socket Shell (SSH) para inicializar o código. Após o programa ter sido inicializado, a aquisição de dados pode ser feita de modo offline, salvando os dados localmente na Raspberry e posteriormente visualizando-os em um computador ou salvando os dados em um banco de dados e visualizando-os em tempo real em um site.

## Tecnologias utilizadas
1. Acquisição e comunicação com os sensores
- O código responsável pela acquisição e comunicação com os sensores foi desenvolvido em Python. A escolha dessa linguagem deve-se ao fato de ser relativamente simples utilizá-la para trabalhar com *threads*, haja visto a necessidade de utilizá-las para trabalhar de modo concorrente, melhorando a eficiência e perfomance do código. Ela também possui simplicidade para a comunicação com os sensores, permitindo uma eficaz leitura e escrita com os protocolos I2C e UART.

- Devido ao fato de ser uma linguagem interpretada, ela pode ser mais lento em algumas tarefas em relação a linguagens compiladas como C. Porém, não foi verificado perda de perfomance nessas tarefas.

- Além disso, foi utilizado o Python para limpar e tratar os dados recebidos, criando a possibilidade de facilmente transformar os dados salvos em txt para planilhas visíveis em Excel ou LibreOffice. Quando há Wi-Fi, existe também um backend utilizando o framework Flask para enviar os arquivos da planilha que estão no formato *csv* para o frontend. Essa parte pode ser considerada um microserviço, visto que consome os dados salvos na API do backend feito em Node e expõe novas rotas que serão utilizadas pelo frontend para visualizar e baixar a planilha. 

2. Servidor e banco de dados
- Quando há possibilidade de visualizar os dados em tempo real, o código construido em Python se comunica com um servidor feito em NodeJs com o framework Express. Foi desenvolvida uma API para que toda vez que houver um novo pacote de dados, o código em Python envia os dados para o backend em NodeJS, que por sua vez salva esses dados no banco de dados. O banco de dados utilizados foi o MongoDB, devido a não necessidade de se utilizar um banco relacional para esse trabalho.

- A API possui diversas rotas que são tanto utilizadas pelo Python para a API, como também pelo frontend, que faz uma requisição para exibir esses dados formatados ao cliente.

3. Frontend
- O usuário pode visualizar os dados, observar o gráfico deles em tempo real ao longo do tempo e baixar os dados em uma planilha de formato *csv* através da página construída utilizando a biblioteca React utilizando o Typescript. Ela está constantemente fazendo requisições para a API feita em Node e também ocasionamente faz requisições para a API feita em Flask para baixar a planilha em *csv*.

4. Docker e Deploy
- O frontend e backend são inicializados através de containers que rodam na própria Raspberry Pi 4, utilizando o Docker. Como nem sempre a rede de Wi-Fi utilizada pela Raspberry será a mesma que o cliente visualizará a página, foi utilizado o Ngrok, que permite expor os serviços que estão sendo executados localmente para a Internet. 
