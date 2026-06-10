# Сдача домашнего задания

**Ссылка на репозиторий:** https://github.com/tshermatova/rag-homework-movies

**Описание:** RAG pipeline на данных Wikipedia Movie Plots
- Ingest: CSV → JSON (1000 фильмов)
- Chunking: RecursiveCharacterTextSplitter (LangChain)
- Index: TF-IDF + scikit-learn
- Retrieval: cosine similarity, top-k
- Generation: demo-ответ с источниками
- UI: Streamlit с отображением источников

**Запуск:** uv sync + build_index + streamlit

**Demo-вопросы:** space astronauts, prison escape, love romance wedding, quantum physics biology (negative)

**Улучшения:** RecursiveCharacterTextSplitter, метаданные, 1000+ записей

**Тесты:** 11 тестов green
