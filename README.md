# Simulador de Algoritmos de Cache

Este projeto implementa um simulador de algoritmos de cache (LRU, LFU e FIFO) usando **Streamlit**. Ele permite visualizar o funcionamento de diferentes estratégias de substituição de cache e monitorar estatísticas como **hits** e **misses**.

## 🚀 Como baixar e rodar o projeto

### 1️⃣ Clonar o repositório
Abra um terminal e execute:
```sh
git clone https://github.com/gui439/simulacaocache.git
```
Entre na pasta do projeto:
```sh
cd simulacaocache
```

### 2️⃣ Criar um ambiente virtual (opcional, mas recomendado)
#### No Windows (CMD/Powershell):
```sh
python -m venv venv
venv\Scripts\activate
```
#### No macOS/Linux:
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar as dependências
```sh
pip install -r requirements.txt
```

### 4️⃣ Rodar o aplicativo
```sh
streamlit run app.py
```
Isso abrirá o aplicativo no seu navegador padrão na URL `http://localhost:8501`.

## 📌 Funcionalidades
- Selecionar o algoritmo de substituição de cache (**LRU, LFU, FIFO**)
- Buscar dados no banco simulado e verificar se estão na cache
- Exibir estatísticas de **hits** e **misses**
- Resetar os dados e reiniciar a simulação

## 📜 Tecnologias utilizadas
- **Python 3**
- **Streamlit**
- **Streamlit Extras**

## 📬 Contribuição
Se desejar contribuir, fique à vontade para abrir uma **issue** ou um **pull request**!

---
**Desenvolvido por [@gui439](https://github.com/gui439)** 🚀


