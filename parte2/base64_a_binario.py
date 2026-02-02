texto = "Hola"
tabla = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def texto_a_base64(texto):
    texto_en_base64 = ""
    for caracter in texto:
        base64_indice = tabla.index(caracter)
        texto_en_base64 += str(base64_indice).strip() + " "
    return texto_en_base64.strip()

def base64_a_binario(texto_en_base64):
    resultado = ""

    for caracter in texto_en_base64.split():
        numero = int(caracter)
        binario = ""
        
        while numero > 0:
            resultado_modulo = numero % 2
            binario = str(resultado_modulo)+ binario
            numero = numero // 2
        resultado += binario + " "

    return resultado.strip()
    

print(base64_a_binario(texto_a_base64(texto)))
