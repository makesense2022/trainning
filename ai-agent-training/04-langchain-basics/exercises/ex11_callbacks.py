"""
练习 11: 回调系统
难度: 🟡 进阶
预计时间: 20分钟

目标：使用LangChain的回调系统追踪执行
"""

from langchain.callbacks import StdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def create_chain_with_callback():
    """
    创建带回调的链
    
    返回:
        LLMChain实例
    """
    # TODO: 创建回调处理器和链
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    callback = StdOutCallbackHandler()
    llm = ChatOpenAI(callbacks=[callback])
    
    prompt = PromptTemplate(
        input_variables=["topic"],
        template="解释：{topic}"
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        chain = create_chain_with_callback()
        if chain:
            chain.run("Python装饰器")

