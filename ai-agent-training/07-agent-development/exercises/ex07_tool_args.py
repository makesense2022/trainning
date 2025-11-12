"""
练习 07: 工具参数
难度: 🟡 进阶
预计时间: 25分钟

目标：创建带复杂参数的工具
"""

from langchain.tools import Tool
from pydantic import BaseModel, Field


class WeatherInput(BaseModel):
    """天气查询输入"""
    city: str = Field(description="城市名称")
    unit: str = Field(default="celsius", description="温度单位：celsius或fahrenheit")


def create_weather_tool() -> Tool:
    """
    创建天气工具（带Pydantic参数验证）
    
    返回:
        Tool对象
    """
    # TODO: 使用StructuredTool创建带参数验证的工具
    from langchain.tools import StructuredTool
    
    def get_weather(city: str, unit: str = "celsius") -> str:
        """获取城市天气"""
        # 模拟天气API
        return f"{city}今天25°C，晴天"
    
    return StructuredTool.from_function(
        func=get_weather,
        name="get_weather",
        description="获取城市天气信息",
        args_schema=WeatherInput
    )


if __name__ == "__main__":
    tool = create_weather_tool()
    print(f"工具名称: {tool.name}")
    print(f"工具描述: {tool.description}")

