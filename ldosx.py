

# L-DOS X



import os

import winsound



home=os.getcwd()



class emu:

    def mussym(col1, col2):

        import turtle

        turtle.pu()

        turtle.goto(-100, 100)

        turtle.pencolor(col1)

        turtle.write("Wav", move="True", align="left", font=("Arial", 30, "bold"))

        turtle.pencolor(col2)

        turtle.write("Read", move="True", align="left", font=("Arial", 30, 'bold'))

    def logo():

        emu.pg("L", 1, 25, "bold")

        emu.pg("L-", 1, 25, 'bold')

        emu.pg("L-D", 1, 25, 'bold')

        emu.pg('L-DO', 1, 25, 'bold')

        emu.pg('L-DOS', 1, 25, 'bold')

        for i in range(10):

            emu.pg('', 0.1, 25, 'bold')

            emu.pg('L-DOS', 0.1, 25, 'bold')

        emu.pg('', 0, 25, '')

        emu.startup()

    def pgui(text, fon):

        import time

        import turtle

        turtle.screensize(250,250)

        turtle.penup()

        turtle.goto(0,0)

        turtle.pendown()

        turtle.ht()

        turtle.title("Graphical Interface")

        turtle.clear()

        turtle.write(text, align = "center", font = (fon, 10, "bold"))

        turtle.pu

        time.sleep(10)

    def square():

        import turtle

        turtle.clear()

        turtle.pu()

        turtle.begin_fill()

        turtle.goto(400,400)

        turtle.pd()

        for i in range(4):

            turtle.forward(200)

            turtle.right(90)

    def update():

        import winsound

        import tkinter.messagebox

        winsound.Beep(700,1000)

        print("This software reqires a newer version of L-DOS.")

        pg("This software requires a newer version of L-DOS.", 5, 24, "bold")

    def startup():

        import winsound

        filename = 'g_boot.wav'

        winsound.PlaySound(filename, winsound.SND_FILENAME)

    def winerr():

        import winsound

        filename = 'g_error.wav'

        winsound.PlaySound(filename, winsound.SND_FILENAME)

    def ttext():

        import turtle

        import os

        import time

        turtle.screensize(250, 250)

        turtle.penup()

        turtle.goto(0,225)

        turtle.pendown()

        turtle.ht()

        turtle.title("Graphical Interface")

        turtle.write("Graphical Interface", align = "center", font = ("Arial", 10, "bold"))

        turtle.pu()

        turtle.goto(0, -150)

        turtle.pd()

        path = os.getcwd()

        turtle.write(path, align="center", font=("Arial", 8, "bold"))

        turtle.pu()

        turtle.goto(0, -225)

        turtle.pd()

    def pg(text, length, size, mod):

        import time

        import turtle

        turtle.screensize(250,250)

        turtle.penup()

        turtle.goto(0,0)

        turtle.pendown()

        turtle.ht()

        turtle.title("Graphical Interface")

        turtle.clear()

        turtle.write(text, align = "center", font = ("Arial", size, mod))

        turtle.pu

        time.sleep(length)

    def notins():

        import winsound

        winsound.Beep(700,1000)

        print("This software is not installed. Install it through fshop.")

        pg("""This software

    is not installed.

    Install it

    through fshop.""", 5, 45, "bold")

    def invalid():

        import winsound

        winsound.Beep(700,1000)

        print("What you have inputted is invalid.")

        pg("""What you have

    inputted is invalid.""", 5, 45, "bold")

    def confbeep():

        import winsound

        winsound.Beep(1600,100)

    def errbeep():

        import winsound

        winsound.Beep(1200,1500)

    def load():

        f = open("theme.ldos", 'r')

        s = f.read()

        bg='#' + s[0:6]

        text='#' + s[7:13]

        wav1='#' + s[14:20]

        wav2='#' + s[21:29]

        ver = "0.1.3"

        et = 0

        math = 0

        lock = 0

        beep = 0

        command = "N/A"

        import turtle

        import time

        from random import randint

        import winsound

        import os

        import getpass

        import glob

        import tkinter

        turtle.pencolor(text)

        turtle.bgcolor(bg)

        print("Booting L-DOS " + ver + "...")

        print("Finalizing...")

        print("L-DOS " + ver + " has booted. Loading command prompt...")

        drive = "C:/"

        home = os.getcwd()

        path = home

        predir = home

        emu.logo()

        emu.ttext()

        print("A second window has been opened for graphical capability.")

        print("If a program requires graphics, open the secondary window.")

        print("Make sure L-DOS Folder is on the desktop.")

        print("L-DOS requires a version of Microsoft Windows.")

        winsound.Beep(1000,1000)

        while 1 == 1:

                turtle.bgcolor(bg)

                turtle.pencolor(text)

                lCom = command

                turtle.pu()

                turtle.goto(0, 0)

                turtle.pd()

                turtle.clear()

                emu.ttext()

                turtle.write("Last Command: " + lCom, align = "center", font = ("Arial", 10, "normal"))

                command = input(drive)

                emu.confbeep()

                if command == "break":

                    return 0

                if drive == "C:/":

                    if command == "print":

                        toPrint = input("")

                        print(toPrint)

                    if command == "help":

                        print("""

        L-DOS HELP

        ----------

        Welcome to L-DOS, an OS programmed in Python!

        Python has basic input and output commands, which

        is perfect for a DOS-based operating system.

        ----------

        COMMANDS

        ----------

        break: returns you to python prompt

        print: echoes what you say

        update: updates L-DOS

        version: shows version

        fshop: function shop

        fshop /nw: function shop without delays

        pgui: prints to the gui

        graphic: GUI

        graphic /nw: GUI without delays

        file: text editor and reader

        wavread: plays a wav file

        dir: shows directory

        cd: change directory

        pd: previous directory

        nd: new directory

        dirs: searches for anything

        ----------

        FSHOP HELP

        ----------

        NOTE: FSHOP DOES NOT CONNECT TO THE INTERNET. ALL DOWNLOADS

        ARE FAKE AND CAN BE SKIPPED BY USING THE /nw TAG.

        ----------

        fshop: opens function shop

        example interface:

        1. option 1

        2. option 2

        3. option 3

        ect.

        choice: []

        select whatever you want

        1. math.exe

        2. lock.exe

        3. etest.exe

        choice: 3

        install etest? y/n

        []

        type y to install

        install etest? y/n

        y

        installing etest...

        installed successfully.

        launch program:

        C:/etest

        [program]

        ----------

        Thank you for downloading L-DOS.

        ----------

        NOTE: Scroll up to view all of help.""")

                        emu.errbeep()

                    if command == "p-lang" or command == "plang":

                        emu.update()

                    if command == "doc" or command == "docedit":

                        emu.update()

                if command == "A:/" or "A:" or "A":

                    drive = "A:/"

                if command == "B:/" or "B:" or "B":

                    drive = "B:/"

                if command == "C:/" or "C:" or "C":

                    drive = "C:/"

                if command == "update":

                            print("Loading L-DOS Setup...")

                            print("""

        L-DOS is loading...

        L-DOS is now rebooting...""")

                            time.sleep(1)

                            print("L-DOS Update is not available. Rebooting...")

                            time.sleep(0.1)

                            print("Reboot initalized...")

                            print("Reboot cancelled.")

                            errbeep()

                if command == "version":

                    print("You are running L-DOS version " + ver + ".")

                if command == "etest":

                    if et == 1:

                        print("Loading etest tool...")

                        time.sleep(0.5)

                        print("etest tool loaded.")

                        ets = int(input("What error key to test? Use integer key. "))

                        emu.confbeep()

                        if ets == 1:

                            print("ekey 1 - requires newer version")

                            emu.update()

                        elif ets == 2:

                            print("ekey 2 - program not currently installed.")

                            emu.notins()

                        elif ets == 3:

                            print("ekey 3 - invalid operation")

                            emu.invalid()

                        else:

                            emu.invalid()

                    else:

                        notins()

                if command == "beep":

                    if beep == 1:

                        bp = int(input("Beep Pitch: "))

                        bl = int(input("Beep Length: "))

                        winsound.Beep(bp, bl)

                    else:

                        emu.notins()

                if command == "fshop /nw":

                    print("Loading Function Shop...")

                    print("""

        Function Shop

        -----------

        1. math.exe

        2. lock.exe

        3. etest.exe

        4. beep.exe

        5. bonusGui.exe

        -----------""")

                    choice1 = input("Insert choice: ")

                    emu.confbeep()

                    if choice1 == "1":

                        print("Install math?")

                        if input() == "y" or "Y":

                            emu.confbeep()

                            print("Installing math function...")

                            print("Math has been installed successfully.")

                            math = 1

                    elif choice1 == "2":

                        print ("Install lock?")

                        if input() == "y" or "Y":

                            emu.confbeep()

                            print("Installing lock...")

                            print("Lock has been installed successfully.")

                            lock = 1

                    elif choice1 == "3":

                        print("Install error tester?")

                        if input() == "y" or "Y":

                            emu.confbeep()

                            print("Installing error test...")

                            print("Error tester has been installed successfully.")

                            et = 1

                    elif choice1 == "4":

                        print("Install beep?")

                        if input() == "y" or "Y":

                            emu.confbeep()

                            print("Installing beep...")

                            beep = 1

                            print("Beep has been installed successfully.")

                    elif choice1 == "5":

                        print("Install Bonus GUI?")

                        if input() == "y" or "Y":

                            emu.confbeep()

                            print("Installing bonus GUI...")

                            emu.errbeep()

                            print("First attempt failed.")

                            emu.errbeep()

                            print("Second attempt failed. Trying final time...")

                            emu.errbeep()

                            print("Third attempt failed. Cannot download bonusGui.exe.")

                    else:

                        emu.invalid()

                        emu.confbeep()

                if command == "pgui":

                    emu.pgui(input("What to print to GUI: "), "Arial")

                if command == "graphic":

                    print("Direct your attention to the Graphical Interface.")

                    emu.startup()

                    emu.pg("Welcome to L-DOS Graphic!", 2, 25, 'bold')

                    emu.pg('''L-DOS Graphic is not fully complete yet.

        Please consider this when using L-DOS Graphic.''', 5, 25, 'bold')

                if command == "file":

                    choice = input("""

        What do you want to do with file manager?

        1. Open file

        2. Create file

        3. Edit existing file

        """)

                    if choice == "1":

                        file = input("Please input filename: ")

                        f = open(file, "r")

                        con = f.read()

                        print(con)

                        pg(con, 5, 10, 'bold')

                    elif choice == "2":

                        file = input("What to name this file? ")

                        f = open(file, 'w+')

                    elif choice == "3":

                        file = input("What file to edit? ")

                        edit = input("What to add? ")

                        f = open(file, 'a+')

                        f.write(edit)

                if command == "sound":

                    snd = input("Input integer ID: ")

                    if snd == "1":

                        print("GUI Logon Noise")

                        emu.startup()

                    elif snd == "2":

                        print("Error Sound")

                        emu.winerr()

                if command == "guiprint":

                    tp = input("What to print on-screen? ")

                    fnt = input("What font to use? ")

                    emu.pgui(tp, fnt)

                if 'wavread' in command:

                    filename = command[8:len(command)]

                    if not '.wav' in command:

                        filename = filename + ".wav"

                    print("Playing " + filename)

                    emu.pg(filename, 0, 30, "bold")

                    emu.mussym(wav1, wav2)

                    winsound.PlaySound(filename, winsound.SND_FILENAME)

                if command == "dir":

                    for x in os.listdir('.'):

                        print(x)

                if "cd" in command:

                    predir = os.getcwd()

                    os.chdir(command[3:len(command)])

                if command == "pd":

                    os.chdir(predir)

                if command == "nd":

                    os.makedirs(input("What to name directory?"))

                if command == "":

                    emu.invalid()

                if command == "credits":

                    print("Lim Industries L-DOS")

                    emu.pg("Lim Industries L-DOS", 1, 12, "bold")

                    emu.confbeep()

                    print("Created by Lim95")

                    emu.pg("Created by Lim95", 1, 12, "bold")

                    emu.confbeep()

                    print("Programmed in Python 3.0")

                    emu.pg("Programmed in Python 3.0", 1, 12, "bold")

                    emu.confbeep()

                    print("Music from Friday Night Funkin'")

                    emu.pg("Music from Friday Night Funkin'", 1, 12, "bold")

                    emu.confbeep()

                    print("GUI Boot Sound from Windows 95")

                    pg("GUI Boot Sound from Windows 95", 1, 12, "bold")

                    confbeep()

                    print("Thanks for using L-DOS!")

                    emu.pg("Thanks for using L-DOS!", 5, 12, "bold")

                    emu.errbeep()

                if command == "lib":

                    print("""

        L-DOS v0.1.0 uses the following Pythin libraries:

        Turtle [GUI]

        Time [DELAY]

        Random [LOCK]

        Winsound [BEEP]

        OS [FILES]

        Getpass [USER DIRECTORY]

        Glob [SEARCH]""")

                    theme = "L"

                if command == "math":

                    if math == 1:

                        a = input("Number A? ")

                        b = input("Number 2? ")

                        op =input("""

        Input Option:

        A: Add

        S: Subtract

        M: Multiply

        D: Divide

        """)

                        if op == "a" or "A":

                            print(int(a) + int(b))

                    elif op == "s" or "S":

                        print(int(a) - int(b))

                    elif op == "m" or "M":

                        print(int(a) * int(b))

                    elif op == "d" or "D":

                        print(int(a) / int(b))

                if command == "lock":

                    if lock == 1:

                        file = input("What file to lock? ")

                        password = input("What password to lock it with? ")

                        file = open(file + ".pass", "a+")

                        file = open(file + ".pass", "w")

                        file.write(password)

                        print(file + ".pass has been locked.")

                if 'dirs' in command:

                    for x in os.listdir('.'):

                        if command[5:len(command)] in x:

                            print(x)

                if 'open' in command:

                    if '.wav' in command[5:len(command)]:

                        print("Use wavread to open this file.")

                    else:

                        file = command[5:len(command)]

                        f = open(file, "r")

                        con = f.read()

                        print(con)

                        pg(con, 5, 10, 'bold')

                if command == 'theme':

                    print("Welcome to Theme Manager!")

                    cmd = input("""What do you want to do here?

        1. Change theme

        2. Restore default theme

        3. Restore Backed Up Theme

        Input choice here: """)

                    if cmd == "1":

                        f = open("tbackup.ldos", "w")

                        f.write(str(bg + '/' + text + '/' + wav1 + '/' + wav2))

                        bg = '#' + input("Background? Use a hex value (xxxxxx). ")

                        text = '#' + input("Text color? Use a hex value (xxxxxx). ")

                        wav1 = '#' + input("Wav? Use a hex value (xxxxxx). ")

                        wav2 = '#' + input("Read? Use a hex value (xxxxxx). ")

                        f = open("theme.ldos", 'w')

                        f.write(str(bg + '/' + text + '/' + wav1 + '/' + wav2))

                    elif cmd == "2":

                        bg = "#FFFFFF"

                        text= "#000000"

                        wav1 = "#0062ff"

                        wav2 = "#d4ff00"

                    elif cmd == '3':

                        f = open("tbackup.ldos", 'r')

                        s = f.read()

                        bg='#' + s[0:6]

                        text='#' + s[7:13]

                        wav1='#' + s[14:20]

                        wav2='#' + s[21:29]       

                    else:

                        emu.invalid()

                if command == "story":

                    print("Welcome! This is basically Mad Libs.")

                    name = input("Name: ")

                    noun1 = input("Noun: ")

                    noun2 = input("Noun: ")

                    noun3 = input("Noun: ")

                    verb = input("Verb ending in -ing: ")

                    adj = input("Adjective: ")

                    print("Ok! Compiling story...")

                    time.sleep(0.5)

                    input("Story compiled! Press enter to read it.")

                    print("Once, a person named " + name + " went to the gym.")

                    print("Once " + name + " got on the " + noun1 + ", they started to exercise.")

                    print("After they were done with the " + noun1 + ", they started to use a " + noun2 + ".")

                    print("For the other people, this was a sight to behold. " + name + " using a " + noun2 + "?!")

                    print("Then " + name + " finished with the " + noun2 + ". " + name + " got on a " + noun3 + " and started " + verb + "!")

                    print("Someone asked, '" + name + ", is that how you're supposed to use a " + noun3 + "?'")

                    print(name + " replied, 'Of course! This is the secret use of any " + noun3 + "!'")

                    print("This day became imfamous as 'The Day that " + name + " used a " + noun3 + " wrong.'")

                    print("The end!")

                if command == "guitest":

                    t = input("Input integer key... ")

                    if t == "1":

                        emu.logo()

                    elif t == "2":

                        emu.mussym(wav1, wav2)

                    elif t == "3":

                        emu.notins()

                    elif t == '4':

                        emu.invalid()

                    elif t == "5":

                        emu.pg("hdntstmsg", 1, 25, 'bold')

                    elif t == '6':

                        emu.pgui('hdntstmsg', 'Comic Sans MS')

                    else:

                        emu.invalid()

                if command == "whatsnew":

                    print("""

        L-DOS v0.1.3 Patch Notes

        -----

        Fixed Bugs

        Added a New Game

        Added some More Themes""")

                if command == 'settle':

                    itm1 = input("What do you think is good? ")

                    itm2 = input("What does your friend think is good? ")

                    cho = randint(1, 2)

                    if cho == 1:

                        print("Oh yeah, " + itm1 + " is WAAAAAAY better than " + itm2 + ".")

                    else:

                        print("Definitley, " + itm2 + " is the best.")

                if command == "colors":

                    print(bg)

                    print(text)

                    print(wav1)

                    print(wav2)

                if command == "copy":

                    f1 = open(input("What file to copy from? "), 'r')

                    f2 = input("What file to copy to? ")

                    f = open(f2, "w")

                    f.write(f1.read())

                if "getcol" in command:

                    col = command[7:len(command)]

                    if col == "red" or col == "Red":

                        print("ff0000")

                    elif col == "orange" or col == "Orange":

                        print("ff8400")

                    elif col == "yellow" or col == "Yellow":

                        print("eeff00")

                    elif col == "green" or col == "Green":

                        print("00ff08")

                    elif col == "blue" or col == "Blue":

                        print("008cff")

                    elif col == "purple" or col == "Purple":

                        print("9d00ff")

                    elif col == "pink" or col == "Pink":

                        print("ff00e1")

                    elif col == "black" or col == "Black":

                        print("000000")

                    elif col == "white" or col == "White":

                        print("FFFFFF")

                    else:

                        print("Visit this link: https://www.google.com/search?client=firefox-b-1-d&q=hex+color+picker")





