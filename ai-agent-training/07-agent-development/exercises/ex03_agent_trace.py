"""
练习 03: Agent执行追踪
难度: 🟡 进阶
预计时间: 15分钟

目标：追踪Agent的执行过程，理解思维链
"""

from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain.tools import Tool
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def create_traceable_agent(tools: list) -> AgentExecutor:
    """
    创建可追踪的Agent
    
    参数:
        tools: 工具列表
    
    返回:
        AgentExecutor（verbose=True）
    """
    # TODO: 创建Agent，设置verbose=True
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    llm = ChatOpenAI()
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    
    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,  # 启用详细输出
        return_intermediate_steps=True  # 返回中间步骤
    )
    return executor


def run_with_trace(executor: AgentExecutor, query: str) -> dict:
    """
    运行Agent并获取追踪信息
    
    参数:
        executor: AgentExecutor
        query: 查询
    
    返回:
        {
            "output": 最终输出,
            "intermediate_steps": 中间步骤
        }
    """
    # TODO: 调用executor并返回结果
    if executor is None:
        return {"output": "请设置API Key", "intermediate_steps": []}
    
    result = executor.invoke({"input": query})
    return {
        "output": result["output"],
        "intermediate_steps": result.get("intermediate_steps", [])
    }


if __name__ == "__main__":
    # 创建简单工具
    @Tool
    def calculator(expression: str) -> str:
        """计算数学表达式"""
        try:
            return str(eval(expression))
        except:
            return "计算错误"
    
    if os.getenv("OPENAI_API_KEY"):
        executor = create_traceable_agent([calculator])
        if executor:
            result = run_with_trace(executor, "计算 5 + 3 * 2")
            print(f"输出: {result['output']}")
            print(f"中间步骤数: {len(result['intermediate_steps'])}")

