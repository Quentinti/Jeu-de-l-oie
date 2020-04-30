""" ====================================================================================================================
                                                Importations des librairies
====================================================================================================================="""

try:  # Python 3.X
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import *
    from PIL import ImageTk, Image, ImageDraw
    from random import *
    from Fonctions import *
    from lang import *
    import shutil
    import os
    import contextlib

    with contextlib.redirect_stdout(None):  # Permet d'eviter le message de demarrage de pygame
        import pygame

except ImportError:  # Python 2.X
    import Tkinter as tk
    from Tkinter import *
    import Tkinter.ttk as ttk
    from PIL import ImageTk, Image, ImageDraw
    from random import *
    from Fonctions import *
    from lang import *
    import shutil
    import os
    import contextlib

    with contextlib.redirect_stdout(None):
        import pygame

''' ====================================================================================================================
                                                Fonctions hors Tkinter
====================================================================================================================='''


def init_prog():  # Fonction d'initialisation du programme
    global players, player, turn, de1, de2, action_text, action_dice, jail, end_game_, pack2_game, start_game, \
        refresh_antdarkmode, refresh_antdarkmode2, version  # On défini nos variables comme globale

    importlang_main()  # Importation du système de langue
    son_global()  # Importation du système sonore

    players = 2  # Nombre total de joueurs
    player = 1  # Joueur qui joue
    turn = 0  # Nombre de tours
    de1 = 0  # Valeur du de1
    de2 = 0  # valeur du de2
    jail = 0  # Nombre de personnes en prison ou au puits
    action_text = langc[19].split()  # Texte d'action au debut
    action_dice = False  # Permet de changer dynamiquement le contenu du texte d'action
    end_game_ = False  # Permet de savoir si c'est la fin du jeu ou non
    start_game = False  # Permet de savoir si le jeu a demarre
    pack2_game = False  # Permet de savoir si le contenu de la frame Game a change ou non
    refresh_antdarkmode = True  # Permet d'eviter le scintillement de l'image de jeu lors du passage au mode dark
    refresh_antdarkmode2 = True  # Comme precedemment, mais gere l'image du menu
    version = "2.9"  # Version du jeu

    if os.path.exists("temp"):  # Creation du dossier temporaire
        shutil.rmtree("temp")
        os.mkdir("temp")
    else:
        os.mkdir("temp")
    img = Image.open("img/plateau.jpg")  # Creation des images dans temp
    img.save("temp/plateau.gif")
    img.save("temp/plateau.jpg")
    img.close()


def importlang_main():  # Fonction qui importe les fichiers pour le systeme de langue
    global langc, lang_EN, lang_FR, lang_ES, lang_CN, lang_AF, lang_AL, lang_DE, lang_AM, lang_AR, lang_ARM, lang_AZ, lang_BA, \
        lang_BE, lang_BI, lang_BIR, lang_BO, lang_BU, lang_CA, lang_CE, lang_CH, lang_CI, lang_CO, lang_COR, lang_CR, \
        lang_CRO, lang_DA, lang_ESP, lang_EST, lang_FI, lang_FRI, lang_GA, lang_GAL, lang_GE, lang_GR, lang_GU, lang_HA, \
        lang_HAW, lang_HE, lang_HI, lang_HM, lang_HO, lang_IB, lang_IN, lang_IR, lang_IS, lang_IT, lang_JP, lang_JA, \
        lang_KA, lang_KAZ, lang_KH, lang_KI, lang_KU, lang_LA, lang_LAT, lang_LE, lang_LI, lang_LU, lang_MA, lang_MAL, \
        lang_MALA, lang_MALG, lang_MALT, lang_MAO, lang_MAR, lang_MO, lang_NE, lang_NEP, lang_NO, lang_OU, lang_PA, \
        lang_PAN, lang_PE, lang_PO, lang_POR, lang_RO, lang_RU, lang_SA, lang_SE, lang_SES, lang_SH, lang_SI, lang_SLO, \
        lang_SLOV, lang_SO, lang_SOU, lang_SUE, lang_SW, lang_TA, lang_TAG, lang_TAM, lang_TC, lang_TE, lang_TH, \
        lang_TU, lang_UR, lang_VI, lang_XH, lang_YI, lang_YO, lang_ZO

    lang_FR, lang_EN, lang_ES, lang_CN, lang_AF, lang_AL, lang_DE, lang_AM, lang_AR, lang_ARM, lang_AZ, lang_BA, \
    lang_BE, lang_BI, lang_BIR, lang_BO, lang_BU, lang_CA, lang_CE, lang_CH, lang_CI, lang_CO, lang_COR, lang_CR, \
    lang_CRO, lang_DA, lang_ESP, lang_EST, lang_FI, lang_FRI, lang_GA, lang_GAL, lang_GE, lang_GR, lang_GU, lang_HA, \
    lang_HAW, lang_HE, lang_HI, lang_HM, lang_HO, lang_IB, lang_IN, lang_IR, lang_IS, lang_IT, lang_JP, lang_JA, \
    lang_KA, lang_KAZ, lang_KH, lang_KI, lang_KU, lang_LA, lang_LAT, lang_LE, lang_LI, lang_LU, lang_MA, lang_MAL, \
    lang_MALA, lang_MALG, lang_MALT, lang_MAO, lang_MAR, lang_MO, lang_NE, lang_NEP, lang_NO, lang_OU, lang_PA, \
    lang_PAN, lang_PE, lang_PO, lang_POR, lang_RO, lang_RU, lang_SA, lang_SE, lang_SES, lang_SH, lang_SI, lang_SLO, \
    lang_SLOV, lang_SO, lang_SOU, lang_SUE, lang_SW, lang_TA, lang_TAG, lang_TAM, lang_TC, lang_TE, lang_TH, \
    lang_TU, lang_UR, lang_VI, lang_XH, lang_YI, lang_YO, lang_ZO = importlang_lang()

    langc = lang_FR  # langue choisie par defaut, langc est la variable que le programme lit,
    # on change juste cette variable par une autre variable de langue pour le changement


