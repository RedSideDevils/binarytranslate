def binary_to_decimal(digits, constant):
    out = 0

    for i in range(len(digits)):
        smth = int(digits[i]) * (constant ** (len(digits) - i - 1))
        out += smth

    return out 


if __name__ == "__main__":
    ans = binary_to_decimal(str(1011), 2)
    print(ans)

#input 1011 | Output 11
