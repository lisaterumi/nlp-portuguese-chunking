#!/usr/bin/env python
# coding: utf-8


#!pip install -U spacy
#!python -m spacy download pt_core_news_md
import spacy

import pt_core_news_md
nlp = pt_core_news_md.load()

def get_np(frase):
        print('frase:', frase[0])
        doc = nlp(frase[0])
        novaFrase = ' '.join([token.text for token in doc])
        lista_chunks = []
        all_novo_chunk = []
        temNoun=0
        tokens_chunk = []
        all_novo_chunk.append(novaFrase)
        for num, token in enumerate(doc):
            if token.pos_ != 'VERB' and token.pos_ != 'AUX' and token.pos_ != 'PUNCT' and token.pos_ != 'PRON' and token.pos_ != 'SPACE' and token.text != '+' and token.text != '#':
                if len(tokens_chunk)!=0 or (len(tokens_chunk)==0 and (token.pos_ != 'ADP' and token.pos_ != 'DET' and token.pos_ != 'SCONJ' and token.pos_ != 'CCONJ')):
                  #chunk = chunk + token.text + ' '
                  tokens_chunk.append(token)
                if token.pos_ == 'NOUN':
                  temNoun=1
            else:
              if len(tokens_chunk)!=0 and temNoun == 1:
                novo_chunk = ''
                # ver se os ultimos tokens não são DET, ADP, etc
                #print(tokens_chunk)
                deve_manter = 0
                for i in range(len(tokens_chunk)-1,-1,-1):
                  #print('i:', i)
                  pos = tokens_chunk[i].pos_
                  texto = tokens_chunk[i].text
                  #print('pos:', pos)
                  #print('texto:', texto)
                  if pos != 'DET' and pos != 'SCONJ' and pos != 'CCONJ' and pos != 'ADP':
                    deve_manter = 1

                  if deve_manter==1:
                    novo_chunk = texto+' '+novo_chunk
                  else:
                    #print('----descartando:-------', texto)
                    pass
                all_novo_chunk.append(novo_chunk.strip())
                # acrescenta na lista
                lista_chunks.append(tokens_chunk)
                tokens_chunk = []
                temNoun = 0
        print('retornando:', all_novo_chunk)
        
        return all_novo_chunk 
