Una encriptacion simple usando el codigo ASCII
y funciones propias ord() y chr()

    for simbolo in mensaje:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += clave
 
            if simbolo.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif simbolo.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
 
            traduccion += chr(num)
        else:
            traduccion += simbolo
    return traduccion 
