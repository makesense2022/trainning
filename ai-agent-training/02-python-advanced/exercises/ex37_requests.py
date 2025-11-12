"""
练习 37: HTTP请求（requests库）
难度: 🟡 进阶
预计时间: 20分钟

目标：使用requests库进行HTTP请求（类似axios）
"""

import requests
from typing import Dict, Any


def get_request(url: str) -> Dict[str, Any]:
    """
    GET请求
    
    参数:
        url: URL
    
    返回:
        响应信息字典
    """
    # TODO: 使用requests.get()
    response = requests.get(url)
    return {
        "status_code": response.status_code,
        "content": response.text[:100],  # 前100字符
        "headers": dict(response.headers)
    }


def post_request(url: str, data: Dict) -> Dict[str, Any]:
    """
    POST请求
    
    参数:
        url: URL
        data: 数据字典
    
    返回:
        响应信息
    """
    # TODO: 使用requests.post()
    response = requests.post(url, json=data)
    return {
        "status_code": response.status_code,
        "json": response.json() if response.headers.get("content-type") == "application/json" else None
    }


def request_with_headers(url: str, headers: Dict[str, str]) -> requests.Response:
    """
    带自定义headers的请求
    
    参数:
        url: URL
        headers: 请求头
    
    返回:
        Response对象
    """
    # TODO: 使用headers参数
    return requests.get(url, headers=headers)


def handle_errors(url: str) -> Dict[str, Any]:
    """
    处理HTTP错误
    
    参数:
        url: URL
    
    返回:
        结果字典（包含错误信息）
    """
    # TODO: 使用try/except处理requests异常
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # 如果状态码不是2xx，抛出异常
        return {"success": True, "data": response.text[:100]}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}


if __name__ == "__main__":
    # 测试GET请求
    result = get_request("https://httpbin.org/get")
    print(f"状态码: {result['status_code']}")
    
    # 测试错误处理
    error_result = handle_errors("https://httpbin.org/status/404")
    print(error_result)

