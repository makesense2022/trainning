"""
练习 09: 简单RAG链
难度: 🟡 进阶
预计时间: 25分钟

目标：构建第一个完整的RAG系统
"""

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def build_rag_system(documents: list, query: str) -> str:
    """
    构建RAG系统并回答问题
    
    步骤：
    1. 切分文档
    2. 创建向量库
    3. 创建检索器
    4. 创建RAG链
    5. 回答问题
    
    参数:
        documents: 文档列表
        query: 问题
    
    返回:
        RAG生成的答案
    """
    # TODO: 实现完整RAG流程
    pass


if __name__ == "__main__":
    # 测试RAG系统
    # loader = TextLoader("test.txt")
    # docs = loader.load()
    # answer = build_rag_system(docs, "文档的主要内容是什么？")
    # print(answer)
    pass

