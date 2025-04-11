import re
import unicodedata

# --- Função de normalização para remover acentos e pontuações ---
def normalizar_texto(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')
    texto = re.sub(r'[^\w\s]', '', texto)  # remove pontuações
    return texto

# --- Conjuntos de palavras positivas e negativas ---
positivas = {"bom", "otimo", "excelente", "incrivel", "adorei", "top", "massa", "recomendo", "maravilhoso", "amei"}
negativas = {"ruim", "pessimo", "horrivel", "odiei", "fraco", "sem condicao", "detestei", "terrivel", "lixo", "enganoso"}

# --- Comentários simulados usando dicionário ---
comentarios = {
    1: "Esse produto é ótimo, adorei!",
    2: "Achei horrível, muito ruim mesmo.",
    3: "Top demais, super recomendo!",
    4: "Não gostei, é fraco e péssimo.",
    5: "É ok, nada demais.",
    6: "Produto excelente, valeu a pena!",
    7: "Terrível atendimento, detestei.",
    8: "Massa demais esse serviço.",
    9: "Sem condição, horrível.",
    10: "Bom produto, mas entrega atrasou."
}

# --- Função para classificar comentários com feedback detalhado ---
def classificar_comentario(comentario):
    texto = normalizar_texto(comentario)
    palavras = texto.split()
    positivos = sum(1 for p in palavras if p in positivas)
    negativos = sum(1 for p in palavras if p in negativas)

    if positivos > negativos:
        return "Positivo"
    elif negativos > positivos:
        return "Negativo"
    else:
        return "Neutro"

# --- Execução com relatório visual ---
print("RELATÓRIO DE ANÁLISE DE SENTIMENTOS\n")
for numero, texto in comentarios.items():
    classificacao = classificar_comentario(texto)
    print(f"Comentário {numero}: \"{texto}\"")
    print(f"Classificação: {classificacao}")
    print("-" * 50)
