import os
import pickle
import random
class Hangman:
    score=0
    counter=0
    name=""
    Q_no=0
    counter2=0
    name2=""
    hint=""
    Q_no2=0

    def Menu(self):
        print "\n"
        print "************  MENU  ************"
        print "Enter 1 to Continue.  "
        print "Enter 2 for New Game.  "
        print "Enter 3 for Instructions.  "
        print "Enter 4 for Credits.  "
        print "Enter 5 to Save.  "
        print "Enter 6 to Quit.  "

    def HangmanUH(self):
        print '    ___________\n          |\n          |\n          |\n         (_)\n        _____\n       ||    ||\n       ||    ||\n        -------',
        print '\n       ||    ||\n        |    |\n        -------\n        |    |\n        |    |\n        |    |\n        |    |\n-----------------------'

    def HangmanH(self):
        print '    ___________\n          |\n          |\n          |\n          |\n         (_)\n         ____\n       /|    |\ \n     /  |    |  \  ',
        print '\n   /     ------     \ \n /      |    |      \  \n        |    |          \n         ------\n        |    |\n        |    |\n        |    |\n        |    |'

    def PLAY(self):
        rn=self.name2
        print "Your hint is",self.hint
        alp=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        gn=list()
        print 'LETS PLAY'
        c2=-1
        for x in rn:
            if(x==' '):
                print ' ',
                gn.append(' ')
            else:
                gn.append('_')
                print '_',
                continue
                        
        c1=1
        ch1=''
        print ''
        while(c1<=5):
            print 'You have ',6-c1,'chances left wih you.'
            c1+=1
            print 'Enter a letter from the alphabets given below'
            print alp
            ch1=raw_input("Enter the letter of your guess  :")
            ch1=ch1.upper()

            if(ch1 in alp):
                alp.remove(ch1)
            elif(ch1==''):
                print '\n'
                print 'Please do not enter nothing'
                c1-=1
                continue
            elif(ch1==' '):
                print '\n'
                print 'Please do not enter a space. They are already shown to you.'
                c1-=1
                continue
            else:
                print '\n'
                print 'You have already entered this letter. Please enter your guess again.'
                c1-=1
                continue

            chk=0
            c2=-1
            for x in rn:
                c2+=1
                if(x==ch1):
                    chk=5
                    print ch1,
                    c1-=1
                    gn[c2]=ch1
                else:
                    print gn[c2],
                    continue
            print ''
            if(list(rn)==gn):
                    print 'Yes, the right answer is ',self.name2
                    print 'You won this part of game.'
                    self.score+=100
                    print "Your score is =",self.score
                    break    
            elif(chk==5):
                print 'You guessed it right'
                continue
            else:
                print ' OOPS! you guessed it wrong'
                continue
        if(c1>=5):
                print 'You lost this part of game'
                print 'The right anwser is ',self.name2
                print "Your score is =",self.score
                print 'Lets continue to next part of game'
        print '\n'

    def Continue(self):
        while(1):
            if (os.path.isfile("Score.DAT")):
                file2=open("Score.DAT", "rb")
                f2l1=pickle.load(file2)
                file1=open("Questions.txt","r")
                password=input("Enter the password :")
                self.counter=f2l1[4]
                if (password == f2l1[3]):
                    print "So, Mr.",f2l1[1]," lets resume the game"
                    self.score=f2l1[2]
                    self.Q_no=f2l1[0]
                    self.counter2=0
                    f1l1=file1.readlines()
                    if(self.Q_no <= 25):
                        for i in f1l1:
                            f1l2=i.split("-")
                            if (self.counter == f2l1[4]):
                                self.Q_no2=int(f1l2[0])
                                if (self.Q_no == self.Q_no2):
                                    if (self.counter <=5):
                                        print "\n"
                                        self.name2=f1l2[2]
                                        self.hint=f1l2[1]
                                        self.PLAY()
                                        self.Q_no+=1
                                        self.counter+=1
                                        self.Q_no2+=1
                                        print "To continue playing game enter 1   and   type 2 for main menu."
                                        ch=raw_input("You can save your proceedings choose save option from main menu :")
                                        if (ch == '1'):
                                            print "Continuing game"
                                            continue
                                        elif(ch == '2'):
                                            print "Ending game"
                                            self.counter2=1
                                            break
                                        else:
                                            print "wrong input"
                                    else:
                                        if (self.score >=500):
                                            self.HangmanUH()
                                            self.counter2=1
                                            print "Congratulations! You saved HANGMAN and even won the game."
                                        else:
                                            self.HangmanH()
                                            self.counter2=1
                                            print "Sorry! You could not save HANGMAN. "
                                        break
                                else:
                                    continue
                            else:
                                if (self.Q_no ==self.Q_no2):
                                    if (self.counter <=5):
                                        self.name2=f1l2[2]
                                        self.hint=f1l2[1]
                                        self.PLAY()
                                        self.Q_no+=1
                                        self.Q_no2+=1
                                        self.counter+=1
                                        print "To continue playing game enter 1   and   type 2 for main menu."
                                        ch=input("You can save your proceedings choose save option from main menu :")
                                        if (ch == 1):
                                            continue
                                        else:
                                            self.counter2=1
                                            break
                                    else:
                                        if (self.score >=500):
                                            self.HangmanUH()
                                            self.counter2=1
                                            print "Congratulations! You saved      HANGMAN and even won the game."
                                        else:
                                            self.HangmanH()
                                            self.counter2=1
                                            print "Sorry! You could not save HANGMAN. "
                                        break
                                else:
                                    continue
                        if(self.counter2 == 1):
                            break
                    elif((self.Q_no2> 25) and (self.counter2 == 0)):
                        self.Q_no2=1
                        for i in f1l1:
                            f1l2=i.split("-")
                            if (self.counter <= 5):
                                print "\n"
                                self.name2=f1l2[2]
                                self.hint=f1l2[1]
                                self.PLAY()
                                self.counter+=1
                                self.Q_no2+=1
                                print "To continue playing game enter 1   and   type 2 for main menu."
                                ch=input("You can save your proceedings choose save option from main menu :")
                                if (ch == 1):
                                    continue
                                else:
                                    self.counter2=1
                                    break
                            else:
                                if (self.score >=500):
                                    self.HangmanUH()
                                    self.counter2=1
                                    print "Congratulations! You saved HANGMAN and even won the game."
                                else:
                                    self.HangmanH()
                                    self.counter2=1
                                    print "Sorry! You could not save HANGMAN. "
                            break
                    if (self.counter2 == 1):
                                    break
                else:
                    print "Your entered password  is wrong."
                    ch1=input("Type 1 to enter password again and type 2 for main menu. :")
                    if (ch1 == 1):
                        continue
                    else:
                        break
                file1.close()
                file2.close()    
            else:
                print "No save file exists. "
                break

    def NewGame(self):
        self.HangmanUH()
        print "Welcome to the game Hangman"
        self.name=raw_input("Enter your name :")
        print "So, Mr.",self.name," lets play the game."
        file1=open("Questions.txt","r")
        f1l1=file1.readlines()
        self.counter2=0
        self.counter=0
        self.Q_no=random.randint(0,25)
        if(self.Q_no <= 24):
            for i in f1l1:
                f1l2=i.split("-")
                if (self.counter == 0):
                    self.Q_no2=int(f1l2[0])
                    if (self.Q_no == self.Q_no2):
                        if (self.counter <=5):
                            print "\n"
                            self.name2=f1l2[2]
                            self.hint=f1l2[1]
                            self.PLAY()
                            self.Q_no+=1
                            self.counter+=1
                            self.Q_no2+=1
                            print "To continue playing game enter 1   and   type 2 for main menu."
                            ch=input("You can save your proceedings choose save option from main menu :")
                            if (ch == 1):
                                continue
                            else:
                                self.counter2=1
                                break
                        else:
                            if (self.score >=500):
                                self.HangmanUH()
                                print "Congratulations! You saved HANGMAN and even won the game."
                            else:
                                self.HangmanH()
                                print "Sorry! You could not save HANGMAN. "
                            break
                    else:
                        continue
                else:
                    if (self.Q_no ==self.Q_no2):
                        if (self.counter <=5):
                            self.name2=f1l2[2]
                            self.hint=f1l2[1]
                            self.PLAY()
                            self.Q_no+=1
                            self.Q_no2+=1
                            self.counter+=1
                            print "To continue playing game enter 1   and   type 2 for main menu."
                            ch=input("You can save your proceedings choose save option from main menu :")
                            if (ch == 1):
                                continue
                            else:
                                self.counter2=1
                                break
                        else:
                            if (self.score >=500):
                                self.HangmanUH()
                                print "Congratulations! You saved HANGMAN and even won the game."
                            else:
                                self.HangmanH()
                                print "Sorry! You could not save HANGMAN. "
                            break
                    else:
                        continue

        elif((self.Q_no2>25) and (self.counter2 == 0)):
            self.Q_no2=1
            for i in f1l1:
                f1l2=i.split("-")
                if (self.counter <= 5):
                    print "\n"
                    self.name2=f1l2[2]
                    self.hint=f1l2[1]
                    self.PLAY()
                    self.counter+=1
                    self.Q_no2+=1
                    print "To continue playing game enter 1   and   type 2 for main menu."
                    ch=input("You can save your proceedings choose save option from main menu 3:")
                    if (ch == 1):
                        continue
                    else:
                        self.counter2=1
                        break
                else:
                    if (self.score >=500):
                        self.HangmanUH()
                        print "Congratulations! You saved HANGMAN and even won the game."
                    else:
                        self.HangmanH()
                        print "Sorry! You could not save HANGMAN. "
                    file1.close()
                    break
        file1.close()

    def Instructions(self):
            print '\n'
            print 'Hey friends! Lets start the hangman game.The rules are gona be simple. I will be showing you a name as blank spaces'
            print 'and you are going to guess it letter by letter. If you guessed it right within 5 turns then you will save HANGMAN'
            print 'otherwise he will be hanged. For each right guess you will get an extra guess for the number of letters you guessed '
            print 'right. You should not enter a single alphabet twice otherwise you will be responsible for the conseqences.'
            print "You need to score more than or equal to 500. You have 6 chances to save HANGMAN."
            print 'I hope you understood the rules. Lets start the game.'

    def Credits(self):
        print "\n"
        print "    GAME DEVELOPER"
        print "\n"*2
        print "                                                       ---VISHAL BAGHEL"
        print "\n"*2
        print "    PROGRAM CODER"
        print "\n"*2
        print "                                                        ---VISHAL BAGHEL"

    def Save(self):
        if (self.counter2 == 1):
            l1=[]
            l1.append(self.Q_no2)
            l1.append(self.name)
            l1.append(self.score)
            if (os.path.isfile("Score.DAT")):
                ch2=input("There already exist a save file. Would you like to overwrite it. Type 1 for yes and 2 for no.")
                if (ch2==1):
                    password=random.randint(0,100000)
                    print " This is your password remember this to resume your game ",password
                    l1.append(password)
                    l1.append(self.counter)
                    file3=open("Score2.DAT","wb")
                    pickle.dump(l1,file3)
                    os.remove("Score.DAT")
                    os.rename("Score2.DAT", "Score.DAT")
                    print "Your game is saved."
                else:
                    print "Game not saved."
            else:
                password=random.randint(0,100000)
                print " This is your password remember this to resume your game ",password
                l1.append(password)
                l1.append(self.counter)
                file2=open("Score.DAT","wb")
                pickle.dump(l1,file2)
        else:
            print "Either you have completed the game or not yet started. So, there is no need to save."

HM=Hangman()
while(1):
    HM.Menu()
    choice=input("Enter your choice :")
    if (choice == 1):
        HM.Continue()
    elif(choice == 2):
        HM.NewGame()
    elif(choice == 3):
        HM.Instructions()
    elif(choice == 4):
        HM.Credits()
    elif(choice == 5):
        HM.Save()
        break
    elif(choice == 6):
        ch=input("Type 1 to save and quit   and   type 2 to to quit without saving.")
        if (ch == 1):
            HM.Save()
        else:
            break
    else:
        print "Wrong input. Please re-enter."
        Continue




