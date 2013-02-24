import datetime
import fileinput
def sprawdz(p):
    l=int(p[10])
    suma =((1*int(p[0]))+3*int(p[1])+(7*int(p[2]))+(9*int(p[3]))+(1*int(p[4]))+(3*int(p[5]))+(7*int(p[6]))+(9*int(p[7]))+(1*int(p[8]))+(3*int(p[9])))
    lm = (suma%10) ## dzielenie wyniku modulo 10
    kontrola=(10-lm) #sprawdzenie ostatniej liczby kontrolnej
    if (kontrola==10) or (l==kontrola): #w przypadku liczby kontrolnej 10 i 0 sa jednoznaczne a 0 moze byc wynikiem odejmowania
        return 1 ##domyslana wartosc logczna dla ifa klasy roboczej
    else:
        return 0 ##domyslna wartosc logiczna dla elsa
class robocza():
    def index():
        plik= open ('pesel.txt') ##otworzenie pliku do odczytu
        f =open('nowy.txt','a') ## do zapisu z opcja by program dopisywal na koncu dane
        while 1: #nieskonczony while
            pobranie=plik.readline() #czytanie pliku po linii
            if not pobranie: #zakoncz petle jezeli nie ma juz lini w pliku
                break 
            else:
                p=int(pobranie[9]) %2 ##pobranie 10 elementu z peselu okreslajacego plec wlasciciela
                r=int(pobranie[0:2]) ##pobranie koncowki roku z poczatku peselu
                m=int(pobranie[2:4]) ##miesiac
                d=int(pobranie[4:6]) ##dzien
                
                if (sprawdz(pobranie)) and d<=31 and m<=32 and d>0: ##ograniczenie miesiacy do 32 ze wzgledu na zamiane dla dzieci urodzonych po 2000r
                        if p ==1:#parzyste mezczyzni
                                plec = "M"
                        else:
                                plec = "F"
                        if r<99 and r>12 and m<=12: ##ograniczenie roku i miesiaca, co juz wyklucza daty powyzej 2000r
                                pr=1900 ##dodanie poczatku daty
                                m=pobranie[2:4]
                        elif r>=01 and r<=12 and m>=21 and m<=29:
                                pr=2000
                                m=pobranie[0:4:3]
                        elif r>=01 and r<=12 and m==30:
                                pr=2000
                                m=(m-20)
                        elif r>=01 and r<=12 and m==31:
                                pr=2000
                                m=(m-20)
                        elif r>=01 and r<=12 and m==32:
                                pr=2000
                                m=(m-20)
                else:
                    f.write('bledny pesel: ') ## w przypadku blednego peselu wpisanie uwagi do dokumentu
                year = datetime.date.today().year ##wpobranie czesci daty z biblioteki 
                wiek= year - (pr+r) ## wyliczenie wieku wlasciciela
                lista =[str(pr+r),' ',str(m),' ',str(d),' ',plec,' ',str(wiek),' ','\n'] #lista stringow do zapisu 
                zapis = f.writelines(lista) ## zapis
        f.close()
        plik.close()
                
        
    index()
        
