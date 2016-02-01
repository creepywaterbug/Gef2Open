# -----------------------------------------------------------------------------
# Name   : UtlGef.py
# Purpose: Set van Gef gerelateerde functies.
# Note   : - gaat ervan uit dat Gef2.dll bereikbaar is via search path
#          - standaard data type voor dll functie return (restype):
#            ctypes.c_int (= Python int/long)
# Versies: Python 2.5, ArcGIS 9.3.1
# Updated: PL, 13 Jul 2012
# Aangepaste versie RH, 1 Februari 2016
# - deze versie maakt geen gebruikt van Gef2.dll maar van de open versie Gef2.py
# - In dit script zijn alleen de functies onder A. zo aangepast dat ze Gef2.py
#   ipv Gef2.dll aanroepen. De functies onder B tm F zijn ongewijzigd.
# -----------------------------------------------------------------------------


# System module
#import ctypes, datetime
import datetime

# Globale constante
#oDll = ctypes.windll.Gef2
import Gef2

# De functies zijn hieronder - alfabetisch - ingedeeld in 4 categorieen:
#    A. een-op-een vertalingen uit de gef2.dll
#    B. aanvullende helper functies
#    C. voor vullen kolommen gebruikt door meerdere tabellen (ALG)
#    D. voor vullen kolommen gebruikt door tabel SONDERING (SON)
#    E. voor vullen kolommen gebruikt door tabel BORING (BOR)
#    F. voor vullen kolommen gebruikt door tabel PEILBUISPUT (PBP)

# -----------------------------------------------------------------------------
# CATEGORIE A. een-op-een vertalingen uit de gef2.dll
# -----------------------------------------------------------------------------

# Purpose: Vrijgeven interne geheugenstructuur
#def Free_Gef():
#    oFunc = oDll.free_gef
#    iRetVal = oFunc()
#    return bool(iRetVal)

# Purpose: Of een GEF-BORE-Report file is (boring)
def Gbr_Is_Gbr():
    #oFunc = oDll.gbr_is_gbr
    #iRetVal = oFunc()
    #return bool(iRetVal)
    iRetVal = Gef2.gbr_is_gbr()
    return iRetVal

# Purpose: Of een GEF-CPT-Report file is (sondering)
def Gcr_Is_Gcr():
    #oFunc = oDll.gcr_is_gcr
    #iRetVal = oFunc()
    #return bool(iRetVal)
    iRetVal = Gef2.gcr_is_gcr()
    return iRetVal

# Purpose: Of #COMPANYID aanwezig
def Get_CompanyID_Flag():
    #oFunc = oDll.get_companyid_flag
    #iRetVal = oFunc()
    #return bool(iRetVal)
    iRetVal = Gef2.get_companyid_flag()
    return iRetVal

# Purpose: Geeft aantal kolommen in het data block
def Get_Column():
    #oFunc = oDll.get_column
    #iRetVal = oFunc()
    iRetVal = Gef2.get_column()
    return iRetVal

# Purpose: Of #COLUMN aanwezig
def Get_Column_Flag():
    #oFunc = oDll.get_column_flag
    #iRetVal = oFunc()
    #return bool(iRetVal)
    iRetVal = Gef2.get_column_flag()
    return iRetVal

# Purpose: Geeft company naam
def Get_CompanyID_Name():
    #oFunc = oDll.get_companyid_Name
    #oFunc.restype = ctypes.c_char_p # apart aangeven
    #sRetVal = oFunc()
    sRetVal = Gef2.get_companyid_Name()
    return sRetVal

# Purpose: Geeft waarde uit bepaalde cel van data block
def Get_Data(i_Kol, iRij):
    #oFunc = oDll.get_data
    #oFunc.restype = ctypes.c_double # apart aangeven
    #fRetVal = oFunc(i_Kol, iRij)
    fRetVal = Gef2.get_data(i_Kol,iRij)
    return fRetVal

# Purpose: Of gegeven #MEASUREMENTTEXT index aanwezig
def Get_MeasurementText_Flag(i_Index):
    #oFunc = oDll.get_measurementtext_flag
    #iRetVal = oFunc(i_Index)
    #return bool(iRetVal)
    iRetVal = Gef2.get_measurementtext_flag(i_Index)
    return iRetVal

