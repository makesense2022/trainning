"""
练习 09: MMR检索
难度: 🟡 进阶
预计时间: 25分钟

目标：使用MMR提高检索多样性
"""

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv()


def mmr_retrieval(vectorstore: Chroma, query: str, k: int = 3, fetch_k: int = 10) -> list:
    """
    MMR检索
    
    参数:
        vectorstore: 向量库
        query: 查询
        k: 返回数量
        fetch_k: 初始检索数量
    
    返回:
        多样化的文档列表
    """
    # TODO: 使用max_marginal_relevance_search
    return vectorstore.max_marginal_relevance_search(query, k=k, fetch_k=fetch_k)


if __name__ == "__main__":
    documents = [
        Document(page_content="Python是一种编程语言"),
        Document(page_content="Python用于数据科学"),
        Document(page_content="Python用于Web开发"),
    ]
    
    if os.getenv("OPENAI_API_KEY"):
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(documents, embeddings)
        results = mmr_retrieval(vectorstore, "Python", k=2)
        for doc in results:
            print(doc.page_content)

