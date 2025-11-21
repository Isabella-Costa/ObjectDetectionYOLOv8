## Detecção de Objetos: Caderno, Xícara e Piloto com YOLOv8

✨ Introdução ao Projeto
Este repositório contém o código-fonte e o modelo treinado para um projeto de Visão Computacional focado na Detecção de Objetos em Tempo Real utilizando a arquitetura YOLOv8 (You Only Look Once, versão 8).

O objetivo do projeto foi realizar o Fine-Tuning de um modelo YOLOv8 pré-treinado para reconhecer e localizar três classes específicas:

* 📘 Caderno
* ☕ Xícara
* 🖊️ Piloto de Quadro
---
## Como Executar o Projeto
Siga os passos abaixo.

### 1. Pré-requisitos
Certifique-se de ter instalado:
* Python 3.8+
* Git

### 2. Clonar o Repositório
Primeiro, clone este repositório para o seu sistema local usando o Git:

```Bash

git clone https://docs.github.com/pt/repositories/creating-and-managing-repositories/quickstart-for-repositories
cd [Nome da Pasta Clonada]
```

### 4. Criar e Ativar o Ambiente Virtual
É altamente recomendado criar um ambiente virtual para isolar as dependências:

Criar o ambiente:

```Bash
python -m venv venv
```
Ativar o ambiente:
```bash
.\venv\Scripts\activate #Windows (PowerShell)

source venv/bin/activate #Linux/macOS (Bash):
```
### 5. Instalar as Dependências

```Bash
pip install -r requirements.txt
````

### 6. Rodar o Arquivo Principal
O arquivo principal, detect_camera.py (ou o nome do seu script), irá carregar o modelo treinado e iniciar a captura de vídeo pela sua webcam.
```bash
python detect_camera.py
```
Uma janela pop-up se abrirá, mostrando a detecção de objetos em tempo real. Pressione a tecla 'q' para fechar a janela.
