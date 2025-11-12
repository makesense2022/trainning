"""
练习 05: Runnable接口
难度: 🟡 进阶
预计时间: 20分钟

目标：理解LangChain的Runnable接口（链式调用）
"""

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()


def create_runnable_chain():
    """
    创建Runnable链（使用|操作符）
    
    返回:
        Runnable链
    
    示例:
        prompt | llm | output_parser
    """
    # TODO: 创建prompt、llm、parser，然后用|连接
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    prompt = ChatPromptTemplate.from_template("用一句话解释：{topic}")
    llm = ChatOpenAI()
    output_parser = StrOutputParser()
    
    chain = prompt | llm | output_parser
    return chain


def invoke_chain(chain, topic: str) -> str:
    """
    调用链
    
    参数:
        chain: Runnable链
        topic: 主题
    
    返回:
        结果
    """
    # TODO: 使用chain.invoke()
    if chain is None:
        return "请设置API Key"
    
    return chain.invoke({"topic": topic})


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        chain = create_runnable_chain()
        if chain:
            result = invoke_chain(chain, "Python装饰器")
            print(result)

