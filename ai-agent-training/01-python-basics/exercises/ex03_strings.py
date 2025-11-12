"""
练习 03: 字符串操作和格式化
难度: 🟢 基础
预计时间: 10分钟

对比学习：
JS:  const name = "Alice"; const msg = `Hello ${name}`;
Python: name = "Alice"; msg = f"Hello {name}"

关键特性：
1. Python的f-string（类似JS的模板字符串）
2. 字符串是不可变的（immutable）
3. 支持多行字符串（三引号）
"""


def format_greeting(name: str) -> str:
    """
    使用f-string格式化问候语
    
    JS: `Hello, ${name}!`
    Python: f"Hello, {name}!"
    
    参数:
        name: 姓名
    
    返回:
        格式化后的问候语
    
    示例:
        format_greeting("Alice") -> "Hello, Alice!"
    """
    # TODO: 使用f-string实现
    pass


def string_concatenate(str1: str, str2: str) -> str:
    """
    字符串拼接
    
    JS: str1 + str2
    Python: str1 + str2 (相同)
    
    参数:
        str1: 第一个字符串
        str2: 第二个字符串
    
    返回:
        拼接后的字符串
    """
    return str1 + str2


def string_methods(text: str) -> dict:
    """
    演示常用字符串方法
    
    返回包含以下信息的字典:
    {
        "upper": 转大写,
        "lower": 转小写,
        "strip": 去除首尾空格,
        "replace": 替换"Python"为"JavaScript",
        "split": 按空格分割成列表,
        "len": 字符串长度
    }
    
    示例:
        string_methods("  Hello Python World  ")
        -> {
            "upper": "  HELLO PYTHON WORLD  ",
            "lower": "  hello python world  ",
            "strip": "Hello Python World",
            "replace": "  Hello JavaScript World  ",
            "split": ["Hello", "Python", "World"],
            "len": 22
        }
    """
    return {
        "upper": text.upper(),
        "lower": text.lower(),
        "strip": text.strip(),
        "replace": text.replace("Python", "JavaScript"),
        "split": text.split(),
        "len": len(text)
    }


def multi_line_string() -> str:
    """
    创建多行字符串
    
    JS: 使用反引号
    Python: 使用三引号 '''...'''
    
    返回:
        包含以下内容的多行字符串:
        Line 1
        Line 2
        Line 3
    """
    return """Line 1
Line 2
Line 3"""


if __name__ == "__main__":
    print(format_greeting("Alice"))
    print(string_concatenate("Hello", "World"))
    print(string_methods("  Hello Python World  "))

