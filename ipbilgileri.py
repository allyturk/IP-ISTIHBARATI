import json
import requests
import webbrowser
import os
#Karabağ=Azerbaycan=Türkiye=Turan
os.system("color a")
os.system("cls")
print(""" 
....::..::::::::::::::::::....:::......::::::..:::::....::..:::::..::........:::..:::::..::..:::::..::..:::::..:::::..:::::........::
:@alismsk234::::@alismsk234::::@alismsk234::::@alismsk234::::@alismsk234::::@alismsk234::::@alismsk234::::@alismsk234::::@alismsk234:
....::..::::::::::::::::::....:::......::::::..:::::....::..:::::..::........:::..:::::..::..:::::..::..:::::..:::::..:::::........::
'####:'########:::::::::::'####::'######::'########:'####:'##::::'##:'########:::::'###::::'########:::::'###::::'########:'##:::::::
. ##:: ##.... ##::::::::::. ##::'##... ##:... ##..::. ##:: ##:::: ##: ##.... ##:::'## ##::: ##.... ##:::'## ##:::... ##..:: ##:::::::
: ##:: ##:::: ##::::::::::: ##:: ##:::..::::: ##::::: ##:: ##:::: ##: ##:::: ##::'##:. ##:: ##:::: ##::'##:. ##::::: ##:::: ##:::::::
: ##:: ########::'#######:: ##::. ######::::: ##::::: ##:: #########: ########::'##:::. ##: ########::'##:::. ##:::: ##:::: ##:::::::
: ##:: ##.....:::........:: ##:::..... ##:::: ##::::: ##:: ##.... ##: ##.... ##: #########: ##.. ##::: #########:::: ##:::: ##:::::::
: ##:: ##:::::::::::::::::: ##::'##::: ##:::: ##::::: ##:: ##:::: ##: ##:::: ##: ##.... ##: ##::. ##:: ##.... ##:::: ##:::: ##:::::::
'####: ##:::::::::::::::::'####:. ######::::: ##::::'####: ##:::: ##: ########:: ##:::: ##: ##:::. ##: ##:::: ##:::: ##:::: ##:::::::
....::..::::::::::::::::::....:::......::::::..:::::....::..:::::..::........:::..:::::..::..:::::..::..:::::..:::::..:::::........::
:@alismsk234::::@alismsk234::::@alismsk234::::@alismsk234::::@alismsk234::::@alismsk234::::@alismsk234::::@alismsk234::::@alismsk234:
....::..::::::::::::::::::....:::......::::::..:::::....::..:::::..::........:::..:::::..::..:::::..::..:::::..:::::..:::::........::

""")
ipA = input("Hedef ip adresini gir>> ")
adres = ("https://tools.keycdn.com/geo.json?host="+ipA)
baglan = requests.post(adres)
baGlann = baglan.json()


print("İp adresi: "+baGlann["data"]["geo"]["ip"])
print("Konumu: "+baGlann["data"]["geo"]["timezone"])
print("Posta Kodu: "+baGlann["data"]["geo"]["postal_code"])
a = baGlann["data"]["geo"]["latitude"]
b = baGlann["data"]["geo"]["longitude"]
print("Koordinat: ",a,",",b)
c = baGlann["data"]["geo"]["city"]
d = baGlann["data"]["geo"]["region_code"]
print("Şehir ve şehir kodu: ",c,d)

soru = input("Koordinat adreslerine bakılsın mı? [E-H]>> ")
if soru == "e" or soru == "E":
    
    url = "https://www.google.com.tr/maps/search/"+str(a)+","+str(b)
    webbrowser.open(url)
elif soru == "h" or soru == "H":
    print(" [(:)] İyi günler [:)] ")
else:
    print("[!]Hatalı tuşlama[!]")
#88.227.59.77