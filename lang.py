""" ====================================================================================================================
                                                Script gerant les langues, permet d'eviter d'avoir
                                                        ce code dans le programme prncipal
====================================================================================================================="""

def importlang_lang():  # Fonction qui importe les fichiers pour le systeme de langue

    # Attribution puis ouverture des fichiers textes de langue

    FR = open("lang/FR.txt", encoding='UTF-8')  # Francais
    EN = open("lang/EN.txt", encoding='UTF-8')  # Anglais
    ES = open("lang/ES.txt", encoding='UTF-8')  # Espagnol
    CN = open("lang/CN.txt", encoding='UTF-8')  # Mandarin
    AF = open("lang/AF.txt", encoding='UTF-8')  # Afrikaans
    AL = open("lang/AL.txt", encoding='UTF-8')  # Albanais
    DE = open("lang/DE.txt", encoding='UTF-8')  # Allemand
    AM = open("lang/AM.txt", encoding='UTF-8')  # Amharique
    AR = open("lang/AR.txt", encoding='UTF-8')  # Arabe
    ARM = open("lang/ARM.txt", encoding='UTF-8')  # Armenien
    AZ = open("lang/AZ.txt", encoding='UTF-8')  # Azeri
    BA = open("lang/BA.txt", encoding='UTF-8')  # Basque
    BE = open("lang/BE.txt", encoding='UTF-8')  # Bengali
    BI = open("lang/BI.txt", encoding='UTF-8')  # Bielorusse
    BIR = open("lang/BIR.txt", encoding='UTF-8')  # Birman
    BO = open("lang/BO.txt", encoding='UTF-8')  # Bosniaque
    BU = open("lang/BU.txt", encoding='UTF-8')  # Bulgare
    CA = open("lang/CA.txt", encoding='UTF-8')  # Catalan
    CE = open("lang/CE.txt", encoding='UTF-8')  # Cebuano
    CH = open("lang/CH.txt", encoding='UTF-8')  # Chichewa
    CI = open("lang/CI.txt", encoding='UTF-8')  # Cingalais
    CO = open("lang/CO.txt", encoding='UTF-8')  # Coreeen
    COR = open("lang/COR.txt", encoding='UTF-8')  # Corse
    CR = open("lang/CR.txt", encoding='UTF-8')  # Creole haitien
    CRO = open("lang/CRO.txt", encoding='UTF-8')  # Croate
    DA = open("lang/DA.txt", encoding='UTF-8')  # Danois
    ESP = open("lang/ESP.txt", encoding='UTF-8')  # Esperanto
    EST = open("lang/EST.txt", encoding='UTF-8')  # Estonien
    FI = open("lang/FI.txt", encoding='UTF-8')  # Finnois
    FRI = open("lang/FRI.txt", encoding='UTF-8')  # Frison
    GA = open("lang/GA.txt", encoding='UTF-8')  # Gaelique
    GAL = open("lang/GAL.txt", encoding='UTF-8')  # Gallois
    GE = open("lang/GE.txt", encoding='UTF-8')  # Geogien
    GR = open("lang/GR.txt", encoding='UTF-8')  # Grec
    GU = open("lang/GU.txt", encoding='UTF-8')  # Gujarati
    HA = open("lang/HA.txt", encoding='UTF-8')  # Haoussa
    HAW = open("lang/HAW.txt", encoding='UTF-8')  # Hawaien
    HE = open("lang/HE.txt", encoding='UTF-8')  # Hebreu
    HI = open("lang/HI.txt", encoding='UTF-8')  # Hindi
    HM = open("lang/HM.txt", encoding='UTF-8')  # Hmong
    HO = open("lang/HO.txt", encoding='UTF-8')  # Hongrois
    IB = open("lang/IB.txt", encoding='UTF-8')  # Igbo
    IN = open("lang/IN.txt", encoding='UTF-8')  # Indonesien
    IR = open("lang/IR.txt", encoding='UTF-8')  # Irlandais
    IS = open("lang/IS.txt", encoding='UTF-8')  # Islandais
    IT = open("lang/IT.txt", encoding='UTF-8')  # Italien
    JP = open("lang/JP.txt", encoding='UTF-8')  # Japonais
    JA = open("lang/JA.txt", encoding='UTF-8')  # Javanais
    KA = open("lang/KA.txt", encoding='UTF-8')  # Kannada
    KAZ = open("lang/KAZ.txt", encoding='UTF-8')  # Kazakh
    KH = open("lang/KH.txt", encoding='UTF-8')  # Khmer
    KI = open("lang/KI.txt", encoding='UTF-8')  # Kirghiz
    KU = open("lang/KU.txt", encoding='UTF-8')  # Kurde
    LA = open("lang/LA.txt", encoding='UTF-8')  # Laotien
    LAT = open("lang/LAT.txt", encoding='UTF-8')  # Latin
    LE = open("lang/LE.txt", encoding='UTF-8')  # Letton
    LI = open("lang/LI.txt", encoding='UTF-8')  # Lituanien
    LU = open("lang/LU.txt", encoding='UTF-8')  # Luxembourgeois
    MA = open("lang/MA.txt", encoding='UTF-8')  # Macedonien
    MAL = open("lang/MAL.txt", encoding='UTF-8')  # Malaisien
    MALA = open("lang/MALA.txt", encoding='UTF-8')  # Malayalam
    MALG = open("lang/MALG.txt", encoding='UTF-8')  # Malgache
    MALT = open("lang/MALT.txt", encoding='UTF-8')  # Maltais
    MAO = open("lang/MAO.txt", encoding='UTF-8')  # Maori
    MAR = open("lang/MAR.txt", encoding='UTF-8')  # Marathi
    MO = open("lang/MO.txt", encoding='UTF-8')  # Mongol
    NE = open("lang/NE.txt", encoding='UTF-8')  # Neerlandais
    NEP = open("lang/NEP.txt", encoding='UTF-8')  # Nepalais
    NO = open("lang/NO.txt", encoding='UTF-8')  # Norvegien
    OU = open("lang/OU.txt", encoding='UTF-8')  # Ouzbek
    PA = open("lang/PA.txt", encoding='UTF-8')  # Pachto
    PAN = open("lang/PAN.txt", encoding='UTF-8')  # Panjabi
    PE = open("lang/PE.txt", encoding='UTF-8')  # Persan
    PO = open("lang/PO.txt", encoding='UTF-8')  # Polonais
    POR = open("lang/POR.txt", encoding='UTF-8')  # Portugais
    RO = open("lang/RO.txt", encoding='UTF-8')  # Roumain
    RU = open("lang/RU.txt", encoding='UTF-8')  # Russe
    SA = open("lang/SA.txt", encoding='UTF-8')  # Samoan
    SE = open("lang/SE.txt", encoding='UTF-8')  # Serbe
    SES = open("lang/SES.txt", encoding='UTF-8')  # Sesotho
    SH = open("lang/SH.txt", encoding='UTF-8')  # Shona
    SI = open("lang/SI.txt", encoding='UTF-8')  # Sindhi
    SLO = open("lang/SLO.txt", encoding='UTF-8')  # Slovaque
    SLOV = open("lang/SLOV.txt", encoding='UTF-8')  # Slovene
    SO = open("lang/SO.txt", encoding='UTF-8')  # Somali
    SOU = open("lang/SOU.txt", encoding='UTF-8')  # Soundanais
    SUE = open("lang/SUE.txt", encoding='UTF-8')  # Suedois
    SW = open("lang/SW.txt", encoding='UTF-8')  # Swahili
    TA = open("lang/TA.txt", encoding='UTF-8')  # Tadjik
    TAG = open("lang/TAG.txt", encoding='UTF-8')  # Tagalog
    TAM = open("lang/TAM.txt", encoding='UTF-8')  # Tamoul
    TC = open("lang/TC.txt", encoding='UTF-8')  # Tcheque
    TE = open("lang/TE.txt", encoding='UTF-8')  # Telugu
    TH = open("lang/TH.txt", encoding='UTF-8')  # Thai
    TU = open("lang/TU.txt", encoding='UTF-8')  # Turc
    UR = open("lang/UR.txt", encoding='UTF-8')  # Urdu
    VI = open("lang/VI.txt", encoding='UTF-8')  # Vietnamien
    XH = open("lang/XH.txt", encoding='UTF-8')  # Xhosa
    YI = open("lang/YI.txt", encoding='UTF-8')  # Yiddish
    YO = open("lang/YO.txt", encoding='UTF-8')  # Yorouba
    ZO = open("lang/ZO.txt", encoding='UTF-8')  # Zoulou
    lang_FR = FR.readlines()
    lang_EN = EN.readlines()
    lang_ES = ES.readlines()
    lang_CN = CN.readlines()
    lang_AF = AF.readlines()
    lang_AL = AL.readlines()
    lang_DE = DE.readlines()
    lang_AM = AM.readlines()
    lang_AR = AR.readlines()
    lang_ARM = ARM.readlines()
    lang_AZ = AZ.readlines()
    lang_BA = BA.readlines()
    lang_BE = BE.readlines()
    lang_BI = BI.readlines()
    lang_BIR = BIR.readlines()
    lang_BO = BO.readlines()
    lang_BU = BU.readlines()
    lang_CA = CA.readlines()
    lang_CE = CE.readlines()
    lang_CH = CH.readlines()
    lang_CI = CI.readlines()
    lang_CO = CO.readlines()
    lang_COR = COR.readlines()
    lang_CR = CR.readlines()
    lang_CRO = CRO.readlines()
    lang_DA = DA.readlines()
    lang_ESP = ESP.readlines()
    lang_EST = EST.readlines()
    lang_FI = FI.readlines()
    lang_FRI = FRI.readlines()
    lang_GA = GA.readlines()
    lang_GAL = GAL.readlines()
    lang_GE = GE.readlines()
    lang_GR = GR.readlines()
    lang_GU = GU.readlines()
    lang_HA = HA.readlines()
    lang_HAW = HAW.readlines()
    lang_HE = HE.readlines()
    lang_HI = HI.readlines()
    lang_HM = HM.readlines()
    lang_HO = HO.readlines()
    lang_IB = IB.readlines()
    lang_IN = IN.readlines()
    lang_IR = IR.readlines()
    lang_IS = IS.readlines()
    lang_IT = IT.readlines()
    lang_JP = JP.readlines()
    lang_JA = JA.readlines()
    lang_KA = KA.readlines()
    lang_KAZ = KAZ.readlines()
    lang_KH = KH.readlines()
    lang_KI = KI.readlines()
    lang_KU = KU.readlines()
    lang_LA = LA.readlines()
    lang_LAT = LAT.readlines()
    lang_LE = LE.readlines()
    lang_LI = LI.readlines()
    lang_LU = LU.readlines()
    lang_MA = MA.readlines()
    lang_MAL = MAL.readlines()
    lang_MALA = MALA.readlines()
    lang_MALG = MALG.readlines()
    lang_MALT = MALT.readlines()
    lang_MAO = MAO.readlines()
    lang_MAR = MAR.readlines()
    lang_MO = MO.readlines()
    lang_NE = NE.readlines()
    lang_NEP = NEP.readlines()
    lang_NO = NO.readlines()
    lang_OU = OU.readlines()
    lang_PA = PA.readlines()
    lang_PAN = PAN.readlines()
    lang_PE = PE.readlines()
    lang_PO = PO.readlines()
    lang_POR = POR.readlines()
    lang_RO = RO.readlines()
    lang_RU = RU.readlines()
    lang_SA = SA.readlines()
    lang_SE = SE.readlines()
    lang_SES = SES.readlines()
    lang_SH = SH.readlines()
    lang_SI = SI.readlines()
    lang_SLO = SLO.readlines()
    lang_SLOV = SLOV.readlines()
    lang_SO = SO.readlines()
    lang_SOU = SOU.readlines()
    lang_SUE = SUE.readlines()
    lang_SW = SW.readlines()
    lang_TA = TA.readlines()
    lang_TAG = TAG.readlines()
    lang_TAM = TAM.readlines()
    lang_TC = TC.readlines()
    lang_TE = TE.readlines()
    lang_TH = TH.readlines()
    lang_TU = TU.readlines()
    lang_UR = UR.readlines()
    lang_VI = VI.readlines()
    lang_XH = XH.readlines()
    lang_YI = YI.readlines()
    lang_YO = YO.readlines()
    lang_ZO = ZO.readlines()

    #Fermeture des fichiers textes

    FR.close()
    EN.close()
    ES.close()
    CN.close()
    AF.close()
    AL.close()
    DE.close()
    AM.close()
    AR.close()
    ARM.close()
    AZ.close()
    BA.close()
    BE.close()
    BI.close()
    BIR.close()
    BO.close()
    BU.close()
    CA.close()
    CE.close()
    CH.close()
    CI.close()
    CO.close()
    COR.close()
    CR.close()
    CRO.close()
    DA.close()
    ESP.close()
    EST.close()
    FI.close()
    FRI.close()
    GA.close()
    GA.close()
    GE.close()
    GR.close()
    GU.close()
    HA.close()
    HAW.close()
    HE.close()
    HI.close()
    HM.close()
    HO.close()
    IB.close()
    IN.close()
    IR.close()
    IS.close()
    IT.close()
    JP.close()
    JA.close()
    KA.close()
    KA.close()
    KH.close()
    KI.close()
    KU.close()
    LA.close()
    LAT.close()
    LE.close()
    LI.close()
    LU.close()
    MA.close()
    MAL.close()
    MALA.close()
    MALG.close()
    MALT.close()
    MAO.close()
    MAR.close()
    MO.close()
    NE.close()
    NEP.close()
    NO.close()
    OU.close()
    PA.close()
    PAN.close()
    PE.close()
    PO.close()
    POR.close()
    RO.close()
    RU.close()
    SA.close()
    SE.close()
    SES.close()
    SH.close()
    SI.close()
    SLO.close()
    SLOV.close()
    SO.close()
    SOU.close()
    SUE.close()
    SW.close()
    TA.close()
    TAG.close()
    TAM.close()
    TC.close()
    TE.close()
    TH.close()
    TU.close()
    UR.close()
    VI.close()
    XH.close()
    YI.close()
    YO.close()
    ZO.close()

    #On retourne ici les listes contenant les langues dans le programme principal

    return lang_FR, lang_EN, lang_ES, lang_CN, lang_AF, lang_AL, lang_DE, lang_AM, lang_AR, lang_ARM, lang_AZ, \
           lang_BA, lang_BE, lang_BI, lang_BIR, lang_BO, lang_BU, lang_CA, lang_CE, lang_CH, lang_CI, lang_CO, lang_COR, \
           lang_CR, lang_CRO, lang_DA, lang_ESP, lang_EST, lang_FI, lang_FRI, lang_GA, lang_GAL, lang_GE, lang_GR, \
           lang_GU, lang_HA, lang_HAW, lang_HE, lang_HI, lang_HM, lang_HO, lang_IB, lang_IN, lang_IR, lang_IS, lang_IT, \
           lang_JP, lang_JA, lang_KA, lang_KAZ, lang_KH, lang_KI, lang_KU, lang_LA, lang_LAT, lang_LE, lang_LI, lang_LU, \
           lang_MA, lang_MAL, lang_MALA, lang_MALG, lang_MALT, lang_MAO, lang_MAR, lang_MO, lang_NE, lang_NEP, lang_NO, \
           lang_OU, lang_PA, lang_PAN, lang_PE, lang_PO, lang_POR, lang_RO, lang_RU, lang_SA, lang_SE, lang_SES, lang_SH, \
           lang_SI, lang_SLO, lang_SLOV, lang_SO, lang_SOU, lang_SUE, lang_SW, lang_TA, lang_TAG, lang_TAM, lang_TC, \
           lang_TE, lang_TH, lang_TU, lang_UR, lang_VI, lang_XH, lang_YI, lang_YO, lang_ZO



def choixlang_lang(x, lang_EN, lang_FR, lang_ES, lang_CN, lang_AF, lang_AL, lang_DE, lang_AM, lang_AR, lang_ARM,
                   lang_AZ,
                   lang_BE, lang_BI, lang_BIR, lang_BO, lang_BU, lang_CA, lang_CE, lang_CH, lang_CI, lang_CO, lang_COR,
                   lang_CR,
                   lang_CRO, lang_DA, lang_ESP, lang_EST, lang_FI, lang_FRI, lang_GA, lang_GAL, lang_GE, lang_GR,
                   lang_GU, lang_HA,
                   lang_HAW, lang_HE, lang_HI, lang_HM, lang_HO, lang_IB, lang_IN, lang_IR, lang_IS, lang_IT, lang_JP,
                   lang_JA,
                   lang_KA, lang_KAZ, lang_KH, lang_KI, lang_KU, lang_LA, lang_LAT, lang_LE, lang_LI, lang_LU, lang_MA,
                   lang_MAL,
                   lang_MALA, lang_MALG, lang_MALT, lang_MAO, lang_MAR, lang_MO, lang_NE, lang_NEP, lang_NO, lang_OU,
                   lang_PA,
                   lang_PAN, lang_PE, lang_PO, lang_POR, lang_RO, lang_RU, lang_SA, lang_SE, lang_SES, lang_SH, lang_SI,
                   lang_SLO,
                   lang_SLOV, lang_SO, lang_SOU, lang_SUE, lang_SW, lang_TA, lang_TAG, lang_TAM, lang_TC, lang_TE,
                   lang_TH,
                   lang_TU, lang_UR, lang_VI, lang_XH, lang_YI, lang_YO, lang_ZO, lang_BA): #Fonction qui permet le changement de langue

	#Ici on cherche quelle valeur du combobox correspond a quelle langue

    if x == "Francais":
        langc = lang_FR
    if x == "English":
        langc = lang_EN
    if x == "Espanol":
        langc = lang_ES
    if x == "柑":
        langc = lang_CN
    if x == "Afrikaans":
        langc = lang_AF
    if x == "shqiptar":
        langc = lang_AL
    if x == "አማርኛ":
        langc = lang_AM
    if x == "العربية":
        langc = lang_AR
    if x == "հայերեն":
        langc = lang_ARM
    if x == "Azərbaycan":
        langc = lang_AZ
    if x == "Euskal":
        langc = lang_BA
    if x == "বাঙালি":
        langc = lang_BE
    if x == "беларускі":
        langc = lang_BI
    if x == "မြန်မာ":
        langc = lang_BIR
    if x == "bosanski":
        langc = lang_BO
    if x == "български":
        langc = lang_BU
    if x == "Català":
        langc = lang_CA
    if x == "Cebuano":
        langc = lang_CE
    if x == "Chichewa":
        langc = lang_CH
    if x == "සිංහලයන්":
        langc = lang_CI
    if x == "한국의":
        langc = lang_CO
    if x == "Corsica":
        langc = lang_COR
    if x == "Kreyòl Ayisyen":
        langc = lang_CR
    if x == "hrvatski":
        langc = lang_CRO
    if x == "dansk":
        langc = lang_DA
    if x == "Deutsch":
        langc = lang_DE
    if x == "Esperanto":
        langc = lang_ESP
    if x == "eesti":
        langc = lang_EST
    if x == "suomalainen":
        langc = lang_FI
    if x == "Frysk":
        langc = lang_FRI
    if x == "Gàidhlig":
        langc = lang_GA
    if x == "Cymraeg":
        langc = lang_GAL
    if x == "ქართული":
        langc = lang_GE
    if x == "ελληνικά":
        langc = lang_GR
    if x == "ગુજરાતી":
        langc = lang_GU
    if x == "Hausa":
        langc = lang_HA
    if x == "Hawaiian":
        langc = lang_HAW
    if x == "עברי:":
        langc = lang_HE
    if x == "हिन्दी":
        langc = lang_HI
    if x == "hmong":
        langc = lang_HM
    if x == "magyar":
        langc = lang_HO
    if x == "igbo":
        langc = lang_IB
    if x == "Indonesia":
        langc = lang_IN
    if x == "Gaeilge":
        langc = lang_IR
    if x == "Íslendingur":
        langc = lang_IS
    if x == "Italiano":
        langc = lang_IT
    if x == "Jawa":
        langc = lang_JA
    if x == "日本の":
        langc = lang_JP
    if x == "ಕನ್ನಡ":
        langc = lang_KA
    if x == "Қазақ":
        langc = lang_KAZ
    if x == "ខ្មែរ":
        langc = lang_KH
    if x == "Kirghiz":
        langc = lang_KI
    if x == "Kurdî":
        langc = lang_KU
    if x == "ລາວ":
        langc = lang_LA
    if x == "Latine":
        langc = lang_LAT
    if x == "Latvijas":
        langc = lang_LE
    if x == "Lietuvos":
        langc = lang_LI
    if x == "Lëtzebuerg":
        langc = lang_LU
    if x == "Македонски":
        langc = lang_MA
    if x == "Malaysia":
        langc = lang_MAL
    if x == "മലയാളം":
        langc = lang_MALA
    if x == "Malagasy":
        langc = lang_MALG
    if x == "Malti":
        langc = lang_MALT
    if x == "Maori":
        langc = lang_MAO
    if x == "मराठी":
        langc = lang_MAR
    if x == "Монгол":
        langc = lang_MO
    if x == "Nederlands":
        langc = lang_NE
    if x == "नेपाली":
        langc = lang_NEP
    if x == "norsk":
        langc = lang_NO
    if x == "O zbekiston":
        langc = lang_OU
    if x == "پښتو":
        langc = lang_PA
    if x == "ਪੰਜਾਬੀ":
        langc = lang_PAN
    if x == "فارسی":
        langc = lang_PE
    if x == "Polski":
        langc = lang_PO
    if x == "Português":
        langc = lang_POR
    if x == "Românesc":
        langc = lang_RO
    if x == "русский":
        langc = lang_RU
    if x == "Samoa":
        langc = lang_SA
    if x == "српски":
        langc = lang_SE
    if x == "Sesotho":
        langc = lang_SES
    if x == "Shona":
        langc = lang_SH
    if x == "سنڌي":
        langc = lang_SI
    if x == "Slovenský":
        langc = lang_SLO
    if x == "slovenski":
        langc = lang_SLOV
    if x == "Soomaali":
        langc = lang_SO
    if x == "Sunda":
        langc = lang_SOU
    if x == "Sudans":
        langc = lang_SUE
    if x == "Swahili":
        langc = lang_SW
    if x == "Тоҷикистон":
        langc = lang_TA
    if x == "tagalog":
        langc = lang_TAG
    if x == "தமிழ்":
        langc = lang_TAM
    if x == "český":
        langc = lang_TC
    if x == "telugu":
        langc = lang_TE
    if x == "ไทย":
        langc = lang_TH
    if x == "Türk":
        langc = lang_TU
    if x == "اردو":
        langc = lang_UR
    if x == "tiếng Việt":
        langc = lang_VI
    if x == "isiXhosa":
        langc = lang_XH
    if x == "ייִדיש":
        langc = lang_YI
    if x == "Yoruba":
        langc = lang_YO
    if x == "Zulu":
        langc = lang_ZO

    #Retour dans le programme principal de la langue choisie

    return langc
