import sys

PALAVRAS_RESERVADAS = {
    "class", "else", "fi", "if", "in", "inherits", "isvoid", "let",
    "loop", "pool", "then", "while", "case", "esac", "new", "of", "not"
}

SEPARADORES = {
    "{": "abre_chaves", "}": "fecha_chaves",
    "(": "abre_parenteses", ")": "fecha_parenteses",
    ";": "ponto_e_virgula", ":": "dois_pontos", ",": "virgula", ".": "ponto",
    "@": "arroba"
}

OPERADORES_2 = {"<-", "<=", "=>"}
OPERADORES_1 = {"+", "-", "*", "/", "~", "<", "="}


def lexico(codigo):
    tokens = []
    linha = 1
    i = 0
    tamanho = len(codigo)

    while i < tamanho:
        c = codigo[i]

        if c == "\n":
            linha += 1
            i += 1
            continue

        if c.isspace():
            i += 1
            continue

        # comentario de linha
        if codigo[i:i + 2] == "--":
            while i < tamanho and codigo[i] != "\n":
                i += 1
            continue

        # comentario de bloco
        if codigo[i:i + 2] == "(*":
            i += 2
            while i < tamanho and codigo[i:i + 2] != "*)":
                if codigo[i] == "\n":
                    linha += 1
                i += 1
            i += 2
            continue

        # string: le do " inicial ao " final, guardando o conteudo
        if c == '"':
            linha_inicio = linha
            i += 1
            valor = ""
            while i < tamanho and codigo[i] != '"':
                if codigo[i] == "\\" and i + 1 < tamanho:
                    valor += codigo[i:i + 2]
                    i += 2
                    continue
                if codigo[i] == "\n":
                    linha += 1
                valor += codigo[i]
                i += 1
            i += 1
            texto = '"' + valor + '"'
            tokens.append((texto, "string", texto, linha_inicio))
            continue

        # numero inteiro
        if c.isdigit():
            inicio = i
            while i < tamanho and codigo[i].isdigit():
                i += 1
            valor = codigo[inicio:i]
            tokens.append((valor, "Inteiro", valor, linha))
            continue

        # identificador ou palavra reservada: [a-zA-Z][a-zA-Z0-9_]*
        if c.isalpha() or c == "_":
            inicio = i
            while i < tamanho and (codigo[i].isalnum() or codigo[i] == "_"):
                i += 1
            valor = codigo[inicio:i]
            if valor.lower() in PALAVRAS_RESERVADAS:
                tokens.append((valor, "Palavra reservada", valor, linha))
            else:
                tokens.append((valor, "Identificador", valor, linha))
            continue

        # operadores de 2 caracteres (<- <= =>)
        dois = codigo[i:i + 2]
        if dois in OPERADORES_2:
            tokens.append((dois, "Operador", dois, linha))
            i += 2
            continue

        # separadores
        if c in SEPARADORES:
            tokens.append((c, "Separador", SEPARADORES[c], linha))
            i += 1
            continue

        # operadores de 1 caractere
        if c in OPERADORES_1:
            tokens.append((c, "Operador", c, linha))
            i += 1
            continue

        print(f"Erro lexico: caractere nao reconhecido '{c}' na linha {linha}")
        i += 1

    return tokens


def imprime_tokens(tokens):
    for lexema, tipo, valor, linha in tokens:
        print(lexema)
        print(f"    Tipo: {tipo}")
        print(f"    Valor: {valor}")
        print(f"    linha: {linha}")
        print()


if __name__ == "__main__":
    arquivo = sys.argv[1] if len(sys.argv) > 1 else "exemplo.cl"
    with open(arquivo, "r", encoding="utf-8") as f:
        codigo = f.read()

    tokens = lexico(codigo)
    imprime_tokens(tokens)
