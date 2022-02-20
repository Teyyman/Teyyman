import os
import platform
import sys
import time
import pyautogui


#####  DÉBUT #####

def restart():
    couleur("9", "f")
    clean()
    ASCII()
    loading(True)
    menu()

def start():
    couleur("9", "f")
    pressTouche('f11')
    clean()
    ASCII()
    loading(True)
    menu()


#####  ECHAP  #####

#####  DÉCO  #####

def couleur(fond="0", lettre="f"):
    os.system("color " + fond + lettre + "")

def clean():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")

def loading(x=5, done=False):
    x = 5
    for i in range(x):
        sys.stdout.write('\rloading |')
        time.sleep(0.1)
        sys.stdout.write('\rloading /')
        time.sleep(0.1)
        sys.stdout.write('\rloading -')
        time.sleep(0.1)
        sys.stdout.write('\rloading \\')
        time.sleep(0.1)
    if done == True:
        sys.stdout.write('\rDone!     ')
        time.sleep(1.5)
    clean()
    ASCII()

def ASCII():
    __header__ ="""

    d888888b d888888b .88b  d88. d88888b       .o88b.  .d88b.  d8b   db db    db d88888b d8888b. d888888b d88888b d8888b. 
    `~~88~~'   `88'   88'YbdP`88 88'          d8P  Y8 .8P  Y8. 888o  88 88    88 88'     88  `8D `~~88~~' 88'     88  `8D 
       88       88    88  88  88 88ooooo      8P      88    88 88V8o 88 Y8    8P 88ooooo 88oobY'    88    88ooooo 88oobY' 
       88       88    88  88  88 88           8b      88    88 88 V8o88 `8b  d8' 88      88`8b      88    88      88`8b   
       88      .88.   88  88  88 88.          Y8b  d8 `8b  d8' 88  V888  `8bd8'  88.     88 `88.    88    88.     88 `88. 
       YP    Y888888P YP  YP  YP Y88888P       `Y88P'  `Y88P'  VP   V8P    YP    Y88888P 88   YD    YP    Y88888P 88   YD 
                                                                                                                      
                                                                                                                      

                                                                                      
    """

    print(__header__)

def pressTouche(touche):
    touche = 'f11'
    pyautogui.press(touche)

#####  MENU  #####

def menu():
    print("1. Write in second")
    print("2. Write in minute")
    print("3. Write in hour")
    print("4. Write in day")
    print("5. Write in week")
    print("6. Write in month")
    print("0. Exit")
    choice()

def choice():
        option = askOption()
        match option:
            case 1:
                second()
            case 2:
                minute()
            case 3:
                hour()
            case 4:
                day()
            case 5:
                week()
            case 6:
                month()
            case 0:
                clean()
                print("Good Bye :)")
                time.sleep(2)
                os._exit(0)

        
def askOption():
    while True:
        option = ''
        try:
            option = int(input("Choose an option between 1 and 6 : "))
            if option >= 0 and option <= 6:
                return option
            else:
                print("Error ! You need to choose an option between 1 and 6 !!\n")
                time.sleep(2)
        except:
            print("Error ! You need to enter a NUMBER between 1 and 6 !!\n")
            time.sleep(2)

##### CALCUL  #####

def second():
    while True:
        sec = ''
        try:
            sec = int(input("How much secondes ? : "))
            calculSecond(sec)
        except:
            print('Wrong input. Please enter a number ...')
def minute():
    while True:
        min = ''
        try:
            min = int(input("How much minutes ? : "))
            calculMinute(min)
        except:
            print('Wrong input. Please enter a number ...')
def hour():
    while True:
        h = ''
        try:
            h = int(input("How much hour ? : "))
            calculHour(h)
        except:
            print('Wrong input. Please enter a number ...')
def day():
    while True:
        d = ''
        try:
            d = int(input("How much day ? : "))
            calculDay(d)
        except:
            print('Wrong input. Please enter a number ...')
