"""
练习 01: ReAct原理
难度: 🟢 基础
预计时间: 15分钟

目标：理解ReAct（Reasoning + Acting）思维链
"""


def demonstrate_react_flow():
    """
    演示ReAct思维流程
    
    返回:
        ReAct思维步骤的示例
    """
    # TODO: 演示ReAct的思考-行动-观察循环
    steps = [
        {
            "thought": "用户问天气，我需要调用天气工具",
            "action": "get_weather(city='北京')",
            "observation": "北京今天晴天，25°C"
        },
        {
            "thought": "已经获得天气信息，可以回答用户了",
            "action": "final_answer",
            "observation": "北京今天晴天，25°C，适合外出"
        }
    ]
    return steps


def explain_react():
    """
    解释ReAct的核心概念
    
    返回:
        解释文本
    """
    explanation = """
    ReAct = Reasoning (推理) + Acting (行动)
    
    思维流程：
    1. Thought: LLM思考需要做什么
    2. Action: 选择并执行工具
    3. Observation: 观察工具返回的结果
    4. 重复直到可以回答
    
    优势：
    - 可以自主选择工具
    - 可以多步推理
    - 可以处理复杂任务
    """
    return explanation.strip()


if __name__ == "__main__":
    print(explain_react())
    print("\n示例流程:")
    for i, step in enumerate(demonstrate_react_flow(), 1):
        print(f"\n步骤 {i}:")
        print(f"  思考: {step['thought']}")
        print(f"  行动: {step['action']}")
        print(f"  观察: {step['observation']}")

