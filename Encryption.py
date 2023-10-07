from Key import Key
from Function import Function
# 实例化函数和密钥扩展函数
class Encryption:
    def encryption(self, plain_text, key):
        func = Function()
        key_func = Key()
        # 扩展密钥
        k1, k2 = key_func.key_expansion(key)
        # 加密过程
        plain_text = func.IP(plain_text)
        plain_left = plain_text[:4]
        plain_right = plain_text[4:]
        middle1 = func.FFunction(plain_right, k1)
        middle1_left = "".join(str(int(x) ^ int(y)) for x, y in zip(plain_left, middle1))
        new_left, new_right = func.swap(middle1_left, plain_right)
        middle2 = func.FFunction(new_right, k2)
        middle2_left = "".join(str(int(x) ^ int(y)) for x, y in zip(new_left, middle2))
        cipher_text = func.PI(middle2_left + new_right)
        return cipher_text
