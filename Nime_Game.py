
from random import randrange
import pickle

# affichage de l'état du jeu
def afficher(A):
	m = max(A)

	for n, i in enumerate(A) :
		print( n+1, '|', '*'*i, ' '*(m-i), '|', i )

# le jeu proprement dit
def Game():
	# loading des anciens scores
	try :
		file = open('score', 'rb')
		score = pickle.load(file)
		file.close()
	except :
		file = open('score', 'wb')
		file.close()
		score = {}

	# enregistrement des joueurs
	players = [ 0, 0 ]

	players[0] = input('Joueur 1, entrez votre nom :')
	players[1] = input('Joueur 2, entrez votre nom :')

	tour, coups = randrange(2), 0

	# initialisation de la planche de jeu
	A = []
	for i in range(randrange(3,8)):
		A.append( randrange(5,24) )
	afficher(A)

	# alterance des joueur jusqu'a la fin des pierre
	while sum(A) > 0 :
		u = input( 'Entrez votre coups '+players[tour]+' :' )
		a, b = u.split('-')

		# interception des coups illégeaux
		if eval(a) > len(A) :
			print('Coups illégal')
			continue
		if A[ eval(a)-1 ] < eval(b) :
			print('Coups illégal')
			continue
		else : 
			A[ eval(a)-1 ] -= eval(b)

		afficher(A)

		coups += 1
		tour = int(not tour)

	# calcule du score
	total = sum( (n+1)*10**(n+1) for n in range(coups) )

	# mise a jour des scores
	if players[ tour ] in score :
		score[ players[tour] ] = [ min(total, score[ players[tour] ][0] ), total ]
	else :
		score[ players[tour] ] = [ total, total ]

	if players[ int(not tour) ] in score :
		score[ players[ int(not tour) ] ][1] = float('inf')
	else :
		score[ players[ int(not tour) ] ] = [ float('inf'), float('inf') ]

	S = sorted( score.items(), key = lambda x: x[1][0] )
	N = min( len(S), 10 )

	# impression des 10 best scores
	for i in range(N):
		print(S[i][0], ':', S[i][1][0] )

	# enregistrement des scores mis a jour
	file = open('score', 'wb')
	pickle.dump(score, file)
	file.close()

	# rejouer
	if input("Entrez 'oui' pour rejouer :") == 'oui' :
		Game()

Game()
