"""
练习 13: 对话式Agent
难度: 🔴 挑战
预计时间: 30分钟

目标：创建支持多轮对话的Agent
"""

from langchain.agents import create_react_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain import hub
from langchain.tools import Tool
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def create_conversational_agent(tools: list) -> AgentExecutor:
    """
    创建对话式Agent（带记忆）
    
    参数:
        tools: 工具列表
    
    返回:
        AgentExecutor实例
    """
    # TODO: 创建Memory和Agent
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    prompt = hub.pull("hwchase17/react")
    
    agent = create_react_agent(llm, tools, prompt)
    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True
    )
    return executor


if __name__ == "__main__":
    @Tool
    def calculator(expression: str) -> str:
        """计算数学表达式"""
        try:
            return str(eval(expression))
        except:
            return "计算错误"
    
    if os.getenv("OPENAI_API_KEY"):
        executor = create_conversational_agent([calculator])
        if executor:
            executor.invoke({"input": "计算 5 + 3"})
            executor.invoke({"input": "刚才的结果乘以2"})  # 应该能记住上下文

