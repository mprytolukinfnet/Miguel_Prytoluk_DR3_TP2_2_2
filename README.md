# TP2 Exercício 2_2: Tradução via OpenAI e LangChain
Aplicação FastAPI que utiliza LangChain para integrar a API da OpenAI e traduzir textos do inglês para o francês.

**Passos para Configuração**:

1. Certifique-se de que o ambiente Python está configurado.
2. Crie um arquivo `.env` e adicione sua chave de API da OpenAI:
3. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

**Como Executar**: Inicie o servidor FastAPI com o comando:
```bash
uvicorn 2_2:app --reload
```

**Uso da API**: Traduza um texto:

```bash
curl -X POST "http://127.0.0.1:8000/translate_openai/" \
-H "Content-Type: application/json" \
-d '{"text": "Hello, how are you?"}'
```