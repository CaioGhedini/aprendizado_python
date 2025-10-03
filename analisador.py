def main():
    texto = """
    O Python é uma linguagem de programação incrível. 
    Python é fácil de aprender e poderoso.
    Programação em Python é divertida!
    """
    palavras = limpar_texto(texto)
    print(f"Total de palavras: {contar_palavras(palavras)}")
    print(f"Palavras únicas: {contar_palavras_unicas(palavras)}")
    print(f"Palavras que mais repetem: {palavras_mais_repetidas(palavras)}")
    
def limpar_texto(texto):
    """Remove pontuação e divide as palvras"""
    #Convertendo para minúsculas
    texto = texto.lower()
    
    #Removendo pontuação        
    for char in '_-.,!?;:':
        texto = texto.replace(char, ' ') # Substitui cada símbolo por espaço
        
    # Dividindo o texto em palavras
    palavras = texto.split()
    return palavras

def contar_palavras(palavras):
    
    """Retorna o total de palavras"""
    return len(palavras)

def contar_palavras_unicas(palavras):
    """Retorna quantas palavras únicas existem"""
    
    palavras_unicas = set(palavras) # Comando set elimina duplicatas
    return len(palavras_unicas)

def palavras_mais_repetidas(palavras):
    """Encontrando as palavras que mais se repetem no texto"""
    
    contador = {} # Armazena a contagem de cada palavra
    
    for palavra in palavras:
        if palavra in contador:
            contador[palavra] +=1 # Caso a palavra esteja no dicionário, incrementa a contagem
        else: 
            contador[palavra] = 1 # Caso contrário, inicializa a contagem com 1
    
    # Comparando os valores do dicionário para encontrar a maior contagem
    
    repete = max(contador.values()) # Maior valor obstido no dicionário contador
    return repete

if __name__ == "__main__":
    main()

                   
        