"""
练习 29: 循环导入
难度: 🔴 挑战
预计时间: 25分钟

目标：理解和解决循环导入问题
"""

# 循环导入示例：
# module_a.py: from module_b import func_b
# module_b.py: from module_a import func_a


def avoid_circular_import() -> dict:
    """
    避免循环导入的方法
    
    返回:
        解决方案说明
    """
    return {
        "problem": "模块A导入模块B，模块B导入模块A",
        "solutions": [
            "1. 重构代码，提取公共部分到第三个模块",
            "2. 使用延迟导入（在函数内部导入）",
            "3. 使用类型提示（from __future__ import annotations）",
            "4. 重新设计模块依赖关系"
        ]
    }


if __name__ == "__main__":
    print(avoid_circular_import())

