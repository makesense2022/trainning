"""
练习 15: 结构化输出
难度: 🔴 挑战
预计时间: 30分钟

目标：让Agent返回结构化数据
"""

from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain.tools import Tool
from langchain.chat_models import ChatOpenAI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()


class AgentResponse(BaseModel):
    """Agent响应模型"""
    answer: str
    confidence: float
    sources: list


def create_structured_agent(tools: list) -> AgentExecutor:
    """
    创建返回结构化输出的Agent
    
    参数:
        tools: 工具列表
    
    返回:
        AgentExecutor实例
    """
    # TODO: 创建Agent并配置输出解析
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    llm = ChatOpenAI()
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    
    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True
    )
    return executor


def parse_agent_output(output: str) -> AgentResponse:
    """
    解析Agent输出为结构化数据
    
    参数:
        output: Agent的文本输出
    
    返回:
        AgentResponse对象
    """
    # TODO: 解析输出（简化实现）
    return AgentResponse(
        answer=output,
        confidence=0.8,
        sources=[]
    )


if __name__ == "__main__":
    @Tool
    def search(query: str) -> str:
        """搜索工具"""
        return f"搜索结果：{query}"
    
    if os.getenv("OPENAI_API_KEY"):
        executor = create_structured_agent([search])
        if executor:
            result = executor.invoke({"input": "搜索Python"})
            structured = parse_agent_output(result["output"])
            print(structured)

