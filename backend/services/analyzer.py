from backend.services.summarizer import generate

def analyze_paper(text: str) -> dict:
    trimmed = " ".join(text.split()[:1000])

    def ask(question):
        prompt = f"Based on this research paper, answer the question briefly.\n\nPaper:\n{trimmed}\n\nQuestion: {question}\nAnswer:"
        try:
            return generate(prompt, max_new_tokens=150)
        except Exception:
            return "Could not extract."

    return {
        "research_question": ask("What is the main research question or problem this paper addresses?"),
        "methodology": ask("What methods or techniques were used in this study?"),
        "dataset": ask("What dataset or sample was used?"),
        "findings": ask("What were the main findings or results?"),
        "limitations": ask("What are the limitations of this study?"),
        "conclusion": ask("What is the main conclusion of this paper?"),
    }