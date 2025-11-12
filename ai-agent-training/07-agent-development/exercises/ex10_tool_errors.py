"""
练习 10: 工具错误处理
难度: 🔴 挑战
预计时间: 25分钟

目标：处理工具调用中的错误
"""

from langchain.tools import tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


@tool
def risky_tool(value: int) -> str:
    """
    可能失败的工具
    
    参数:
        value: 值（如果<0会失败）
    
    返回:
        结果字符串
    """
    # TODO: 实现可能失败的工具
    if value < 0:
        raise ValueError("值不能为负")
    return f"处理成功: {value}"


def create_robust_agent(tools: list) -> AgentExecutor:
    """
    创建健壮的Agent（能处理工具错误）
    
    参数:
        tools: 工具列表
    
    返回:
        AgentExecutor实例
    """
    # TODO: 创建Agent，设置handle_parsing_errors
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    llm = ChatOpenAI()
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    
    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        handle_parsing_errors=True,  # 处理解析错误
        max_iterations=5
    )
    return executor


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        executor = create_robust_agent([risky_tool])
        if executor:
            # 测试正常情况
            result1 = executor.invoke({"input": "使用risky_tool处理5"})
            print(result1)
            
            # 测试错误情况
            result2 = executor.invoke({"input": "使用risky_tool处理-5"})
            print(result2)

