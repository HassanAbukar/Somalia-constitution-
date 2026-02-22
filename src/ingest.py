from pypdf import PdfReader
from memvid import MemvidEncoder
# from sentence_transformers import SentenceTransformer
from tqdm import tqdm
import os

PDF_PATH = "data/constitution.pdf"
OUTPUT_VIDEO = "memory/constitution.mp4"
OUTPUT_INDEX = "memory/index.json"

CHUNK_SIZE = 500  # characters

def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def chunk_text(text, size):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + size])
        start += size
    return chunks

def main():
    os.makedirs("memory", exist_ok=True)

    print("📄 Akhrinaya PDF...")
    text = load_pdf(PDF_PATH)

    print("✂️ Chunking...")
    chunks = chunk_text(text, CHUNK_SIZE)

    print(f"🧠 Helay {len(chunks)} chunks")

    print("🎥 Dhisaya Memvid memory...")
    encoder = MemvidEncoder()
        # embedder=SentenceTransformer("all-MiniLM-L6-v2")
    

    for chunk in tqdm(chunks):
        encoder.add_chunks(chunk)

    encoder.build_video(
        OUTPUT_VIDEO,
        OUTPUT_INDEX
    )

    print("✅ Dhamaaday!")
    print(f"Memory: {OUTPUT_VIDEO}")
    print(f"Index:  {OUTPUT_INDEX}")

if __name__ == "__main__":
    main()
