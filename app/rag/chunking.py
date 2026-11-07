from pathlib import Path

from langchain_core.embeddings import Embeddings
from langchain_experimental.text_splitter import SemanticChunker

from app.rag.embeddings import get_embedding_model


def chunk_text(
    text: str,
    embeddings: Embeddings | None = None,
    threshold: float = 90.0,
) -> list[str]:

    if not text or not text.strip():
        return []

    if not 0 <= threshold <= 100:
        raise ValueError("Threshold must be between 0 and 100.")

    if embeddings is None:
        embeddings = get_embedding_model()

    splitter = SemanticChunker(
        embeddings=embeddings,
        breakpoint_threshold_type="percentile",
        breakpoint_threshold_amount=threshold,
        buffer_size=0,
    )

    documents = splitter.create_documents([text])

    return [
        document.page_content.strip()
        for document in documents
        if document.page_content.strip()
    ]


def chunk_file(
    file_path: str | Path,
    embeddings: Embeddings | None = None,
    threshold: float = 90.0,
) -> list[str]:

    path = Path(file_path)
    text = path.read_text(encoding="utf-8")

    return chunk_text(
        text=text,
        embeddings=embeddings,
        threshold=threshold
    )