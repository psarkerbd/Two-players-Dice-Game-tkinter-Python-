'''
__________________________________________________________
                                                          |
@Author      : Pranta Sarker                              |
@Dept        : CSE                                        |
@Batch       : 6th                                        |
@Institute   : North East University Bangladesh           |
                                                          |
__________________________________________________________|


'''


from tkinter import *;
from tkinter import messagebox;
from PIL import ImageTk, Image;
from random import *;

firstPlayerName = StringVar;
secondPlayerName = StringVar;
playerNames = [];
score1 = IntVar;
score2 = IntVar;
mainscore = 5;
p1 = IntVar;
p2 = IntVar;
headCounter = 0;
tailCounter = 0;

def authorButtonAction(mainWindow, ftypeuno):
    title = "Author";
    name = "Pranta Sarker\n";
    batch = "Batch: 6th\n";
    dept = "Department: CSE\n";
    institute="North East University Bangladesh";
    myinfo = name+batch+dept+institute;
    messagebox.showinfo(title, myinfo);

def disAppearMainWindow(master):
    master.quit();
    master.withdraw();

def theDice(flag, master):
    par = randint(1, 6);
    global p1, p2;
    if(par == 1):
        p1 = 1;
        p2 = 1;
    elif(par == 2):
        p1 = 2;
        p2 = 2;
    elif(par == 3):
        p1 = 3;
        p2 = 3;
    elif(par == 4):
        p1 = 4;
        p2 = 4;
    elif(par == 5):
        p1 = 5;
        p2 = 5;
    elif(par == 6):
        p1 = 6;
        p2 = 6;
    master.quit();
    master.withdraw();


def player1(mainscore, headPlayer, ftypeuno):
    global p1, p2;
    p1 = 0;
    p2 = 0;
    root = Tk();
    root.title(headPlayer + " Dice");
    root.geometry("450x350");
    txt = "Winning Score: " + str(mainscore);
    mainScoreLabel = Label(root, text = txt);
    mainScoreLabel.place(relx=0.7, rely=0.1);
    mainScoreLabel.config(bg="black", fg="white", font=ftypeuno);

    playerLabel = Label(root, text = "Turn-> " + headPlayer);
    playerLabel.place(relx = 0.5, rely = 0.4, anchor = "center");
    playerLabel.config(bg="yellow", fg="blue", font = ftypeuno);

    theButton = Button(root, text="Throw the Dice", width = 25 , command = lambda : theDice(1, root));
    theButton.place(relx = 0.5, rely = 0.5, anchor="center");
    theButton.config(font=ftypeuno, bg="#17c1c1", fg = "black");

    root.resizable(False, False);
    root.mainloop();

def player2(mainscore, tailPlayer, ftypeuno):
    global p1, p2;
    p1 = 0;
    p2 = 0;
    root = Tk();
    root.title(tailPlayer + " Dice");
    root.geometry("450x350");

    txt = "Winning Score: " + str(mainscore);
    mainScoreLabel = Label(root, text=txt);
    mainScoreLabel.place(relx=0.7, rely=0.1);
    mainScoreLabel.config(bg="black", fg="white", font=ftypeuno);

    playerLabel = Label(root, text = "Turn-> " + tailPlayer);
    playerLabel.place(relx=0.5, rely=0.4, anchor="center");
    playerLabel.config(bg="yellow", fg="blue", font=ftypeuno);

    theButton = Button(root, text="Throw the Dice", width = 25, command=lambda : theDice(2, root));
    theButton.place(relx=0.5, rely=0.5, anchor="center");
    theButton.config(font=ftypeuno, bg="#17c1c1", fg="black");

    root.resizable(False, False);
    root.mainloop();

def thrown_Dice(p, playerName , score, ftypeuno, mainscore):
    root = Toplevel();
    title = playerName + " Dice";
    root.title(title)
    root.geometry("450x350");

    txt = "Winning Score: " + str(mainscore);
    mainScoreLabel = Label(root, text=txt);
    mainScoreLabel.place(relx=0.7, rely=0.1);
    mainScoreLabel.config(bg="black", fg="white", font=ftypeuno);

    imageName = "dice_" + str(p) + ".jpg";
    img = Image.open(imageName);
    img = img.resize((90, 90), Image.ANTIALIAS);
    photo = ImageTk.PhotoImage(img);

    imlabel = Label(root, image=photo);
    imlabel.place(relx=0.5, rely=0.5, anchor="center");

    nameLabel = Label(root, text = playerName, width = 20);
    nameLabel.place(relx=0.5, rely=0.7, anchor="center");
    nameLabel.config(bg="#e78c10", fg="black", font = ftypeuno);

    infoLabel = Label(root, text = "Score: " + str(score), width = 20);
    infoLabel.place(relx=0.5, rely=0.8, anchor="center");
    infoLabel.config(bg="black", fg="white", font = ftypeuno);

    root.resizable(False, False);
    #root.after(2000, lambda : root.withdraw());
    #root.mainloop();
    root.wait_window();

