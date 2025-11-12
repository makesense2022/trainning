"""
练习 39: 日志系统
难度: 🟡 进阶
预计时间: 20分钟

目标：使用logging模块记录日志
"""

import logging
from logging import Logger


def setup_logger(name: str, level: int = logging.INFO) -> Logger:
    """
    设置日志记录器
    
    参数:
        name: 记录器名称
        level: 日志级别
    
    返回:
        Logger实例
    """
    # TODO: 配置logging
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # 创建控制台处理器
    handler = logging.StreamHandler()
    handler.setLevel(level)
    
    # 创建格式器
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger


def log_different_levels(logger: Logger):
    """
    记录不同级别的日志
    
    参数:
        logger: Logger实例
    """
    # TODO: 使用不同级别记录
    logger.debug("调试信息")
    logger.info("一般信息")
    logger.warning("警告信息")
    logger.error("错误信息")
    logger.critical("严重错误")


if __name__ == "__main__":
    logger = setup_logger("my_app")
    log_different_levels(logger)