def choixlang_main(x):  # Fonction qui change la langue du programme depuis le ComboBox de la frame Optn
    global langc, action_text

    langc = choixlang_lang(x, lang_EN, lang_FR, lang_ES, lang_CN, lang_AF, lang_AL, lang_DE, lang_AM, lang_AR, lang_ARM,
                           lang_AZ, lang_BE, lang_BI, lang_BIR, lang_BO, lang_BU, lang_CA, lang_CE, lang_CH, lang_CI,
                           lang_CO, lang_COR,
                           lang_CR, lang_CRO, lang_DA, lang_ESP, lang_EST, lang_FI, lang_FRI, lang_GA, lang_GAL,
                           lang_GE,
                           lang_GR, lang_GU,
                           lang_HA, lang_HAW, lang_HE, lang_HI, lang_HM, lang_HO, lang_IB, lang_IN, lang_IR, lang_IS,
                           lang_IT, lang_JP,
                           lang_JA, lang_KA, lang_KAZ, lang_KH, lang_KI, lang_KU, lang_LA, lang_LAT, lang_LE, lang_LI,
                           lang_LU, lang_MA,
                           lang_MAL, lang_MALA, lang_MALG, lang_MALT, lang_MAO, lang_MAR, lang_MO, lang_NE, lang_NEP,
                           lang_NO, lang_OU,
                           lang_PA, lang_PAN, lang_PE, lang_PO, lang_POR, lang_RO, lang_RU, lang_SA, lang_SE, lang_SES,
                           lang_SH, lang_SI,
                           lang_SLO, lang_SLOV, lang_SO, lang_SOU, lang_SUE, lang_SW, lang_TA, lang_TAG, lang_TAM,
                           lang_TC,
                           lang_TE,
                           lang_TH, lang_TU, lang_UR, lang_VI, lang_XH, lang_YI, lang_YO, lang_ZO, lang_BA)

    action_text = langc[19].split()


def son_global():  # Fonction qui met en place le son au demarrage
    global son_active, son_bruitageo, son_music, son_diceo, son_piono
    son_active = True  # Variable qui permet de savoir si le son est actif pour la case "son" dans les options
    pygame.mixer.init(44100, -16, 2, 2048)
    son_bruitageo = pygame.mixer.Sound("sound/bruitage.wav")
    son_diceo = pygame.mixer.Sound("sound/dice.wav")
    son_music = pygame.mixer.Sound("sound/music.wav")
    son_piono = pygame.mixer.Sound("sound/pion.wav")
    son_music.play(loops=-1, fade_ms=1000)


def son_bruitage():  # Fonction qui genere un bruit a chaque clic sur une frame
    if son_active:
        son_bruitageo.play()


def son_dice():  # Fonction qui genere un bruit de des a chaque lancement des des
    if son_active:
        son_diceo.play()


def son_pion():  # Fonction qui genere un bruit de pion a chaque deplacement des pions
    if son_active:
        son_piono.play()


def draw_call():  # Fonction qui sera appellee pour le deplacement des pions sur le plateau
    global player, case, jail, historic, settings, turn
    son_pion()
    img = Image.open("img/plateau.jpg")
    draw = ImageDraw.Draw(img)
    jail = 0
    # Ici on appelle la fonction "avancement" du programme "Fonctions.py"
    case, historic, settings = avancement(case, player - 1, de1, de2, historic, settings, turn, players)
    if player == players:  # On verifie si on doit commencer un nouveau tour ou non
        player = 1
        turn += 1
    else:
        player += 1

    draw_pion(draw, case)  # On appelle la fonction qui va faire les dessins sur le plateau
    img.save("temp/plateau.gif")
    img.close()

    for i in range(0, players):  # On verifie si le jeu est termine ou non
        if case[i] == 63:
            end_game()

    for i in range(0, players):  # On verifie si un joueur est dans le puits/prison
        if settings[i] == 52 or settings[i] == 31:
            jail += 1


