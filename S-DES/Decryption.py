from Key import Key
from Function import Function
# 实例化函数和密钥扩展函数
from Key import Key
from Function import Function


class Decryption:
    def decryption(self, cipher_text, key):
        # 实例化函数和密钥扩展函数
        func = Function()
        key_func = Key()

        # 扩展密钥
        k1, k2 = key_func.key_expansion(key)

        func = Function()
        key_func = Key()

        # 扩展密钥
        k1, k2 = key_func.key_expansion(key)

        # 解密过程
        cipher_text = func.IP(cipher_text)
        cipher_left = cipher_text[:4]
        cipher_right = cipher_text[4:]
        middle2 = func.FFunction(cipher_right, k2)
        middle2_left = "".join(str(int(x) ^ int(y)) for x, y in zip(cipher_left, middle2))
        new_left, new_right = func.swap(middle2_left, cipher_right)
        middle1 = func.FFunction(new_right, k1)
        middle1_left = "".join(str(int(x) ^ int(y)) for x, y in zip(new_left, middle1))
        plain_text = func.PI(middle1_left + new_right)
        return plain_text