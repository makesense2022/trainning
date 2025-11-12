"""
练习 03: 本地Embedding模型
难度: 🟡 进阶
预计时间: 20分钟

目标：使用本地Embedding模型（不调用API）
"""

from langchain.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer


def create_local_embedder(model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
    """
    创建本地Embedding模型
    
    参数:
        model_name: 模型名称
    
    返回:
        HuggingFaceEmbeddings实例
    """
    # TODO: 使用HuggingFaceEmbeddings
    return HuggingFaceEmbeddings(model_name=model_name)


def embed_with_local(embedder, texts: list) -> list:
    """
    使用本地模型生成Embedding
    
    参数:
        embedder: Embedding模型
        texts: 文本列表
    
    返回:
        Embedding列表
    """
    # TODO: 使用embed_documents
    return embedder.embed_documents(texts)


if __name__ == "__main__":
    # 注意：首次运行会下载模型
    embedder = create_local_embedder()
    texts = ["Python是一种编程语言", "JavaScript用于前端开发"]
    embeddings = embed_with_local(embedder, texts)
    print(f"生成了 {len(embeddings)} 个Embedding")

