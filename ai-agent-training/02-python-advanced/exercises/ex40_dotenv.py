"""
练习 40: 环境变量管理
难度: 🟢 基础
预计时间: 10分钟

目标：使用python-dotenv管理环境变量
"""

from dotenv import load_dotenv
import os


def load_environment():
    """
    加载.env文件
    
    返回:
        是否成功加载
    """
    # TODO: 使用load_dotenv()
    return load_dotenv()


def get_env_var(key: str, default: str = None) -> str:
    """
    获取环境变量
    
    参数:
        key: 变量名
        default: 默认值
    
    返回:
        变量值
    """
    # TODO: 使用os.getenv()
    return os.getenv(key, default)


def check_required_env_vars(required: list) -> dict:
    """
    检查必需的环境变量
    
    参数:
        required: 必需的变量名列表
    
    返回:
        {
            "missing": 缺失的变量列表,
            "present": 存在的变量列表
        }
    """
    # TODO: 检查每个变量
    missing = []
    present = []
    
    for var in required:
        if os.getenv(var):
            present.append(var)
        else:
            missing.append(var)
    
    return {"missing": missing, "present": present}


if __name__ == "__main__":
    load_environment()
    api_key = get_env_var("OPENAI_API_KEY")
    print(f"API Key已设置: {api_key is not None}")
    
    result = check_required_env_vars(["OPENAI_API_KEY", "DEEPSEEK_API_KEY"])
    print(result)