def week():
    while True:
        w = ''
        try:
            w = int(input("How much week ? : "))
            calculWeek(w)
        except:
            print('Wrong input. Please enter a number ...')
def month():
    while True:
        m = ''
        try:
            m = int(input("How much month ? : "))
            calculMonth(m)
        except:
            print('Wrong input. Please enter a number ...')

def calculSecond(sec):
    valeurType = sec
    reste = 0
    if sec >= 31536000:
        ye = sec / 31536000
        reste = sec % 31536000
    else:
        reste = sec
        ye = 0
    if reste >= 2628000:
        mo = reste / 2628000
        reste = reste % 2628000
    else:
        mo = 0
    if reste >= 604800:
        we = reste / 604800
        reste = reste % 604800
    else:
        we = 0
    if reste >= 86400:
        da = reste / 86400
        reste = reste % 86400
    else:
        da = 0
    if reste >= 3600:
        ho = reste / 3600
        reste = reste % 3600
    else:
        ho = 0
    if reste >= 60:
        mi = reste / 60
        reste = reste % 60
    else:
        mi = 0
    se = reste
    type = 1
    ye = int(ye)
    mo = int(mo)
    we = int(we)
    da = int(da)
    ho = int(ho)
    mi = int(mi)
    se = int(se)


    resultat(se, mi, ho, da, we, mo, ye, type, valeurType)
def calculMinute(min):
    valeurType = min
    reste = 0
    if min >= 525600:
        ye = min / 525600
        reste = min % 525600
    else:
        reste = min
        ye = 0
    if reste >= 43800:
        mo = reste / 43800
        reste = reste % 43800
    else:
        mo = 0
    if reste >= 10080:
        we = reste / 10080
        reste = reste % 10080
    else:
        we = 0
    if reste >= 1440:
        da = reste / 1440
        reste = reste % 1440
    else:
        da = 0
    if reste >= 60:
        ho = reste / 60
        reste = reste % 60
    else:
        ho = 0
    if reste >= 1:
        mi = reste / 1
        reste = reste % 1
    else:
        mi = 0
    se = reste
    type = 2
    ye = int(ye)
    mo = int(mo)
    we = int(we)
    da = int(da)
    ho = int(ho)
    mi = int(mi)
    se = int(se)

    resultat(se, mi, ho, da, we, mo, ye, type, valeurType)
def calculHour(h):
    valeurType = h
    reste = 0
    if h >= 8760:
        ye = h / 8760
        reste = h % 8760
    else:
        reste = h
        ye = 0
    if reste >= 730:
        mo = reste / 730
        reste = reste % 730
    else:
        mo = 0
    if reste >= 168:
        we = reste / 168
        reste = reste % 168
    else:
        we = 0
    if reste >= 24:
        da = reste / 24
        reste = reste % 24
    else:
        da = 0
    ho = reste
    mi = 0
    se = 0
    type = 3
    ye = int(ye)
    mo = int(mo)
    we = int(we)
    da = int(da)
    ho = int(ho)
    mi = int(mi)
    se = int(se)
    resultat(se, mi, ho, da, we, mo, ye, type, valeurType)
    
def calculDay(d):
    valeurType = d
    reste = 0
    if d >= 365:
        ye = d / 365
        reste = d % 365
    else:
        reste = d
        ye = 0
    if reste >= 30:
        mo = reste / 30
        reste = reste % 30
    else:
        mo = 0
    if reste >= 7:
        we = reste / 7
        reste = reste % 7
    else:
        we = 0

    da = reste
    mi = 0
    se = 0
    type = 4
    ye = int(ye)
    mo = int(mo)
    we = int(we)
    da = int(da)
    ho = int(ho)
    mi = int(mi)
    se = int(se)
    resultat(se, mi, ho, da, we, mo, ye, type, valeurType)
def calculWeek(w):
    valeurType = w
    reste = 0
    if w >= 52:
        ye = w / 52
        reste = w % 52
    else:
        reste = w
        ye = 0
    if reste >= 4:
        mo = reste / 4
        reste = reste % 4
    else:
        mo = 0

    w = reste
    da = 0
    mi = 0
    se = 0
    type = 5
    ye = int(ye)
    mo = int(mo)
    we = int(we)
    da = int(da)
    ho = int(ho)
    mi = int(mi)
    se = int(se)  