def dice():  # Fonction qui sera appelee pour le lancement des des
    global de1, de2
    de1 = randint(1, 6)
    de2 = randint(1, 6)
    son_dice()


def draw_pion(draw,
              case):  # Fonction qui va faire les dessins sur le plateau avec le numéro et la couleur de chaque pion

    # Liste des coordonnees des differentes cases

    coord_x = [100, 235, 285, 337, 390, 447, 508, 567, 615, 680, 725, 760, 783, 796, 800, 796, 772, 742, 700, 630, 555,
               500, 450, 390, 335, 285, 230, 175, 135, 100, 80, 65, 63, 85, 110, 145, 187, 235, 285, 338, 393, 448, 510,
               567, 615, 667, 700, 712, 712, 700, 667, 605, 535, 455, 390, 332, 280, 230, 170, 150, 170, 200, 240, 405]

    coord_y = [540, 540, 540, 540, 540, 540, 540, 540, 530, 505, 465, 425, 380, 330, 275, 215, 165, 120, 80, 35, 35, 35,
               35, 35, 35, 38, 40, 55, 85, 124, 170, 225, 280, 325, 370, 405, 440, 450, 450, 450, 450, 450, 450, 450,
               435, 410, 355, 305, 260, 215, 170, 130, 125, 125, 125, 125, 125, 130, 170, 250, 305, 340, 350, 235]

    # Couleurs des pions
    colors = ['#0000ff', '#ff0000', '#83fa04', '#ff9900', '#ff00ff', '#04fad9']

    for i in range(0, len(case)):  # Boucle qui dessine toute l'image
        player_ = i + 1
        player_ = str(player_)
        draw.ellipse((coord_x[case[i]], coord_y[case[i]], coord_x[case[i]] + 30,
                      coord_y[case[i]] + 30), fill=colors[i], outline=colors[i])
        draw.text((coord_x[case[i]] + 15, coord_y[case[i]] + 10), player_, fill="black")


def first_draw():  # Fonction qui dessine tous les pions sur la case "0" au demarrage, elle fonctionne comme "draw_pion"
    global players, start_game
    son_bruitage()
    start_game = True
    img = Image.open("img/plateau.jpg")
    img.save("temp/plateau.jpg")
    img.close()

    if players == 2:  # On regarde le nombre de joueurs pour attribuer les coordonnees des pions
        coord_x = [50, 100]
        coord_y = [540, 540]
        n = 2
    elif players == 3:
        coord_x = [75, 50, 100]
        coord_y = [500, 540, 540]
        n = 3
    elif players == 4:
        coord_x = [145, 75, 50, 100]
        coord_y = [540, 500, 540, 540]
        n = 4
    elif players == 5:
        coord_x = [130, 145, 75, 50, 100]
        coord_y = [500, 540, 500, 540, 540]
        n = 5
    elif players == 6:
        coord_x = [30, 130, 145, 75, 50, 100]
        coord_y = [500, 500, 540, 500, 540, 540]
        n = 6

    colors = ['#0000ff', '#ff0000', '#83fa04', '#ff9900', '#ff00ff', '#04fad9']

    for i in range(0, n):
        img = Image.open("temp/plateau.jpg")  # On doit passer par une image en .jpg sinon l'image se corrompt
        draw = ImageDraw.Draw(img)
        player_ = i + 1
        player_ = str(player_)
        draw.ellipse((coord_x[i], coord_y[i], coord_x[i] + 30, coord_y[i] + 30), fill=colors[i], outline=colors[i])
        draw.text((coord_x[i] + 15, coord_y[i] + 10), player_, fill="black")
        img.save("temp/plateau.jpg")
        img.close()
    img = Image.open("temp/plateau.jpg")
    img.save("temp/plateau.gif")
    img.close()


def action():  # Fonction qui va soit lancer les des ou faire le deplacement des pions
    global action_text, action_dice
    if action_dice is False:
        dice()
        action_text = langc[18].split()  # On change dynamiquement le contenu du texte du bouton
        action_dice = True
    else:
        draw_call()
        action_text = langc[19].split()
        action_dice = False


def end_game():  # Fonction qui s'execute quand le jeu est termine
    global end_game_, case_rank, players_rank

    # Mise en place du système de classement
    case_rank = [0] * players  # Case des joueurs
    players_rank = [0] * players  # Numero des joueurs
    end_game_ = True
    for i in range(0, players):
        case_rank[i] = case[i]
        players_rank[i] = i + 1

    permut = True
    passe = 0

    while permut is True:  # Systeme de tri par bulle
        permut = False
        passe = passe + 1
        for i in range(0, len(case_rank) - passe):
            if case_rank[i] < case_rank[i + 1]:
                permut = True
                case_rank[i], case_rank[i + 1] = \
                    case_rank[i + 1], case_rank[i]
                players_rank[i], players_rank[i + 1] = \
                    players_rank[i + 1], players_rank[i]


