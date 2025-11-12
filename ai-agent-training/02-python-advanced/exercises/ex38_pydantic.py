"""
练习 38: Pydantic数据验证
难度: 🟡 进阶
预计时间: 20分钟

目标：使用Pydantic进行数据验证和序列化
"""

from pydantic import BaseModel, Field, validator
from typing import Optional


class User(BaseModel):
    """用户模型"""
    
    name: str = Field(..., min_length=1, max_length=50, description="姓名")
    age: int = Field(..., ge=0, le=150, description="年龄")
    email: Optional[str] = Field(None, regex=r'^[^@]+@[^@]+\.[^@]+$', description="邮箱")
    
    @validator('name')
    def name_must_not_be_empty(cls, v):
        """验证姓名不能为空"""
        if not v.strip():
            raise ValueError('姓名不能为空')
        return v.strip()
    
    class Config:
        """配置"""
        json_encoders = {
            # 自定义编码器
        }


class Product(BaseModel):
    """产品模型"""
    
    name: str
    price: float = Field(..., gt=0, description="价格必须大于0")
    stock: int = Field(..., ge=0, description="库存不能为负")
    
    @validator('price')
    def price_must_be_positive(cls, v):
        """验证价格"""
        if v <= 0:
            raise ValueError('价格必须大于0')
        return v


def create_user(data: dict) -> User:
    """
    创建用户（带验证）
    
    参数:
        data: 用户数据字典
    
    返回:
        User对象
    """
    # TODO: 使用User(**data)创建，会自动验证
    return User(**data)


def validate_product(data: dict) -> dict:
    """
    验证产品数据
    
    参数:
        data: 产品数据
    
    返回:
        {"valid": bool, "product": Product or None, "errors": list}
    """
    # TODO: 尝试创建Product，捕获验证错误
    try:
        product = Product(**data)
        return {"valid": True, "product": product, "errors": []}
    except Exception as e:
        return {"valid": False, "product": None, "errors": [str(e)]}


if __name__ == "__main__":
    # 测试用户创建
    user_data = {"name": "Alice", "age": 25, "email": "alice@example.com"}
    user = create_user(user_data)
    print(f"用户: {user.name}, 年龄: {user.age}")
    
    # 测试产品验证
    product_data = {"name": "商品", "price": 99.9, "stock": 10}
    result = validate_product(product_data)
    print(f"验证结果: {result['valid']}")

