#!env/bin/python
# Datum:  1 Februari 2016
# Waterbug,waterbug@bitmessage.ch

import re
import os
import pickle
import ast
import sys


# Hulpfuncties
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def removetrailers(string):
    d = re.sub('^[\t|\ ]*', '', string)
    e = re.sub('\r\n$', '', d)
    return e


class Gef2OpenClass:
    def __init__(self):
        print "init"

    # Purpose: Of een BORE-Report file is (boring)
    def gbr_is_gbr(self):
        if 'PROCEDURECODE' in self.headerdict:
            if 'GEF-BORE-Report' in self.headerdict['PROCEDURECODE']:
                out = True
            else:
                out = False
        else:
            if 'REPORTCODE' in self.headerdict:
                if 'GEF-BORE-Report' in self.headerdict['REPORTCODE']:
                    out = True
                else:
                    out = False
            else:
                out = False
        try:
            return out
        except:
            return None

    # Purpose: Of een GEF-CPT-Report file is (sondering)
    def gcr_is_gcr(self):
        if 'PROCEDURECODE' in self.headerdict:
            if 'GEF-CPT-Report' in self.headerdict['PROCEDURECODE']:
                out = True
            else:
                out = False
        else:
            if 'REPORTCODE' in self.headerdict:
                if 'GEF-CPT-Report' in self.headerdict['REPORTCODE']:
                    out = True
                else:
                    out = False
            else:
                out = False
        try:
            return out
        except:
            return None

    # Purpose: Of #COMPANYID aanwezig
    def get_companyid_flag(self):
        if 'COMPANYID' in self.headerdict:
            if len(self.headerdict['COMPANYID']) > 0:
                out = True
            else:
                out = False
        else:
            out = False
        try:
            return out
        except:
            return None

    # Purpose: Geeft aantal kolommen in het data block
    def get_column(self):
        if 'COLUMN' in self.headerdict:
            if len(self.headerdict['COLUMN']) > 0:
                out = self.headerdict['COLUMN'][0]
            else:
                err = 'MissingValue'
        else:
            err = 'MissingKeyword'
        try:
            return out
        except:
            # return None
            return 'Error:%s' % (err)

    # Purpose: Of #COLUMN aanwezig
    def get_column_flag(self):
        if ('COLUMN' in self.headerdict):
            if len(self.headerdict['COLUMN']) > 0:
                out = True
            else:
                out = False
        else:
            out = False
        try:
            return out
        except:
            return None

    # Purpose: Geeft company naam
    def get_companyid_Name(self):
        if 'COMPANYID' in self.headerdict:
            if len(self.headerdict['COMPANYID']) > 0:
                out = self.headerdict['COMPANYID'][0]
            else:
                err = 'MissingValue'
        else:
            err = 'MissingKeyword'
        try:
            return out
        except:
            # return None
            return 'Error:%s' % (err)

    # Purpose: Geeft waarde uit bepaalde cel van data block
    def get_data(self, i_Kol, iRij):
        if 'datablok' in self.headerdict:
            if iRij in self.headerdict['datablok']:
                if len(self.headerdict['datablok'][iRij]) >= i_Kol - 1:
                    out = self.headerdict['datablok'][iRij][i_Kol - 1]
                else:
                    err = 'MissingKol'
            else:
                err = 'MissingRij'
        else:
            err = 'MissingDatablok'
        try:
            return out
        except:
            # return None
            return err

    # Purpose: Of gegeven #MEASUREMENTTEXT index aanwezig
    def get_measurementtext_flag(self, i_Index):
        if 'MEASUREMENTTEXT' in self.headerdict:
            if i_Index in self.headerdict['MEASUREMENTTEXT']:
                out = True
            else:
                out = False
        else:
            out = False
        try:
            return out
        except:
            return None

    # Purpose: Of gegeven #MEASUREMENTVAR index aanwezig
    def get_measurementvar_flag(self, i_Index):
        if 'MEASUREMENTVAR' in self.headerdict:
            if i_Index in self.headerdict['MEASUREMENTVAR']:
                out = True
            else:
                out = False
        else:
            out = False
        try:
            return out
        except:
            return None

    # Purpose: Geeft measurementtext tekst
    def get_measurementtext_Tekst(self, i_Index):
        if 'MEASUREMENTTEXT' in self.headerdict:
            if i_Index in self.headerdict['MEASUREMENTTEXT']:
                if 1 in self.headerdict['MEASUREMENTTEXT'][i_Index]:
                    out = self.headerdict['MEASUREMENTTEXT'][i_Index][1]  # ??
                else:
                    err = 'MissingValue'
            else:
                err = 'MissingIndex'
        else:
            err = 'MissingKeyword'
        try:
            return out
        except:
            # return None
            return 'Error:%s' % (err)

    # Purpose: Geeft measurementvar value
    def get_measurementvar_Value(self, i_Index):
        if 'MEASUREMENTVAR' in self.headerdict:
            if i_Index in self.headerdict['MEASUREMENTVAR']:
                if len(self.headerdict['MEASUREMENTVAR'][i_Index]) > 0:
                    out = self.headerdict['MEASUREMENTVAR'][i_Index][1]
                else:
                    err = 'MissingValue'
            else:
                err = 'MissingIndex'
        else:
            err = 'MissingKeyword'
        try:
            return out
        except:
            # return None
            return 'Error:%s' % (err)

    # Purpose: Geeft aantal rijen in het data block
    # neem aan waarde achter 'LASTSCAN', maar check dit!
    def get_nr_scans(self):
        if 'LASTSCAN' in self.headerdict:
            if len(self.headerdict['LASTSCAN']) > 0:
                out = self.headerdict['LASTSCAN'][0]
            else:
                err = 'MissingValue'
        else:
            err = 'MissingKeyword'
        try:
            return out
        except:
            # return None
            return 'Error:%s' % (err)

    # Purpose: Of #PARENT aanwezig
    # neeem aan dat er een par 'PARENT' aanwezig moet zijn. Check!
    def get_parent_flag(self):
        if ('PARENT' in self.headerdict):
            if len(self.headerdict['PARENT']) > 0:
                out = True
            else:
                out = False
        else:
            out = False
        try:
            return out
        except:
            return None  # test

    # Purpose: Geeft referentie naar de parent, bv bestandsnaam
    def get_parent_reference(self):
        if 'PARENT' in self.headerdict:
            if len(self.headerdict['PARENT']) > 0:
                out = self.headerdict['PARENT'][0]
            else:
                err = 'MissingValue'
        else:
            err = 'MissingKeyword'
        try:
            return out
        except:
            return 'Error:%s' % (err)

    # Purpose: Of #PROCEDURECODE aanwezig
    def get_procedurecode_flag(self):
        if 'PROCEDURECODE' in self.headerdict:
            if len(self.headerdict['PROCEDURECODE']) > 0:
                out = True
            else:
                out = False
        else:
            out = False
        try:
            return out
        except:
            return None

    # Purpose: Geeft procedurecode code
    def get_procedurecode_Code(self):
        if 'PROCEDURECODE' in self.headerdict:
            if len(self.headerdict['PROCEDURECODE']) > 0:
                out = self.headerdict['PROCEDURECODE'][0]
            else:
                err = 'MissingValue'
        else:
            err = 'MissingKeyword'
        try:
            return out
        except:
            # return None
            return 'Error:%s' % (err)

    # Purpose: Of #PROJECTID aanwezig
    def get_projectid_flag(self):
        if 'PROJECTID' in self.headerdict:
            if len(self.headerdict['PROJECTID']) > 0:
                out = True
            else:
                out = False
        try:
            return out
        except:
            return None

    # Purpose: Geeft projectid nummer
    def get_projectid_Number(self):
        if 'PROJECTID' in self.headerdict:
            if len(self.headerdict['PROJECTID']) > 1:
                out = self.headerdict['PROJECTID'][1]
            else:
                err = 'MissingValue'
        else:
            err = 'MissingKeyword'
        try:
            return out
        except:
            # return None
            return 'Error:%s' % (err)

    # Purpose: Of #REPORTCODE aanwezig
    def get_reportcode_flag(self):
        if 'REPORTCODE' in self.headerdict:
            if len(self.headerdict['REPORTCODE']) > 0:
                out = True
            else:
                out = False
        else:
            out = False
        try:
            return out
        except:
            return None

    # Purpose: Geeft reportcode code
    def get_reportcode_Code(self):
        if 'REPORTCODE' in self.headerdict:
            if len(self.headerdict['REPORTCODE']) > 0:
                out = self.headerdict['REPORTCODE'][0]
            else:
                err = 'MissingValue'
        else:
            err = 'MissingKeyword'
        try:
            return out
        except:
            # return None
            return 'Error:%s' % (err)

    # Purpose: Of #STARTDATE aanwezig
    def get_startdate_flag(self):
        if 'STARTDATE' in self.headerdict:
            if len(self.headerdict['STARTDATE']) > 2:
                out = True
            else:
                out = False
        else:
            out = False
        try:
            return out
        except:
            return None

    # Purpose: Geeft startdate jaar (yyyy)
    def get_startdate_Yyyy(self):
        if 'STARTDATE' in self.headerdict:
            if len(self.headerdict['STARTDATE']) > 2:
                out = int(self.headerdict['STARTDATE'][0])
            else:
                err = 'MissingValue'
        else:
            err = 'MissingKeyword'
        try:
            return out
        except:
            # return None
            return 'Error:%s' % (err)

    # Purpose: Geeft startdate maand (mm)
    def get_startdate_Mm(self):
        if 'STARTDATE' in self.headerdict:
            if len(self.headerdict['STARTDATE']) > 2:
                out = int(self.headerdict['STARTDATE'][1])
            else:
                err = 'MissingValue'
        else:
            err = 'MissingKeyword'
        try:
            return out
        except:
            # return None
            return 'Error:%s' % (err)

    # Purpose: Geeft startdate dag (dd)
    def get_startdate_Dd(self):
        if 'STARTDATE' in self.headerdict:
            if len(self.headerdict['STARTDATE']) > 2:
                out = int(self.headerdict['STARTDATE'][2])
            else:
                err = 'MissingValue'
        else:
            err = 'MissingKeyword'
        try:
            return out
        except:
            # return None
            return 'Error:%s' % (err)

    # Purpose: Of #XYID aanwezig
    def get_xyid_flag(self):
        if 'XYID' in self.headerdict:
            if len(self.headerdict['XYID']) > 2:
                out = True
            else:
                out = False
        try:
            return out
        except:
            return None

    # Purpose: Geeft X coordinaat
    def get_xyid_X(self):
        if 'XYID' in self.headerdict:
            if len(self.headerdict['XYID']) > 0:
                out = self.headerdict['XYID'][1]
            else:
                err = 'MissingValue'
        else:
            err = 'MissingKeyword'
        try:
            return out
        except:
            # return None
            return 'Error:%s' % (err)

    # Purpose: Geeft Y coordinaat
    def get_xyid_Y(self):
        if 'XYID' in self.headerdict:
            if len(self.headerdict['XYID']) > 1:
                out = self.headerdict['XYID'][2]
            else:
                err = 'MissingValue'
        else:
            err = 'MissingKeyword'
        try:
            return out
        except:
            # return None
            return 'Error:%s' % (err)

    # Purpose: Of #ZID aanwezig
    def get_zid_flag(self):
        if 'ZID' in self.headerdict:
            if len(self.headerdict['ZID']) > 0:
                out = True
            else:
                out = False
        else:
            out = False
        try:
            return out
        except:
            return None

    # Purpose: Geeft Z coordinaat
    def get_zid_Z(self):
        if 'ZID' in self.headerdict:
            if len(self.headerdict['ZID']) > 1:
                out = self.headerdict['ZID'][1]
            else:
                err = 'MissingValue'
        else:
            err = 'MissingKeyword'
        try:
            return out
        except:
            # return None
            return 'Error:%s' % (err)

    # Purpose: Initialiseren interne geheugenstructuur
    # niet nodig
    def init_gef(self):
        True

    # Purpose: Geeft kolom nummer die correspondeert met gegeven 'quantity
    #          number', en 0 wanneer deze niet aanwezig.
    # Note   : Bv, quantity number voor 'gecorrigeerde diepte' is 11.
    def qn2column(self, i_iQtyNumber):
        try:
            if i_iQtyNumber == 1:
                out = 0
                for i in self.headerdict['COLUMNINFO']:
                    j = self.headerdict['COLUMNINFO'][i]
                    if 'sondeerlengte' in str.lower(str(j)):
                        out = j[0]
                    if 'penetration length' in str.lower(str(j)):
                        out = j[0]
                    if 'diepte bovenkant' in str.lower(str(j)):
                        out = j[0]
                    if 'laag van' in str.lower(str(j)):
                        out = j[0]
            elif i_iQtyNumber == 11:
                out = 0
                for i in self.headerdict['COLUMNINFO']:
                    j = self.headerdict['COLUMNINFO'][i]
                    if 'gecorrigeerde diepte' in str.lower(str(j)):
                        out = j[0]
            return int(out)
        except:
            # return None
            return 'Error: Index nog niet verwerkt in library'

    # Purpose: Leest een gegeven Gef bestand en zet alle info in een dictionary
    def read_gef(self, i_sBestandGef):
        EOH = False
        try:
            multipars = ['COLUMNINFO', 'COLUMNVOID', 'MEASUREMENTTEXT', 'MEASUREMENTVAR', 'SPECIMENVAR', 'SPECIMENTEXT']
            self.headerdict = {}
            f = open(i_sBestandGef, 'r')
            tel = 0
            for line in f.readlines():
                line = re.sub('\r\n', '', line)  # haal alle \r\n aan het einde van de regel weg
                linetmp = re.sub('(^[ \t]*)', '', line)  # remove trailing whitespace
                # if not re.sub('^[\ \t]*$','',line)=='': # lege regels uitsluiten. moet dit in test_gef?
                if not re.sub('^[\ \t]{0,}\n', '', linetmp) == '':  # lege regels uitsluiten. moet dit in test_gef?
                    if 1 == 1:  # test1: begint line1 met '#' en komt '=' minstens 1x voor
                        line = linetmp.split('=', 1)
                        par = re.sub('^#([^ \t]*)[ \t]*$', '\\1', line[0])
                        # start test
                        # if par == 'EOH': deel='data'
                        if EOH is False and not re.sub('^[^#].*', '',
                                                       linetmp) == '':  # er komen regels niet begin met # voor.
                            # einde test
                            if len(line) > 1:
                                keyinfo = line[1]
                                keyinfo = re.sub('(^[ \t]*)', '', keyinfo)  # remove trailing whitespace
                                keyinfo = re.sub('([,])([ \t])+', '\\1', re.sub('([ \t])+([,])', '\\2',
                                                                                keyinfo))  # haal eerst alle witruimte (spaties/tabs) rond de separators (',') weg. 15-10-29
                                if keyinfo <> '':
                                    # print 'keyinfo: %s'%(keyinfo)
                                    keyinfo = keyinfo.split(',')
                                else:
                                    keyinfo = None
                            else:
                                keyinfo = None
                            b = keyinfo
                            # print 'b: %s'%(b)
                            if par in multipars:  # tabje hoger gezet zodat conditie alleen geldt als een par bestaat. 2015-10-29
                                if is_number(b[0]):
                                    parno = float(b[0])
                                else:
                                    parno = b[0]
                                # del keyinfo[0]
                                testpar = 'par1'
                                c = []
                                if keyinfo is not None:
                                    for i in b:
                                        e = removetrailers(i)
                                        if is_number(e):
                                            c.append(float(e))
                                        else:
                                            c.append(e)
                                    if par not in self.headerdict:
                                        self.headerdict[par] = {parno: c}
                                    else:
                                        self.headerdict[par][parno] = c
                                else:
                                    parno = None
                        if par == 'EOH':
                            self.headerdict['datablok'] = {}
                            EOH = True
                            self.headerdict[par] = {}
                        if EOH is True and par <> 'EOH':
                            tel = tel + 1
                            data = par
                            data = re.sub(';!', '', data)  # einde dataregel. moet hier een test op?
                            data = re.sub("'", "", data)
                            data = re.sub('"', '', data)
                            data = re.split(';|\ |\t|\n', data)
                            a2 = []
                            for i in data:
                                if is_number(i):
                                    a2.append(float(i))
                                else:
                                    a2.append(i)
                            self.headerdict['datablok'][tel] = a2
                        if (par <> 'EOH') and (par not in multipars) and (EOH is not True):
                            testpar = 'par2'
                            c = []
                            if b is not None:
                                for i in b:
                                    e = removetrailers(i)
                                    if is_number(e):
                                        c.append(float(e))
                                    else:
                                        c.append(e)
                                self.headerdict[par] = c

            return True

        except IndexError:
            print (
                "%s Headerdict() in UtlGefOpen.py geef IndexError: fout bij uitlezen gef" % os.path.basename(
                    i_sBestandGef))
            return False

    # Purpose: Of een bestand geplot kan worden
    def is_plotable(self):
        return 'datmoetenwenogeensuitzoeken'

    # Purpose: Of een bepaald aspect van een bestand correct is
    # Parms  : Toegestaan: 'HEADER', 'DATA', 'GEF-CPT-Report','GEF-BORE-Report'
    def test_gef(self, i_sAspect):
        return 'datmoetenwenogeensuitzoeken'


if __name__ == '__main__':
    # This is used for debugging. Using this separated structure makes it much
    # easier to debug using standard Python development tools.

    tool = Gef2OpenClass()
    tool.read_gef(r'p:\1248421\GIS\Import\Tauw\GEFTEST01.gef')

    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(tool.headerdict)
