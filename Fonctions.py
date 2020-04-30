'''-------------------------------Fonction principale-----------------------------------'''
'''Elle appelle toutes les autres fonctions et simplifie donc l'utilisation de celles-ci'''

def avancement(positions, joueur, de1, de2, historique, parametres, tour, participants): #Tous les arguments sont définis dans le programme principal 

	for i in range(1): #Cette boucle permet de sauter la dernière commande selon la condition vérifiée grâce au break

		if historique[joueur] != positions[joueur]: #Les joueurs peuvent être déplacés même s'ils ne jouent pas, dans ce
													#cas on vérifie si ils ne sont pas sur une case piège
			if positions[joueur] == 52:
				positions, parametres = case_52(positions, joueur, de1, de2, historique, parametres, participants); break

			if positions[joueur] == 19:
				positions, parametres = case_19(positions, parametres, de1, de2, joueur, historique, participants)
				parametres[joueur] -= 1; break

			if positions[joueur] == 31:
				positions, parametres = case_31(positions, joueur, parametres, historique, participants); break

		if parametres[joueur] == 0:
			if positions[joueur] == 51 and de1+de2 == 8: #Un problème dans les règles fait que le joueur se déplace à
				positions[joueur] += 4 #l'infini s'il fait 8 en étant sur la case 51
			else:
				positions[joueur] += de1+de2

		'''Le joueur vient de se déplacer, maintenant on regarde s'il se trouve sur une case piège et on lui attribue 
																	les paramètres correspondant si c'est le cas'''
		if de1+de2 == 9 and tour == 0:
			positions[joueur] = des_9(positions[joueur], de1, de2); break

		if de1+de2 == 6 and parametres[joueur] == 0:
			positions = des_6(positions, joueur, historique, de1, de2, participants); break

		if positions[joueur] == 52:
			positions, parametres = case_52(positions, joueur, de1, de2, historique, parametres, participants); break

		if positions[joueur] == 19:
			positions, parametres = case_19(positions, parametres, de1, de2, joueur, historique, participants); break

		if positions[joueur] == 42:
			positions[joueur] = case_42(positions[joueur]); break

		if positions[joueur] == 31:
			positions, parametres = case_31(positions, joueur, parametres, historique, participants); break

		if positions[joueur] == 58:
			positions[joueur] = case_58(positions[joueur]); break
	
		if positions[joueur] > 63:
			positions[joueur] = 63 - positions[joueur]%63

		positions = tombe_sur_oie(positions, de1, de2, joueur, historique, parametres, participants)

	historique[joueur] = positions[joueur]

	return positions, historique, parametres

def meme_case(positions, joueur, historique, de1, de2, participants):

	for i in range(0, participants):
		if positions[joueur] == positions[i] and positions[i] != 0 and joueur != i:
			positions[i] = historique[joueur]
			break

	return positions

def tombe_sur_oie(positions, de1, de2, joueur, historique, parametres, participants):
	for i in (5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59):
		if positions[joueur] == i:
			positions[joueur] += de1+de2

	if positions[joueur] == 31:
		positions, parametres = case_31(positions, joueur, parametres, historique, participants)
	elif positions[joueur] == 52:
		positions, parametres = case_52(positions, joueur, de1, de2, historique, parametres, participants)
	elif positions[joueur] == 19:
		positions, parametres = case_19(positions, parametres, de1, de2, joueur, historique, participants)
	elif positions[joueur] == 58:
		positions[joueur] = case_58(positions[joueur])
	elif positions[joueur] > 63:
		positions[joueur] = 63 - positions[joueur]%63
	else:
		positions = meme_case(positions, joueur, historique, de1, de2, participants)

	return positions

def case_42(positions):
	positions = 30
	return positions

def case_52(positions, joueur, de1, de2, historique, parametres, participants):
	if parametres[joueur] == 0:
		parametres[joueur] = 52
	else:
		for i in range(0, participants): #On regarde à chaque tour si un joueur est tombé sur cette case
			if (positions[i] == 52) and (i != joueur):
				positions[joueur] += de1+de2
				positions = tombe_sur_oie(positions, de1, de2, joueur, historique, parametres, participants)
				parametres[joueur] = 0
				break

	return positions, parametres

def case_58(positions):
	positions = 0
	return positions

def des_9(positions, de1, de2):
	if de1 == 6 or de1 == 3:
		positions = 53
	elif de1 == 4 or de1 == 5:
		positions = 26

	return positions

def case_19(positions, parametres, de1, de2, joueur, historique, participants):
	if parametres[joueur] == 0:
		parametres[joueur] = 3
	elif parametres[joueur] == 1:
		parametres[joueur] = 0
		positions[joueur] += de1+de2
		if de1+de2 == 4 or de1+de2 == 12:
			positions[joueur] = 31
			positions, parametres = case_31(positions, joueur, parametres, historique, participants)
		else:
			positions = tombe_sur_oie(positions, de1, de2, joueur, historique, parametres, participants)
	else:
		parametres[joueur] -= 1 #Décompte du nombre de tour à passer
		
	return positions, parametres

def case_31(positions, joueur, parametres, historique, participants):
	if parametres[joueur] == 0:
		parametres[joueur] = 31
		for i in range(0, participants): #On regarde la position de chaque joueur pour voir s'il n'y avait personne sur la case
			if (positions[i] == 31) and (i != joueur):
				positions[i] = historique[joueur]
				parametres[i] = 0

	return positions, parametres

def des_6(positions, joueur, historique, de1, de2, participants):
	positions[joueur] = 12
	positions = meme_case(positions, joueur, historique, de1, de2, participants)
	return positions