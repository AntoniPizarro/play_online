def crypt(code):
    out = ""
    for character in code:
        val = str(ord(character))
        while len(val) < 3:
            val = "0" + val
        out += val
    return out

def decrypt(code):
    if type(code) != "str":
        code = str(code)
    out = ""
    comodin = ""
    recode = []
    for digit in code:
        comodin += digit
        if len(comodin) == 3:
            recode.append(comodin)
            comodin = ""
    for group in recode:
        out += chr(int(group))
    return out