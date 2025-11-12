"""
练习 04: Agent vs Chain对比
难度: 🟡 进阶
预计时间: 20分钟

目标：理解Agent和Chain的区别
"""

from langchain.chains import LLMChain
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain import hub
from langchain.tools import Tool
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def demonstrate_chain():
    """
    演示Chain（固定流程）
    
    返回:
        Chain示例
    """
    # TODO: 创建固定流程的Chain
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    llm = ChatOpenAI()
    prompt = PromptTemplate(
        input_variables=["query"],
        template="回答：{query}"
    )
    return LLMChain(llm=llm, prompt=prompt)


def demonstrate_agent(tools: list):
    """
    演示Agent（动态决策）
    
    参数:
        tools: 工具列表
    
    返回:
        Agent示例
    """
    # TODO: 创建Agent
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    llm = ChatOpenAI()
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools)


def compare_chain_vs_agent(query: str) -> dict:
    """
    对比Chain和Agent
    
    参数:
        query: 查询
    
    返回:
        对比结果
    """
    # TODO: 对比两种方式
    return {
        "chain": "固定流程，无法选择工具",
        "agent": "动态决策，可以选择工具"
    }


if __name__ == "__main__":
    print(compare_chain_vs_agent("测试"))

