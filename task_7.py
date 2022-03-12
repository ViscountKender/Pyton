# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат (Попробовать решить с помощью таблицы истинности)
X = [True,False]
Y = [True,False]
Z = [True,False]
for i in X:
    for j in Y:
        for k in Z:
            
            if not(X or Y or Z) == (not X and not Y and not Z):
                print(True)
            else:
                print(False)    
