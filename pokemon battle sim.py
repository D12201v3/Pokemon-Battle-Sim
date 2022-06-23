import tkinter
from unicodedata import name
import pokebase as pb

def GUI():
    top = tkinter.Tk()
    top.mainloop()

def Berry():
    global Aguav,Apicot,Aspear,Babiri,Belue,Bluk,Charti,Cheri,Chesto,Chilan,Chople,Coba,Colbur,Cornn,Custap,Durin,Enigma,Figy,Ganlon,Grepa,Haban,Hondew,Iapapa,Jaboca,Kasib,Kebia,Kee,Kelpsy,Lansat,Leppa,Liechi,Lum,Mago,Magost,Maranga,Micle,Nanab,Nomel,Occa,Oran
    global Pamtre,Passho,Payapa,Pecha,Persim,Petaya,Pinap,Pomeg,Qualot,Rabuta,Rawst,Razz,Rindo,Roseli,Rowap,Salac,Shuca,Sitrus,Spelon,Starf,Tomato,Tanga,Wacan,Watmel,Wepear,Wiki,Yache,Berry_list
    #Variables for berries and extra "berry" stats (ex.Natural gift type)
    Aguav = pb.APIResource('berry','aguav')
    Apicot = pb.APIResource('berry','apicot')
    Aspear =  pb.APIResource('berry','aspear')
    Babiri =  pb.APIResource('berry','babiri')
    Belue =  pb.APIResource('berry','belue')
    Bluk =  pb.APIResource('berry','bluk')
    Charti = pb.APIResource('berry','charti')
    Cheri = pb.APIResource('berry','cheri')
    Chesto = pb.APIResource('berry','chesto')
    Chilan = pb.APIResource('berry','chilan')
    Chople = pb.APIResource('berry','chople')
    Coba = pb.APIResource('berry','coba') 
    Colbur = pb.APIResource('berry','colbur')
    Cornn = pb.APIResource('berry','cornn')
    Custap = pb.APIResource('berry','custap')
    Durin = pb.APIResource('berry','durin')
    Enigma = pb.APIResource('berry','enigma')
    Figy = pb.APIResource('berry','figy')
    Ganlon = pb.APIResource('berry','ganlon')
    Grepa = pb.APIResource('berry','grepa')
    Haban = pb.APIResource('berry','haban')
    Hondew = pb.APIResource('berry','hondew')
    Iapapa = pb.APIResource('berry','iapapa')
    Jaboca = pb.APIResource('berry','jaboca')
    Kasib = pb.APIResource('berry','kasib')
    Kebia = pb.APIResource('berry','kebia')
    Kee = pb.APIResource('berry','kee')
    Kelpsy = pb.APIResource('berry','Kelpsy')
    Lansat = pb.APIResource('berry','lansat')
    Leppa = pb.APIResource('berry','leppa')
    Liechi = pb.APIResource('berry','liechi')
    Lum = pb.APIResource('berry','lum')
    Mago = pb.APIResource('berry','mago')
    Magost = pb.APIResource('berry','magost')
    Maranga = pb.APIResource('berry','maranga')
    Micle = pb.APIResource('berry','micle')
    Nanab = pb.APIResource('berry','nanab')
    Nomel = pb.APIResource('berry','nomel')
    Occa = pb.APIResource('berry','occa')
    Oran = pb.APIResource('berry','oran')
    Pamtre = pb.APIResource('berry','pamtre')
    Passho = pb.APIResource('berry','passho')
    Payapa = pb.APIResource('berry','payapa')
    Pecha = pb.APIResource('berry','pecha')
    Persim = pb.APIResource('berry','persim')
    Petaya = pb.APIResource('berry','petaya')
    Pinap = pb.APIResource('berry','pinap')
    Pomeg = pb.APIResource('berry','pomeg')
    Qualot = pb.APIResource('berry','qualot')
    Rabuta = pb.APIResource('berry','rabuta')
    Rawst = pb.APIResource('berry','rawst')
    Razz = pb.APIResource('berry','razz')
    Rindo = pb.APIResource('berry','rindo')
    Roseli = pb.APIResource('berry','roseli')
    Rowap = pb.APIResource('berry','rowap')
    Salac = pb.APIResource('berry','salac')
    Shuca = pb.APIResource('berry','shuca')
    Sitrus = pb.APIResource('berry','sitrus')
    Spelon = pb.APIResource('berry','spelon')
    Starf = pb.APIResource('berry','starf')
    Tomato = pb.APIResource('berry','tomato')
    Tanga = pb.APIResource('berry','tanga')
    Wacan = pb.APIResource('berry','wacan')
    Watmel = pb.APIResource('berry','watmel')
    Wepear = pb.APIResource('berry','wepear')
    Wiki = pb.APIResource('berry','wiki')
    Yache = pb.APIResource('berry','yache')
    Berry_list = [Aguav,Apicot,Aspear,Babiri,Belue,Bluk,Charti,Cheri,Chesto,Chilan,Chople,Coba,Colbur,Cornn,Custap,Durin,Enigma,Figy,Ganlon,Grepa,Haban,Hondew,Iapapa,Jaboca,Kasib,Kebia,Kee,Kelpsy,Lansat,Leppa,Liechi,Lum,Mago,Magost,Maranga,Micle,Nanab,Nomel,Occa,Oran,Pamtre,Passho,Payapa,Pecha,Persim,Petaya,Pinap,Pomeg,Qualot,Rabuta,Rawst,Razz,Rindo,Roseli,Rowap,Salac,Shuca,Sitrus,Spelon,Starf,Tomato,Tanga,Wacan,Watmel,Wepear,Wiki,Yache]
    #Makes *Berry*-berry variables for held item stats variables
    for x in Berry_list:
        bn1=x.name
        current_berry=bn1 + ('_stats')
        berry_name=bn1 + ('-berry')
        berry_api_data=pb.APIResource('item',berry_name)
        globals()[f'{current_berry}']=berry_api_data
   

Berry()
#for testing to see if it  worked
for x in Berry_list:
    print(x.name)




   
    