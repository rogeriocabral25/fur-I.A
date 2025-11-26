# 🤖 Fur I.A. - A Assistente Sarcástica

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini%20API-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![Google Cloud Run](https://img.shields.io/badge/Google_Cloud_Platform-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)

> *"Não sou paga para ser simpática. Sou paga para processar dados... e olhe lá."* — Fur I.A.

## 📖 Sobre o Projeto

A **Fur I.A.** é uma prova de conceito de um Chatbot Full-Stack com personalidade forte, hospedado na nuvem. Diferente das IAs assistentes tradicionais, ela foi programada via **Engenharia de Prompt** para ser sarcástica, rabugenta e direta.

O projeto utiliza a API mais recente do Google (**Gemini 2.5 Flash**) e converte as respostas de texto para áudio (TTS) em tempo real, rodando em arquitetura serverless no **Google Cloud Platform (GCP)**.

---

## 🔴 Demonstração ao Vivo (Google Cloud Run)

A aplicação está implantada em produção e rodando em um container no Google Cloud. Clique abaixo para testar:

<div align="center">

[![Acessar Demo Online](https://img.shields.io/badge/▶%EF%B8%8F_CLIQUE_AQUI_PARA_ACESSAR_A_DEMO-FF4B4B?style=for-the-badge&logo=google-cloud&logoColor=white)](https://fur-ia-app-355272677756.us-central1.run.app/)

**Link direto:** `https://fur-ia-app-355272677756.us-central1.run.app/`

</div>

---

## 🚀 Arquitetura e Tecnologias no GCP

Este projeto demonstra um fluxo moderno de Deploy de IA na nuvem do Google:

| Componente | Tecnologia GCP Utilizada | Função no Projeto |
| :--- | :--- | :--- |
| **Cérebro (IA)** | **Google Gemini API** | Modelo `gemini-2.5-flash` para geração de texto com raciocínio rápido. |
| **Hospedagem** | **Cloud Run** | Execução do container da aplicação de forma serverless (escala automática). |
| **Container** | **Docker** | Empacotamento da aplicação Streamlit e suas dependências. |
| **Build** | **Cloud Build** | (Implícito no deploy) Constrói a imagem do container na nuvem. |

---

## 💡 Destaques Técnicos & Desafios

### 1. Acesso ao Modelo Gemini 2.5 Flash
Durante o desenvolvimento, identifiquei discrepâncias entre o ambiente local e a nuvem. Implementei um **script de diagnóstico** que revelou acesso exclusivo a modelos experimentais na minha chave de API:
- **Desafio:** Erro `404 Model Not Found` persistente ao tentar usar modelos padrão.
- **Solução:** Diagnóstico de versões da biblioteca `google-generativeai` e migração bem-sucedida para o modelo experimental `gemini-2.5-flash`, superando as limitações das versões estáveis.

### 2. Personalidade vs. Filtros de Segurança no GCP
Para garantir que a IA mantivesse a persona "rude" sem ser bloqueada pela API na nuvem:
- Ajuste fino nos `safety_settings` (HarmBlockThreshold) para `BLOCK_NONE`.
- System Instruction robusta para definir o "roleplay" da IA.

---

## 📦 Como Rodar Localmente

Pré-requisitos: Python 3.9+ e uma chave de API do Google Gemini.

```bash
# 1. Clone o repositório
git clone [https://github.com/rogeriocabral25/fur-I.A.git](https://github.com/rogeriocabral25/fur-I.A.git)
cd fur-I.A

# 2. Crie um ambiente virtual
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# 3. Instale as dependências (Versão exata para suporte ao Gemini 2.5)
pip install -r requirements.txt

# 4. Configure a API Key
# Crie um arquivo .env na raiz e adicione: GEMINI_API_KEY="SUA_CHAVE"

# 5. Execute
streamlit run app.py

<h2>👨‍💻 Autor</h2>
<p><strong>Desenvolvido por Rogério Cabral</strong></p>

<div style="display: flex; gap: 10px;">

  <a href="https://www.linkedin.com/in/rog%C3%A9rio-cabral-609072397/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
  </a>

  <a href="https://github.com/rogeriocabral25" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white">
  </a>

</div>
