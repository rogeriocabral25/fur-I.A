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
