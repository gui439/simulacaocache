Para rodar essa aplicação Streamlit em qualquer máquina, você só precisa seguir alguns passos!:

Instalar Python: Verifique se o Python está instalado na máquina. 
Criar um ambiente virtual (opcional, mas recomendado):

sh
python -m venv venv
Ativar o ambiente virtual:

No Windows:
sh
venv\Scripts\activate
No macOS/Linux:
sh
source venv/bin/activate
Instalar as dependências: Crie um arquivo chamado requirements.txt na mesma pasta do seu script com o seguinte conteúdo:

txt
streamlit
streamlit-extras
Depois, rode o comando:

sh
pip install -r requirements.txt
Baixar o arquivo do código: Salve o código que você me enviou em um arquivo chamado, por exemplo, app.py.

Rodar a aplicação: Na pasta onde está o arquivo app.py, execute:

sh
streamlit run app.py
Acessar a aplicação: O Streamlit vai abrir uma aba no seu navegador padrão com o endereço local, algo como http://localhost:8501. Pronto! A aplicação estará rodando.

