import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. Carrega a chave
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("--- DIAGNÓSTICO FUR I.A ---")

# Se não achou no .env, tenta forçar (SUBSTITUA AQUI SE PRECISAR)
if not api_key:
    print("AVISO: Chave não encontrada no .env")
    # api_key = "COLE_SUA_CHAVE_NOVA_AQUI_SE_DER_ERRO" 
else:
    print(f"Chave carregada: {api_key[:5]}... (Verifique se é a correta)")

if not api_key:
    print("ERRO FATAL: Sem chave de API.")
    exit()

#  Configura
genai.configure(api_key=api_key)

#  Pergunta pro Google quais modelos existem
print("\nPerguntando ao Google quais modelos estão disponíveis para você...")
try:
    modelos = list(genai.list_models())
    encontrou_flash = False
    
    if not modelos:
        print("RESULTADO: A lista veio vazia! Sua chave ou projeto tem problemas.")
    
    for m in modelos:
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ Disponível: {m.name}")
            if "gemini-1.5-flash" in m.name:
                encontrou_flash = True

    if encontrou_flash:
        print("\nCONCLUSÃO: O modelo 1.5 Flash ESTÁ disponível. O erro no app é digitação ou cache.")
    else:
        print("\nCONCLUSÃO: Sua conta NÃO tem acesso ao Flash. Você precisa habilitar no Google Cloud.")

except Exception as e:
    print(f"\n❌ ERRO CRÍTICO AO CONECTAR: {e}")
    print("Dica: Verifique se a 'Generative Language API' está ativada no seu projeto.")