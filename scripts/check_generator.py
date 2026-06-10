"""Проверка demo-ответа из консоли."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app.generator import ask

def main():
    questions = [
        "space astronauts",
        "prison escape",
        "love romance wedding",
        "quantum physics biology",  # negative
    ]
    
    for q in questions:
        print(f"\n{'='*60}")
        print(f"Вопрос: {q}")
        result = ask(q)
        print(f"\nОтвет:\n{result['answer']}")
        print(f"\nИсточники ({len(result['sources'])}):")
        for src in result["sources"]:
            meta = src.get("metadata", {})
            print(f"  - {src['name']} ({meta.get('year', 'N/A')}) | score={src['score']:.4f}")

if __name__ == "__main__":
    main()
