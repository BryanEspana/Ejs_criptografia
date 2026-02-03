texto = "1010011 1001001 1010000 1010101 1000101 1010011 1011000 1000100"
tabla = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def binario_a_decimal(texto_en_binario):
    texto_en_decimal = ""
    for caracter in texto_en_binario.split():
        numero = int(caracter, 2)
        texto_en_decimal += str(numero).strip() + " "
    return texto_en_decimal.strip()

def decimal_a_ascii(texto_en_decimal):
    resultado = ""

    for caracter in texto_en_decimal.split():
        numero = int(caracter)
        ascii_caracter = chr(numero)
        resultado += ascii_caracter

    return resultado.strip()

def ascii_a_base64(texto_ascii):
    bits_concatenados = ""
    
    for caracter in texto_ascii:
        numero = ord(caracter)
        binario = ""
        
        while numero > 0:
            resultado_modulo = numero % 2
            binario = str(resultado_modulo) + binario
            numero = numero // 2
        
        while len(binario) < 8:
            binario = "0" + binario
        
        bits_concatenados += binario
    
    while len(bits_concatenados) % 6 != 0:
        bits_concatenados += "0"
    
    resultado = ""
    for i in range(0, len(bits_concatenados), 6):
        grupo = bits_concatenados[i:i+6]
        indice = int(grupo, 2)
        resultado += tabla[indice]
    
    while len(resultado) % 4 != 0:
        resultado += "="
    
    return resultado

texto_descifrado = decimal_a_ascii(binario_a_decimal(texto))
texto_base64 = ascii_a_base64(texto_descifrado)

print("Binario: " + texto)
print("BASE64: " + texto_base64)
