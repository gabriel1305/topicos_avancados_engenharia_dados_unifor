# 🔧 Projeto de Simulação de Sensor de Temperatura e Umidade

Este projeto simula um sensor que gera dados de temperatura e umidade, os envia via Kafka, armazena no MongoDB e apresenta em tempo real por meio de Streamlit.

## 📁 Estrutura do Projeto

├── app.py # Aplicação Streamlit para visualização dos dados
├── consumer.py # Consumidor Kafka que persiste dados no MongoDB
├── producer.py # Produtor Kafka que envia os dados gerados
├── data_generate.py # Script que simula geração dos dados de sensores
├── requirements.txt # Dependências necessárias
├── Dockerfile / docker-compose.yml (opcional) # Ambiente Kafka + MongoDB
└── README.md # Este arquivo

## 🎯 Objetivo

Construir um pipeline simples para:

- Gerar dados sintéticos de temperatura e umidade via `data_generate.py`
- Enviar dados para um tópico Kafka (`producer.py`)
- Consumir dados do Kafka e salvar no MongoDB (`consumer.py`)
- Visualizar dados em tempo real com `app.py` via Streamlit

Ideal para aprendizado de ingestão e processamento de dados em tempo real.

## 🧰 Tecnologias

- **Python** – código principal
- **Kafka** – stream de mensagens entre produtor e consumidor
- **MongoDB** – armazenamento NoSQL dos dados coletados
- **Streamlit** – dashboard simples e interativo para visualização
- **confluent_kafka** ou **kafka-python** – cliente Kafka Python
- **pymongo** – driver MongoDB para Python

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8+
- Kafka e MongoDB rodando localmente ou via Docker Compose
- Dependências Python instaladas (`pip install -r requirements.txt`)

### Usando Docker (exemplo)

```yaml
services:
  zookeeper:
    image: wurstmeister/zookeeper
    ports:
      - "2181:2181"
  kafka:
    image: wurstmeister/kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
  mongo:
    image: mongo
    ports:
      - "27017:27017"
