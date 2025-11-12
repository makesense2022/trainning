"""
练习 11: RAG作为工具
难度: 🔴 挑战
预计时间: 30分钟

目标：将RAG系统封装成Agent可以使用的工具
"""

from langchain.tools import tool
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv()


class RAGTool:
    """RAG工具类"""
    
    def __init__(self, documents: list):
        """
        初始化RAG工具
        
        参数:
            documents: 文档列表
        """
        # TODO: 创建向量库和QA链
        if os.getenv("OPENAI_API_KEY"):
            embeddings = OpenAIEmbeddings()
            vectorstore = Chroma.from_documents(documents, embeddings)
            retriever = vectorstore.as_retriever()
            llm = ChatOpenAI()
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=retriever
            )
        else:
            self.qa_chain = None
    
    def search(self, query: str) -> str:
        """
        搜索知识库
        
        参数:
            query: 查询文本
        
        返回:
            答案
        """
        # TODO: 使用QA链回答问题
        if not self.qa_chain:
            return "请设置API Key"
        return self.qa_chain.run(query)


def create_rag_tool(documents: list) -> tool:
    """
    创建RAG工具（LangChain Tool格式）
    
    参数:
        documents: 文档列表
    
    返回:
        Tool对象
    """
    # TODO: 创建RAG工具实例并包装成Tool
    rag = RAGTool(documents)
    
    @tool
    def search_knowledge_base(query: str) -> str:
        """
        在知识库中搜索相关信息
        
        参数:
            query: 搜索查询
        
        返回:
            相关信息和答案
        """
        return rag.search(query)
    
    return search_knowledge_base


if __name__ == "__main__":
    documents = [
        Document(page_content="Python是一种编程语言"),
        Document(page_content="JavaScript用于前端开发"),
    ]
    
    tool = create_rag_tool(documents)
    print(f"工具名称: {tool.name}")
    print(f"工具描述: {tool.description}")

