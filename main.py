from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from explanation_module import explain_concept
from qna import answer_question
from summary_module import summarize_text
from quiz_module import generate_quiz
from learning_path import generate_learning_path

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/ask")
async def ask(data: dict):
    question = data.get("question", "")

    if not question:
        return JSONResponse(
            {"answer": "Please enter a question."}
        )

    result = answer_question(question)

    return JSONResponse(
        {"answer": result}
    )


@app.post("/explain")
async def explain(data: dict):
    topic = data.get("topic", "")

    if not topic:
        return JSONResponse(
            {"explanation": "Please enter a topic."}
        )

    result = explain_concept(topic)

    return JSONResponse(
        {"explanation": result}
    )


@app.post("/summarize")
async def summarize(data: dict):
    text = data.get("text", "")

    if not text:
        return JSONResponse(
            {"summary": "Please enter some text."}
        )

    result = summarize_text(text)

    return JSONResponse(
        {"summary": result}
    )


@app.post("/quiz")
async def quiz(data: dict):
    topic = data.get("topic", "")

    if not topic:
        return JSONResponse(
            {"quiz": []}
        )

    result = generate_quiz(topic)

    return JSONResponse(
        {"quiz": result}
    )


@app.post("/learning-path")
async def learning_path(data: dict):
    topic = data.get("topic", "")

    if not topic:
        return JSONResponse(
            {"learning_path": "Please enter a subject."}
        )

    result = generate_learning_path(topic)

    return JSONResponse(
        {"learning_path": result}
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )