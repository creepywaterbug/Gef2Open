# -----------------------------------------------------------------------------
# Name   : UtlGef.py
# Purpose: Set van Gef gerelateerde functies.
# Note   : - gaat ervan uit dat Gef2.dll bereikbaar is via search path
#          - standaard data type voor dll functie return (restype):
#            ctypes.c_int (= Python int/long)
# Versies: Python 2.5, ArcGIS 9.3.1
# Updated: PL, 13 Jul 2012
# Updated: Waterbug, 1 Februari 2016: Alleen de functies die rechtstreeks gef2.dll
#	   aanroepen zijn (ongewijzigd) overgenomen. De rest is weg gelaten
# -----------------------------------------------------------------------------

# System module
import ctypes, datetime

# Globale constante
oDll = ctypes.windll.Gef2

# -----------------------------------------------------------------------------
# CATEGORIE A. een-op-een vertalingen uit de gef2.dll
# -----------------------------------------------------------------------------

# Purpose: Vrijgeven interne geheugenstructuur
def Free_Gef():
    oFunc = oDll.free_gef
    iRetVal = oFunc()
    return bool(iRetVal)

# Purpose: Of een GEF-BORE-Report file is (boring)
def Gbr_Is_Gbr():
    oFunc = oDll.gbr_is_gbr
    iRetVal = oFunc()
    return bool(iRetVal)

# Purpose: Of een GEF-CPT-Report file is (sondering)
def Gcr_Is_Gcr():
    oFunc = oDll.gcr_is_gcr
    iRetVal = oFunc()
    return bool(iRetVal)

# Purpose: Of #COMPANYID aanwezig
def Get_CompanyID_Flag():
    oFunc = oDll.get_companyid_flag
    iRetVal = oFunc()
    return bool(iRetVal)

# Purpose: Geeft aantal kolommen in het data block
def Get_Column():
    oFunc = oDll.get_column
    iRetVal = oFunc()
    return iRetVal

# Purpose: Of #COLUMN aanwezig
def Get_Column_Flag():
    oFunc = oDll.get_column_flag
    iRetVal = oFunc()
    return bool(iRetVal)

# Purpose: Geeft company naam
def Get_CompanyID_Name():
    oFunc = oDll.get_companyid_Name
    oFunc.restype = ctypes.c_char_p # apart aangeven
    sRetVal = oFunc()
    return sRetVal

# Purpose: Geeft waarde uit bepaalde cel van data block
def Get_Data(i_Kol, iRij):
    oFunc = oDll.get_data
    oFunc.restype = ctypes.c_double # apart aangeven
    fRetVal = oFunc(i_Kol, iRij)
    return fRetVal

# Purpose: Of gegeven #MEASUREMENTTEXT index aanwezig
def Get_MeasurementText_Flag(i_Index):
    oFunc = oDll.get_measurementtext_flag
    iRetVal = oFunc(i_Index)
    return bool(iRetVal)

# Purpose: Of gegeven #MEASUREMENTVAR index aanwezig
def Get_MeasurementVar_Flag(i_Index):
    oFunc = oDll.get_measurementvar_flag
    iRetVal = oFunc(i_Index)
    return bool(iRetVal)

# Purpose: Geeft measurementtext tekst
def Get_MeasurementText_Tekst(i_Index):
    oFunc = oDll.get_measurementtext_Tekst
    oFunc.restype = ctypes.c_char_p # apart aangeven
    sRetVal = oFunc(i_Index)
    return sRetVal

# Purpose: Geeft measurementvar value
def Get_MeasurementVar_Value(i_Index):
    oFunc = oDll.get_measurementvar_Value
    oFunc.restype = ctypes.c_float # apart aangeven
    fRetVal = oFunc(i_Index)
    return round(fRetVal, 3) # rond af op 3 decimalen

# Purpose: Geeft aantal rijen in het data block
def Get_Nr_Scans():
    oFunc = oDll.get_nr_scans
    iRetVal = oFunc()
    return iRetVal

# Purpose: Of #PARENT aanwezig
def Get_Parent_Flag():
    oFunc = oDll.get_parent_flag
    iRetVal = oFunc()
    return bool(iRetVal)

# Purpose: Geeft referentie naar de parent, bv bestandsnaam
def Get_Parent_Reference():
    oFunc = oDll.get_parent_reference
    oFunc.restype = ctypes.c_char_p # apart aangeven
    sRetVal = oFunc()
    return sRetVal

# Purpose: Of #PROCEDURECODE aanwezig
def Get_ProcedureCode_Flag():
    oFunc = oDll.get_procedurecode_flag
    iRetVal = oFunc()
    return bool(iRetVal)

