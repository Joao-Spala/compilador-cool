# Compilador Cool - Análise Léxica

Etapa de análise léxica do compilador de Cool, feita em Python, de forma manual (leitura caractere a caractere + reconhecimento de padrões, sem usar flex/bison).

## Como rodar

```
python3 lexer.py exemplo.cl
```

Imprime cada token reconhecido no formato:

```
lexema
    Tipo: <categoria>
    Valor: <valor>
    linha: <numero da linha>
```

## Tokens reconhecidos

- Palavras reservadas: class, else, fi, if, in, inherits, isvoid, let, loop, pool, then, while, case, esac, new, of, not
- Identificadores: `[a-zA-Z][a-zA-Z0-9_]*`
- Inteiros
- Strings (entre aspas duplas, com suporte a escapes)
- Separadores: `{ } ( ) ; : , . @`
- Operadores: `+ - * / ~ < <= = <- =>`
- Comentários de linha (`--`) e de bloco (`(* ... *)`) são ignorados
