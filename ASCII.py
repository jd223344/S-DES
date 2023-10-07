from Encryption import Encryption
from Decryption import Decryption

class ASCII:
    def encryption(self, plaintext, key):
        # 实例化函数和密钥扩展函数
        # 将 ASCII 字符串转换为二进制
        binary_plaintext = ''.join(format(ord(char), '08b') for char in plaintext)
        # 将二进制字符串分成八位一组
        blocks = [binary_plaintext[i:i + 8] for i in range(0, len(binary_plaintext), 8)]
        ciphertext = []
        for block in blocks:
            cipher = Encryption().encryption(block, key)
            ciphertext.append(cipher)
        ciphertext = ''.join(ciphertext)
        # 如果需要，可以将二进制结果转换回 ASCII 字符串
        ciphertext_ascii = ''.join(chr(int(ciphertext[i:i + 8], 2)) for i in range(0, len(ciphertext), 8))
        return ciphertext_ascii

    def decryption(self, ciphertext, key):
        # 实例化函数和密钥扩展函数
        # 将 ASCII 字符串转换为二进制
        binary_ciphertext = ''.join(format(ord(char), '08b') for char in ciphertext)
        # 将二进制字符串分成八位一组
        blocks = [binary_ciphertext[i:i + 8] for i in range(0, len(binary_ciphertext), 8)]
        plaintext = []
        for block in blocks:
            plain = Decryption().decryption(block, key)
            plaintext.append(plain)
        plaintext = ''.join(plaintext)
        # 如果需要，可以将二进制结果转换回 ASCII 字符串
        plaintext_ascii = ''.join(chr(int(plaintext[i:i + 8], 2)) for i in range(0, len(plaintext), 8))
        return plaintext_ascii
