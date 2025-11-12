"""
练习 19: Human-in-the-Loop
难度: 🔥 困难
预计时间: 45分钟

目标：实现人工审批机制
"""

from langgraph.graph import StateGraph, END
from langgraph.checkpoint import MemorySaver
from typing import TypedDict
import os
from dotenv import load_dotenv

load_dotenv()


class ApprovalState(TypedDict):
    """审批状态"""
    action: str
    approved: bool
    result: str


def create_approval_workflow():
    """
    创建需要人工审批的工作流
    
    返回:
        StateGraph实例
    """
    # TODO: 创建带中断的工作流
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    workflow = StateGraph(ApprovalState)
    
    def request_approval(state: ApprovalState):
        """请求审批"""
        print(f"需要审批的操作: {state['action']}")
        # 在实际应用中，这里会等待人工输入
        state["approved"] = True  # 模拟审批通过
        return state
    
    def execute_action(state: ApprovalState):
        """执行操作"""
        if state["approved"]:
            state["result"] = f"已执行: {state['action']}"
        else:
            state["result"] = "操作被拒绝"
        return state
    
    workflow.add_node("request_approval", request_approval)
    workflow.add_node("execute", execute_action)
    
    workflow.add_edge("request_approval", "execute")
    workflow.add_edge("execute", END)
    
    workflow.set_entry_point("request_approval")
    
    # 使用checkpointer支持中断
    checkpointer = MemorySaver()
    return workflow.compile(checkpointer=checkpointer)


if __name__ == "__main__":
    workflow = create_approval_workflow()
    if workflow:
        result = workflow.invoke({"action": "删除文件", "approved": False, "result": ""})
        print(result)

