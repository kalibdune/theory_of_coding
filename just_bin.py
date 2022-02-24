def binary_code(text):
    result = ''
    for code in text:
        code=format(ord(code), 'b')
        code=str(code)
        result += code + '\n'
    return result

def to_word_chet_mat(text, code):
    code = code.split()
    array = text.split('<br>')

    plain_text_array = []
    for word in array:
        if word.find("""<span style="color:red;">""" and """</span>"""):
            plain_text_array.append(word.replace("""<span style="color:red;">""", '').replace("""</span>""", ''))
        else:
            plain_text_array.append(word)
    del plain_text_array[-1]

    result = ''
    pos_error = 0
    for item in plain_text_array:
        item_arr = list(item)
        real_letter = ''
        for i in range(0, len(item_arr)):
            real_letter+=item_arr[i]
        if real_letter == code[plain_text_array.index(item)]:
            result+=chr(int(real_letter, 2))
        else:
            result+="""<span style="color:red;">{0}</span>""".format(chr(int(real_letter, 2)))
            pos_error = plain_text_array.index(item)
    
    result+='<br>Код пришёл с ошибкой, без алгоритма исправить невозможно'
    return result