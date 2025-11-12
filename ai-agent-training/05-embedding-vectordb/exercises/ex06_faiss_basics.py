"""
练习 06: FAISS基础
难度: 🟡 进阶
预计时间: 20分钟

目标：使用FAISS向量数据库（适合大规模数据）
"""

from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv()


def create_faiss_vectorstore(documents: list):
    """
    创建FAISS向量库
    
    参数:
        documents: 文档列表
    
    返回:
        FAISS向量库实例
    """
    # TODO: 使用FAISS.from_documents
    if not os.getenv("OPENAI_API_KEY"):
        from langchain.embeddings.fake import FakeEmbeddings
        embeddings = FakeEmbeddings(size=1536)
    else:
        embeddings = OpenAIEmbeddings()
    
    return FAISS.from_documents(documents, embeddings)


def search_faiss(vectorstore, query: str, k: int = 3) -> list:
    """
    在FAISS中搜索
    
    参数:
        vectorstore: FAISS向量库
        query: 查询文本
        k: 返回数量
    
    返回:
        相似文档列表
    """
    # TODO: 使用similarity_search
    return vectorstore.similarity_search(query, k=k)


if __name__ == "__main__":
    documents = [
        Document(page_content="Python是一种编程语言"),
        Document(page_content="JavaScript用于前端开发"),
    ]
    
    vectorstore = create_faiss_vectorstore(documents)
    results = search_faiss(vectorstore, "编程", k=2)
    for doc in results:
        print(doc.page_content)

