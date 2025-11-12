"""
练习 28: 动态导入
难度: 🔴 挑战
预计时间: 25分钟

目标：使用importlib动态导入模块
"""

import importlib
import sys


def dynamic_import(module_name: str):
    """
    动态导入模块
    
    参数:
        module_name: 模块名（如"math"）
    
    返回:
        模块对象
    """
    # TODO: 使用importlib.import_module
    return importlib.import_module(module_name)


def reload_module(module_name: str):
    """
    重新加载模块
    
    参数:
        module_name: 模块名
    
    返回:
        重新加载的模块
    """
    # TODO: 使用importlib.reload
    if module_name in sys.modules:
        return importlib.reload(sys.modules[module_name])
    return importlib.import_module(module_name)


if __name__ == "__main__":
    # 动态导入math模块
    math = dynamic_import("math")
    print(f"sqrt(16) = {math.sqrt(16)}")

