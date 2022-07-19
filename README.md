# Nlp Bio Portuguese Chunking
## Uma API para extração de *chunks* (*Noun phrases*) em textos clínicos
### Porque "*Chunk Is All You Need*" 😄😄😄

# Índice
1. [Sobre](#sobre)
2. [POS-Tagger](#pos-tagger)
3. [Como executar localmente](#como-executar-localmente)
4. [Executando via docker](#executando-via-docker)
5. [Como citar](#como-citar)

## Sobre

*Chunking* é uma maneira de agrupar elementos sequenciais de um texto como frases, podendo ser frase nominal, frase verbal, frase preposicional etc, utilizando a sua parte do discurso (*POS-tagger*). Ao contrário do reconhecimento de entidade nomeada (NER ou REN), que encontra e classifica pedaços relevantes no texto.

Neste trabalho, extraímos as frases nominais, ou seja, frases que têm um substantivo como cabeça ("*Noun phrases*"). 

Utilizamos dois métodos para gerar o *POS-Tagger* das senteças:

1. A biblioteca `spacy` para tokenizar e extrair o *POS-tagger* de cada palavra da frase, com o *corpus* `pt_core_news_md`.
2. Um modelo *token-sequence* `BERT` treinado com o *corpus* [`MacMorpho`](http://nilc.icmc.usp.br/macmorpho/) usando como *checkpoint* o modelo [BioBERTpt](https://huggingface.co/pucpr/biobertpt-all), sendo este último treinado com textos clínicos e biomédicos em português.

Na sequencia, criamos uma função que extrai todos os substantivos da frase, mantendo-o junto com os seus complementos (adjetivos, advérbios, etc).

Exemplo: 
```
---Frase original:---

Data de Criação do Documento: 22/04/2014   Dispneia importante aos esforços + dor tipo peso no peito no esforço. Obeso, has, icc  c # cintilografia miocardica para avaliar angina.


---Chunks da frase:---

['Data de Criação do Documento 22/04/2014', 'Dispneia importante aos esforços', 'dor tipo peso no peito no esforço', 'Obeso', 'has', 'icc', 'cintilografia miocardica', 'angina']
```

## POS-Tagger

Além do modelo de *POS-tagger* fornecido pelo `spacy`, também treinamos um modelo próprio a partir do *fine-tuning* do modelo de linguagem [BioBERTpt(all)](https://huggingface.co/pucpr/biobertpt-all) com o *corpus* para língua portuguesa [MacMorpho](http://nilc.icmc.usp.br/macmorpho/), com 10 épocas, chegando em um *F1-Score* geral de 0.9814.

Nosso modelo está no repositório oficial do `Hugging Faces`, você pode acessá-lo pelo endereço: https://huggingface.co/pucpr-br/postagger-bio-portuguese.

<img src="img/postagger-huggingfaces.png">

Se você gostou do nosso trabalho, não se esqueça de dar um *like* no modelo no `Hugging Faces` ❤️

Como usar o modelo de *POS-tagger* (sem o *chunking*):

```
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("pucpr-br/postagger-bio-portuguese")

model = AutoModelForTokenClassification.from_pretrained("pucpr-br/postagger-bio-portuguese")
```

Aqui você tem um manual dos tipos gramaticais retornados pelo modelo:

| Sigla  |  Significado  |
| ------------------- | ------------------- |
|  ADJ |  Adjetivo |
|  ADV |  Advérbio |
|  ADV-KS |  Advérbio conjuntivo subordinado  |
|  ADV-KS-REL |   Advérbio relativo subordinado |
|  ART |  Artigo  |
|  CUR |  Moeda  |
|  IN |  Interjeição |
|  KC |  Conjunção coordenativa |
|  KS |  Conjunção subordinativa |
|  N |  Substantivo |
|  NPROP | Substantivo próprio |
|  NUM |  Número |
|  PCP |  Particípio |
|  PDEN |  Palavra denotativa |
|  PREP |  Preposição |
|  PROADJ |  Pronome Adjetivo |
|  PRO-KS |  Pronome conjuntivo subordinado |
|  PRO-KS-REL |  Pronome relativo conectivo subordinado |
|  PROPESS |  Pronome pessoal |
|  PROSUB |  Pronome nominal |
|  V | Verbo |
|  VAUX  | Verbo auxiliar |

Mais informações e exemplos em: http://nilc.icmc.usp.br/macmorpho/macmorpho-manual.pdf

## Como executar localmente

Para gerar os *chunks* (*noun phrases*), você pode executar diretamente pelos *notebooks* [com spacy](https://github.com/lisaterumi/nlp-portuguese-chunking/blob/main/notebook/chunking-portuguese_spacy.ipynb) e com o [POS-Tagger Bio Portuguese](https://github.com/lisaterumi/nlp-portuguese-chunking/blob/main/notebook/chunking-portuguese_postagger_biopt.ipynb)

Ou executar um servidor para ter acesso à interface *web*, seguindo os passos abaixo (os exemplos a seguir são com o uso da bilbioteca `spacy`, por ser um modelo mais leve de executar, principalmente dentro dos *containers*).

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
3. Execute o `app.py` (está configurado para rodar na porta 5000)
```
python app.py
```
4. No navegador, acesse http://localhost:5000/

5. Escreve uma sentença clínica ou selecione alguma frase de exemplo e clicar no botão de pesquisa (lupa). 
 
Serão retornadas os *chunks* identificados na sentença de entrada. 
 
<img src="img/chunk.png">

## Executando via Docker

1. Para executar a API dentro de um *container* `Docker`, onde não é necessário se preocupar com o ambiente e bibliotecas, basta seguir os passos:

1. Caso não possua, instale o `Docker` seguindo [essas orientações](https://docs.docker.com/get-started/).

2. Execute os seguintes comandos (para executar o *container* na porta 5000)
```
docker build -t chunking .

docker run --name chunking_instance -p 0.0.0.0:5000:5000  -d chunking

```
3. No navegador, acesse http://localhost:5000/

## Como citar

** *em breve* **

