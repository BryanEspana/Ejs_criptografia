texto_base64 = "U0lQVUVTWEQ="
tabla = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64_a_indices(texto_base64):
    texto_en_indices = ""
    for caracter in texto_base64:
        if caracter == "=":
            continue
        base64_indice = tabla.index(caracter)
        texto_en_indices += str(base64_indice).strip() + " "
    return texto_en_indices.strip()

def indices_a_binario(texto_en_indices):
    bits_concatenados = ""

    for caracter in texto_en_indices.split():
        numero = int(caracter)
        binario = ""
        
        if numero == 0:
            binario = "0"
        
        while numero > 0:
            resultado_modulo = numero % 2
            binario = str(resultado_modulo) + binario
            numero = numero // 2
        
        while len(binario) < 6:
            binario = "0" + binario
        
        bits_concatenados += binario

    resultado = ""
    for i in range(0, (len(bits_concatenados) // 8) * 8, 8):
        byte = bits_concatenados[i:i+8]
        resultado += byte + " "

    return resultado.strip()

def binario_a_decimal(texto_binario):
    resultado = ""
    
    for binario_num in texto_binario.split():
        decimal = 0
        potencia = 0
        
        for digito in reversed(binario_num):
            decimal += int(digito) * (2 ** potencia)
            potencia += 1
        
        resultado += str(decimal) + " "
    
    return resultado.strip()

def base64_a_ascii(texto_base64):
    indices = base64_a_indices(texto_base64)
    binario = indices_a_binario(indices)
    ascii_resultado = binario_a_decimal(binario)
    return ascii_resultado


indices = base64_a_indices(texto_base64)
binario = indices_a_binario(indices)
ascii_resultado = binario_a_decimal(binario)

print("BASE64: \n  " + texto_base64)
print("BINARIO: \n  " + binario)
print("ASCII: \n  " + ascii_resultado)