def headToheadTable(winner, headplayer, tailplayer, ftypeuno):
    global headCounter, tailCounter;
    root = Tk();
    root.title("Head to Head");
    root.geometry("450x350");

    if(winner is headplayer):
        headCounter += 1;
    else:
        tailCounter += 1;

    headplayerLabel = Label(root, text = headplayer);
    headplayerLabel.place(relx=0.3, rely=0.4, anchor="center");
    headplayerLabel.config(bg="blue", fg="white", font=ftypeuno);

    headplayerCounterLabel = Label(root, text = str(headCounter), width = 10);
    headplayerCounterLabel.place(relx=0.3, rely=0.5, anchor="center");
    headplayerCounterLabel.config(bg="#00c6f2", fg="black", font=ftypeuno);

    tailplayerLabel = Label(root, text = tailplayer);
    tailplayerLabel.place(relx=0.6, rely=0.4, anchor="center");
    tailplayerLabel.config(bg="blue", fg="white", font=ftypeuno);

    tailplayerCounterLabel = Label(root, text = str(tailCounter), width = 10);
    tailplayerCounterLabel.place(relx=0.6, rely=0.5, anchor="center");
    tailplayerCounterLabel.config(bg="#00c6f2", fg="black", font=ftypeuno);

    root.resizable(False, False);
    root.wait_window();



def theWinner(playerName, headplayer, tailplayer, ftypeuno):
    root = Toplevel();
    root.title("Winner");
    root.geometry("450x350");

    global playerNames;

    img = Image.open("emo.jpg");  # file name with extension
    img = img.resize((150, 100), Image.ANTIALIAS);  # resize the photo frame
    photo = ImageTk.PhotoImage(img);

    photoLabel = Label(root, image = photo);
    photoLabel.place(relx = 0.5, rely = 0.2, anchor = "center");

    msg = "Congratulations !!!";
    msgLabel = Label(root, text = msg);
    msgLabel.place(relx = 0.5, rely = 0.4, anchor = "center");
    msgLabel.config(fg="blue", font=ftypeuno);

    winnerLabel = Label(root, text = playerName, width = 25);
    winnerLabel.place(relx = 0.5, rely = 0.5, anchor = "center");
    winnerLabel.config(bg="black", fg="white", font = ftypeuno);

    fLabel = Label(root, text = "Winner of this game");
    fLabel.place(relx = 0.5, rely = 0.6, anchor = "center");
    fLabel.config(bg = "#48b7ea", fg = "#000000", font = ftypeuno);

    playAgainButton = Button(root, text = "Play Again", width = 20,
                             command = lambda : [root.destroy(), headToheadTable(playerName, headplayer, tailplayer, ftypeuno), diceGameCode(headplayer, tailplayer, ftypeuno)]);
                                       # use multiple instructions/functions on a button command
                                        # first function/instruction will execute first
    playAgainButton.place(relx = 0.5, rely = 0.9, anchor = "center");
    playAgainButton.config(bg="blue", fg="white", font=ftypeuno);

    root.resizable(False, False);
    root.mainloop();

# >>>> ---------------------------Start--------------------------------------- >>>>

