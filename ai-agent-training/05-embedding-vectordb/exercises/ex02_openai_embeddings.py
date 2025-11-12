"""
练习 02: OpenAI Embeddings
难度: 🟢 基础
预计时间: 15分钟

目标：使用OpenAI的Embedding API
"""

from langchain.embeddings import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()


def create_embedding_model() -> OpenAIEmbeddings:
    """
    创建OpenAI Embedding模型
    
    返回:
        OpenAIEmbeddings实例
    """
    # TODO: 创建OpenAIEmbeddings
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("请设置OPENAI_API_KEY")
    
    return OpenAIEmbeddings()


def embed_texts(embedder: OpenAIEmbeddings, texts: list) -> list:
    """
    批量生成Embedding
    
    参数:
        embedder: Embedding模型
        texts: 文本列表
    
    返回:
        Embedding向量列表
    """
    # TODO: 使用embed_documents方法
    return embedder.embed_documents(texts)


def embed_query(embedder: OpenAIEmbeddings, query: str) -> list:
    """
    生成查询的Embedding
    
    参数:
        embedder: Embedding模型
        query: 查询文本
    
    返回:
        Embedding向量
    """
    # TODO: 使用embed_query方法
    return embedder.embed_query(query)


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        embedder = create_embedding_model()
        texts = ["Python是一种编程语言", "JavaScript用于前端开发"]
        embeddings = embed_texts(embedder, texts)
        print(f"生成了 {len(embeddings)} 个Embedding")
        print(f"每个Embedding维度: {len(embeddings[0])}")

