#Importando el modulo PLY
import ply.lex as lex

#Definimos las palabras reservadas como tokens
reservadas = {
              'class'   :   'CLASS',
              'return'  :   'RETURN',
              'this'    :   'THIS',
              'extends' :   'EXTENDS',
              'if'      :   'IF',
              'new'     :   'NEW',
              'void'    :   'VOID',
              'else'    :   'ELSE',
              'length'  :   'LENGTH',
              'int'     :   'INT',
              'while'   :   'WHILE',
              'true'    :   'TRUE',
              'boolean' :   'BOLEAN',
              'break'   :   'BREAK',
              'false'   :   'FALSE',
              'string'  :   'STRING',
              'continue'    :   'CONTINUE',
              'null'    :   'NULL',    
              }

#Definimos los tipos y operadores del lenguaje como tokens
tokens = [
#Operadores Logicos de comparacion
   'OR',                ## ||
   'AND',               ## &&
   'NOT',               ## NOT
   'MENOR',             ## <
   'MENORIGUAL',        ## <=
   'MAYOR',             ## >
   'MAYORIGUAL',        ## >=
   'IGUALIGUAL',        ## ==
   'DIFERENTE',         ## !=

# Operadores Aritmeticos
   'SUMA',              ## +
   'RESTA',             ## -
   'MULT',              ## *
   'DIV',               ## /
   'MODULO',            ## %
   'IGUAL',             ## =

# Simbolos Especiales
   'LLIZQ',             ## {
   'LLDER',             ## }
   'PARIZQ',            ## (
   'PARDER',            ## )
   'CORIZQ',            ## [           
   'CORDER',            ## ]
   
# Tipos Numericos
    'HEXA',             ## 0x...
    'FLOAT',            ## 0.00...     
    'ENTERO',           ## 0           

# Signos de Puntuacion
    'COMA',             ## ,
    'PUNTO',            ## . 
    'PUNTOCOMA',        ## ;
    'DOSPUNTOS',        ## :
    
# Literales
    'COMENTARIO',       ## /**/ - // //
    'IDENTIFICADOR',    ## Tipo
    'CADENA'            ## "Esto es una cadena"
    
] + list(reservadas.values())

# Definicion de las reglas de las Expresiones Regulares A Los Tokens
# Operadores Logicos de comparacion
t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'~'
t_MENOR = r'<'
t_MENORIGUAL = r'<='
t_MAYOR = r'>'
t_MAYORIGUAL = r'>='
t_DIFERENTE = r'!='
t_IGUALIGUAL = r'=='

# Operadores Aritmeticos
t_SUMA = r'\+'
t_MENOS = r'-'
t_MULTI = r'\*'
t_DIVI = r'/'
t_MODULO = r'%'
t_IGUAL = r'='

# Simbolor Especiales
t_LLIZQ = r'\{'
t_LLDER = r'\}'
t_PARDER  = r'\('
t_PARIZQ  = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'

# Signos De Puntuacion
t_COMA = r','
t_PUNTO = r'\.'
t_PUNTOCOMA = r';'
t_DOSPUNTOS = r':'


# Tipos Numericos
# Expresion Regular Para Los Numeros En Hexa 
def t_HEXA(t):
    r'0[x|X][0-9A-F]+'
    return t

# Expresion Regular Para Los Numeros En Entero
def t_ENTERO(t):
    r'-?[\d+]'
    t.value = int(t.value)
    return t
