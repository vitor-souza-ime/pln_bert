# Instalar a biblioteca transformers
!pip install transformers

# Importar as bibliotecas necessárias
from transformers import pipeline

# Carregar o pipeline de análise de sentimento
# Usamos um modelo pré-treinado multilingual para suportar português
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment",
    tokenizer="nlptown/bert-base-multilingual-uncased-sentiment"
)


# Lista de frases em português para análise
frases = [
    "Eu amo esse filme, é incrível!",
    "Esse restaurante é horrível, nunca mais volto.",
    "O dia está bonito hoje.",
    "Não gostei muito do atendimento, mas a comida era boa."
]

# Realizar a análise de sentimento para cada frase
for frase in frases:
    result = sentiment_analyzer(frase)
    label = result[0]['label']
    score = result[0]['score']
    print(f"Frase: {frase}")
    print(f"Sentimento: {label} (Score: {score:.4f})\n")
