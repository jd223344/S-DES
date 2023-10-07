import time
from Encryption import Encryption
import numpy as np
#from Decryption import Decryption

# 实例化加解密函数
E = Encryption()
#D = Decryption()

def bf(known_plain_text,known_cipher_text):
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
            # 输出结果
            print(f"成功破解密钥为 {binary_key}")
            print(f"尝试次数: {key + 1}")
            print(f"破解时间: {elapsed_time} 秒")
            break
        else:
            print(f"第 {key + 1}次：密钥为{binary_key}，密文为{current_cipher_text}，未匹配！")
    # 如果循环结束没有找到正确的密钥
    else:
        print("本次未找到正确的密钥。")

    return binary_key, key, elapsed_time


# 记录每一个明密文对和破解到的第一个密钥及相关信息
known_plain_text = []
known_cipher_text = []
binary_key = []
key = []
elapsed_time = []
print("请输入明密文对对数：", end="")
num = int(input())
for i in range(num):
    print(f"请输入第{i+1}对8-bit明文：", end="")
    i_plain_text = input()  # 8-bit明文
    known_plain_text.append(i_plain_text)
    print(f"请输入第{i+1}对8-bit密文：", end="")
    i_cipher_text = input()  # 8-bit密文
    known_cipher_text.append(i_cipher_text)

for i in range(num):
    print("\n")
    b_k, k, e_t = bf(known_plain_text[i], known_cipher_text[i])
    binary_key.append(b_k)
    key.append(k)
    elapsed_time.append(e_t)

print("\n")
du
for i in range(num):
    print(f"第{i+1}对明密文对找到密钥：{binary_key[i]}  尝试次数：{key[i]},破解时间：{elapsed_time[i]}秒")
print(f"{num}对明密文暴力破解找到密钥的平均用时为：{np.mean(elapsed_time)}秒")