def calculMonth(m):
    valeurType = m
    reste = 0
    if m >= 52:
        ye = m / 52
        reste = m % 52
    else:
        reste = m
        ye = 0
    if reste >= 4:
        mo = reste / 4
        reste = reste % 4
    else:
        mo = 0

    m = reste
    w = 0
    da = 0
    mi = 0
    se = 0
    type = 6
    ye = int(ye)
    mo = int(mo)
    we = int(we)
    da = int(da)
    ho = int(ho)
    mi = int(mi)
    se = int(se)
    resultat(se, mi, ho, da, we, mo, ye, type, valeurType)

def askRestart():
    while True:
        restart = input('Restart ? [y/n] : ')
        if restart == "y" or "Y":
            restart()
        elif restart == "n" or "N":
            clean()
            print("Good Bye :)")
            time.sleep(2)
            os._exit(0)
        else:
            print(" Please choose yes (y) or  no (n) !")
             
def resultat(se=0, mi=0, ho=0, da=0, we=0, mo=0, ye=0, type=0, valeurType=0):
    match type:
        case 1:
            if  valeurType > 1:
                type = "secondes"
            else:
                type = "second"
        case 2:
            if  valeurType > 1:
                type = "minutes"
            else:
                type = "second"
        case 3:
            if  valeurType > 1:
                type = "hours"
            else:
                type = "hour"
        case 4:
            if  valeurType > 1:
                type = "days"
            else:
                type = "day"
        case 5:
            if  valeurType > 1:
                type = "weeks"
            else:
                type = "week"
        case 6:
            if  valeurType > 1:
                type = "months"
            else:
                type = "month"
    
    type = str(type)
    valeurType = str(valeurType)
    print(valeurType + " " + type + " are equal to : ")    
    loading(3)
    if ye == 0:
        yeStatu = False
    else:
        yeStatu = True
    if mo == 0:
        moStatu = False
    else:
        moStatu = True
    if we == 0:
        weStatu = False
    else:
        weStatu = True
    if da == 0:
        daStatu = False
    else:
        daStatu = True
    if ho == 0:
        hoStatu = False
    else:
        hoStatu = True
    if mi == 0:
        miStatu = False
    else:
        miStatu = True


    ye = str(ye)
    mo = str(mo)
    we = str(we)
    da = str(da)
    ho = str(ho)
    mi = str(mi)
    se = str(se)





    if yeStatu == True and moStatu == True and weStatu == True and daStatu == True and hoStatu == True and miStatu == True:
        print("  " + ye + " year  |  " + mo + " month  |  " + we + " week  |  " + da + " day  |  " + ho + " hour  |  " + mi + " minute  |  " + se +  " secondes")
        askRestart()
    elif moStatu == True and weStatu == True and daStatu == True and hoStatu == True and miStatu == True:
        print("  " + mo + " month  |  " + we + " week  |  " + da + " day  |  " + ho + " hour  |  " + mi + " minute  |  "  + se + " secondes")
        askRestart()
    elif weStatu == True and daStatu == True and hoStatu == True and miStatu == True:
        print("  " + we + " week  |  " + da + " day  |  " + ho + " hour  |  " + mi + " minute  |  "  + se + " secondes")
        askRestart()
    elif daStatu == True and hoStatu == True and miStatu == True:
        print("  " + da + " day  |  " + ho + " hour  |  " + mi + " minute  |  "  + se + " secondes")
        askRestart()
    elif hoStatu == True and miStatu == True:
        print("  " + ho + " hour  |  " + mi + " minute  |  "  + se + " secondes")
        askRestart()
    elif miStatu == True:
        print("  " + mi + " minute  |  "  + se + " secondes")
        askRestart()
    else:
        print("  " + se + " secondes")

    


start()