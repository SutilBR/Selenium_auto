Cadastro de Notas e Análise de Dados
Este é um projeto desenvolvido para otimizar o processo de cadastro de notas fiscais e análise de dados utilizando Python, Streamlit, SQLite e Selenium. O sistema automatiza o cadastro de notas em um banco de dados SQLite e gera gráficos interativos de forma simples e eficiente.

Objetivo
O objetivo principal do projeto é fornecer uma solução rápida e automatizada para o cadastro de notas fiscais, permitindo o acompanhamento de dados por contrato e a geração de relatórios dinâmicos. O sistema também integra funcionalidades de automação para coletar dados e preenchê-los diretamente em um sistema web.

Funcionalidades
Cadastro de Notas: Permite ao usuário cadastrar informações de notas fiscais (contrato, número da nota, quantidade e valor) diretamente em um banco de dados SQLite.
Visualização de Dados: Exibe um gráfico de barras que mostra a quantidade de notas por contrato.
Automação Web com Selenium: Automação do preenchimento de um sistema web utilizando Selenium para enviar dados de notas pendentes diretamente no sistema.
Tecnologias Usadas
Streamlit: Para construção da interface interativa.
SQLite: Banco de dados leve e simples para armazenar as notas fiscais.
Python: Linguagem de programação para automatizar o processo de coleta, cadastro e visualização dos dados.
Selenium: Para automação de navegação e preenchimento de formulários em um sistema web.
Pandas: Para manipulação e análise dos dados.
Matplotlib: Para geração de gráficos.
Como Rodar o Projeto
Requisitos
Antes de rodar o projeto, certifique-se de ter o Python instalado em sua máquina. Além disso, instale as dependências necessárias:

pip install -r requirements.txt
Rodando o Projeto
Certifique-se de que o banco de dados cadastro.db está presente na raiz do projeto.
Execute o seguinte comando para iniciar o aplicativo Streamlit:

streamlit run src/main.py
Para rodar a automação de preenchimento de notas, execute:

python src/auto.py
Exemplo de Fluxo
Cadastro de Notas: Abra o sistema Streamlit para preencher as informações de cada nota.
Visualização de Gráficos: Após o cadastro, você poderá ver o gráfico de barras que exibe a quantidade de notas por contrato.
Automação de Preenchimento: Utilize o Selenium para preencher automaticamente as notas pendentes em um sistema web configurado localmente.
Estrutura do Projeto

meu-sistema/
│
├── src/
│   ├── main.py        # Código principal para o cadastro e visualização de dados
│   ├── auto.py        # Código para automação com Selenium
│
├── cadastro.db        # Banco de dados SQLite contendo as notas
├── notas pendentes.xlsx # Planilha Excel com as notas pendentes
├── venv/              # Ambiente virtual (não versionado)
├── requirements.txt   # Dependências do projeto
