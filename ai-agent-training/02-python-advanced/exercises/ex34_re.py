"""
练习 34: 正则表达式
难度: 🟡 进阶
预计时间: 20分钟

目标：使用re模块进行文本匹配和提取
"""

import re


def find_pattern(text: str, pattern: str) -> list:
    """
    查找所有匹配
    
    参数:
        text: 文本
        pattern: 正则表达式模式
    
    返回:
        匹配列表
    """
    # TODO: 使用re.findall()
    return re.findall(pattern, text)


def extract_emails(text: str) -> list:
    """
    提取邮箱地址
    
    参数:
        text: 文本
    
    返回:
        邮箱列表
    """
    # TODO: 使用正则表达式匹配邮箱
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return find_pattern(text, pattern)


def validate_phone(phone: str) -> bool:
    """
    验证手机号（中国手机号格式）
    
    参数:
        phone: 手机号
    
    返回:
        是否有效
    """
    # TODO: 使用正则表达式验证（11位数字，1开头）
    pattern = r'^1[3-9]\d{9}$'
    return bool(re.match(pattern, phone))


def replace_pattern(text: str, pattern: str, replacement: str) -> str:
    """
    替换匹配的文本
    
    参数:
        text: 文本
        pattern: 正则表达式
        replacement: 替换文本
    
    返回:
        替换后的文本
    """
    # TODO: 使用re.sub()
    return re.sub(pattern, replacement, text)


if __name__ == "__main__":
    text = "联系我：alice@example.com 或 bob@test.com"
    emails = extract_emails(text)
    print(f"找到邮箱: {emails}")
    
    print(validate_phone("13812345678"))  # True
    print(validate_phone("12345678901"))   # False
    
    result = replace_pattern("Hello World", r"World", "Python")
    print(result)

