"""Проверка retrieval из консоли."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app.retriever import Retriever

def main():
    r = Retriever()
    
    queries = [
        "dreams subconscious",
        "space astronauts",
        "prison escape",
        "how to cook borscht",
    ]
    
    for q in queries:
        print(f"\n{'='*50}")
        print(f"Вопрос: {q}")
        results = r.search(q, k=3)
        if not results:
            print("Нет результатов")
            continue
        for i, hit in enumerate(results, 1):
            meta = hit.get("metadata", {})
            print(f"\n[{i}] {hit['name']} ({meta.get('year', 'N/A')})")
            print(f"    doc_id={hit['doc_id']}, score={hit['score']:.4f}")
            print(f"    {hit['text'][:200]}...")

if __name__ == "__main__":
    main()