# Purpose: Of gegeven #MEASUREMENTVAR index aanwezig
def Get_MeasurementVar_Flag(i_Index):
    #oFunc = oDll.get_measurementvar_flag
    #iRetVal = oFunc(i_Index)
    #return bool(iRetVal)
    iRetVal = Gef2.get_measurementvar_flag(i_Index)
    return iRetVal

# Purpose: Geeft measurementtext tekst
def Get_MeasurementText_Tekst(i_Index):
    #oFunc = oDll.get_measurementtext_Tekst
    #oFunc.restype = ctypes.c_char_p # apart aangeven
    #sRetVal = oFunc(i_Index)
    sRetVal = Gef2.get_measurementtext_Tekst(i_Index)
    return sRetVal

# Purpose: Geeft measurementvar value
def Get_MeasurementVar_Value(i_Index):
    #oFunc = oDll.get_measurementvar_Value
    #oFunc.restype = ctypes.c_float # apart aangeven
    #fRetVal = oFunc(i_Index)
    #return round(fRetVal, 3) # rond af op 3 decimalen
    fRetVal = Gef2.get_measurementvar_Value(i_Index)
    return fRetVal

# Purpose: Geeft aantal rijen in het data block
def Get_Nr_Scans():
    #oFunc = oDll.get_nr_scans
    #iRetVal = oFunc()
    iRetVal = Gef2.get_nr_scans()
    return iRetVal

# Purpose: Of #PARENT aanwezig
def Get_Parent_Flag():
    #oFunc = oDll.get_parent_flag
    #iRetVal = oFunc()
    #return bool(iRetVal) #levert een true ipv false
    iRetVal = Gef2.get_parent_flag()
    return iRetVal

# Purpose: Geeft referentie naar de parent, bv bestandsnaam
def Get_Parent_Reference():
    #oFunc = oDll.get_parent_reference
    #oFunc.restype = ctypes.c_char_p # apart aangeven
    #sRetVal = oFunc()
    sRetVal = Gef2.get_parent_reference()
    return sRetVal

# Purpose: Of #PROCEDURECODE aanwezig
def Get_ProcedureCode_Flag():
    #oFunc = oDll.get_procedurecode_flag
    #iRetVal = oFunc()
    #return bool(iRetVal)
    iRetVal = Gef2.get_procedurecode_flag()
    return iRetVal

# Purpose: Geeft procedurecode code
def Get_ProcedureCode_Code():
    #oFunc = oDll.get_procedurecode_Code
    #oFunc.restype = ctypes.c_char_p # apart aangeven
    #sRetVal = oFunc()
    sRetVal = Gef2.get_procedurecode_Code()
    return sRetVal

# Purpose: Of #PROJECTID aanwezig
def Get_ProjectID_Flag():
    #oFunc = oDll.get_projectid_flag
    #iRetVal = oFunc()
    #return bool(iRetVal)
    iRetVal = Gef2.get_projectid_flag()
    return iRetVal

# Purpose: Geeft projectid nummer
def Get_ProjectID_Number():
    #oFunc = oDll.get_projectid_Number
    #oFunc.restype = ctypes.c_char_p # apart aangeven
    #sRetVal = oFunc()
    sRetVal = Gef2.get_projectid_Number()
    return sRetVal

# Purpose: Of #REPORTCODE aanwezig
def Get_ReportCode_Flag():
    #oFunc = oDll.get_reportcode_flag
    #iRetVal = oFunc()
    #return bool(iRetVal)
    iRetVal = Gef2.get_reportcode_flag()
    return iRetVal

# Purpose: Geeft reportcode code
def Get_ReportCode_Code():
    #oFunc = oDll.get_reportcode_Code
    #oFunc.restype = ctypes.c_char_p # apart aangeven
    #sRetVal = oFunc()
    sRetVal = Gef2.get_reportcode_Code()
    return sRetVal

# Purpose: Of #STARTDATE aanwezig
def Get_StartDate_Flag():
    #oFunc = oDll.get_startdate_flag
    #iRetVal = oFunc()
    #return bool(iRetVal)
    iRetVal = Gef2.get_startdate_flag()
    return iRetVal

