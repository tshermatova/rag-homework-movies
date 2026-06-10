"""Тесты нарезки текста на чанки."""

from app.chunker import chunk_document, get_text_splitter, run
from app.config import CHUNK_MAX_CHARS, CHUNKS_JSONL

def test_splitter_respects_max_size():
    splitter = get_text_splitter()
    text = "Абзац один.\n\n" + "слово " * 200
    chunks = splitter.split_text(text)
    assert chunks
    assert all(len(c) <= CHUNK_MAX_CHARS for c in chunks)

def test_splitter_splits_by_paragraphs():
    splitter = get_text_splitter()
    text = "Первый абзац про кино.\n\nВторой абзац про театр."
    chunks = splitter.split_text(text)
    assert len(chunks) >= 1
    full_text = " ".join(chunks)
    assert "кино" in full_text
    assert "театр" in full_text

def test_splitter_overlap():
    splitter = get_text_splitter()
    para1 = "А" * 300
    para2 = "Б" * 300
    text = f"{para1}\n\n{para2}"
    chunks = splitter.split_text(text)
    assert len(chunks) >= 2
    assert len(chunks[1]) > 0

def test_chunk_document_has_doc_id():
    splitter = get_text_splitter()
    doc = {
        "doc_id": "42",
        "name": "Тестовый фильм",
        "text": "Описание сюжета: главный герой спасает мир.",
        "metadata": {"year": 2020},
    }
    chunks = chunk_document(doc, splitter)
    assert len(chunks) >= 1
    assert chunks[0]["doc_id"] == "42"
    assert chunks[0]["chunk_id"].startswith("42_")
    assert chunks[0]["name"] == "Тестовый фильм"
    assert chunks[0]["metadata"]["year"] == 2020

def test_run_creates_chunks_jsonl(tmp_path):
    docs = tmp_path / "documents.jsonl"
    docs.write_text(
        '{"doc_id": "0", "name": "A", "text": "Короткий текст.", "metadata": {}}\n',
        encoding="utf-8",
    )
    out = tmp_path / "chunks.jsonl"
    count = run(input_path=docs, output_path=out)
    assert count >= 1
    assert out.exists()
    line = out.read_text(encoding="utf-8").strip()
    assert '"doc_id": "0"' in line
