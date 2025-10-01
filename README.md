# Wikipedia Automation

Este projeto uma pessoa na Wikipédia e retorna o valor da linha **Alma mater** da infobox, se existir.

---

## Requirements

* **Python 3.9+**
* **Selenium**
* **webdriver-manager**
* **Google Chrome**

---

## Instalação

1. Decompacte o projeto e abra a pasta wikipedia_automation

2. Crie um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
.venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

Como Executar

```bash
python -m src.runner
```

## Padrão de Projeto

O projeto segue o padrão **Page Object Model (POM)**:

* Cada página da web tem uma classe que contém os elementos e ações da página
* A classe `BasePage` guarda o driver e pode ser expandida futuramente para mais métodos
* O `runner.py` é o script de test

## Para ver os logs

```bash
cat logs/run.log
```
