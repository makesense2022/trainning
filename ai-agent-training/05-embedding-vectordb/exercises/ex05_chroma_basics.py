"""
练习 05: ChromaDB基础
难度: 🟢 基础
预计时间: 20分钟

目标：掌握ChromaDB向量数据库的基本使用
"""

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv()


def create_vectorstore(documents: list) -> Chroma:
    """
    创建ChromaDB向量库
    
    参数:
        documents: 文档列表
    
    返回:
        Chroma向量库实例
    """
    # TODO: 使用Chroma.from_documents创建向量库
    # 如果没有API Key，可以使用fake embeddings
    if os.getenv("OPENAI_API_KEY"):
        embeddings = OpenAIEmbeddings()
    else:
        # 使用fake embeddings用于测试
        from langchain.embeddings.fake import FakeEmbeddings
        embeddings = FakeEmbeddings(size=1536)
    
    # TODO: 创建向量库
    pass


def add_documents_to_store(vectorstore: Chroma, documents: list):
    """
    向向量库添加文档
    
    参数:
        vectorstore: Chroma向量库
        documents: 新文档列表
    """
    # TODO: 使用add_documents方法
    pass


def search_similar(vectorstore: Chroma, query: str, k: int = 3) -> list:
    """
    在向量库中搜索相似文档
    
    参数:
        vectorstore: Chroma向量库
        query: 查询文本
        k: 返回结果数量
    
    返回:
        相似文档列表
    """
    # TODO: 使用similarity_search方法
    pass


if __name__ == "__main__":
    # 创建测试文档
    documents = [
        Document(page_content="Python是一种编程语言", metadata={"source": "doc1"}),
        Document(page_content="JavaScript是前端开发语言", metadata={"source": "doc2"}),
        Document(page_content="AI是人工智能的缩写", metadata={"source": "doc3"}),
    ]
    
    # 测试向量库
    vectorstore = create_vectorstore(documents)
    results = search_similar(vectorstore, "编程", k=2)
    for doc in results:
        print(f"内容: {doc.page_content}")
        print(f"来源: {doc.metadata}")

