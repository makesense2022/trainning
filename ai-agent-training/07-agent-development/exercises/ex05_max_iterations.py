"""
练习 05: 迭代限制
难度: 🟡 进阶
预计时间: 15分钟

目标：限制Agent的迭代次数，防止无限循环
"""

from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain.tools import Tool
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def create_limited_agent(tools: list, max_iterations: int = 3) -> AgentExecutor:
    """
    创建带迭代限制的Agent
    
    参数:
        tools: 工具列表
        max_iterations: 最大迭代次数
    
    返回:
        AgentExecutor实例
    """
    # TODO: 创建Agent，设置max_iterations
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    llm = ChatOpenAI()
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    
    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        max_iterations=max_iterations,
        verbose=True
    )
    return executor


if __name__ == "__main__":
    @Tool
    def simple_tool(x: str) -> str:
        """简单工具"""
        return f"结果: {x}"
    
    if os.getenv("OPENAI_API_KEY"):
        executor = create_limited_agent([simple_tool], max_iterations=2)
        if executor:
            result = executor.invoke({"input": "测试"})
            print(result)

