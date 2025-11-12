"""
练习 24: __init__.py
难度: 🟡 进阶
预计时间: 15分钟

目标：理解__init__.py的作用
"""

# __init__.py的作用：
# 1. 标识目录为Python包
# 2. 控制包的导入行为
# 3. 可以初始化包


def create_init_file_content() -> str:
    """
    生成__init__.py文件内容示例
    
    返回:
        __init__.py内容
    """
    # TODO: 返回示例内容
    return '''
"""
包的初始化文件
"""

# 导入包的主要功能
from .module1 import function1
from .module2 import function2

# 定义__all__控制from package import *
__all__ = ["function1", "function2"]

# 包级别的变量
VERSION = "1.0.0"
'''


if __name__ == "__main__":
    print(create_init_file_content())