# Purpose: Geeft startdate jaar (yyyy)
def Get_StartDate_Yyyy():
    #oFunc = oDll.get_startdate_Yyyy
    #iRetVal = oFunc()
    iRetVal = Gef2.get_startdate_Yyyy()
    return iRetVal

# Purpose: Geeft startdate maand (mm)
def Get_StartDate_Mm():
    #oFunc = oDll.get_startdate_Mm
    #iRetVal = oFunc()
    iRetVal = Gef2.get_startdate_Mm()
    return iRetVal

# Purpose: Geeft startdate dag (dd)
def Get_StartDate_Dd():
    #oFunc = oDll.get_startdate_Dd
    #iRetVal = oFunc()
    iRetVal = Gef2.get_startdate_Dd()
    return iRetVal

# Purpose: Of #XYID aanwezig
def Get_XYID_Flag():
    #oFunc = oDll.get_xyid_flag
    #iRetVal = oFunc()
    #return bool(iRetVal)
    iRetVal = Gef2.get_xyid_flag()
    return iRetVal

# Purpose: Geeft X coordinaat
def Get_XYID_X():
    #oFunc = oDll.get_xyid_X
    #oFunc.restype = ctypes.c_double # apart aangeven
    #fRetVal = oFunc()
    fRetVal = Gef2.get_xyid_X()
    return fRetVal

# Purpose: Geeft Y coordinaat
def Get_XYID_Y():
    #oFunc = oDll.get_xyid_Y
    #oFunc.restype = ctypes.c_double # apart aangeven
    #fRetVal = oFunc()
    fRetVal = Gef2.get_xyid_Y()
    return fRetVal

# Purpose: Of #ZID aanwezig
def Get_ZID_Flag():
    #oFunc = oDll.get_zid_flag
    #iRetVal = oFunc()
    #return bool(iRetVal)
    iRetVal = Gef2.get_zid_flag()
    return iRetVal

# Purpose: Geeft Z coordinaat
def Get_ZID_Z():
    #oFunc = oDll.get_zid_Z
    #oFunc.restype = ctypes.c_double # apart aangeven
    #fRetVal = oFunc()
    fRetVal = Gef2.get_zid_Z()
    return fRetVal

# Purpose: Initialiseren interne geheugenstructuur
def Init_Gef():
    #oFunc = oDll.init_gef
    #iRetVal = oFunc()
    #return bool(iRetVal)
    iRetVal = Gef2.init_gef()
    return iRetVal

# Purpose: Of een bestand geplot kan worden
def Is_Plotable():
    #oFunc = oDll.is_plotable
    #iRetVal = oFunc()
    #return bool(iRetVal)
    iRetVal = Gef2.is_plotable()
    return iRetVal

# Purpose: Geeft kolom nummer die correspondeert met gegeven 'quantity
#          number', en 0 wanneer deze niet aanwezig.
# Note   : Bv, quantity number voor 'gecorrigeerde diepte' is 11.
def Qn2Column(i_iQtyNumber):
    #oFunc = oDll.qn2column
    #iRetVal = oFunc(i_iQtyNumber)
    iRetVal = Gef2.qn2column(i_iQtyNumber)
    return iRetVal

# Purpose: Leest een gegeven Gef bestand in geheugen
def Read_Gef(i_sBestandGef):
    #oFunc = oDll.read_gef
    #iRetVal = oFunc(i_sBestandGef)
    #return bool(iRetVal)
    iRetVal = Gef2.read_gef(i_sBestandGef)
    return iRetVal

# Purpose: Of een bepaald aspect van een bestand correct is
# Parms  : Toegestaan: 'HEADER', 'DATA', 'GEF-CPT-Report','GEF-BORE-Report'
# Note   : - heb gemerkt dat deze functie bij aanroep met parm 'GEF-CPT-Report'
#            bij een corrupte gef een onverwachte fout kan genereren:
#            WindowsError: exception: access violation reading 0x00000004
def Test_Gef(i_sAspect):
    #oFunc = oDll.test_gef
    #iRetVal = oFunc(i_sAspect)
    #return bool(iRetVal)
    iRetVal = Gef2.test_gef(i_sAspect)
    return iRetVal

