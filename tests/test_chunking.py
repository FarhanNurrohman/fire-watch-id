from pathlib import Path

from langchain_core.embeddings import Embeddings
from app.rag.chunking import chunk_file, chunk_text


class FakeEmbeddings(Embeddings):

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        vectors = []

        for text in texts:
            text = text.lower()

            if "asap" in text:
                vectors.append([1.0, 0.0])

            elif "banjir" in text:
                vectors.append([0.0, 1.0])

            else:
                vectors.append([0.5, 0.5])

        return vectors

    def embed_query(self, text: str) -> list[float]:
        return self.embed_documents([text])[0]


def test_empty_text():
    result = chunk_text("", embeddings=FakeEmbeddings())
    assert result == []


def test_invalid_threshold():
    try:
        chunk_text(
            "Contoh teks.",
            embeddings=FakeEmbeddings(),
            threshold=133
        )
    except ValueError:
        pass
    else:
        assert False, "Exception ValueError"


def test_chunk_file(tmp_path: Path):
    file_path = tmp_path / "document.txt"

    file_path.write_text(
        "Asap dapat mengganggu pernapasan. "
        "Asap kebakaran perlu dihindari. "
        "Banjir dapat menyebabkan genangan air. "
        "Banjir dapat merusak permukiman.",
        encoding="utf-8"
    )

    chunks = chunk_file(
        file_path,
        embeddings=FakeEmbeddings(),
        threshold=50
    )

    assert isinstance(chunks, list)
    assert len(chunks) >= 2

    for chunk in chunks:
        assert isinstance(chunk, str)
        assert len(chunk) > 0