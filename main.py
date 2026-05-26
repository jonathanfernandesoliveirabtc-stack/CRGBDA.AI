# Primeiro instala a biblioteca se não tiver: pip install python-dotenv
from dotenv import load_dotenv
import os

# Carrega as informações do arquivo .env
load_dotenv()

# Pega a chave que está dentro do arquivo
chave_api = os.getenv("GEMINI_API_KEY")