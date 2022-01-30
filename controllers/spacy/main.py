from email.mime import text
import spacy

def get_spacy_ex():
  message = "Eu gosto de Cuiabá, mas gostaria de morar nos Estados Unidos."

  nlp = spacy.load("pt_core_news_sm")
  doc = nlp(message)

  text_treatment = ""
  response = []
  for token in doc:
    response.append({
      "text": token.text,
      "is_stop": token.is_stop
    })

    if token.is_stop is False and token.pos_ != "PUNCT":
      text_treatment = text_treatment + " " + token.text


  return text_treatment

