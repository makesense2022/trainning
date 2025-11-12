"""
练习 20: Agent评测
难度: 🔴 挑战
预计时间: 40分钟

目标：评测Agent的性能和质量
"""

from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain.tools import Tool
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def evaluate_agent(executor: AgentExecutor, test_cases: list) -> dict:
    """
    评测Agent
    
    参数:
        executor: AgentExecutor
        test_cases: 测试用例 [{"input": "...", "expected_tool": "...", "expected_output": "..."}]
    
    返回:
        评测结果
    """
    # TODO: 运行测试用例并计算指标
    results = []
    for case in test_cases:
        try:
            result = executor.invoke({"input": case["input"]})
            tool_used = extract_tool_from_result(result)
            
            results.append({
                "input": case["input"],
                "output": result["output"],
                "tool_used": tool_used,
                "expected_tool": case.get("expected_tool"),
                "tool_correct": tool_used == case.get("expected_tool"),
                "output_match": case.get("expected_output", "").lower() in result["output"].lower()
            })
        except Exception as e:
            results.append({
                "input": case["input"],
                "error": str(e),
                "success": False
            })
    
    success_rate = sum(1 for r in results if r.get("success", True) and r.get("tool_correct", False)) / len(results) if results else 0
    
    return {
        "success_rate": success_rate,
        "total": len(results),
        "details": results
    }


def extract_tool_from_result(result: dict) -> str:
    """从结果中提取使用的工具"""
    # TODO: 从intermediate_steps提取工具名
    if "intermediate_steps" in result:
        steps = result["intermediate_steps"]
        if steps:
            return steps[0][0].tool if hasattr(steps[0][0], 'tool') else "unknown"
    return "unknown"


if __name__ == "__main__":
    @Tool
    def calculator(expr: str) -> str:
        """计算工具"""
        try:
            return str(eval(expr))
        except:
            return "错误"
    
    if os.getenv("OPENAI_API_KEY"):
        llm = ChatOpenAI()
        prompt = hub.pull("hwchase17/react")
        agent = create_react_agent(llm, [calculator], prompt)
        executor = AgentExecutor(agent=agent, tools=[calculator])
        
        test_cases = [
            {"input": "计算 5 + 3", "expected_tool": "calculator", "expected_output": "8"}
        ]
        
        evaluation = evaluate_agent(executor, test_cases)
        print(f"成功率: {evaluation['success_rate']:.2%}")