# -----------------------------------------------------------------------------
# CATEGORIE B. aanvullende helper functies
# -----------------------------------------------------------------------------

# Purpose: Converteert ISO datum tekst string (yyyy-mm-dd),
#          bv '2011-1-17', als tekst string volgens ingestelde Windows locale
# Note   : - datum is in gef bestand altijd aangegeven volgens 'ISO' standaard
def Get_ISODate_AsText_Local(i_sISODatum):
    oListISODatum = i_sISODatum.split('-')
    iJaar = int(oListISODatum[0])
    iMaand = int(oListISODatum[1])
    iDag = int(oListISODatum[2])
    oDate = datetime.date(iJaar, iMaand, iDag)
    return oDate.strftime('%x') # format volgens ingestelde Windows locale

# Purpose: Of een gegeven report string voorkomt in de tags
#          #PROCEDURECODE dan wel #REPORTCODE.
# Parms  : Toegestane waarden zijn:
#          - 'GEF-CPT-Report'
#          - 'GEF-BORE-Report'
#          - 'GEF-BOREHOLE-Report'
# Note   : Gef2.dll herkent niet 'GEF-BOREHOLE-Report'
def Get_ReportType_Flag(i_sReportString):
    if Get_ProcedureCode_Flag() and \
       Get_ProcedureCode_Code().upper() == i_sReportString.upper():
            return True
    elif Get_ReportCode_Flag() and \
         Get_ReportCode_Code().upper() == i_sReportString.upper():
            return True
    else:
        return False

# Purpose: Geeft startdate combinatie als ISO tekst string
#           (yyyy-mm-dd), bv '2011-1-17'
# Note   :  - een geodatabase datum kolom accepteert geen Python datum object,
#             alleen een tekst string
def Get_StartDate_AsText_ISO():
    return str(Get_StartDate_Yyyy()) + '-' + \
           str(Get_StartDate_Mm()) + '-' + \
           str(Get_StartDate_Dd())

# Purpose: Geeft startdate combinatie als lokale tekst string. Bij NL
#          (dd-mm-yyyy), bv '17-1-2011'
# Note   :  - een geodatabase datum kolom accepteert geen Python datum object,
#             alleen een tekst string
def Get_StartDate_AsText_Local():
    iJaar = Get_StartDate_Yyyy()
    iMaand = Get_StartDate_Mm()
    iDag = Get_StartDate_Dd()
    oDate = datetime.date(iJaar, iMaand, iDag)
    return oDate.strftime('%x') # format volgens ingestelde Windows locale

# -----------------------------------------------------------------------------
# CATEGORIE C. voor vullen kolommen gebruikt door meerdere tabellen (ALG)
# -----------------------------------------------------------------------------

# Purpose: Waarde voor kolom 'BEDRIJF' (# COMPANYID)
def Get_ALG_Bedrijf():
    if Get_CompanyID_Flag():
        return Get_CompanyID_Name()

# Purpose: Waarde voor kolom 'MV_NAP' (# ZID)
def Get_ALG_MVNAP():
    if Get_ZID_Flag():
        return Get_ZID_Z()

# Purpose: Waarde voor kolom 'PROJECTNUMMER' (# PROJECTID)
def Get_ALG_ProjectNummer():
    if Get_ProjectID_Flag():
        return Get_ProjectID_Number()

# Purpose: Waarde voor kolom 'X_RD' (# XYID)
def Get_ALG_XRD():
    if not Get_XYID_Flag():
        return 0.0
    else:
        return Get_XYID_X()

# Purpose: Waarde voor kolom 'Y_RD' (# XYID)
def Get_ALG_YRD():
    if not Get_XYID_Flag():
        return 0.0
    else:
        return Get_XYID_Y()

# -----------------------------------------------------------------------------
# CATEGORIE D. voor vullen kolommen gebruikt door tabel SONDERING (SON)
# -----------------------------------------------------------------------------

# Purpose: Datum van sondering (# STARTDATE)
def Get_SON_DatumSondering():
    if Get_StartDate_Flag():
        return Get_StartDate_AsText_Local()

