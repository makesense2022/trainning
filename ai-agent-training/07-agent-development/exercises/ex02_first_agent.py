"""
练习 02: 第一个Agent
难度: 🟡 进阶
预计时间: 20分钟

目标：创建第一个能使用工具的AI Agent
"""

from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain.tools import Tool
from langchain.chat_models import ChatOpenAI


def create_simple_tool() -> Tool:
    """
    创建一个简单的计算器工具
    
    返回:
        Tool对象
    """
    # TODO: 使用 @tool 装饰器或 Tool 类创建工具
    pass


def create_agent(tools: list) -> AgentExecutor:
    """
    创建ReAct Agent
    
    参数:
        tools: 工具列表
    
    返回:
        AgentExecutor实例
    """
    # TODO: 使用 create_react_agent 创建agent
    pass


def run_agent(agent: AgentExecutor, query: str) -> str:
    """
    运行Agent
    
    参数:
        agent: AgentExecutor
        query: 用户问题
    
    返回:
        Agent的回答
    """
    # TODO: 调用agent.invoke()
    pass


if __name__ == "__main__":
    # 测试Agent
    # tool = create_simple_tool()
    # agent = create_agent([tool])
    # result = run_agent(agent, "计算 5 + 3")
    # print(result)
    pass

