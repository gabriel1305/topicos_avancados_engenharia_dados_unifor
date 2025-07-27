# 🔧 Projeto de Simulação de Sensor de Temperatura e Umidade

Este projeto simula um sensor que gera dados de temperatura e umidade, os envia via Kafka, armazena no MongoDB e apresenta em tempo real por meio de Streamlit.

---

## 📁 Estrutura do Projeto

```bash
├── app.py                  # Aplicação Streamlit para visualização dos dados
├── consumer.py             # Consumidor Kafka que persiste dados no MongoDB
├── producer.py             # Produtor Kafka que envia os dados gerados
├── data_generate.py        # Script que simula geração dos dados de sensores
├── requirements.txt        # Dependências necessárias
├── Dockerfile              # (Opcional) Configuração para container do app
├── docker-compose.yml      # (Opcional) Ambiente Kafka + MongoDB
└── README.md               # Este arquivo

---

🎯 Objetivo

Construir um pipeline simples para:

Gerar dados sintéticos de temperatura e umidade via data_generate.py

Enviar dados para um tópico Kafka (producer.py)

Consumir dados do Kafka e salvar no MongoDB (consumer.py)

Visualizar dados em tempo real com app.py via Streamlit

Ideal para aprendizado de ingestão e processamento de dados em tempo real.
