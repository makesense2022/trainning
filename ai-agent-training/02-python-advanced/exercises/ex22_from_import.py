"""
练习 22: from...import
难度: 🟢 基础
预计时间: 10分钟

目标：掌握from...import的用法
"""

from math import sqrt, pi
from datetime import datetime, timedelta


def use_imported_functions():
    """
    使用导入的函数
    
    返回:
        计算结果
    """
    # TODO: 使用导入的函数
    result = sqrt(16)  # 4.0
    return {
        "sqrt_16": result,
        "pi_value": pi
    }


def import_specific_class():
    """
    导入特定类
    
    返回:
        类实例
    """
    # TODO: 使用导入的类
    now = datetime.now()
    return now


if __name__ == "__main__":
    print(use_imported_functions())
    print(import_specific_class())

