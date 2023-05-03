# Repositório base do artigo submetido no Simpósio Brasileiro de Telecomunicações e Processamento de Sinais - SBRT2023.

OBS: Para executar os códigos desenvolvidos, é necessário ter o Python instalado e instalar as dependências solicitadas pela IDE. Outra alternativa é usar o Google Colab, que já é um ambiente configurado.

## O artigo está disponível na raiz do documento com o nome de SBRT2023.pdf.

Na pasta Alg/data/disc/test/image, há uma imagem disponível que foi usada como base. Na pasta Alg/results, os resultados do algoritmo são apresentados.

### O código fonte está dentro da pasta Alg. Dentro dela, existem várias mains:

* A main.py executa o algoritmo para apenas uma imagem. 
* A main_multiple.py executa o algoritmo para um conjunto de imagens. 
* A main_results.py gera um gráfico comparando a imagem base com a imagem processada. 
* A main_test_parameters.py tem alguns parâmetros testados até se definir o melhor para o algoritmo. 

Os demais arquivos .py fazem parte do algoritmo ou são auxiliares do mesmo.

## Resultados principais

#### A imagem abaixo é a imagem base.
![base](/Alg/data/disc/test/image/BINRUSHED1_image2.jpg)

#### A imagem abaixo é a imagem resultante.
![res](/Alg/results/img-res.jpg)

#### A imagem abaixo mostra todos os passos executados até se chegar à imagem resultante.
![ciclo](/Alg/results/img-final.jpg)

#### A imagem abaixo mostra o resultado da comparação entre a imagem base (linhas pontilhadas) e a imagem resultante (linhas contínuas).
![hist](/Alg/results/histogram.jpg)

#### Os testes de parâmetros geraram as imagens abaixo. A primeira imagem foi a escolhida para dar sequência ao algoritmo.
![params](/Alg/results/tests/concat.jpg)
