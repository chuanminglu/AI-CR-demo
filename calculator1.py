# ❌ 错误1：硬编码的密钥 (安全隐患)
API_KEY = "sk-1234567890abcdef1234567890abcdef"

def division(a, b):
    # ❌ 错误2：没有检查分母为0 (逻辑漏洞)
    # ❌ 错误3：打印调试信息而不是使用日志 (规范问题)
    print(f"Doing math: {a} / {b}")
    return a / b

# 测试调用
result = division(10, 0)
print(result)
