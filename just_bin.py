def binary_code(text):
    result = ''
    for code in text:
        code=format(ord(code), 'b')
        code=str(code)
        result += code + '\n'
    return result
