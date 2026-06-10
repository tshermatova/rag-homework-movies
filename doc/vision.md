# Vision — техническое видение проекта

**Учебный RAG** на описаниях фильмов Wikipedia: локально, просто, с ответом и источниками.

## Технологии

| Слой | Выбор | Комментарий |
|------|-------|-------------|
| Язык | Python 3.10+ | — |
| Окружение | uv + `.venv` | Локально, не коммитим |
| UI | Streamlit | Один entry point, видны чанки, scores и источники |
| Поиск | TF-IDF + cosine similarity (scikit-learn) | Без torch и тяжёлых моделей |
| Индекс | Локальные файлы (`data/index/`) | `vectorizer.pkl` + `matrix.npz` + `chunks.jsonl` |
| LLM | Только demo-режим | Ответ из найденных чанков по правилам |
| Chunking | RecursiveCharacterTextSplitter (LangChain) | Улучшение по сравнению с кастомным chunker |
| Данные | Wikipedia Movie Plots → `datasets.json` | 1000 записей |
| Тесты | pytest | 5+ тестов: chunking, retrieval, источники |

## Улучшения

1. **RecursiveCharacterTextSplitter** вместо кастомного chunker — лучшее разбиение по семантическим границам
2. **Метаданные** (год, режиссёр) в UI и ответе

## Не используем в MVP

ChromaDB, sentence-transformers, torch, LangChain (кроме text-splitters), LlamaIndex, FastAPI, Docker, reranking, hybrid search, OpenAI, Kaggle API, pandas для анализа CSV.