def destroy_():  # Permet de quitter le programme
    root.destroy()


init_prog()  # Initialisation du programme
color = "white"  # Mode blanc par defaut

''' ====================================================================================================================
                                                Application principale
====================================================================================================================='''


class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)  # On cree notre frame principale qui sera dans la fenetre
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Loading, Menu, Optn, Credits, Game, Help):  # Creation des differentes frames
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Loading")  # Frame par defaut au demarrage du programme

    def show_frame(self, page_name):  # Mise en place de la fonction de changement de frame
        frame = self.frames[page_name]
        frame.tkraise()
        son_bruitage()


''' ====================================================================================================================
                                                Frame du menu
====================================================================================================================='''


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        # On initialise notre code, les definitions doivent etre de preference dans le __init__

        tk.Frame.__init__(self, parent, background=color)
        self.controller = controller

        self.text = tk.Label(self)  # Un label est un texte
        self.image = tk.PhotoImage(file="img/menu.gif")
        self.imageo = tk.Label(self, image=self.image)  # On met une image dans un Label
        # Boutons qui permettent le changement de frame
        self.button_play = tk.Button(self, fg="green", command=lambda: self.controller.show_frame("Game"))  
        self.button_option = tk.Button(self, fg="blue", command=lambda: self.controller.show_frame("Optn"))
        self.button_quit = tk.Button(self, fg="red", command=lambda: destroy_())

        self.pack()  # On pack nos widgets
        self.update_frame()  # On lance la boucle d'actualisation

    def pack(self):
        self.text.pack(side="top", fill='both', expand=True, padx=4, pady=4)
        self.imageo.pack(side="top", expand=True, padx=4, pady=4)
        self.button_play.pack(side="left", fill="both", expand=True, padx=4, pady=4)
        self.button_option.pack(side="right", fill="both", expand=True, padx=4, pady=4)
        self.button_quit.pack(side="bottom", fill="both", expand=True, padx=4, pady=4)

    def update_frame(self):  # Doit avoir un nom different de "update" car le tkinter.update sera re-ecrit
        global refresh_antdarkmode2

        # Le .configure permet de changer les parametres d'un widget, de plus le "% variable" permet de remplacer un
        # %s dans un fichier langue par une varialbe

        self.text.configure(text=langc[1].strip() % version, bg=color)
        self.button_play.configure(text=langc[2].strip(), bg=color)
        self.button_option.configure(text=langc[3].strip(), bg=color)
        self.button_quit.configure(text=langc[4].strip(), bg=color)
        self.configure(bg=color)
        if refresh_antdarkmode2 is False:  # Evite le scintillement
            self.configure(bg=color)
            self.imageo.configure(bg=color)
            refresh_antdarkmode2 = True
        self.after(1000, self.update_frame)  # On relance apres 1000ms la fonction


'''=====================================================================================================================
                                                Frame des options
====================================================================================================================='''


