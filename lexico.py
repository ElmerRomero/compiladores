import tkinter as tk
from tkinter import scrolledtext
from ply import lex, yacc

root = tk.Tk()
root.title("Resultados del Analizador")

def mostrar_resultados(resultados):
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=30, bg='black', fg='white')
    text_area.pack()
    text_area.insert(tk.INSERT, resultados)

tokens = (
    'INCLUDE', 'COMMENT', 'ID', 'INT', 'FLOAT', 'CHAR', 'STRING', 'IF', 'ELSE', 'WHILE', 'RETURN',
    'PARENTESIS_IZQ', 'PARENTESIS_DER', 'LLAVE_IZQ', 'LLAVE_DER', 'CORCHETE_IZQ', 'CORCHETE_DER',
    'ASIGNACION', 'MENOR', 'MAYOR', 'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION', 'AND', 'OR', 'NOT',
    'NUMERO', 'CADENA', 'PUNTO_Y_COMA','COMA'
)

t_INCLUDE = r'\#include\s*<.*?>'
t_COMMENT = r'\/\/[^\n]*|\/\*[\s\S]*?\*\/'

t_INT = r'int'
t_FLOAT = r'float'
t_CHAR = r'char'
t_STRING = r'string'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_RETURN = r'return'

t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'

t_ASIGNACION = r'='
t_MENOR = r'<'
t_MAYOR = r'>'
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

t_NUMERO = r'\d+(\.\d+)?'
t_CADENA = r'\"([^\\\n]|(\\.))*?\"'
t_PUNTO_Y_COMA = r';'
t_COMA=r','

t_ignore = ' \t\n'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def analizador(entrada):
    lexer.input(entrada)
    resultados = ""
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        resultados += f"Token: {tok.type}, Valor: {tok.value}\n"
    mostrar_resultados(resultados)

def leer(codigo_fuente):
    with open(codigo_fuente, 'r') as file:
        entrada = file.read()
    analizador(entrada)

codigo = 'prueba.cpp'
leer(codigo)
root.mainloop()
