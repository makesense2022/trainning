"""
练习 04: 链构建
难度: 🟡 进阶
预计时间: 20分钟

目标：掌握LangChain的Chain概念
"""

from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def create_simple_chain(llm: ChatOpenAI) -> LLMChain:
    """
    创建简单的LLM链
    
    参数:
        llm: Chat Model
    
    返回:
        LLMChain实例
    """
    # TODO: 创建Prompt和Chain
    prompt = PromptTemplate(
        input_variables=["topic"],
        template="用一句话解释：{topic}"
    )
    return LLMChain(llm=llm, prompt=prompt)


def create_sequential_chain(llm: ChatOpenAI) -> SimpleSequentialChain:
    """
    创建顺序链（多个步骤）
    
    参数:
        llm: Chat Model
    
    返回:
        SimpleSequentialChain实例
    
    示例：
        步骤1：生成主题
        步骤2：基于主题写摘要
    """
    # TODO: 创建多个链并组合
    chain1 = LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            input_variables=[],
            template="生成一个技术主题"
        )
    )
    
    chain2 = LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            input_variables=["topic"],
            template="为以下主题写摘要：{topic}"
        )
    )
    
    return SimpleSequentialChain(chains=[chain1, chain2])


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        llm = ChatOpenAI()
        chain = create_simple_chain(llm)
        result = chain.run("Python装饰器")
        print(result)