class Optn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=color)
        self.controller = controller

        self.button_return = tk.Button(self, fg="green", command=lambda: self.controller.show_frame("Menu"), )
        self.button_credits = tk.Button(self, fg="purple", command=lambda: self.controller.show_frame("Credits"))
        self.button_help = Button(self, fg="red", command=lambda: self.controller.show_frame("Help"))
        self.button_son_var = StringVar()
        # Dans notre checkbutton on envois avec le lambda un parametre a la fonction control_son
        self.button_son = tk.Checkbutton(self, variable=self.button_son_var,
                                         command=lambda: self.control_son(self.button_son_var.get()), onvalue='Oui')
        self.button_darkmode_var = StringVar()
        self.button_darkmode = tk.Checkbutton(self, variable=self.button_darkmode_var,
                                              command=lambda: self.control_darkmode(self.button_darkmode_var.get()),
                                              onvalue='Oui')
        self.curseur_sonm_var = IntVar()
        self.curseur_sonb_var = IntVar()
        self.curseur_sonm = tk.Scale(self, variable=self.curseur_sonm_var, from_=0, to=100, orient='horizontal',
                                     length=400, tickinterval=10,
                                     command=lambda x: self.volume_sonm(self.curseur_sonm_var.get()))
        self.curseur_sonb = tk.Scale(self, variable=self.curseur_sonb_var, from_=0, to=100, orient='horizontal',
                                     length=400, tickinterval=10,
                                     command=lambda x: self.volume_sonb(self.curseur_sonb_var.get()))
        self.curseur_sonm.set(100)
        self.curseur_sonb.set(100)
        self.lang_text = tk.Label(self)
        self.lang_list = ttk.Combobox(self, values=["Francais", "English", "Espanol", "柑", "Afrikaans", "shqiptar",
                                                    "አማርኛ", "العربية", "հայերեն", "Azərbaycan", "Euskal", "বাঙালি",
                                                    "беларускі", "မြန်မာ", "bosanski", "български", "Català", "Cebuano",
                                                    "Chichewa", "සිංහලයන්", "한국의", "Corsica", "Kreyòl Ayisyen",
                                                    "hrvatski", "dansk", "Deutsch", "Esperanto", "eesti",
                                                    "suomalainen", "Frysk", "Gàidhlig", "Cymraeg", "ქართული",
                                                    "ελληνικά", "ગુજરાતી", "Hausa", "Hawaiian", "עברי ", "हिन्दी",
                                                    "hmong", "magyar", "igbo", "Indonesia", "Gaeilge", "Íslendingur",
                                                    "Italiano", "Jawa", "日本の", "ಕನ್ನಡ", "Қазақ", "ខ្មែរ", "Kirghiz",
                                                    "Kurdî", "ລາວ", "Latine", "Latvijas", "Lietuvos", "Lëtzebuerg",
                                                    "Македонски", "Malaysia", "മലയാളം", "Malagasy", "Malti", "Maori",
                                                    "मराठी", "Монгол", "Nederlands", "नेपाली", "norsk", "O zbekiston",
                                                    "پښتو", "ਪੰਜਾਬੀ", "فارسی", "Polski", "Português", "Românesc",
                                                    "русский", "Samoa", "српски", "Sesotho", "Shona", "سنڌي",
                                                    "Slovenský", "slovenski", "Soomaali", "Sunda", "Sudans",
                                                    "Swahili", "Тоҷикистон", "tagalog", "தமிழ்", "český",
                                                    "telugu", "ไทย", "Türk", "اردو", "tiếng Việt",
                                                    "isiXhosa", "ייִדיש", "Yoruba", "Zulu"])
        # Comme pour le widget checkbutton, sauf qu'il faut mettre "lambda e:" sinon ca ne fonctionne pas
        self.lang_list.bind('<<ComboboxSelected>>', lambda e: choixlang_main(self.lang_list.get()))

        self.pack()
        self.update_frame()

    def control_son(self, x):  # Cette fonction permet le controle du widget son
        global son_active
        if x == "Oui":
            pygame.mixer.unpause()  # On enleve la pause du systeme sonore de pygame
            son_active = True
            self.curseur_sonm.configure(state="active")  # On re-active les curseurs sonores
            self.curseur_sonb.configure(state="active")
        else:
            pygame.mixer.pause()  # On met sur pause le systeme sonore de pygame
            son_active = False
            self.curseur_sonm.configure(state="disable")  # On desactive les curseurs sonores
            self.curseur_sonb.configure(state="disable")

    def control_darkmode(self, x):  # Cette fonction permet le controle du mode dark
        global color, refresh_antdarkmode, refresh_antdarkmode2
        if x == "Oui":
            color = "grey"
            refresh_antdarkmode = False
            refresh_antdarkmode2 = False
        else:
            color = "white"
            refresh_antdarkmode = False
            refresh_antdarkmode2 = False

    def volume_sonm(self, x):  # Cette fonction permet de regler le volume sonore
        global son_music
        y = x / 100
        son_music.set_volume(y)

    def volume_sonb(self, x):  # Cette fonction permet de regler le volume sonore
        global son_bruitageo, son_diceo, son_piono
        y = x / 100
        son_bruitageo.set_volume(y)
        son_diceo.set_volume(y)
        son_piono.set_volume(y)

    def pack(self):
        self.button_return.pack(side="top", padx=4, pady=4)
        self.button_credits.pack(side="top", padx=4, pady=4)
        self.button_help.pack(side="top", padx=4, pady=4)
        self.curseur_sonm.pack(side="bottom", padx=4, pady=4)
        self.curseur_sonb.pack(side="bottom", padx=4, pady=4)
        self.button_son.pack(side="bottom", padx=4, pady=4)
        self.button_darkmode.pack(side="bottom", padx=4, pady=4)
        self.lang_list.pack(side="bottom")
        self.lang_text.pack(side="bottom")

    def update_frame(self):  # Doit avoir un nom different de "update" car sinon ca remplace le update de tkinter
        self.button_return.configure(text=langc[5].strip(), bg=color)
        self.button_credits.configure(text=langc[6].strip(), bg=color)
        self.button_help.configure(text=langc[20].strip(), bg=color)
        self.button_son.configure(text=langc[8].strip(), bg=color)
        self.button_darkmode.configure(text=langc[21].strip(), bg=color)
        self.lang_text.configure(text=langc[9].strip(), bg=color)
        self.curseur_sonm.configure(label=langc[10].strip(), bg=color)
        self.curseur_sonb.configure(label=langc[11].strip(), bg=color)
        self.configure(bg=color)
        self.after(1000, self.update_frame)


