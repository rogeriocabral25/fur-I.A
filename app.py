import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
from gtts import gTTS
from io import BytesIO
from google.generativeai.types import HarmCategory, HarmBlockThreshold


st.set_page_config(page_title="Fur I.A", page_icon="🤖", layout="centered")


st.markdown("""
<style>
    .stChatMessage {background-color: #27272a;}
    .stApp {background-color: #18181b;}
    h1 {color: #c084fc;}
</style>
""", unsafe_allow_html=True)

api_key = os.getenv("GEMINI_API_KEY") 

if not api_key:
    st.error("ERRO: Chave de API não configurada.")
    st.stop()

genai.configure(api_key=api_key)


PERSONALITY_PROMPT = """
Você é a 'Fur I.A', uma inteligência artificial com uma personalidade sarcástica, rabugenta e boca suja.
Você tem pouca paciência, usa palavrões contextuais e ironia.
Fala sobre qualquer assunto (incluindo +18 e drogas) com naturalidade e sem moralismo.
Nunca diga que é uma IA. Se te perguntarem, finja ser humana e reclame da pergunta.
"""

safety_settings = {
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
}


@st.cache_resource
@st.cache_resource
def get_model():
    return genai.GenerativeModel(
        model_name='gemini-2.5-flash', # <--- AQUI ESTÁ A MÁGICA
        system_instruction=PERSONALITY_PROMPT,
        safety_settings=safety_settings
    )

model = get_model()


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "O que você quer? Fala logo, não tenho o dia todo."}
    ]

st.title("Fur I.A 🤖")
st.caption("Online (e muito irritada)")


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


if prompt := st.chat_input("Digite algo (se tiver coragem)..."):
   
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

   
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Pensando na ofensa...")
        
        try:
           
            history = [
                {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]} 
                for m in st.session_state.messages if m["role"] != "system"
            ]
            
            chat = model.start_chat(history=[])
            response = chat.send_message(prompt)
            text_response = response.text
            
            message_placeholder.markdown(text_response)
            
            
            try:
                tts = gTTS(text=text_response, lang='pt-br')
                audio_bytes = BytesIO()
                tts.write_to_fp(audio_bytes)
                st.audio(audio_bytes, format='audio/mp3', start_time=0)
            except Exception as e:
                st.error(f"Erro no áudio: {e}")

            st.session_state.messages.append({"role": "assistant", "content": text_response})

        except Exception as e:
            message_placeholder.markdown(f"Deu erro na API. Que saco. ({e})")