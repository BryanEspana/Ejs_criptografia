binario = "1000101 1110011 1110100 1100001 1000101 1110011 1010101 1101110 1100001 1010000 1110010 1110101 1100101 1100010 1100001"

def binario_a_decimal(binario):
    decimal = 0
    potencia = 0
    
    for digito in reversed(binario):
        decimal += int(digito) * (2 ** potencia)
        potencia += 1
    
    return decimal

def binario_a_ascii(texto_binario):
    resultado = ""
    
    for binario_num in texto_binario.split():
        decimal = binario_a_decimal(binario_num)
        resultado += str(decimal) + " "
    
    return resultado.strip()

print("BINARIO: \n  " + binario)
print("ASCII: \n  " + binario_a_ascii(binario))