def command(cmd):

    if cmd[0:3].lower()=="dir":

        print(os.getcwd())

        search=cmd[4:len(cmd)]

        for x in os.listdir():

            if search in x:

                print(x)

    elif cmd[0:2].lower()=="cd" and not cmd[0:4]=="cdir":

        goto=cmd[3:len(cmd)]

        try:

            os.chdir(goto)

            print(f"Moved to {os.getcwd()}")

        except FileNotFoundError:

            print("Error 404: File not found.")

    elif cmd.lower()=="home":

        os.chdir(home)

    elif cmd.lower()=="help":

        hlp=open(f"{home}/system/data/help.ldos")

        print(hlp.read())

        hlp.close()

    elif cmd[0:4]=="cdir":

        goto=cmd[5:len(cmd)]

        try:

            try:

                os.chdir(goto)

                print(f"Moved to {os.getcwd()}")

                for x in os.listdir():

                    print(x)

            except OSError:

                print("Error 0: Some OS error happened.")

        except FileNotFoundError:

            print(f"Error 404: File not found:{goto}")

    elif cmd.lower()=="exit":

        exit()

    elif cmd[0:3]=="bat" and not cmd[0:5]=="batch":

        file=cmd[4:len(cmd)]

        try:

            b=open(file)

            code=b.readlines()

            b.close()

            for i in code:

                command(i.strip())

        except FileNotFoundError:

            print(f"File {file} not found.")

    elif cmd[0:5]=="batch":

        file=cmd[6:len(cmd)]

        try:

            b=open(file)

            code=b.readlines()

            b.close()

            for i in code:

                command(i.strip())

        except FileNotFoundError:

            print(f"File {file} not found.")

    elif cmd[0:4]=="echo":

        print(cmd[5:len(cmd)])

    elif cmd[0:4]=="beep":

        spoint=cmd.find(",")

        freq=int(cmd[5:spoint])

        duration=int(cmd[spoint+1:len(cmd)])

        try:

            winsound.Beep(freq,duration)

        except ValueError:

            print("Please make frequency between 37 and 32767.")

    elif cmd=="emulator":

        try:

            os.chdir(f"{home}\system/apps\emulator-files")

            if os.getcwd()==f"{home}\system/apps\emulator-files":

                emu.load()

            else:

                os.chdir(f"{home}\system/apps\emulator-files")

                emu.load()

        except FileNotFoundError:

            print("Emulator package is not installed.")

    elif cmd[0:4]=="mdir":

        os.mkdir(cmd[5:len(cmd)])

