from operator import mod

def cipher(input, key):
    len_input = len(input)
    ret = '' 
    for i in range(1, len_input+ 1): 
        p = input[len_input - i]
        
        p_i = index(p)
        k_i = index(key[0])        
        k_j = index(key[1])
        k_k = index(key[2])

        ret += modulo(pow(k_i, 3) - pow(k_i, 2) + k_j * k_k - p_i)

        key[0] = modulo(-pow(k_i, 3) + k_k * pow(k_i, 2))
        key[1] = modulo(-pow(k_j, 3) + k_i * pow(k_j, 2))
        key[2] = modulo(-pow(k_k, 3) + k_j * pow(k_k, 2))

    return ret

def index(character):
    ord_char = ord(character)
    if ord_char <= ord('9') and ord_char >= ord('0'):
        i = ord_char - ord('0') + 26
    elif character == ' ':
        i = 36
    elif character == '.':
        i = 37
    elif character == '?':
        i = 38
    elif character == '!':
        i = 39
    elif character == ':':
        i = 40
    else:
        i = ord_char - ord('A')
    return i

def modulo(shift):
    m_switch = mod(shift, 41)
    if m_switch > 35:
        if m_switch == 36:
            return ' '
        elif m_switch == 37:
            return '.'
        elif m_switch == 38:
            return '?'
        elif m_switch == 39:
            return '!'
        elif m_switch == 40:
            return ':'
    elif m_switch > 25:
        return chr(ord('0') + m_switch - 26)
    else:
        return chr(ord('A') + m_switch)

if __name__ == '__main__' :
    print("Enter text to cipher: ")
    vstup = input().upper()
    print("Enter three letter key: ")
    klic = list(input().upper())
    print(cipher(vstup, klic)[::-1])
    print("Press ENTER to exit.")
    input()
 