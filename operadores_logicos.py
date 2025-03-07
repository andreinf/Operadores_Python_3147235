

op1 = False
op2 = True
op3 = op1 or op2
print(op3)

#operador not
op4 = not op2

'''JERARQUIA DEFINITIVA DE OPERADORES
1. ()
2. **
3. +, -
4. *, /, %
5. >, <, !=, ==, >=, <=
6. NOT
7. AND
8. OR
9. =
NOTA: si hay operaciones en el mismo nivel de jerarquia, se resuelven de izquierda a derecha
'''


op1 = False
op2 = True
op3 = False
op4 = True

resultado = not op1 and op2 or op3 and not op4