def main():
    texto = """
    Python, é não até;até até até... tudo tudo nada tudo didático, prolixo, sabe sabe sabe sabe tudo mesmo, ok, ok, ok, ok
    """
    palavras = limpar_texto(texto)
    repetidas = palavras_mais_repetidas(palavras)
    print("ANALISADOR DE PALAVRAS\n=====================================================================")
    print(f"Total de palavras: {contar_palavras(palavras)}")
    print("=====================================================================")
    print(f"Total de palavras únicas: {contar_palavras_unicas(palavras)}")
    print("=====================================================================")
    print(f"Palavras únicas encontradas: {set(palavras)}")
    print("=====================================================================")
    print(f"Quantas palavras mais repetem: {len(repetidas)}")
    print("=====================================================================")
    print(f"Palavras que mais repetem: {repetidas}")
    
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
    
    contador = {} # Armazena a palavra como chave e a contagem como valor
    
    for palavra in palavras:
        contador[palavra] = contador.get(palavra, 0) + 1
        # Caso a palavra já exista no dicionário, incrementa o valor em 1
        
        if not contador:
            return []
        # Caso o dicionário esteja vazio, retorna uma lista vazia
        
    
    # Comparando os valores do dicionário para encontrar a maior contagem
    
    repeticoes = max(contador.values()) # Maior valor obtido no dicionário contador
   
    # encontrando as palavras que se encaixam no total atribuído à repeticoes
    mais_repetidas = [ palavra for palavra, contagem in contador.items() 
        if contagem == repeticoes]
    
    return mais_repetidas


if __name__ == "__main__":
    main()

                   
        