import random

def random_error(text):
    try:
        array = text.split()
        
        for pos in range(0, len(array)):
            array[pos] = list(array[pos])
        
        count_error_letter = random.randint(0, len(array)-1)
        error_bit_num = random.randint(0, len(array[count_error_letter])-1)

        if array[count_error_letter][error_bit_num] == '0':
            array[count_error_letter][error_bit_num] = """<span style="color:red;">1</span>"""
        else:
            array[count_error_letter][error_bit_num] = """<span style="color:red;">0</span>"""

        error_text = ''
        for item in array:#to string
            for num in item:
                error_text += num
            error_text += '<br>'
        
        return error_text
    except:
        return ''