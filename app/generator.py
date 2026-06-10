"""Demo-ответ: top-k чанки -> текст + источники (без внешней LLM)."""

from app.config import TOP_K
from app.prompts import REFUSAL_EMPTY_QUESTION, REFUSAL_NO_CONTEXT
from app.retriever import Retriever

def build_answer(hits: list[dict]) -> str:
    """Формирует ответ только из релевантных чанков."""
    if not hits:
        return REFUSAL_NO_CONTEXT
    
    max_score = max(h["score"] for h in hits)
    
    # Если максимальный score слишком низкий — полный отказ
    if max_score < 0.21:
        return REFUSAL_NO_CONTEXT
    
    # Порог: выше 0.5 * максимального
    threshold = 0.5 * max_score
    
    relevant = [h for h in hits if h["score"] >= threshold]
    
    if not relevant:
        return REFUSAL_NO_CONTEXT

    parts = ["На основании найденных фрагментов:"]
    for i, hit in enumerate(relevant, 1):
        meta = hit.get("metadata", {})
        year = meta.get("year")
        director = meta.get("director", "Unknown")
        
        parts.append(f"\n[{i}] {hit['name']}")
        if year:
            parts.append(f"Год: {year}, Режиссёр: {director}")
        parts.append(f"doc_id={hit['doc_id']}, score={hit['score']:.2f}")
        parts.append(hit["text"])
    return "\n".join(parts)

def format_sources(hits: list[dict]) -> list[dict]:
    return [
        {
            "doc_id": hit["doc_id"],
            "name": hit.get("name", ""),
            "text": hit["text"],
            "score": hit["score"],
            "metadata": hit.get("metadata", {}),
        }
        for hit in hits
    ]

def ask(
    question: str,
    k: int = TOP_K,
    retriever: Retriever | None = None,
) -> dict:
    """Вопрос -> ответ и список источников."""
    if not question.strip():
        return {"answer": REFUSAL_EMPTY_QUESTION, "sources": []}

    r = retriever or Retriever()
    hits = r.search(question.strip(), k=k)
    return {
        "answer": build_answer(hits),
        "sources": format_sources(hits),
    }