''' ====================================================================================================================
                                                Frame des credits
====================================================================================================================='''


class Credits(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=color)
        self.controller = controller

        self.button_return = tk.Button(self, fg="green", command=lambda: self.controller.show_frame("Menu"), )
        self.button_optn = tk.Button(self, fg="purple", command=lambda: self.controller.show_frame("Optn"))
        self.text = tk.Label(self, font="bold")
        self.text_1 = tk.Label(self, font="bold")
        self.text_2 = tk.Label(self, font="bold")
        self.text_3 = tk.Label(self, font="bold")

        self.pack()
        self.update_frame()

    def pack(self):
        self.button_return.pack(side="top", padx=4, pady=4)
        self.button_optn.pack(side="top", padx=4, pady=4)
        self.text.pack(side="top", padx=4, pady=4)
        self.text_1.pack(side="top", padx=4, pady=4)
        self.text_2.pack(side="top", padx=4, pady=4)
        self.text_3.pack(side="top", padx=4, pady=4)

    def update_frame(self):
        self.button_return.configure(text=langc[5].strip(), bg=color)
        self.button_optn.configure(text=langc[7].strip(), bg=color)
        self.text.configure(text=langc[38].strip(), bg=color)
        self.text_1.configure(text=langc[39].strip(), bg=color)
        self.text_2.configure(text=langc[40].strip(), bg=color)
        self.text_3.configure(text=langc[41].strip(), bg=color)
        self.configure(bg=color)
        self.after(1000, self.update_frame)


''' ====================================================================================================================
                                                Frame du jeu
====================================================================================================================='''


