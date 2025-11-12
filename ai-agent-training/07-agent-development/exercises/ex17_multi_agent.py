"""
练习 17: 多Agent协作
难度: 🔥 困难
预计时间: 60分钟

目标：实现多个Agent协作完成任务
"""

from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain.tools import Tool
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


class PlannerAgent:
    """规划Agent（负责制定计划）"""
    
    def __init__(self, tools: list):
        if not os.getenv("OPENAI_API_KEY"):
            self.executor = None
            return
        
        llm = ChatOpenAI()
        prompt = hub.pull("hwchase17/react")
        agent = create_react_agent(llm, tools, prompt)
        self.executor = AgentExecutor(agent=agent, tools=tools)
    
    def plan(self, task: str) -> str:
        """制定计划"""
        if self.executor is None:
            return "请设置API Key"
        result = self.executor.invoke({"input": f"为以下任务制定计划：{task}"})
        return result["output"]


class ExecutorAgent:
    """执行Agent（负责执行任务）"""
    
    def __init__(self, tools: list):
        if not os.getenv("OPENAI_API_KEY"):
            self.executor = None
            return
        
        llm = ChatOpenAI()
        prompt = hub.pull("hwchase17/react")
        agent = create_react_agent(llm, tools, prompt)
        self.executor = AgentExecutor(agent=agent, tools=tools)
    
    def execute(self, plan: str) -> str:
        """执行计划"""
        if self.executor is None:
            return "请设置API Key"
        result = self.executor.invoke({"input": f"执行以下计划：{plan}"})
        return result["output"]


def multi_agent_collaboration(task: str) -> dict:
    """
    多Agent协作
    
    参数:
        task: 任务描述
    
    返回:
        协作结果
    """
    # TODO: 创建多个Agent并协作
    @Tool
    def search_tool(query: str) -> str:
        """搜索工具"""
        return f"搜索结果：{query}"
    
    tools = [search_tool]
    
    planner = PlannerAgent(tools)
    executor = ExecutorAgent(tools)
    
    plan = planner.plan(task)
    result = executor.execute(plan)
    
    return {
        "plan": plan,
        "result": result
    }


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        result = multi_agent_collaboration("研究Python的最佳实践")
        print(result)

