"""
练习 21: import机制
难度: 🟢 基础
预计时间: 10分钟

目标：理解Python的import机制
"""


def demonstrate_import():
    """
    演示不同的import方式
    
    返回:
        说明字典
    """
    # TODO: 演示各种import方式
    return {
        "import_module": "import math",
        "from_import": "from math import sqrt",
        "import_as": "import numpy as np",
        "from_import_as": "from datetime import datetime as dt"
    }


def check_module_loaded(module_name: str) -> bool:
    """
    检查模块是否已加载
    
    参数:
        module_name: 模块名
    
    返回:
        是否已加载
    """
    # TODO: 使用sys.modules检查
    import sys
    return module_name in sys.modules


if __name__ == "__main__":
    print(demonstrate_import())
    print(check_module_loaded("math"))