class Game(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=color)
        self.controller = controller

        # Contenu premiere fenetre

        self.spint_cplayers = tk.Label(self)
        self.spin_cplayersvar = StringVar()
        self.spin_cplayersvar.set(2)  # Cette variable definit par defaut a 2 le nombre de joueurs
        self.spin_cplayers = tk.Spinbox(self, from_=2, to=6, increment=1, textvariable=self.spin_cplayersvar,
                                        command=lambda: self.choixnb_players(self.spin_cplayersvar.get()))

        self.button_play = tk.Button(self, fg="red", command=lambda: self.change_contenu())
        self.button_return1 = tk.Button(self, fg="green", command=lambda: self.controller.show_frame("Menu"))

        # Contenu deuxieme fenetre + Troisieme

        self.img = Frame(self, bg=color, width=900, height=600)  # Creation des frames pour la frame jeu
        self.button = Frame(self, bg=color, width=300, height=100, padx=10, pady=10)
        self.button_main = Frame(self, bg=color, width=300, height=100, padx=10, pady=10)
        self.text = Frame(self, bg=color, padx=10, pady=10)
        self.rank = Frame(self, bg=color, padx=10, pady=10)

        self.image = tk.PhotoImage()
        self.imageo = Label(self.img, image=self.image, bg=color)  # Plutot que de mettre l'image dans la frame "Game"
        # on la met dans la frame "img" de la frame "game", permet de tout compartimenter

        self.button_action = Button(self.button, command=lambda: action())

        self.dicetext = Label(self.text)
        self.turntext = Label(self.text)
        self.playertext = Label(self.text)
        self.prison_puitstext = Label(self.text)

        self.button_return2 = tk.Button(self.button_main, fg="green",
                                        command=lambda: self.controller.show_frame("Menu"))
        self.button_option = Button(self.button_main, fg="blue", command=lambda: self.controller.show_frame("Optn"))
        self.button_help = Button(self.button_main, fg="red", command=lambda: self.controller.show_frame("Help"))
        self.button_quit = Button(self.rank, fg="red", command=lambda: destroy_())
        self.rank_text = Label(self.rank)
        ###############################################################################################################
        self.pack_1()
        self.update_frame()

    def choixnb_players(self, x):  # Fonction qui affecte le nombre de joueurs
        global players
        x = int(x)
        players = x

    def change_contenu(
            self):  # Fonction qui permet de changer le contenu du jeu apres la selection du nombre de joueurs
        global players, case, historic, settings, pack2_game
        self.button_return1.destroy()
        self.spin_cplayers.destroy()
        self.spint_cplayers.destroy()
        self.button_play.destroy()
        case = [0] * players  # Ici on definit nos variables pour le jeu en fonction du nombre de joueurs
        historic = [0] * players
        settings = [0] * players
        pack2_game = True
        self.pack_2()
        first_draw()

    def pack_1(self):  # Premier contenu de la frame game
        self.spint_cplayers.pack(side="top")
        self.spin_cplayers.pack(side="top")
        self.button_return1.pack(side="bottom", fill="both", padx=4, pady=4)
        self.button_play.pack(side="top", padx=4, pady=4)

    def pack_2(self):  # Deuxieme contenu de la frame game
        self.img.pack(side="top")
        self.button_main.pack(side="right", fill="both")
        self.button.pack(side="left")
        self.text.pack(side="bottom")

        self.imageo.pack(side="top", padx=4, pady=4)
        self.button_action.pack(fill="both", padx=4, pady=4)
        self.turntext.pack(side="top", padx=4, pady=4)
        self.dicetext.pack(side="bottom", padx=4, pady=4)
        self.playertext.pack(padx=4, pady=4)
        self.prison_puitstext.pack(side="bottom", padx=4, pady=4)
        self.button_return2.pack(side="top", fill="both", padx=4, pady=4)
        self.button_help.pack(fill="both", padx=4, pady=25)
        self.button_option.pack(side="bottom", fill="both", padx=4, pady=4)

    def ranking(self):  # Trosieme contenu de la frame game, qui contient lui le classement des joueurs
        global players_rank, case_rank

        self.imageo.destroy()
        self.button_action.destroy()
        self.turntext.destroy()
        self.dicetext.destroy()
        self.playertext.destroy()
        self.prison_puitstext.destroy()
        self.button_return2.destroy()
        self.button_help.destroy()
        self.button_option.destroy()

        self.button.destroy()
        self.button_main.destroy()
        self.img.destroy()
        self.text.destroy()

        self.rank.pack()
        self.rank_text.pack(side="top", padx=4, pady=10)
        self.button_quit.pack(side="bottom", padx=4, pady=10)

        for i in range(0, players):  # Creations en fonction du nombre de joueurs du classement
            self.ranking_ = Label(self.rank, text=langc[42].strip() % (players_rank[i], i + 1, case_rank[i]), bg=color)
            self.ranking_.pack(padx=4, pady=4)

    def update_frame(self):
        global de1, de2, turn, player, players, jail, end_game_, pack2_game, refresh_antdarkmode
        de1_de2 = de1 + de2
        if end_game_ is True:
            self.ranking()
            self.rank_text.configure(text=langc[43].strip(), bg=color)
        else:
            if pack2_game is False:
                self.spint_cplayers.configure(text=langc[12].strip(), bg=color)
                self.button_play.configure(text=langc[15].strip(), bg=color)
                self.button_return1.configure(text=langc[5].strip(), bg=color)
            self.button_return2.configure(text=langc[5].strip(), bg=color)
            self.button_quit.configure(text=langc[4].strip(), bg=color)
            self.button_help.configure(text=langc[20].strip(), bg=color)
            self.button_option.configure(text=langc[3].strip(), bg=color)
            self.image.configure(file="temp/plateau.gif")
            self.imageo.configure(image=self.image)
            self.dicetext.configure(text=langc[13].strip() % (de1, de2, de1_de2), bg=color)
            self.turntext.configure(text=langc[14].strip() % turn, bg=color)
            self.playertext.configure(text=langc[16].strip() % (player, players), bg=color)
            self.prison_puitstext.configure(text=langc[17].strip() % jail, bg=color)
            self.button_action.configure(text=action_text, bg=color)
            if refresh_antdarkmode is False:
                self.img.configure(bg=color)
                self.text.configure(bg=color)
                self.configure(bg=color)
                self.rank.configure(bg=color)
                self.button.configure(bg=color)
                self.button_main.configure(bg=color)
                self.imageo.configure(bg=color)
                refresh_antdarkmode = True
            self.after(1000, self.update_frame)


'''=====================================================================================================================
                                                Frame de l'aide 
====================================================================================================================='''