# Purpose: Geeft procedurecode code
def Get_ProcedureCode_Code():
    oFunc = oDll.get_procedurecode_Code
    oFunc.restype = ctypes.c_char_p # apart aangeven
    sRetVal = oFunc()
    return sRetVal

# Purpose: Of #PROJECTID aanwezig
def Get_ProjectID_Flag():
    oFunc = oDll.get_projectid_flag
    iRetVal = oFunc()
    return bool(iRetVal)

# Purpose: Geeft projectid nummer
def Get_ProjectID_Number():
    oFunc = oDll.get_projectid_Number
    oFunc.restype = ctypes.c_char_p # apart aangeven
    sRetVal = oFunc()
    return sRetVal

# Purpose: Of #REPORTCODE aanwezig
def Get_ReportCode_Flag():
    oFunc = oDll.get_reportcode_flag
    iRetVal = oFunc()
    return bool(iRetVal)

# Purpose: Geeft reportcode code
def Get_ReportCode_Code():
    oFunc = oDll.get_reportcode_Code
    oFunc.restype = ctypes.c_char_p # apart aangeven
    sRetVal = oFunc()
    return sRetVal

# Purpose: Of #STARTDATE aanwezig
def Get_StartDate_Flag():
    oFunc = oDll.get_startdate_flag
    iRetVal = oFunc()
    return bool(iRetVal)

# Purpose: Geeft startdate jaar (yyyy)
def Get_StartDate_Yyyy():
    oFunc = oDll.get_startdate_Yyyy
    iRetVal = oFunc()
    return iRetVal

# Purpose: Geeft startdate maand (mm)
def Get_StartDate_Mm():
    oFunc = oDll.get_startdate_Mm
    iRetVal = oFunc()
    return iRetVal

# Purpose: Geeft startdate dag (dd)
def Get_StartDate_Dd():
    oFunc = oDll.get_startdate_Dd
    iRetVal = oFunc()
    return iRetVal

# Purpose: Of #XYID aanwezig
def Get_XYID_Flag():
    oFunc = oDll.get_xyid_flag
    iRetVal = oFunc()
    return bool(iRetVal)

# Purpose: Geeft X coordinaat
def Get_XYID_X():
    oFunc = oDll.get_xyid_X
    oFunc.restype = ctypes.c_double # apart aangeven
    fRetVal = oFunc()
    return fRetVal

# Purpose: Geeft Y coordinaat
def Get_XYID_Y():
    oFunc = oDll.get_xyid_Y
    oFunc.restype = ctypes.c_double # apart aangeven
    fRetVal = oFunc()
    return fRetVal

# Purpose: Of #ZID aanwezig
def Get_ZID_Flag():
    oFunc = oDll.get_zid_flag
    iRetVal = oFunc()
    return bool(iRetVal)

# Purpose: Geeft Z coordinaat
def Get_ZID_Z():
    oFunc = oDll.get_zid_Z
    oFunc.restype = ctypes.c_double # apart aangeven
    fRetVal = oFunc()
    return fRetVal

# Purpose: Initialiseren interne geheugenstructuur
def Init_Gef():
    oFunc = oDll.init_gef
    iRetVal = oFunc()
    return bool(iRetVal)

# Purpose: Of een bestand geplot kan worden
def Is_Plotable():
    oFunc = oDll.is_plotable
    iRetVal = oFunc()
    return bool(iRetVal)

# Purpose: Geeft kolom nummer die correspondeert met gegeven 'quantity
#          number', en 0 wanneer deze niet aanwezig.
# Note   : Bv, quantity number voor 'gecorrigeerde diepte' is 11.
def Qn2Column(i_iQtyNumber):
    oFunc = oDll.qn2column
    iRetVal = oFunc(i_iQtyNumber)
    return iRetVal

# Purpose: Leest een gegeven Gef bestand in geheugen
def Read_Gef(i_sBestandGef):
    oFunc = oDll.read_gef
    iRetVal = oFunc(i_sBestandGef)
    return bool(iRetVal)

# Purpose: Of een bepaald aspect van een bestand correct is
# Parms  : Toegestaan: 'HEADER', 'DATA', 'GEF-CPT-Report','GEF-BORE-Report'
# Note   : - heb gemerkt dat deze functie bij aanroep met parm 'GEF-CPT-Report'
#            bij een corrupte gef een onverwachte fout kan genereren:
#            WindowsError: exception: access violation reading 0x00000004
def Test_Gef(i_sAspect):
    oFunc = oDll.test_gef
    iRetVal = oFunc(i_sAspect)
    return bool(iRetVal)
