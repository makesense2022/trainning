"""
练习 07: 混合检索
难度: 🔴 挑战
预计时间: 30分钟

目标：结合向量检索和关键词检索（BM25）
"""

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv()


def hybrid_search(vectorstore: Chroma, query: str, k: int = 3) -> list:
    """
    混合检索（向量 + 关键词）
    
    参数:
        vectorstore: 向量库
        query: 查询
        k: 返回数量
    
    返回:
        融合后的文档列表
    
    注意：这里简化实现，实际应该使用BM25进行关键词检索
    """
    # TODO: 实现混合检索
    # 1. 向量检索
    vector_results = vectorstore.similarity_search(query, k=k*2)
    
    # 2. 关键词检索（简化：使用包含查询词的文档）
    # 实际应该使用BM25算法
    keyword_results = [
        doc for doc in vectorstore.similarity_search(query, k=k*2)
        if query.lower() in doc.page_content.lower()
    ]
    
    # 3. 融合结果（去重）
    seen = set()
    results = []
    for doc in vector_results + keyword_results:
        if doc.page_content not in seen:
            seen.add(doc.page_content)
            results.append(doc)
            if len(results) >= k:
                break
    
    return results


if __name__ == "__main__":
    documents = [
        Document(page_content="Python是一种编程语言"),
        Document(page_content="JavaScript用于前端开发"),
    ]
    
    if os.getenv("OPENAI_API_KEY"):
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(documents, embeddings)
        results = hybrid_search(vectorstore, "编程", k=2)
        print(f"混合检索找到 {len(results)} 个文档")

