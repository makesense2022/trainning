"""
练习 08: 工具描述优化
难度: 🔴 挑战
预计时间: 30分钟

目标：编写清晰有效的工具描述，让Agent正确选择工具
"""

from langchain.tools import tool


@tool
def search_knowledge_base(query: str) -> str:
    """
    在公司知识库中搜索相关文档
    
    适用场景：
    - 查询公司政策、流程、规范
    - 查找技术文档、API文档
    - 历史项目信息和经验
    
    不适用场景：
    - 实时信息（如当前时间、天气）
    - 需要计算的数学问题
    
    参数:
        query: 搜索关键词，如"报销流程"、"Python编码规范"
    
    返回:
        相关文档摘要，JSON格式
    
    示例:
        search_knowledge_base("报销流程")
        -> {"docs": [...], "total": 3}
    """
    # TODO: 实现知识库搜索（模拟）
    return f"找到关于'{query}'的3篇文档"


@tool
def get_weather(city: str) -> str:
    """
    获取城市的实时天气信息
    
    适用场景：
    - 查询当前天气
    - 查询天气预报
    
    参数:
        city: 城市名称，如"北京"、"上海"
    
    返回:
        天气描述字符串
    
    示例:
        get_weather("北京")
        -> "北京今天晴天，25°C，湿度60%"
    """
    # TODO: 实现天气查询（模拟）
    return f"{city}今天晴天，25°C"


def create_tool_list() -> list:
    """
    创建工具列表
    
    返回:
        工具列表
    """
    # TODO: 返回所有工具
    return [search_knowledge_base, get_weather]


if __name__ == "__main__":
    tools = create_tool_list()
    for tool in tools:
        print(f"{tool.name}: {tool.description[:50]}...")

