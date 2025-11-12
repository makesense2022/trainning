"""
练习 12: 工具组合
难度: 🔴 挑战
预计时间: 35分钟

目标：创建可以组合使用的工具
"""

from langchain.tools import tool


@tool
def get_user_location(user_id: str) -> str:
    """
    获取用户位置
    
    参数:
        user_id: 用户ID
    
    返回:
        城市名称
    """
    # TODO: 模拟获取位置
    locations = {"user1": "北京", "user2": "上海"}
    return locations.get(user_id, "未知")


@tool
def get_weather_for_city(city: str) -> str:
    """
    获取城市天气
    
    参数:
        city: 城市名称
    
    返回:
        天气信息
    """
    # TODO: 模拟获取天气
    return f"{city}今天晴天，25°C"


def create_composable_tools() -> list:
    """
    创建可组合的工具列表
    
    返回:
        工具列表
    """
    # TODO: 返回工具列表
    # Agent可以组合使用这些工具：
    # 1. 先调用get_user_location获取位置
    # 2. 再调用get_weather_for_city获取该位置的天气
    return [get_user_location, get_weather_for_city]


if __name__ == "__main__":
    tools = create_composable_tools()
    print(f"创建了 {len(tools)} 个可组合工具")

