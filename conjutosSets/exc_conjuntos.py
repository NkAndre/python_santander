## Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).


conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2
print(uniao)

intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3}


diferenca = conjunto1 - conjunto2
print(diferenca)  # Imprime {1, 2}


diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}