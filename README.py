Análise de Sentimento com Transformers
Este projeto utiliza a biblioteca transformers da Hugging Face para realizar análise de sentimento em frases em português. O modelo pré-treinado nlptown/bert-base-multilingual-uncased-sentiment é usado para classificar o sentimento expresso em cada frase.
Pré-requisitos

Python 3.6 ou superior
Bibliotecas Python:
transformers


Instalação

Instale a biblioteca transformers usando o pip:pip install transformers


Uso

O script carrega o pipeline de análise de sentimento com o modelo multilingual.
Uma lista de frases em português é fornecida para análise.
O modelo classifica cada frase, retornando o sentimento (positivo, negativo ou neutro) e um score de confiança.

  
Código
O código principal está no arquivo pln.py. Ele inclui:


Importação da biblioteca transformers.
Configuração do pipeline de análise de sentimento.
Lista de frases para análise.
Loop para processar cada frase e exibir o resultado.


Modelo Utilizado

Modelo: nlptown/bert-base-multilingual-uncased-sentiment
Descrição: Um modelo BERT multilingual treinado para análise de sentimento, que suporta vários idiomas, incluindo português. Ele classifica sentimentos em uma escala de 1 a 5 estrelas (1 = muito negativo, 5 = muito positivo).

Como Executar

Clone este repositório:git clone https://github.com/vitor-souza-ime/pln_bert


Navegue até o diretório do projeto:cd pln_bert


Execute o script:python pln.py

Este código foi testado no Google Colab.

Personalização

Adicionar novas frases: Modifique a lista frases no código para incluir suas próprias frases.
Alterar o modelo: Substitua o modelo no pipeline por outro modelo compatível com transformers, se desejar.

Limitações

O modelo pode não capturar nuances específicas de gírias ou contextos culturais em português.
A precisão depende da qualidade do texto de entrada e do treinamento do modelo.

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests no repositório: https://github.com/vitor-souza-ime/pln_bert.
Licença
Este projeto está licenciado sob a MIT License.
