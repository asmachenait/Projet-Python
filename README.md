# Projet-Python
Ce Projet comprend le Jeux Nim Sur Python 3

         Déroulement du jeu
         -------------------
 Lancement du jeu
 .................

Ce jeu se joue à deux. On dispose d’un centain nombre de tas (entre 3 et 7) de pierres empilées avec des
hauteurs différentes. Par exemple, concidérons quatre tas de 3, 8, 7 et 11 pierres par tas. Chaque joueur, à tour
de rôle, prend le nombre de pierres qu’il veut (au moins une) dans un des tas. Le dernier joueur qui prend une
pierre a perdu. Donc, l’idée du jeu est de forcer l’adversaire à prendre la dernière pierre.

Au départ, l’ordinateur demande aux deux joueurs d’introduire leurs noms. Si l’un des deux joueurs a déjà
joué au jeu, l’ordinateur doit récupérer le score de la dernière partie jouée ainsi que le meilleur score obtenu par
le joueur depuis un fichier de sauvegarde. Dans le cas où il s’agit d’un nouveau joueur, un score et un meilleur
score de valeurs nulles lui seront attribués.
L’ordinateur doit maintenant tirer aléatoirement un chiffre entre 3 et 7 représentant le nombre de tas de
pierres. Après, il tire autant de chiffre entre 5 et 23 que de tas de pierres. Ces chiffres représentent le nombre
de pierres par tas.
L’ordinateur affiche les noms de deux joueurs ainsi que l’état du jeu i.e. les tas et les pierres sont affichés
comme suit :
Par exemple, on a 4 tas avec (5, 9, 19, 5) pierres par tas, on doit avoir comme affichage :

1| ∗ ∗ ∗ ∗ ∗                           |5
2| ∗ ∗ ∗ ∗ ∗ ∗ ∗ ∗ ∗                    |9
3| ∗ ∗ ∗ ∗ ∗ ∗ ∗ ∗ ∗ ∗ ∗ ∗ ∗ ∗ ∗ ∗ ∗ ∗ ∗  |19
4| ∗ ∗ ∗ ∗ ∗                            |5


Tour du jeu
............

L’ordinateur demande à un des deux joueurs de commencer et de joueur le premier tour.
Le joueur doit indiquer le tas et le nombre de pierres à retirer. Pour le faire, il doit entrer une chaine de
caractères de la forme "Numéro du tas" - "Nombre de pierres à retirer". Par exemple, si le joueur introduit :
3-13, cela veut dire que l’ordinateur doit retirer 13 pierres du tas numéro 3.
Aprés validation du coup l’ordinateur affiche l’état du jeu. Si on reprend l’exemple précédent, l’état du jeu
est :
1| ∗ ∗ ∗ ∗ ∗          |5
2| ∗ ∗ ∗ ∗ ∗ ∗ ∗ ∗ ∗   |9
3| ∗ ∗ ∗ ∗ ∗∗         |6
4| ∗ ∗ ∗ ∗ ∗          |5
L’ordinateur affiche le nom du joueur suivant et l’invite à jouer son coup pour continuer.

 Fin du jeu
 ...........
 
Le jeu se termine s’il ne reste qu’une pierre à retirer d’un tas. Le joueur qui doit jouer à cette étape a
perdu, et son score et nul. Pour le joueur gagnant, son score dépend du nombre de coups joués pour gagner.

Si le nouveau score obtenu est plus petit que le meilleur score obtenu par le joueur dans les parties précedentes,
la valeur du meilleur score est écrasée par la valeur du nouveau score. La valeur du score de la dernière partie
est également mise à jour. Ces informations sont enregistées localement dans un fichier text ou un fichier pickle.
L’ordinateur affiche à la fin, la liste des noms et scores des 10 meilleurs joueurs et propose une nouvelle
partie ou quitter le jeu.
