from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Inicialização do FastAPI
app = FastAPI()

# Modelo de entrada
class TextInput(BaseModel):
    text: str

# Configuração do LangChain com OpenAI
llm = OpenAI(temperature=0)
prompt_template = PromptTemplate(
    input_variables=["text"],
    template="Translate the following text to French: {text}"
)
translation_chain = LLMChain(llm=llm, prompt=prompt_template)

@app.post("/translate_openai/")
async def translate_text(input: TextInput):
    translation = translation_chain.invoke(input.text)
    return {"input": input.text, "translation": translation}

'''
Set OPENAI_API_KEY in .env

Executar com:
curl -X POST "http://127.0.0.1:8000/translate/"
-H "Content-Type: application/json"
-d '{"text": "I am a Data Scientist and work with machine learning models on a daily basis."}'
'''