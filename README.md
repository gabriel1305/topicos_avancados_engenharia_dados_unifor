# 🔧 Projeto de Simulação de Sensor de Temperatura e Umidade

Este projeto simula um sensor que gera dados de temperatura e umidade, os envia via Kafka, armazena no MongoDB e apresenta em tempo real por meio de Streamlit.

---

## 📁 Estrutura do Projeto


├── app.py                  # Aplicação Streamlit para visualização dos dados
├── consumer.py             # Consumidor Kafka que persiste dados no MongoDB
├── producer.py             # Produtor Kafka que envia os dados gerados
├── data_generate.py        # Script que simula geração dos dados de sensores
├── requirements.txt        # Dependências necessárias
├── Dockerfile              # (Opcional) Configuração para container do app
├── docker-compose.yml      # (Opcional) Ambiente Kafka + MongoDB
└── README.md               # Este arquivo

## 🎯 Objetivo

Construir um pipeline simples para:

    Gerar dados sintéticos de temperatura e umidade via data_generate.py

    Enviar dados para um tópico Kafka (producer.py)

    Consumir dados do Kafka e salvar no MongoDB (consumer.py)

    Visualizar dados em tempo real com app.py via Streamlit

Ideal para aprendizado de ingestão e processamento de dados em tempo real.
## 🧰 Tecnologias Utilizadas

    Python – Código principal

    Kafka – Stream de mensagens entre produtor e consumidor

    MongoDB – Armazenamento NoSQL dos dados coletados

    Streamlit – Dashboard simples e interativo para visualização

    confluent_kafka ou kafka-python – Cliente Kafka para Python

    pymongo – Driver MongoDB para Python

## 🚀 Como Executar
Pré-requisitos

    Python 3.8+

    Kafka e MongoDB rodando localmente ou via Docker Compose

    Dependências Python instaladas:

pip install -r requirements.txt

Passos básicos

    Inicie os containers Kafka e MongoDB (caso use Docker Compose):

docker-compose up -d

    Execute o produtor de dados:

python producer.py

    Inicie o consumidor:

python consumer.py

    Inicie o dashboard:

streamlit run app.py
## 🧠 Possíveis Extensões

    Dashboard mais avançado com gráficos históricos e alertas

    Inclusão de latência, logging ou métricas de performance

    Containerização completa com Docker para cada parte do pipeline

    Estratégias de particionamento Kafka ou escalabilidade de consumidores

📄 Licença

Este projeto está licenciado sob a MIT License.
Fique à vontade para utilizar, modificar ou contribuir.
Para uso comercial, consulte os termos da licença.
