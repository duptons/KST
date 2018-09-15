def maxIntegerRatio(self, param_list):
    """
    最大整数比
    param_list = [int1, int2, ...], 元素类型为 int 且 > 0
    返回值：(flag, str), if flag==True, str = "3:5:6..."
    """
    try:
        maxIR_str = ""
        for param in param_list:
            if isinstance(param, types.IntType) and param > 0:
                pass
            else:
                return (False, "The param_list Error: " + str(param_list))
        minElem = min(param_list)
        N = 1 # 最大公约数
        for n in xrange(minElem):
            sign = 0
            for param in param_list:
                if param % (minElem - n) != 0:
                    break;
                sign += 1
            if sign == len(param_list):
                N = minElem - n
                break
        for param in param_list:
            maxIR_str += str(int(param / N)) + ":"
        if len(maxIR_str) < 4:
            return (False, "Can not get maxIntegerRatio of param_list: " + str(param_list))
        return (True, maxIR_str[:-1])
    except:
        return (False, "Unknown Error in maxIntegerRatio()" + traceback.format_exc())