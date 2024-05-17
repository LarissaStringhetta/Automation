# Projeto de Automação de Teste de Login

Este projeto consiste em testes automatizados para a funcionalidade de login de um sistema utilizando Selenium e Pytest em Python.

## Estrutura do Projeto

C:\Users\Windows11\Projeto\Automation
│   README.md       # Este arquivo
│   int.py          # Script principal de automação
│   pyvenv.cfg      # Configuração do ambiente virtual Python
│
└───tests           # Pasta com os arquivos de teste
│   │   test_login.py            # Testes relacionados ao login
│   │   test_senha_invalida.py   # Testes de senha inválida
│   │   test_login_invalido.py   # Testes de login inválido
│   
└───Lib             # Pasta com as bibliotecas utilizadas
│   └───site-packages
│       # Bibliotecas do Python
│   
└───Scripts         # Scripts de instalação e configuração
│   # Scripts diversos
│
└───assets          # Recursos utilizados nos testes
│   # Imagens, documentos, etc.
│
└───alteracoes      # Pasta com arquivos alterados
│   # Arquivos alterados durante o desenvolvimento
│
└───report.html     # Relatório HTML gerado após a execução dos testes

1.Como Executar
Clone este repositório em sua máquina local:

bash
git clone https://github.com/LarissaStringhetta/Projeto.git

2.Navegue até o diretório do projeto:

bash
cd Projeto/Automation

3.Instale as dependências do projeto:

bash
pip install -r requirements.txt

4.Execute os testes:

bash
pytest tests/
Após a execução dos testes, um relatório em HTML será gerado na raiz do projeto (report.html), contendo os resultados dos testes.