def diceGameCode(headPlayer, tailPlayer, ftypeuno):
    global mainscore, score2, score1, p1, p2;
    p1 = 0;
    p2 = 0;
    mainscore += 5;
    score1 = 0;
    score2 = 0;

    while (score1 <= mainscore or score2 <= mainscore):
        player1(mainscore, headPlayer, ftypeuno);

        score1 += p1; # score for the player 1

        if (score1 > mainscore):
            score1 -= p1;
        if (score1 == mainscore):
            #print(">> Player 1 Win, Score", score1);
            thrown_Dice(p1, headPlayer, score1, ftypeuno, mainscore);
            theWinner(headPlayer , headPlayer, tailPlayer, ftypeuno);
            break;
        else:
            #print("---Player 1 score = ", score1);
            thrown_Dice(p1, headPlayer, score1, ftypeuno, mainscore);

        # p2 = int(input("Player 2 turn: "));
        player2(mainscore, tailPlayer, ftypeuno);
        #print("Player 2 thrown: ", p2);

        score2 += p2; # score for the player 2

        if (score2 > mainscore):
            score2 -= p2;
            # break;
        if (score2 == mainscore):
            #print(">> Player 2 Win, Score", score2);
            thrown_Dice(p2, tailPlayer, score2, ftypeuno, mainscore);
            theWinner(tailPlayer, headPlayer, tailPlayer, ftypeuno);
            break;
        else:
            #print("---Player 2 score = ", score2);
            thrown_Dice(p2, tailPlayer, score2, ftypeuno, mainscore);
    return 0;

# <<<<< --------------------------------End------------------------------------------

def tossButtonAction(event, ftypeuno, pName, par):
    event.withdraw();
    event.destroy();

    # par = 1 = Head
    # par = 2 = Tail

    global playerNames;
    title = "Toss Decided";
    headPlayer = "";
    tailPlayer = "";


    if par == 1:
        if pName == playerNames[0]:
            headPlayer = playerNames[0];
            tailPlayer = playerNames[1];
            messagebox.showinfo(title, playerNames[1] + " will play for Tail");
        else:
            tailPlayer = playerNames[0];
            headPlayer = playerNames[1];
            messagebox.showinfo(title, playerNames[0] + " will play for Tail");
    else:
        if pName == playerNames[0]:
            tailPlayer = playerNames[0];
            headPlayer = playerNames[1];
            messagebox.showinfo(title, playerNames[1] + " will play for Head");
        else:
            tailPlayer = playerNames[1];
            headPlayer = playerNames[0];
            messagebox.showinfo(title, playerNames[0] + " will play for Head");

    # --------------- The Game code will start from here....
    #---------------------------------------------------------------------------------
    diceGameCode(headPlayer , tailPlayer, ftypeuno);

def tossWindow(ftypeuno):
    master = Tk();
    master.title("Toss");
    master.geometry("450x350");

    global playerNames;

    player_id = randint(1, 2);

    if player_id is 1:
        pName = playerNames[0];
    else:
        pName = playerNames[1];

    msg = "Welcome to Toss Round !!\n";

    tossLabel_1 = Label(master, text=msg, width = 20);
    tossLabel_1.place(relx = 0.5, rely = 0.1, anchor = "center");
    tossLabel_1.config(bg="black", fg="white", font=ftypeuno);

    tossLabel_2 = Label(master, text=pName, width = 20, height = 2);
    tossLabel_2.place(relx = 0.5, rely = 0.2, anchor = "center");
    tossLabel_2.config(bg="#0e73a2", fg="white", font = ftypeuno);

    tossLabel_3 = Label(master, text = "\nwill turn the Choice", width = 20);
    tossLabel_3.place(relx = 0.5, rely = 0.3, anchor = "center");
    tossLabel_3.config(bg="black", fg="white", font=ftypeuno);

    headimg = Image.open("head.jpg");
    tailimg = Image.open("tail.jpg");

    headimg = headimg.resize((90, 90), Image.ANTIALIAS);

    tailimg = tailimg.resize((90, 90), Image.ANTIALIAS);

    headPhoto = ImageTk.PhotoImage(headimg, master = master);
    tailPhoto = ImageTk.PhotoImage(tailimg, master = master);

    headButton = Button(master, image = headPhoto, command = lambda : tossButtonAction(master, ftypeuno, pName, 1));
    headButton.place(relx = 0.35, rely = 0.6, anchor = "center");

    taileButton = Button(master, image = tailPhoto , command = lambda : tossButtonAction(master, ftypeuno, pName, 2));
    taileButton.place(relx = 0.65, rely = 0.6, anchor = "center");

    headLabel = Label(master, text="Head", font=ftypeuno);
    headLabel.place(relx=0.35, rely=0.8, anchor="center");

    tailLabel = Label(master, text="Tail", font=ftypeuno);
    tailLabel.place(relx=0.65, rely=0.8, anchor="center");

    master.resizable(False, False);
    master.mainloop();

