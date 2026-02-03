binario = "01010011 01001001 01010000 01010101 01000101 01010011 01011000 01000100"
clave = "01001011"  # Clave para XOR

def xor_binario(binario, clave):
    resultado = ""
    
    for byte in binario.split():
        # Ajustar la clave al tamaño del byte si es necesario
        clave_ajustada = clave
        while len(clave_ajustada) < len(byte):
            clave_ajustada = "0" + clave_ajustada
        
        byte_resultado = ""
        for i in range(len(byte)):
            # Aplicar XOR bit a bit
            if byte[i] == clave_ajustada[i]:
                byte_resultado += "0"
            else:
                byte_resultado += "1"
        
        resultado += byte_resultado + " "
    
    return resultado.strip()


binario_xor = xor_binario(binario, clave)

print("BINARIO ORIGINAL: \n  " + binario)
print("CLAVE XOR: \n  " + clave)
print("BINARIO XOR: \n  " + binario_xor)
