from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

_model = None
_tokenizer = None

def load_model():
    global _model, _tokenizer
    if _model is None:
        print("Loading model...")
        _tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
        _model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
        _model.eval()
        print("Model loaded.")

def generate(prompt: str, max_new_tokens: int = 300) -> str:
    load_model()
    inputs = _tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)
    with torch.no_grad():
        outputs = _model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            pad_token_id=_tokenizer.eos_token_id
        )
    decoded = _tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded[len(_tokenizer.decode(inputs["input_ids"][0], skip_special_tokens=True)):].strip()

def summarize(text: str) -> str:
    trimmed = " ".join(text.split()[:1000])
    prompt = f"Summarize this research paper clearly and concisely:\n\n{trimmed}\n\nSummary:"
    return generate(prompt, max_new_tokens=250)