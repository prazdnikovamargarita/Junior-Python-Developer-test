import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
import uvicorn



# Встановлення API ключа OpenAI
os.environ["OPENAI_API_KEY"] = "your_api_key"
app = FastAPI()

# Ініціалізація моделі GPT-3 від OpenAI
llm = ChatOpenAI(model_name="gpt-3.5-turbo-1106", openai_api_key=os.getenv("OPENAI_API_KEY"))

class TextRequest(BaseModel):
    text: str


@app.post("/summarize")
async def summarize(request: TextRequest):
    data = request.text
    if not data:
        raise HTTPException(status_code=400, detail="Text is required for summarization")
    
    # Використання моделі GPT-3 для підсумовування
    result = llm.invoke(data)

    # Отримання підсумованого тексту з результату
    summary_text = result["output_text"]

    return {"summary": summary_text}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
