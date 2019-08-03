def calculate(data, findall):
    matches = findall(r"([abc])([+-]?=)([+-]?[abc]?\d*)([+-]\d+)?")
    print(data)
    for v1, s , v2, n in matches:

        print(v1, ' ', s, ' ', v2, ' ', n)

        data_v1 = data[v1]
        if s=='=':
            try:
                data_v1 = int(v2)

            except:
                data_v1 = data[v2]
                try:
                    data_v1 += int(n)
                except:
                    pass
        else:
            sign = s[0]

            try:
                operand = int(v2)
            except:
                operand = data[v2]
            try:
                operand += int(n)
            except:
                pass
            if sign=='-':
                data_v1-=operand
            else:
                data_v1+=operand


        data[v1] = data_v1

        print(data)
    return data


# a=1, a=+1, a=-1, a=b, a=b+100, a=b-100, b+=10, b+=+10, b+=-10, b+=b, b+=b+100, b+=b-100, c-=101, c-=+101, c-=-101, c-=b, c-=b+101, c-=b-101