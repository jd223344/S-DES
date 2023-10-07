import time
from Encryption import Encryption
# from Decryption import Decryption

# 实例化加解密函数
E = Encryption()
# D = Decryption()

def bf(known_plain_text, known_cipher_text):
    keynum = 0
    # 开始时间戳
    start_time = time.time()
    # 暴力破解密钥
    for key in range(1024):  # 10-bit密钥范围是0到1023
        binary_key = format(key, '010b')  # 格式化成10位二进制密钥
        # 使用当前密钥进行加密
        current_cipher_text = E.encryption(known_plain_text, binary_key)

        # 如果加密结果与已知的密文相匹配，则成功破解
        if current_cipher_text == known_cipher_text:
            # 计算破解所需的时间
            end_time = time.time()
            elapsed_time = end_time - start_time
            keynum = keynum + 1
            # 输出结果
            print(f"找到密钥{keynum}:{binary_key}  累计尝试次数: {key + 1}，累计破解时间: {elapsed_time} 秒")
            #break
    # 如果循环结束没有找到正确的密钥10
    else:
        if ( keynum == 0): print("本次未找到正确的密钥。")


print("请输入8-bit明文：", end="")
known_plain_text = input()  # 8-bit明文
print("请输入8-bit密文：", end="")
known_cipher_text = input()  # 8-bit密文

bf(known_plain_text, known_cipher_text)
