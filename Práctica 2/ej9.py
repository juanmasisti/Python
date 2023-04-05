#Letra valor
#A, E, I, O, U, L, N, R, S, T  : 1
#D, G  : 2
#B, C, M, P     : 3
#F, H, V, W, Y      : 4
#K      : 5    
#J, X       : 8
#Q, Z  : 10 

dic = {'aeioulnrst': 1, 'dg': 2, 'bcmp': 3,
       'fhvwy': 4, 'k': 5, 'jx': 8, 'qz': 10}
cant = 0

palabra = input("Ingrese una palabra: ")
for letra in palabra:
    for value in dic:
        if letra in value:
            cant += dic[value]
  
print("• Palabra: ",palabra , " \n• valor: ", cant)

