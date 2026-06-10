# Workflow — порядок работы

## Цикл одной итерации

## Итерации

| № | Название | Проверка |
|---|----------|----------|
| 0 | Каркас проекта | `uv sync` без ошибок |
| 1 | Данные Kaggle | CSV → JSON, ≥1000 записей |
| 2 | Ingestion | `documents.jsonl` создан |
| 3 | Chunking (RecursiveCharacterTextSplitter) | `chunks.jsonl`, тесты green |
| 4 | Индекс TF-IDF | файлы в `data/index/` |
| 5 | Retrieval | top-k + score в консоли |
| 6 | Demo-ответ | ответ + источники без UI |
| 7 | Streamlit UI | 3 demo-вопроса в браузере |
| 8 | Тесты и README | `pytest` green, README воспроизводим |
| 9 | Документ о данных | `doc/DATA.md` — источники, назначение |
| 10 | Домашнее задание | `homework/` — планирование + реализация |
