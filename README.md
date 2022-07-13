# Nlp Portuguese Chunking - Uma API para extração de chunks (Noun phrases) em textos clínicos

** *trabalho em andamento* **

# Índice
1. [Sobre](#sobre)
2. [Como executar localmente](#como-executar-localmente)
3. [Executando via docker](#executando-via-docker)
4. [Como citar](#como-citar)

## Sobre

Chunking é uma maneira de agrupar elementos sequenciais de um texto como frases, podendo ser frase nominal, frase verbal, frase preposicional etc, utilizando a sua parte do discurso (POS-tagger). Ao contrário do reconhecimento de entidade nomeada (NER ou REN), que encontra e classifica pedaços relevantes no texto.

Neste trabalho, exrtaímos as frases nominais, ou seja, frases que têm um substantivo como cabeça ("Noun phrases"). 

Utilizamos a biblioteca `spacy` para tokenizar e extrair o POS-tagger de cada palavra da frase, com o corpus `pt_core_news_md`.

Na sequencia, criamos uma função que extrai todos os substantivos da frase, mantendo-o junto com os seus complementos (adjetivos, advérbios, etc).

## Como executar localmente
1. Clone o repositório
2. Instale as biblitecas necessárias (se preferir, use [Anaconda](http://www.anaconda.com))
```
pip install flask == 4.3.0
pip install spacy == 2.3.7
```
ou através do comnando:
```
pip install -r requirements.txt
```
3. Execute o app.py (está configurado para rodar na porta 5000)
```
python app.py
```
4. No navegador, acesse http://localhost:5000/

5. Escreve uma sentença clínica ou selecione alguma frase de exemplo e clicar no botão de pesquisa (lupa). 
 
Serão retornadas os chunking identificados na sentença de entrada. 
 
<img src="img/chunk1.jpg">

<img src="img/chunk2.jpg">

## Executando via Docker

1. Para executar a API dentro de um container Docker, onde não é necessário se preocupar com o ambiente e bibliotecas, basta seguir os passos:

1. Caso não possua, instale o Docker seguindo [essas orientações](https://docs.docker.com/get-started/).

2. Execute os seguintes comandos (para executar o container na porta 5000)
```
docker build -t chunking .

docker run --name chunking_instance -p 0.0.0.0:5000:5000  -d chunking

```
3. No navegador, acesse http://localhost:5000/

## Como citar

** *em breve* **

