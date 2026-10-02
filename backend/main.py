from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.services.pdf_processor import extract_text, chunk_text
from backend.services.summarizer import summarize
from backend.services.analyzer import analyze_paper

app = FastAPI(title="ResearchOS API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    contents = await file.read()
    text = extract_text(contents)

    if not text:
        return {"error": "Could not extract text from this PDF."}

    summary = summarize(text)
    analysis = analyze_paper(text)

    return {
        "filename": file.filename,
        "summary": summary,
        "analysis": analysis
    }

@app.get("/health")
def health():
    return {"status": "ResearchOS is running"}

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")