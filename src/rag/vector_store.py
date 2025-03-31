from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def get_vector_store():
    # โหลด embeddings โมเดล
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")
    # โหลด vector store
    vector_store = FAISS.load_local(
        # path ของ vector_store ที่สร้างไว้
        "D:\\rag-finder\\src\\rag\\faiss_index", embeddings, allow_dangerous_deserialization=True
    )
    return vector_store




