#!/usr/bin/env python
# coding: utf-8

#!pip install -U spacy
#!python -m spacy download pt_core_news_md
import spacy
import re

import pt_core_news_md
nlp = pt_core_news_md.load()

def replaceWhiteSpaces(str):
    return re.sub('\s{2,}',' ',str)

def tokenizaFrase(frase, lower):
    frase = frase.replace('  ',' . ').replace(':',' ').replace('+',' . ').replace('#',' ').replace('(',' (').replace(')',') ').replace('[',' [').replace(']','] ')
    frase = replaceWhiteSpaces(frase.strip())
    if lower==1:
        frase=frase.lower()
    doc = nlp(frase)
    return doc
    
def isTokenFimChunk(pos):
    if pos != 'VERB' and pos != 'AUX' and pos != 'PUNCT' and pos != 'PRON' and pos != 'SPACE':    
        return False
    else:
        return True
    
def isTokenImportant(pos):
    if pos == 'NOUN' or pos == 'PROPN' or pos == 'ADJ':
        return True
    else:
        return False
    
def deveInserirToken(tamanhoTokens, pos):
    if tamanhoTokens!=0 or (tamanhoTokens==0 and (pos != 'ADP' and pos != 'DET' and pos != 'SCONJ' and pos != 'CCONJ')):
        return True
    else:
        return False
    
def deveManterToken(pos):
    if pos != 'DET' and pos != 'SCONJ' and pos != 'CCONJ' and pos != 'ADP':
        return True
    else:
        return False
    

def get_np(frase, lower):
        doc = tokenizaFrase(frase, lower)
        novaFrase = ' '.join([token.text for token in doc])
        lista_chunks = []
        all_novo_chunk = []
        all_novo_chunk.append(novaFrase)
        temNoun=0
        tokens_chunk = []
        for num, token in enumerate(doc):
            if not isTokenFimChunk(token.pos_):
                if deveInserirToken(len(tokens_chunk), token.pos_):
                    tokens_chunk.append(token)
                if isTokenImportant(token.pos_):
                    temNoun=1
            else:
                if len(tokens_chunk)!=0 and temNoun == 1:
                    novo_chunk = ''
                    deve_manter = 0
                    # retirando ultimos tokens do chunk se não forem importantes
                    for i in range(len(tokens_chunk)-1,-1,-1):
                        pos = tokens_chunk[i].pos_
                        texto = tokens_chunk[i].text
                        if deveManterToken(pos):
                            deve_manter = 1
                        if deve_manter==1:
                            novo_chunk = texto+' '+novo_chunk
                    all_novo_chunk.append(novo_chunk.strip())
                    lista_chunks.append(tokens_chunk)
                    tokens_chunk = []
                    temNoun = 0
                else:
                        tokens_chunk = []
                        temNoun = 0
        return all_novo_chunk