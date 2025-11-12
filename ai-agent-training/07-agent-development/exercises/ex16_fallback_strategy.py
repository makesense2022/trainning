"""
练习 16: Agent兜底策略
难度: 🔴 挑战
预计时间: 30分钟

目标：实现Agent失败时的兜底方案
"""

from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain.tools import Tool
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def create_agent_with_fallback(tools: list) -> AgentExecutor:
    """
    创建带兜底策略的Agent
    
    参数:
        tools: 工具列表
    
    返回:
        AgentExecutor实例
    """
    # TODO: 创建Agent，设置max_iterations和early_stopping_method
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    llm = ChatOpenAI()
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    
    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        max_iterations=5,  # 限制迭代次数
        max_execution_time=60,  # 限制执行时间
        early_stopping_method="force",  # 强制停止
        handle_parsing_errors=True  # 处理解析错误
    )
    return executor


def safe_agent_invoke(executor: AgentExecutor, query: str) -> dict:
    """
    安全调用Agent（带兜底）
    
    参数:
        executor: AgentExecutor
        query: 查询
    
    返回:
        {
            "success": bool,
            "output": str,
            "error": str or None
        }
    """
    # TODO: 调用Agent并处理错误
    if executor is None:
        return {"success": False, "output": None, "error": "请设置API Key"}
    
    try:
        result = executor.invoke({"input": query})
        return {
            "success": True,
            "output": result["output"],
            "error": None
        }
    except Exception as e:
        # 兜底：返回默认响应
        return {
            "success": False,
            "output": "抱歉，我无法处理这个请求。",
            "error": str(e)
        }


if __name__ == "__main__":
    @Tool
    def simple_tool(x: str) -> str:
        """简单工具"""
        return f"处理了: {x}"
    
    if os.getenv("OPENAI_API_KEY"):
        executor = create_agent_with_fallback([simple_tool])
        if executor:
            result = safe_agent_invoke(executor, "测试")
            print(result)

