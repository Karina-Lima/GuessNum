# GuessNum - Adivinhador de Números 🔢

https://github.com/user-attachments/assets/9fb54c20-3321-42ac-80c2-7b1597cc02ad

## 🔎 Sobre o Projeto 
O projeto tem sua estrutura a partir do conjunto de dados MNIST, uma base de dados amplamente conhecida como na área do aprendizado de máquina e do aprendizado profundo. Esse dataset é composto por milhares de imagens de números manuscritos em diversas grafias, usado no treinamento e na validação do modelo. O principal objetivo desse projeto foi desenvolver uma rede neural, através da implementação com a biblioteca Keras que não apenas alcançasse altos níveis de precisão, mas que também proporcionasse uma interação direta com o usuário por meio de uma interface intuitiva, permitindo uma experiência prática e acessível.


## 💻Como executar o projeto

### Ambiente de Execução
Para executar e testar nosso projeto em uma máquina local, é necessário que a linguagem de programação Python esteja instalada, ou que você esteja utilizando um ambiente virtual com suporte a essa linguagem. Para verificar se o Python está instalado em seu computador, execute o seguinte comando no Prompt de Comando:

```python –version```

O terminal deverá exibir uma resposta semelhante à imagem acima, fornecendo detalhes sobre a versão da linguagem instalada em sua máquina.


### Instalação das Dependências do Projeto
Em seguida, com o ambiente corretamente configurado, será necessário baixar os arquivos do nosso projeto, que estão disponíveis nesse repositório.

### Execução do Treinamento (Treino.py)
Com o projeto instalado em sua máquina, será necessário acessar a pasta descompactada através do Prompt de Comando. Para facilitar o processo, basta abrir a guia de busca dentro da pasta “GuessNum”, digitar 'Cmd' no campo de busca e pressionar Enter. Esse atalho abrirá o Prompt de Comando diretamente dentro da pasta.

Por padrão, já está incluido um arquivo com o treinamento das épocas (.keras) dentro do projeto. No entanto, caso deseje treinar o sistema novamente, basta excluir esse arquivo "Cachola.keras" executar o seguinte comando no terminal:

```python treino.py```

Este comando executará a rede de treinamento e armazenará as épocas de treino em um arquivo (.keras). 

### Execução do Projeto (Canvas.py)
Com o sistema devidamente treinado nas 50 épocas, execute agora o comando abaixo para acessar a tela de desenho.

```python canvas.py```

Este comando abre a tela de desenho do projeto, onde você pode desenhar um algarismo de sua escolha, entre 0 e 9. Após desenhar, clique no botão 'Submeter'. Isso salvará a imagem do seu desenho e a enviará para o processamento no subsistema 'analise.py', que tentará identificar o número desenhado.

### Saída e Resultado
Uma vez enviada para o processamento, a imagem será mapeada pelas camadas ocultas da rede neural. Através desse mapeamento, o sistema avalia a probabilidade e a similaridade entre a imagem desenhada e outras milhares de imagens presentes nas épocas de treinamento. Após essa avaliação, o modelo retorna o número que ele acredita ser o correspondente, juntamente com o tempo de execução do processamento.
