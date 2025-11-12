"""
练习 08: 元数据过滤
难度: 🟡 进阶
预计时间: 20分钟

目标：在向量搜索中使用元数据过滤
"""

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv()


def create_vectorstore_with_metadata() -> Chroma:
    """
    创建带元数据的向量库
    
    返回:
        Chroma向量库
    """
    # TODO: 创建带metadata的文档
    documents = [
        Document(
            page_content="Python是一种编程语言",
            metadata={"category": "programming", "year": 2024}
        ),
        Document(
            page_content="JavaScript用于前端",
            metadata={"category": "frontend", "year": 2024}
        ),
    ]
    
    if os.getenv("OPENAI_API_KEY"):
        embeddings = OpenAIEmbeddings()
        return Chroma.from_documents(documents, embeddings)
    else:
        from langchain.embeddings.fake import FakeEmbeddings
        embeddings = FakeEmbeddings(size=1536)
        return Chroma.from_documents(documents, embeddings)


def search_with_filter(vectorstore: Chroma, query: str, filter_dict: dict) -> list:
    """
    带过滤的搜索
    
    参数:
        vectorstore: 向量库
        query: 查询
        filter_dict: 过滤条件
    
    返回:
        文档列表
    """
    # TODO: 使用where参数过滤
    return vectorstore.similarity_search(
        query,
        k=3,
        filter=filter_dict
    )


if __name__ == "__main__":
    vectorstore = create_vectorstore_with_metadata()
    results = search_with_filter(vectorstore, "编程", {"category": "programming"})
    print(f"找到 {len(results)} 个文档")

