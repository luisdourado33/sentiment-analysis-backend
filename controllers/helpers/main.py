from email.mime import base
import spacy
import string
import random
import re

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def clear_text(text):
  # Nome do usuário @
  text = re.sub(r"@[A-Za-z0-9$-_@.&+]+", " ", text)

  # URLs
  text = re.sub(r"https?://[A-Za-z0-9./]+", " ", text)

  # Emoticons
  lista_emocoes = {':)': 'emocaopositiva',
                    ':d': 'emocaopositiva',
                    ':(': 'emocaonegativa'}

  for emocao in lista_emocoes:
    text = text.replace(emocao, lista_emocoes[emocao])

  return text

def pre_processamento(texto):
  pln = spacy.load("pt_core_news_sm")
  stop_words = spacy.lang.pt.stop_words.STOP_WORDS

  # Letras minusculas
  texto = texto.lower()

  # Nome do usuário @
  texto = re.sub(r"@[A-Za-z0-9$-_@.&+]+", " ", texto)

  # URLs
  texto = re.sub(r"https?://[A-Za-z0-9./]+", " ", texto)

  # Breakline \n
  texto = re.sub(r"\n+", " ", texto)
  
  # Espaco em branco
  # texto = re.sub(r" +", "", texto)

  # Emoticons
  lista_emocoes = {':)': 'emocaopositiva',
                    ':d': 'emocaopositiva',
                    ':(': 'emocaonegativa'}

  for emocao in lista_emocoes:
    texto = texto.replace(emocao, lista_emocoes[emocao])

  # Lematização
  documento = pln(texto)

  lista = []
  for token in documento:
    # lista.append(token.lemma_)
    lista.append(token.text)

  # Stop Words e Pontuações
  lista = [palavra for palavra in lista if palavra not in stop_words and palavra not in string.punctuation]

  lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()])

  return lista