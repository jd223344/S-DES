class Function:

    def IP(self, input_text):
        new_input = []
        new_input.append(input_text[1])
        new_input.append(input_text[5])
        new_input.append(input_text[2])
        new_input.append(input_text[0])
        new_input.append(input_text[3])
        new_input.append(input_text[7])
        new_input.append(input_text[4])
        new_input.append(input_text[6])
        return ''.join(new_input)

    def EPBox(self,input_text):
        # 定义EPBox扩展规则
        epbox_table = [4, 1, 2, 3, 2, 3, 4, 1]
        # 确保输入的文本时4位
        if len(input_text) != 4:
            raise ValueError("文本长度必须为4位")
        # 进行EPBox扩展
        epbox_text = [input_text[i-1] for i in epbox_table]
        return ''.join(epbox_text)

    def SBox1(self,linput_text):
        tmp1 = linput_text[0]+linput_text[3] #行变量
        tmp2 = linput_text[1]+linput_text[2] #列变量
        if (tmp1 == "00") and (tmp2 == "00"): loutput_text = "01"
        if (tmp1 == "00") and (tmp2 == "01"): loutput_text = "00"
        if (tmp1 == "00") and (tmp2 == "10"): loutput_text = "11"
        if (tmp1 == "00") and (tmp2 == "11"): loutput_text = "10"
        if (tmp1 == "01") and (tmp2 == "00"): loutput_text = "11"
        if (tmp1 == "01") and (tmp2 == "01"): loutput_text = "10"
        if (tmp1 == "01") and (tmp2 == "10"): loutput_text = "01"
        if (tmp1 == "01") and (tmp2 == "11"): loutput_text = "00"
        if (tmp1 == "10") and (tmp2 == "00"): loutput_text = "00"
        if (tmp1 == "10") and (tmp2 == "01"): loutput_text = "10"
        if (tmp1 == "10") and (tmp2 == "10"): loutput_text = "01"
        if (tmp1 == "10") and (tmp2 == "11"): loutput_text = "11"
        if (tmp1 == "11") and (tmp2 == "00"): loutput_text = "11"
        if (tmp1 == "11") and (tmp2 == "01"): loutput_text = "01"
        if (tmp1 == "11") and (tmp2 == "10"): loutput_text = "00"
        if (tmp1 == "11") and (tmp2 == "11"): loutput_text = "10"
        return loutput_text

    def SBox2(self, rinput_text):
        tmp1 = rinput_text[0] + rinput_text[3]  # 行变量
        tmp2 = rinput_text[1] + rinput_text[2]  # 列变量
        if (tmp1 == "00") and (tmp2 == "00"): routput_text = "00"
        if (tmp1 == "00") and (tmp2 == "01"): routput_text = "01"
        if (tmp1 == "00") and (tmp2 == "10"): routput_text = "10"
        if (tmp1 == "00") and (tmp2 == "11"): routput_text = "11"
        if (tmp1 == "01") and (tmp2 == "00"): routput_text = "10"
        if (tmp1 == "01") and (tmp2 == "01"): routput_text = "11"
        if (tmp1 == "01") and (tmp2 == "10"): routput_text = "01"
        if (tmp1 == "01") and (tmp2 == "11"): routput_text = "00"
        if (tmp1 == "10") and (tmp2 == "00"): routput_text = "11"
        if (tmp1 == "10") and (tmp2 == "01"): routput_text = "00"
        if (tmp1 == "10") and (tmp2 == "10"): routput_text = "01"
        if (tmp1 == "10") and (tmp2 == "11"): routput_text = "10"
        if (tmp1 == "11") and (tmp2 == "00"): routput_text = "10"
        if (tmp1 == "11") and (tmp2 == "01"): routput_text = "01"
        if (tmp1 == "11") and (tmp2 == "10"): routput_text = "00"
        if (tmp1 == "11") and (tmp2 == "11"): routput_text = "11"
        return routput_text

    def SBox(self,input_text):
        # 确保输入的文本时8位
        if len(input_text) != 8:
            raise ValueError("文本长度必须为8位")
        linput_text = input_text[:4] #取左边四位
        rinput_text = input_text[4:] #取右边四位
        loutput_text = self.SBox1(linput_text)
        routput_text = self.SBox2(rinput_text)
        sbox_text = loutput_text+routput_text
        return sbox_text

    def SPBox(self,input_text):
        # 确保输入的文本时4位
        if len(input_text) != 4:
            raise ValueError("文本长度必须为4位")
        # 进行SPBox替换
        spbox_text = input_text[1]+input_text[3]+input_text[2]+input_text[0]
        return ''.join(spbox_text)

    def FFunction(self,right,key):
        epbox_right = self.EPBox(right)
        xor_right = "".join(str(int(x) ^ int(y)) for x, y in zip(epbox_right, key))
        sbox_right = self.SBox(xor_right)
        spbox_right = self.SPBox(sbox_right)
        return spbox_right

# 定义最终置换
    def PI(self, input_text):
        new_input = []
        new_input.append(input_text[3])
        new_input.append(input_text[0])
        new_input.append(input_text[2])
        new_input.append(input_text[4])
        new_input.append(input_text[6])
        new_input.append(input_text[1])
        new_input.append(input_text[7])
        new_input.append(input_text[5])
        return ''.join(new_input)

    def swap(self, left, right):
        input = left+right
        new_left = input[4:] #取旧的右四位
        new_right = input[:4] #取旧的左四位
        return new_left, new_right