def playerTwo(master, ftypeuno):

    global secondPlayerName, playerNames;

    disAppearMainWindow(master);

    player2 = Tk();
    player2.title("Second Player");
    player2.geometry("450x350");

    nameLabel = Label(player2, text="Enter Player 2 name", font=ftypeuno, bg="yellow");
    nameLabel.place(relx=0.5, rely=0.3, anchor="center");

    secondPlayerName = Entry(player2, font=ftypeuno, fg="blue");
    secondPlayerName.place(relx=0.5, rely=0.4, anchor="center");

    nameButton = Button(player2, text="get Registered", font=ftypeuno,
                        command = lambda: greetingsToPlayer(player2, secondPlayerName.get(), secondPlayerName, ftypeuno, 2, 2));
    nameButton.place(relx=0.5, rely=0.5, anchor="center");
    nameButton.config(bg="#0e73a2", fg="white");

    player2.resizable(False, False);
    player2.mainloop();

def greetingsToPlayer(master, theName, event, ftypeuno, flag, id):

    event.delete(0, END);

    global playerNames;

    playerName = theName;
    playerNumber = str(flag);

    pNameLen = len(playerName);

    if(pNameLen > 1 and ((playerName[0]>='a' and playerName[0]<='z') or (playerName[0]>='A' and playerName[0]<='Z'))):
        if (len(playerNames) >= 1 and playerNames[0] == playerName):
            messagebox.showerror("Name Error", "Player name should be different");
            if(id == 1):
                playerOne(master, ftypeuno);
            else:
                playerTwo(master, ftypeuno);
        else:
            playerNames.append(playerName);

            #print(playerNames);

            greetingsMessage = "Welcome!!\n" + playerName + "\nYou will play as player " + playerNumber + " on this Dice game\nWish you all the best";

            disAppearMainWindow(master);

            messagebox.showinfo("Greetings", greetingsMessage);

            if (flag == 1):
                playerTwo(master, ftypeuno);
            if (flag == 2):
                tossWindow(ftypeuno);
    else:
        messagebox.showerror("Name Error", "Player should be a valid name");
        if (id == 1):
            playerOne(master, ftypeuno);
        else:
            playerTwo(master, ftypeuno);

def playerOne(master, ftypeuno):

    disAppearMainWindow(master);

    global firstPlayerName, playerNames;

    player1 = Tk();
    player1.title("First Player");
    player1.geometry("450x350");

    nameLabel = Label(player1,text="Enter Player 1 name", font=ftypeuno, bg="yellow");
    nameLabel.place(relx=0.5, rely=0.3, anchor = "center");

    firstPlayerName = Entry(player1, font=ftypeuno, fg="blue");
    firstPlayerName.place(relx=0.5, rely=0.4, anchor = "center");

    nameButton = Button(player1, text = "get Registered", font=ftypeuno,
                        command= lambda : greetingsToPlayer(player1, firstPlayerName.get(), firstPlayerName, ftypeuno, 1 , 1));
    nameButton.place(relx=0.5, rely=0.5, anchor = "center");
    nameButton.config(bg="#0e73a2", fg="white");

    player1.resizable(False, False);
    player1.mainloop();

def main():
    mainWindow = Tk();
    mainWindow.title("Dice Game");
    mainWindow.geometry("450x350");

    ftypeun = "arial 10 bold underline";
    ftypeuno = "arial 10 bold";

    welcomeMessageLabel = Label(mainWindow, text = "Welcome to my Dice Game", font=ftypeuno, bg="yellow", fg="blue");
    welcomeMessageLabel.place(relx=0.5, rely=0.3, anchor = "center");

    startButton = Button(mainWindow, text = "Let's start the game", font = ftypeuno, width = 20, height = 2, fg="green"
                         , command = lambda : playerOne(mainWindow, ftypeuno));
    startButton.place(relx=0.5, rely=0.5, anchor = "center");
    startButton.config(bg="#0e73a2", fg="white");

    authorButton = Button(mainWindow, text = "Author", font = ftypeuno, command = lambda : authorButtonAction(mainWindow, ftypeuno));
    authorButton.place(relx=0.5, rely=0.9, anchor = "center");
    authorButton.config(bg = "#89b9cf", fg = "black");

    mainWindow.resizable(False, False);
    mainWindow.mainloop();


main();