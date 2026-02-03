texto = "EstaEsUnaPrueba"

def texto_a_ascii(texto):
    texto_en_ascii = ""
    for caracter in texto:
        ascii_decimal = ord(caracter) 
        texto_en_ascii += str(ascii_decimal).strip() + " "
    return texto_en_ascii.strip()

def ascii_a_binario(texto_en_ascii):
    resultado = ""

    for caracter in texto_en_ascii.split():
        numero = int(caracter)
        binario = ""
        
        while numero > 0:
            resultado_modulo = numero % 2
            binario = str(resultado_modulo)+ binario
            numero = numero // 2
        resultado += binario + " "

    return resultado.strip()
    
print("TEXTO: \n" + texto)
print("BINARIO: \n" + ascii_a_binario(texto_a_ascii(texto)))