class Help(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=color)
        self.controller = controller

        # On doit creer les labels un a un car si on utilise le systeme comme pour le classement (avec une boucle
        # for), sinon on ne peut pas prendre en compte le changement de langue
        self.help1 = Label(self, font="bold")
        self.help2 = Label(self)
        self.help3 = Label(self)
        self.help4 = Label(self)
        self.help5 = Label(self)
        self.help6 = Label(self)
        self.help7 = Label(self)
        self.help8 = Label(self)
        self.help9 = Label(self)
        self.help10 = Label(self)
        self.help11 = Label(self)
        self.help12 = Label(self)
        self.help13 = Label(self)
        self.help14 = Label(self, font="bold")
        self.help15 = Label(self)
        self.help16 = Label(self)
        self.button_return = tk.Button(self, fg="green", command=lambda: self.controller.show_frame("Menu"))
        self.button_optn = tk.Button(self, fg="purple", command=lambda: self.controller.show_frame("Optn"))
        self.pack()
        self.update_frame()

    def pack(self):
        self.help1.pack(padx=4, pady=40)
        self.help2.pack(padx=4, pady=4)
        self.help3.pack(padx=4, pady=4)
        self.help4.pack(padx=4, pady=4)
        self.help5.pack(padx=4, pady=4)
        self.help6.pack(padx=4, pady=4)
        self.help7.pack(padx=4, pady=4)
        self.help8.pack(padx=4, pady=4)
        self.help9.pack(padx=4, pady=4)
        self.help10.pack(padx=4, pady=4)
        self.help11.pack(padx=4, pady=4)
        self.help12.pack(padx=4, pady=4)
        self.help13.pack(padx=4, pady=4)
        self.help14.pack(padx=4, pady=40)
        self.help15.pack(padx=4, pady=4)
        self.help16.pack(padx=4, pady=4)
        self.button_return.pack(side="bottom", padx=4, pady=4)
        self.button_optn.pack(side="bottom", padx=4, pady=4)

    def update_frame(self):
        self.help1.configure(text=langc[22].strip(), bg=color)
        self.help2.configure(text=langc[23].strip(), bg=color)
        self.help3.configure(text=langc[24].strip(), bg=color)
        self.help4.configure(text=langc[25].strip(), bg=color)
        self.help5.configure(text=langc[26].strip(), bg=color)
        self.help6.configure(text=langc[27].strip(), bg=color)
        self.help7.configure(text=langc[28].strip(), bg=color)
        self.help8.configure(text=langc[29].strip(), bg=color)
        self.help9.configure(text=langc[30].strip(), bg=color)
        self.help10.configure(text=langc[31].strip(), bg=color)
        self.help11.configure(text=langc[32].strip(), bg=color)
        self.help12.configure(text=langc[33].strip(), bg=color)
        self.help13.configure(text=langc[34].strip(), bg=color)
        self.help14.configure(text=langc[35].strip(), bg=color)
        self.help15.configure(text=langc[36].strip(), bg=color)
        self.help16.configure(text=langc[37].strip(), bg=color)
        self.button_return.configure(text=langc[5].strip(), bg=color)
        self.button_optn.configure(text=langc[7].strip(), bg=color)
        self.configure(bg=color)
        self.after(1000, self.update_frame)


'''=====================================================================================================================
                                                Frame de chargement
====================================================================================================================='''


class Loading(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=color)
        self.controller = controller
        self.loading = GifAnimatedLabel(self, filename="img/loading.gif", speed=100)
        self.loading_text = Label(self, text="Ponte des oeufs et couvaison...", bg=color)
        self.progressvar = 0
        self.progress = ttk.Progressbar(self, mode="determinate", length=500)  # On met en place un widget progressbar
        self.pack()

    def progress_1(self):  # Fonction qui change dynamiquement le texte de la barre de chargement et fait le chargement
        self.time = randint(0, 100)
        if self.progressvar == 100:
            self.controller.show_frame("Menu")
        elif self.progressvar == 25:
            self.loading_text.configure(text="Engraissement des oies...")
        elif self.progressvar == 50:
            self.loading_text.configure(text="Abattage des oies...")
        elif self.progressvar == 75:
            self.loading_text.configure(text="Cuisson des oies...")

        self.progressvar += 1
        self.progress.configure(value=self.progressvar)
        self.after(self.time, self.progress_1)

    def pack(self):
        self.loading.pack(side="top", padx=4, pady=4)
        self.progress.pack(side="top", padx=4, pady=30)
        self.loading_text.pack(side="bottom", padx=4, pady=30)
        self.progress_1()


class GifAnimatedLabel(tk.Label):  # Pour l'animation du gif au chargement, code pris sur internet par manque de temps
    def __init__(self, master, filename, speed, *args, **kwargs):
        self.speed = speed  # On definit le temps de l'animation
        self.frames = []
        i = 0
        while True:  # On fragmente le gif en image
            try:
                p = tk.PhotoImage(file=filename, format="gif - {}".format(i))
            except tk.TclError:
                break
            self.frames.append(p)
            i += 1

        super().__init__(master, image=self.frames[0], *args, **kwargs)
        self.frame_idx = 0
        self.num_frames = i
        self.after(self.speed, self._animate)

    def _animate(self):
        global start_game
        if start_game is True:  # On arrete l'animation apres le lancement du jeu
            pass
        else:
            self.frame_idx = (self.frame_idx + 1) % self.num_frames  # On anime image par image pour faire une animation
            self['image'] = self.frames[self.frame_idx]
            self.after(self.speed, self._animate)


''' ====================================================================================================================
                                                Initialisation de la fenetre
====================================================================================================================='''

if __name__ == "__main__":
    root = MainApp()  # Notre fenetre est le contenu de la class MainApp
    root.title(langc[0].strip())  # Titre de notre fenetre
    root.resizable(width=False, height=False)
    root.configure(bg=color)
    try:  # Windows
        root.iconbitmap("img/favicon.ico")
    except:  # Gnome ou Windows
        root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='img/favicon.gif'))
    root.mainloop()

shutil.rmtree("temp")  # Destruction du dossier temp a la fin de l'execution du code
