"""Chunking: documents.jsonl → chunks.jsonl."""

import json
from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import CHUNK_MAX_CHARS, CHUNK_OVERLAP, DOCUMENTS_JSONL, CHUNKS_JSONL

def get_text_splitter() -> RecursiveCharacterTextSplitter:
    """Создаёт RecursiveCharacterTextSplitter с настройками из конфига."""
    return RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_MAX_CHARS,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

def chunk_document(doc: dict, splitter: RecursiveCharacterTextSplitter) -> list[dict]:
    """Один документ → список чанков с метаданными."""
    chunks = []
    texts = splitter.split_text(doc["text"])
    for i, text in enumerate(texts):
        chunks.append({
            "chunk_id": f"{doc['doc_id']}_{i}",
            "doc_id": doc["doc_id"],
            "name": doc["name"],
            "text": text,
            "metadata": doc.get("metadata", {}),
        })
    return chunks

def load_documents(path: Path) -> list[dict]:
    documents = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                documents.append(json.loads(line))
    return documents

def write_chunks(chunks: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

def run(
    input_path: Path = DOCUMENTS_JSONL,
    output_path: Path = CHUNKS_JSONL,
) -> int:
    if not input_path.exists():
        raise FileNotFoundError(f"Не найден файл: {input_path}")

    documents = load_documents(input_path)
    splitter = get_text_splitter()
    all_chunks: list[dict] = []
    for doc in documents:
        all_chunks.extend(chunk_document(doc, splitter))

    write_chunks(all_chunks, output_path)
    return len(all_chunks)

def main() -> None:
    count = run()
    print(f"Записано {count} чанков -> {CHUNKS_JSONL}")

if __name__ == "__main__":
    main()
