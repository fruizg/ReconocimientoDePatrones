primera_lista = [5, -2, 10, -8, 3, -6, -1, 7, -4, 9]
segunda_lista = [-num for num in primera_lista if num < 0]

print("Primera lista:", primera_lista)
print("Segunda lista (valores negativos):", segunda_lista)

matriz = [    [2.5, 1.3, 0.7],
    [-3.8, 4.2, 6.0],
    [9.1, -2.2, -5.5]
]

A=matriz
B=[[1],[2],[3]]
C=[[2],[3],[4]]
D=A*B+C
print(D)
