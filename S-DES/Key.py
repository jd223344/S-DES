
class Key():

    def P10(self,key):
        # 定义P10置换规则
        p10_table = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        # 确保输入的密钥是10位
        if len(key) != 10:
            raise ValueError("密钥长度必须为10位")
        # 进行P10置换
        p10_key = [key[i - 1] for i in p10_table]
        return ''.join(p10_key)


    def P8(self,key):
        p8_key = []
        p8_key.append(key[5])
        p8_key.append(key[2])
        p8_key.append(key[6])
        p8_key.append(key[3])
        p8_key.append(key[7])
        p8_key.append(key[4])
        p8_key.append(key[9])
        p8_key.append(key[8])
        return ''.join(p8_key)


    def left_shift(self,key):
        # 将第一个字符移到最后一个字符的位置
        shifted_key = key[1:] + key[0]

        return shifted_key

    def key_expansion(self, key0):
        p10_key0 = self.P10(key0)
        shifted_k1 = self.left_shift(p10_key0[:5])+self.left_shift(p10_key0[5:])
        k1 = self.P8(shifted_k1)
        shifted_k2 = self.left_shift(shifted_k1[:5])+self.left_shift(shifted_k1[5:])
        k2 = self.P8(shifted_k2)
        return k1,k2





