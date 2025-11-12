"""
练习 06: 定义简单工具
难度: 🟡 进阶
预计时间: 20分钟

目标：创建Agent可以使用的工具
"""

from langchain.tools import tool


@tool
def calculator(expression: str) -> str:
    """
    计算器工具：计算数学表达式
    
    参数:
        expression: 数学表达式，如 "2 + 3 * 4"
    
    返回:
        计算结果字符串
    
    注意：实际应用中应该使用安全的eval或ast.literal_eval
    """
    # TODO: 实现计算器（注意安全性）
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"错误: {e}"


@tool
def get_current_time() -> str:
    """
    获取当前时间
    
    返回:
        当前时间的字符串表示
    """
    # TODO: 使用datetime获取当前时间
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_tool_list() -> list:
    """
    创建工具列表
    
    返回:
        包含所有工具的列表
    """
    # TODO: 返回工具列表
    pass


if __name__ == "__main__":
    tools = create_tool_list()
    print(f"创建了 {len(tools)} 个工具")
    for tool in tools:
        print(f"- {tool.name}: {tool.description}")

