# Projeto de Automação de Teste de Login

Este projeto consiste em testes automatizados para a funcionalidade de login de um sistema utilizando Selenium e Pytest em Python.

## Estrutura do Projeto

C:.
│   README.md
│   int.py
│   pyvenv.cfg
│
├───Lib
│   └───site-packages
│
├───Scripts
│
├───alteracoes
│
├───assets
│
└───tests
        test_login.py
        test_senha_invalida.py
        test_login_invalido.py


## 1.Como Executar
Clone este repositório em sua máquina local:

bash
git clone https://github.com/LarissaStringhetta/Projeto.git

## 2.Navegue até o diretório do projeto:

bash
cd Projeto/Automation

## 3.Instale as dependências do projeto:

bash
pip install -r requirements.txt

## 4.Execute os testes:

bash
pytest tests/
Após a execução dos testes, um relatório em HTML será gerado na raiz do projeto (report.html), contendo os resultados dos testes.
