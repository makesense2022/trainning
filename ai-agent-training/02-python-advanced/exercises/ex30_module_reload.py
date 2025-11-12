"""
练习 30: 模块重载
难度: 🟡 进阶
预计时间: 15分钟

目标：重新加载已导入的模块
"""

import importlib


def reload_module_example(module_name: str):
    """
    重新加载模块示例
    
    参数:
        module_name: 模块名
    
    返回:
        是否成功
    """
    # TODO: 使用importlib.reload
    try:
        module = __import__(module_name)
        importlib.reload(module)
        return True
    except Exception as e:
        print(f"重载失败: {e}")
        return False


if __name__ == "__main__":
    # 注意：在实际开发中，修改模块后可以重载
    result = reload_module_example("math")
    print(f"重载成功: {result}")