def boot():

    try:

        usr=open(f"{home}/system/users/main.ldos",'r')

    except FileNotFoundError:

        print(f"system/users/main.ldos was not found.")

        try:

            os.chdir("system")

        except FileNotFoundError:

            os.mkdir("system")

            os.chdir("system")

        try:

            os.chdir("users")

        except FileNotFoundError:

            os.mkdir("users")

            os.chdir("users")

        usr=open("main.ldos","w")

        usrname=input("Username:")

        password=input("Password:")

        usr.write(f"{usrname}\n{password}")

        usr.close()

        boot()

    usr=open(f"{home}/system/users/main.ldos",'r')

    logged=False

    inf=usr.readlines()

    usr.close()

    while not logged:

        pswd=input("$")

        if pswd==inf[1]:

            logged=True

        else:

            print("Wrong password!")

    print(f"Welcome back, {inf[0].strip()}!")

    print("Checking for system validity...")

    os.chdir(home+"/system")

    checkDirs=["apps","data","files"]

    checkApps=["config.ldos","calc.ldos","emulator.ldos"]

    appContent=["","","0.1.3"]

    checkData=["system.ldos","update.ldos","config.ldos","help.ldos"]

    dataContent=["ldosx\nldosx-build-0.0.0\n0","https://lim95.netlify.app/ldosx.py","$","""L-DOS X Help

help - shows this command

dir - show directory

dir * - search files in directory

cd * - change directory

cdir * - change directory then show files

home - return home"""]

    for i in checkDirs:

        try:

            os.chdir(i)

        except FileNotFoundError:

            print(f"!{i}")

            os.mkdir(i)

    os.chdir(home+"/system/apps")

    for i in range(len(checkApps)):

        try:

            app=open(checkApps[i],"r")

            app.close()

        except FileNotFoundError:

            app=open(checkApps[i],"w")

            app.write(appContent[i])

            app.close()

    os.chdir(home+"/system/data")

    for i in range(len(checkData)):

        try:

            dat=open(checkData[i],"r")

            dat.close()

        except FileNotFoundError:

            dat=open(checkData[i],"w")

            dat.write(dataContent[i])

            dat.close()

    print("All files that were missing have been replaced.")

    print("Loading L-DOS X...")

    os.chdir(home)

    cfg=open(f"{home}/system/data/config.ldos")

    prompt=cfg.readlines()[0]

    while True:

        cmd=input(prompt)

        command(cmd)

while True:

    boot()

