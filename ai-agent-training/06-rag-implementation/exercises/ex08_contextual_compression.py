"""
练习 08: 上下文压缩
难度: 🔴 挑战
预计时间: 30分钟

目标：压缩检索到的文档，只保留相关部分
"""

from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv()


def create_compression_retriever(vectorstore: Chroma) -> ContextualCompressionRetriever:
    """
    创建上下文压缩检索器
    
    参数:
        vectorstore: 向量库
    
    返回:
        ContextualCompressionRetriever实例
    """
    # TODO: 创建压缩器和检索器
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    base_retriever = vectorstore.as_retriever()
    llm = ChatOpenAI()
    compressor = LLMChainExtractor.from_llm(llm)
    
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor,
        base_retriever=base_retriever
    )
    return compression_retriever


if __name__ == "__main__":
    documents = [
        Document(page_content="Python是一种编程语言。它由Guido van Rossum创建。Python支持多种编程范式。")
    ]
    
    if os.getenv("OPENAI_API_KEY"):
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(documents, embeddings)
        retriever = create_compression_retriever(vectorstore)
        if retriever:
            results = retriever.get_relevant_documents("Python的创建者")
            for doc in results:
                print(doc.page_content)