# Purpose: Geeft lijst van waarden van de sondering kolommen
#          [EINDDIEPTE_TYPE, EINDDIEPTE]
def Get_SON_EindDiepteGegevens():
    # Constanten en variabelen
    iQTY_SONDEERLENGTE = 1
    iQTY_GECORRIGEERDE_DIEPTE = 11

    # Verzamel details voor data block
    iKolommenDataBlock = Get_Column()
    iRijenDataBlock = Get_Nr_Scans()
    bHasDataBlock = (iRijenDataBlock > 0)
    iKolomNrSondeerLengte = Qn2Column(iQTY_SONDEERLENGTE)
    iKolomNrGecorrDiepte = Qn2Column(iQTY_GECORRIGEERDE_DIEPTE)

    # Bepaal de einddiepte uit laatste regel data block
    if not bHasDataBlock:
        sEindDiepteType = None
        fEindDiepte = None
    else:
        # Neem gecorr diepte, als bekend. Anders sondeerlengte
        if iKolomNrGecorrDiepte > 0:
            sEindDiepteType = 'corrected depth'
            fEindDiepte = Get_Data(iKolomNrGecorrDiepte, iRijenDataBlock)
        elif iKolomNrSondeerLengte > 0:
            sEindDiepteType = 'uncorrected depth'
            fEindDiepte = Get_Data(iKolomNrSondeerLengte, iRijenDataBlock)
        else:
            # Niets is aangegeven, veronderstel eerste kolom
            sEindDiepteType = 'uncorrected depth'
            fEindDiepte = Get_Data(1, iRijenDataBlock)
    return [sEindDiepteType, fEindDiepte]

# Purpose: Methode van sondering (# MEASUREMENTTEXT 4 (conus type)
def Get_SON_MethodeSondering():
    if Get_MeasurementText_Flag(4):
        return Get_MeasurementText_Tekst(4)

# -----------------------------------------------------------------------------
# CATEGORIE E. voor vullen kolommen gebruikt door tabel BORING (BOR)
# -----------------------------------------------------------------------------

# Purpose: Datum van boring (# MEASUREMENTTEXT 16)
def Get_BOR_DatumBoring():
    if Get_MeasurementText_Flag(16):
        sISODatum = Get_MeasurementText_Tekst(16)
        return Get_ISODate_AsText_Local(sISODatum)

# Purpose: Einddiepte van boring (# MEASUREMENTVAR 16)
def Get_BOR_EindDiepte():
    if Get_MeasurementVar_Flag(16):
        return Get_MeasurementVar_Value(16)

# Purpose: Methode van boring (# MEASUREMENTTEXT 31)
def Get_BOR_MethodeBoring():
    if Get_MeasurementText_Flag(31):
        return Get_MeasurementText_Tekst(31)

# -----------------------------------------------------------------------------
# CATEGORIE F. voor vullen kolommen gebruikt door tabel PEILBUISPUT (PBP)
# -----------------------------------------------------------------------------

# Purpose: Waarde voor kolom 'BESTAND_PARENT' (# PARENT)
def Get_PBP_BestandParent():
    if Get_Parent_Flag():
        return Get_Parent_Reference()

# Purpose: Waarde voor PBP kolom 'AANTAL_PEILBUIZEN' (# MEASUREMENTVAR 1
def Get_PBP_AantalPeilbuizen():
    if not Get_MeasurementVar_Flag(1):
        return 0
    else:
        fResult = Get_MeasurementVar_Value(1)
        return int(fResult)

# Purpose: Waarde voor PBP kolom 'DATUM_PLAATSING' (# MEASUREMENTTEXT 2)
def Get_PBP_DatumPlaatsing():
    if Get_MeasurementText_Flag(2):
        sISODatum = Get_MeasurementText_Tekst(2)
        return Get_ISODate_AsText_Local(sISODatum)

# Purpose: Bovenkant van filter in gegeven peilbuis (# MEASUREMENTVAR 26k+n-10)
def Get_PBP_Filter_Bovenkant(i_iPeilbuisNr, i_iFilterNr):
    f = lambda k, n: 26*k + n - 10
    fResult = None
    if Get_MeasurementVar_Flag(f(i_iPeilbuisNr, i_iFilterNr)):
        fResult = Get_MeasurementVar_Value(f(i_iPeilbuisNr, i_iFilterNr))
    return fResult

