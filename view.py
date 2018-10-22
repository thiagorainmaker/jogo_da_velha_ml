

print("Escolha uma casa")
print("_1__|_2_|_3__")
print("_4__|_5_|_6__")
print(" 7  | 8 | 9  ")
print("\n")
print("-----------------------------------------------------------")

def verifica_empate(jogo):
	return ( jogo[0][0] != ' ' and jogo[0][1] != ' ' and jogo[0][2] != ' '  and
		jogo[1][0] != ' '  and jogo[1][1] != ' ' and jogo[1][2] != ' '  and jogo[2][0] != ' '  and jogo[2][1] != ' '  and jogo[2][2] != ' ')

def jogada_invalida(jogo, numb):
	return (numb == 1 and jogo[0][0] != ' ') or (numb == 2 and jogo[0][1] != ' ') or (numb == 3 and jogo[0][2] != ' ') or (numb == 4 and
		jogo[1][0] != ' ') or (numb == 5 and jogo[1][1] != ' ') or ( numb == 6 and jogo[1][2] != ' ') or (numb == 7 and jogo[2][0] != ' ') or  (numb == 8 and jogo[2][1] != ' ') or (numb == 9 and jogo[2][2] != ' ') or numb > 9 or numb < 1
	

def verifica_vitoria(jogo):
	return (jogo[0][0] != ' ' and jogo[0][0] == jogo[1][0] and jogo[1][0]  == jogo[2][0]) or (jogo[0][1] != ' ' and jogo[0][1] == jogo[1][1] and jogo[1][1]  == jogo[2][1]) or (jogo[0][2] != ' ' and jogo[0][2] == jogo[1][2] and jogo[1][2]  == jogo[2][2]) or (jogo[0][0] != ' ' and jogo[0][0] == jogo[0][1] and jogo[0][1]  == jogo[0][2]) or (jogo[1][0] != ' ' and jogo[1][0] == jogo[1][1] and jogo[1][1]  == jogo[1][2]) or (jogo[2][0] != ' ' and jogo[2][0] == jogo[2][1] and jogo[2][1]  == jogo[2][2]) or ( jogo[0][0] != ' ' and jogo[0][0] == jogo[1][1] and jogo[1][1]  == jogo[2][2])  or (jogo[0][2] != ' ' and jogo[0][2] == jogo[1][1] and jogo[1][1]  == jogo[2][0]) 


def monta_list(jogo, numb , mark):
	if numb == 1:
		jogo[0][0] = mark
	if numb == 2:
		jogo[0][1] = mark
	if numb == 3:
		jogo[0][2] = mark
	if numb == 4:
		jogo[1][0] = mark
	if numb == 5:
		jogo[1][1] = mark
	if numb == 6:
		jogo[1][2] = mark
	if numb == 7:
		jogo[2][0] = mark
	if numb == 8:
		jogo[2][1] = mark
	if numb == 9:
		jogo[2][2] = mark
	
	return jogo


def monta_tela(jogo):
	print("_"+jogo[0][0]+"__|_"+jogo[0][1]+"_|_"+jogo[0][2]+"__")
	print("_"+jogo[1][0]+"__|_"+jogo[1][1]+"_|_"+jogo[1][2]+"__")
	print(" "+jogo[2][0]+"  | "+jogo[2][1]+" | "+jogo[2][2]+"  ")


w, h = 3, 3;
matrix = [[0 for x in range(w)] for y in range(h)] 

matrix[0][0] = ' '
matrix[0][1] = ' '
matrix[0][2] = ' '
matrix[1][0] = ' '
matrix[1][1] = ' '
matrix[1][2] = ' '
matrix[2][0] = ' '
matrix[2][1] = ' '
matrix[2][2] = ' '

i = 0
simbolo = "x"
while not verifica_vitoria(matrix):
	if verifica_empate(matrix):
		print("Jogo empatado")
		break

	if int(i) % 2 == 0:
		simbolo = "x"
	else: 	
		simbolo = "0"
	nb = input('escolha uma casa \n')
	while jogada_invalida(matrix, nb):
		print('Jogada nula, escolha outru numero \n')
		nb = input('escolha uma casa \n')

	matrix = monta_list(matrix, nb , simbolo)	
	monta_tela(matrix)
	i = i+1


print("fim de jogo!")
