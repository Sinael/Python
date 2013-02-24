#-*- coding:windows-1250} -*-
import ephem
import datetime

print 'Planety układu słonecznego włączając słonce oraz księżyc' #intro
print 'Obserwatoria: Gdańsk, Warszawa, Kraków'

l = 's' ##domyslna wartosc start dla petli
while l!='z': #warunek zakonczenia
    h=0 #zmienne dalej przybierajace okreslone wartosci na poczatku petli domyslnie ustawione na 0
    i=0 #by przy kolejnym wykonywaniu whila nie powijawialy sie bledy
    x=0
    a=0
    a=raw_input()#wprowdzanie polskiej nazwy obiektu ktory nas interesuje
    slownik=['księżyc','słońce','merkury','wenus','ziemia','mars','jowisz','saturn','uran','neptun'] #tablica polskich zmiennych
    if a==slownik[0]:#sprawdzanie elementow tablicy z angielskimi zmiennymi z biblioteki
        x=ephem.Moon() #petla byla bardziej pomyslowa ale zostawiala dziury
    if a==slownik[1]:
        x=ephem.Sun()
    if a==slownik[2]:
        x=ephem.Mercury()
    if a== slownik[3]:
        x=ephem.Venus()
    if a==slownik[5]:
        x=ephem.Mars()
    if a==slownik[6]:
        x=ephem.Jupiter()
    if a==slownik[7]:
        x=ephem.Saturn()
    if a==slownik[8]:
        x=ephem.Uranus()
    if a==slownik[9]:
        x=ephem.Neptune()
    if a==slownik[4]:
        print 'jesteś na ziemi więc weź sobie mape' #brak przypisania ziemi ze wzgledu na sprawdzanie danych planet z okreslonego punktu na naszym globie
    x.compute()
 #jakiekolwiek zmienne nie zawarte w tabeli prowdza do braku przypisania zmiennej z biblioteki i blokuja dalsze wykonywanie programu

    miasto = raw_input() #wybor miasta zgodnie z intro
    if miasto =='Gdańsk' or miasto =='Warszawa' or miasto =='Kraków':
        if miasto =='Gdańsk':
            gdansk = ephem.Observer() #utworzenie 'obserwatora'
            gdansk.lat = '52.22' #przypisanie obserwatorowi przyblizonych wspolzednych na ziemi
            gdansk.long = '18.38'
            print 'najdogodniejsza pora obserwacji', gdansk.next_transit(x) #gdansk - przypisany punkt, .next_transit najblizsza data gdy obiekt przemieszcza się nad obserwatorem
            #zmienna (x) pobranie z biblioteki danych o obiekcie, ktory nas interesuje (dlugosc orbity, czas obiegu w okol slonca)
            x.compute(gdansk) #laczenie wszystkich danych (x) zmienne biblioteki, compute koemnda, (gdansk)dane obserwatora
        if miasto =='Warszawa':
            warszawa = ephem.Observer()
            warszawa.lat = '52.15'
            warszawa.long = '21.01'
            print 'najdogodniejsza pora obserwacji', warszawa.next_transit(x)
            x.compute(warszawa)
        if miasto =='Kraków':
            krakow = ephem.Observer()
            krakow.lat = '50.03'
            krakow.long = '19.56'
            print 'najdogodniejsza pora obserwacji', krakow.next_transit(x)
            x.compute(krakow)
    else:
        x=0

    h=x.earth_distance #przypisanie zmiennej h wartosci odleglosci ciala od ziemi (podane w Au - jednostkach astronomicznych)
    h=h*150000000 #1 AU = ~150mln km przypisanie zmiennej h odleglosci podanej w km
    print 'dystans od ziemi', x.earth_distance, 'AU','okolo',h,'km' #podanie odleglosci w dwoch miarach
    if ephem.constellation(x) == ('Ari','Aries'): #zamiana anielskich skrotow i nazw gwiazdozbiorow na polskie odpowiedniki
        print 'Obecnie w gwiazdozbiorze Barana' #wypisanie nazwy gwiazdozbioru
    if ephem.constellation(x) == ('Tau','Taurus'):
        print 'obecnie w gwiazdozbiorze Byka'
    if ephem.constellation(x) == ('Gem','Gemini'):
        print 'Obecnie w gwiazdozbiorze Blizniat'
    if ephem.constellation(x) == ('Can','Cancer'):
        print 'Obecznie w gwiazdozbiorze Raka'
    if ephem.constellation(x) == ('Leo','Leo'):
        print ' Obecnie w gwiazdozbiorze Lwa'
    if ephem.constellation(x) == ('Vir','Virgo'):
        print 'Obecnie w giwazdozbiorze Panny'
    if ephem.constellation(x) == ('Lib','Libra'):
        print 'Obecnie w gwiazdozbiorze Wagi'
    if ephem.constellation(x) == ('Scr','Scorpio'):
        print 'Obecnie w gwiazdozbiorze Skorpiona'
    if ephem.constellation(x) == ('Sag','Sagittarius'):
        print 'Obecnie w gwiazdozbiorze Strzelca'
    if ephem.constellation(x) == ('Cap','Capicorn'):
        print 'Obecnie w gwiazdozbiorze Koziorożca'
    if ephem.constellation(x) == ('Aqr','Aquarius'):
        print 'Obecnie w giwazdozbiorze Wodnika'
    if ephem.constellation(x) == ('Cet','Cetus'):
        print 'Obecnie w gwiazdozbiorze Ryb' 



   ## print x, ephem.constellation(x) ##dane kontrolne

    print 's by powtórzyć lub z by zakonczyć '
    data = datetime.datetime.now().date() ##przypisanie zmiennej daty
    f =open('nowy.txt','a')
    lista =['data: ',str(data),' ',miasto,' ',a, ' odleglosc= ',str(h),'km',' ','konstelacja = ',str(ephem.constellation(x)),'\n'] ##tabela z elementami do wypisania
    f.writelines(lista)
    f.close()

    l=raw_input()
    if l=='s' or l=='z': #warunek ponownego przejscia glownej petli
        continue #spelnienie go - kontynuacja dzialania i dalsza zabawa
    else:
        break #wpisanie byle czego -zatrzymanie, brak zainteresowania

