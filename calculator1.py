# ❌ 错误1：硬编码的密钥 (安全隐患)
# ✅ 修复：从环境变量中读取 API 密钥，而不是在代码中硬编码
API_KEY = os.getenv("API_KEY")

def division(a, b):
    """Return the result of dividing a by b.

    Args:
        a: The dividend (numerical value to be divided).
        b: The divisor (numerical value by which to divide).

    Returns:
        The quotient resulting from a divided by b.
    """
    # ❌ 错误2：没有检查分母为0 (逻辑漏洞)
    # ❌ 错误3：打印调试信息而不是使用日志 (规范问题)
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    print(f"Doing math: {a} / {b}")
    return a / b

# 测试调用
result = division(10, 0)
print(result)