# Purpose: Of een bepaalde filter in een gegeven peilbuis wel voorkomt
# Note   : Naar voorbeeld code Doeke Dam
def Get_PBP_Filter_Exists(i_iPeilbuisNr, i_iFilterNr):
    bResult = False
    # MEASUREMENTVAR 26k + n - 10 (bovenkant filter n van peilbuis k)
    fBoven = lambda k, n: 26*k + n - 10
    # MEASUREMENTVAR 26k + n - 5 (onderkant filter n van peilbuis k)
    fOnder = lambda k, n: 26*k + n - 5
    if Get_MeasurementVar_Flag(fBoven(i_iPeilbuisNr, i_iFilterNr)) and \
          Get_MeasurementVar_Flag(fOnder(i_iPeilbuisNr, i_iFilterNr)):
        bResult = True
    return bResult

# Purpose: Lengte van filter in gegeven peilbuis (# MEASUREMENTVAR 26k+n)
def Get_PBP_Filter_LengteFilter(i_iPeilbuisNr, i_iFilterNr):
    f = lambda k, n: 26*k + n
    fResult = None
    if Get_MeasurementVar_Flag(f(i_iPeilbuisNr, i_iFilterNr)):
        fResult = Get_MeasurementVar_Value(f(i_iPeilbuisNr, i_iFilterNr))
    return fResult

# Purpose: Onderkant van filter in gegeven peilbuis (# MEASUREMENTVAR 26k+n-5)
def Get_PBP_Filter_Onderkant(i_iPeilbuisNr, i_iFilterNr):
    f = lambda k, n: 26*k + n - 5
    fResult = None
    if Get_MeasurementVar_Flag(f(i_iPeilbuisNr, i_iFilterNr)):
        fResult = Get_MeasurementVar_Value(f(i_iPeilbuisNr, i_iFilterNr))
    return fResult

# Purpose: Aantal filters in een gegeven peilbuis
def Get_PBP_Peilbuis_AantalFilters(i_iPeilbuisNr):
    iCount = 1 # teller voor aantal filters
    while Get_PBP_Filter_Exists(i_iPeilbuisNr, iCount):
        iCount += 1
    else:
        # Maak laatste optelling ongedaan
        iCount -= 1
    return iCount

# Purpose: Bovenkant van een gegeven peilbuis (# MEASUREMENTVAR 26k-15)
def Get_PBP_Peilbuis_Bovenkant(i_iPeilbuisNr):
    f = lambda k: 26*k - 15
    fResult = None
    if Get_MeasurementVar_Flag(f(i_iPeilbuisNr)):
        fResult = Get_MeasurementVar_Value(f(i_iPeilbuisNr))
    return fResult

# Purpose: Code van een gegeven peilbuis (# MEASUREMENTTEXT 26k-15)
def Get_PBP_Peilbuis_Code(i_iPeilbuisNr):
    f = lambda k: 26*k - 15
    sResult = None
    if Get_MeasurementText_Flag(f(i_iPeilbuisNr)):
        sResult = Get_MeasurementText_Tekst(f(i_iPeilbuisNr))
    return sResult

# Purpose: Lengte zandvang van een gegeven peilbuis (# MEASUREMENTVAR 26k-11)
def Get_PBP_Peilbuis_LengtePeilbuis(i_iPeilbuisNr):
    f = lambda k: 26*k - 11
    fResult = None
    if Get_MeasurementVar_Flag(f(i_iPeilbuisNr)):
        fResult = Get_MeasurementVar_Value(f(i_iPeilbuisNr))
    return fResult

# Purpose: Lengte zandvang van een gegeven peilbuis (# MEASUREMENTVAR 26k-12)
def Get_PBP_Peilbuis_LengteZandvang(i_iPeilbuisNr):
    f = lambda k: 26*k - 12
    fResult = None
    if Get_MeasurementVar_Flag(f(i_iPeilbuisNr)):
        fResult = Get_MeasurementVar_Value(f(i_iPeilbuisNr))
    return fResult


# EOM
