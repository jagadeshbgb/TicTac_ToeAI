import tkinter as tk
import turtle as te
import time
import sys
class T3Game:
    playersDict = {"Player1AI":None,"Player2AI":None}
    labels = {"Player1AI":[],"Player2AI":[]}
    countL = 0
    countP2 = 0
    countP1 = None
    pTCount =1
    mPTSC = None
    PlayerWinner1 = {"condition":False,"value":None}
    PlayerWinner2 = {"condition":False,"value":None}
    GameOver = False
    PlayerTurn = {"Player":None}
    pTB1 = {"condition":True,"value":None}
    pTB2 = {"condition":True,"value":None}
    pTB3 = {"condition":True,"value":None}
    pTB4 = {"condition":True,"value":None}
    pTB5 = {"condition":True,"value":None}
    pTB6 = {"condition":True,"value":None}
    pTB7 = {"condition":True,"value":None}
    pTB8 = {"condition":True,"value":None}
    pTB9 = {"condition":True,"value":None}
    Screen =[]
    pNGCount = 0
    AIMC = 0

    def window(self,frame=None):
        cF = tk.Frame(frame)
        return cF

    def label(self,element=None,text=None):
        self.element = element
        self.text = text
        createLabel = tk.Label(self.element,text=self.text)
        createLabel.pack(fill="both",expand = True)
        return createLabel

    def button(self,element=None,text=None,command=None,frame=None):
        self.element = element
        self.text = text
        self.command = command
        createButton = tk.Button(self.element,text=self.text,command=self.command,frame=None)
        createButton.pack(fill="both",expand=True)
        return createButton
    
    def newGame(self,frame1=None,frame2=None):
        frame1.pack_forget()
        frame2.pack(fill="both",expand=True)
        for label in T3G.labels.get("Player1AI"):
            label.pack_forget()
        for label in T3G.labels.get("Player2AI"):
            label.pack_forget()
        T3G.playersDict = {"Player1AI":None,"Player2AI":None}
        T3G.labels = {"Player1AI":[],"Player2AI":[]}
        T3G.countL = 0
        T3G.countP2 = 0
        T3G.countP1 = None
        T3G.pTCount =1
        T3G.mPTSC = None
        T3G.PlayerWinner1 = {"condition":False,"value":None}
        T3G.PlayerWinner2 = {"condition":False,"value":None}
        T3G.GameOver = False
        T3G.pTB1 = {"condition":True,"value":None}
        T3G.pTB2 = {"condition":True,"value":None}
        T3G.pTB3 = {"condition":True,"value":None}
        T3G.pTB4 = {"condition":True,"value":None}
        T3G.pTB5 = {"condition":True,"value":None}
        T3G.pTB6 = {"condition":True,"value":None}
        T3G.pTB7 = {"condition":True,"value":None}
        T3G.pTB8 = {"condition":True,"value":None}
        T3G.pTB9 = {"condition":True,"value":None}
        T3G.Screen =[]
        T3G.AIMC = 0
        return

    def anotherNewGame(self,rTK=None,windowScreen=None,gameScreen=None):
        self.rTK = rTK
        self.windowScreen = windowscreen
        self.gameScreen = gameScreen
        T3Game.Screen.append(self.rTK)
        T3Game.Screen.append(self.gameScreen)
        T3Game.Screen.append(self.windowScreen)
        return

    def back(self,*screens):
        for screen in reversed(range(len(screens))):
            screens[screen].pack_forget()
        screens[len(screens)-2].pack(fill="both",expand=True)
        self.countP2 -= 1
        return

    def storeOX(self,value):
        self.valueOX = value
        self.playersDict['Player1AI'].append(self.valueOX)
        return

    def O(self,pGBnO,windowscreen=None,playGameScreen=None):
        value = pGBnO.cget("text")
        if(((value=="O" and (self.labels.get("Player1AI")!=[] or self.labels.get("Player1AI")==[])) or (type(self.playersDict["Player1AI"]) == type(None)) or (type(self.playersDict["Player1AI"]) != type(None))) and (self.countP2==0)):
            if((value=="O" and self.labels.get("Player1AI")!=[])):
                self.countL=0
                self.playersDict["Player1AI"] = value
                self.labels.get("Player1AI")[0].pack_forget()
            else:
                self.playersDict["Player1AI"] = value
                self.countL=0
        else:
            if((value=="O" and (self.labels.get("Player2AI")!=[])and(type(self.playersDict.get("Player1AI")) != type(None)))and self.playersDict.get("Player1AI")!="O"):
                self.countL=0
                self.playersDict["Player2AI"] = value
                for label in self.labels.get("Player2AI"):
                    label.pack_forget()
            else:
                if(self.playersDict.get("Player1AI")!="O"):
                    self.playersDict["Player2AI"] = value
                else:
                    for label in self.labels.get("Player2AI"):
                        label.pack_forget()
                    self.labels.get("Player2AI")[len(self.labels.get("Player2AI"))-1].pack()
        return
    def X(self,pGBnX):
        value = pGBnX.cget("text")
        if(((value=="X" and (self.labels.get("Player1AI")!=[] or self.labels.get("Player1AI")==[])) or (type(self.playersDict["Player1AI"]) == type(None)) and (type(self.playersDict["Player1AI"]) != type(None))) and (self.countP2==0)):
            if((value=="X" and self.labels.get("Player1AI")!=[])):
                self.countL=0
                self.playersDict["Player1AI"] = value
                self.labels.get("Player1AI")[0].pack_forget()
            else:
                self.playersDict["Player1AI"] = value
                self.countL=0
        else:
            if((value=="X" and self.labels.get("Player2AI")!=[]) and self.playersDict.get("Player1AI")!="X"):
                self.countL=0
                self.playersDict["Player2AI"] = value
                for label in self.labels.get("Player2AI"):
                    label.pack_forget()
            else:
                if(self.playersDict.get("Player1AI")!="X"):
                    self.playersDict["Player2AI"] = value
                else:
                    for label in self.labels.get("Player2AI"):
                        label.pack_forget()
                    self.labels.get("Player2AI")[len(self.labels.get("Player2AI"))-1].pack(fill="both",expand=True)
        return

    def AITurn(self):
        if(self.pNGCount%2==1):
            self.playersDict["Player1AI"] = "O"
        else:
            self.playersDict["Player1AI"] = "X"
        return

    def AITurn2(self):
        if(self.playersDict["Player1AI"]=="O"):
            self.playersDict["Player2AI"]="X"
        else:
            self.playersDict["Player2AI"]="O"
        print("players2Dict",self.playersDict["Player2AI"])
        self.countL=0
        return

    def next(self,*screens):
        if(self.playersDict["Player1AI"]==None):
            self.AITurn()
        elif(self.playersDict["Player2AI"]==None):
            print("player2Ai")
            self.AITurn2()
        if(type(self.playersDict.get("Player1AI"))==type(None) and self.countL==0 and self.countP2==0):
            Player1AI = self.label(screens[len(screens)-2],"Player did not selected X or O")
            if(type(self.playersDict.get("Player1AI"))==type(None)):
                self.labels["Player1AI"].append(Player1AI)
                self.countL+=1
        elif(self.countP2==0 and type(self.playersDict.get("Player1AI"))!=type(None)):
            self.countL=0
            for screen in screens:
                screen.pack_forget()
            if self.countL>0:
                screens[len(screens)-2].pack(fill="both",expand=True)
            else:
                screens[len(screens)-1].pack(fill="both",expand=True)
                self.countP2 += 1
                self.countP1 = False
        else:
            self.countP1 = True
        print("players1Dict",self.playersDict["Player1AI"])
        print("players2Dict",self.playersDict["Player2AI"])
        if(type(self.playersDict.get("Player1AI"))!=type(None) and self.countL==0 and self.countP2==1):
            if((type(self.playersDict.get("Player2AI"))==type(None)) and self.countL==0 and self.countP2==1):
                Player2AI = self.label(screens[len(screens)-1],f"Player did not select Player1AI choice {self.playersDict.get('Player1AI')}")
                if(type(self.playersDict.get("Player2AI"))==type(None)and self.countL==0):
                    for label in self.labels.get("Player2AI"):
                        label.pack_forget()
                    self.labels["Player2AI"].clear()
                    self.labels["Player2AI"].append(Player2AI)
                    self.countL+=1
            elif(self.countP2==1 and type(self.playersDict.get("Player2AI"))!=type(None)and self.countP1):
                print("player2AI")
                if((self.playersDict.get("Player1AI")==self.playersDict.get("Player2AI")) and self.countP1 and self.countL==0):
                    Player2AI = self.label(screens[len(screens)-2],f"Player did not select Player1AI choice {self.playersDict.get('Player1AI')}")
                    for label in self.labels.get("Player2AI"):
                        label.pack_forget()
                    self.labels["Player2AI"].clear()
                    self.labels["Player2AI"].append(Player2AI)
                    self.countL+=1
                for screen in screens:
                    screen.pack_forget()
                if self.countL>0:
                    screens[len(screens)-2].pack(fill="both",expand=True)
                else:
                    screens[len(screens)-1].pack(fill="both",expand=True)
                    self.countP2 += 1
                    self.countP1 = False
            else:
                self.countP1 = True
        return

    def playerTurnScreen(self):
        self.pTS = te.Turtle()
        self.pTS.hideturtle()
        self.pTS.penup()
        self.pTS.goto(-100,-150)
        self.pTS.pendown()
        self.pTS.forward(100)
        self.pTS.right(90)
        self.pTS.forward(50)
        self.pTS.right(90)
        self.pTS.forward(150)
        self.pTS.right(90)
        self.pTS.forward(50)
        self.pTS.right(90)
        self.pTS.forward(75)
        self.pTS.penup()
        self.pTS.goto(-80,-170)
        if(self.pTCount==1):
            self.PlayerTurn["Player"]=f"Player{self.pTCount}AI"
        else:
            self.PlayerTurn["Player"]=f"Player{self.pTCount}AI"
        player = str(self.playersDict.get(f"{self.PlayerTurn.get('Player')}"))
        self.pTS.write(f"{self.PlayerTurn.get('Player')} Turn {player}",align="center",font=("ROBOTIC",10,"bold"))
        if(self.pTCount==2):
            self.pTCount=0
        return (self.pTS,player)

    def checkpTBV(self):
        if(self.pTB1["value"] == None):
            return (-150,110)
        elif(self.pTB2["value"]==None):
            return (-50,110)
        elif(self.pTB3["value"]==None):
            return (50,110)
        elif(self.pTB4["value"]==None):
            return (-150,10)
        elif(self.pTB5["value"]==None):
            return (-50,10)
        elif(self.pTB6["value"]==None):
            return (50,10)
        elif(self.pTB7["value"]==None):
            return (-150,-90)
        elif(self.pTB8["value"]==None):
            return (-50,-90)
        elif(self.pTB9["value"]==None):
            return (50,-90)        
        return

    def AIMove(self,mSC,mPTSC):
        resultPW = self.PlayerWinner(mSC)
        print("resultPW",resultPW)
        if(resultPW==True):
            return
        if(self.AIMC==0 and self.pTB1["value"] == None):
            mSC.goto(-150,110)
            self.pTB1["value"] = self.mPTSC[1]
            mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
            self.mPTSC[0].clear()
            self.pTCount += 1
            self.mPTSC = self.playerTurnScreen()
            mSC.showturtle()
            self.pTB1["condition"]=False
            self.PlayerWinner(mSC)
        elif(self.AIMC and self.pTB2["value"]==None):
            result = self.checkpTBV()
            mSC.goto(result[0],result[1])
            self.pTB2["value"] = self.mPTSC[1]
            mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
            self.mPTSC[0].clear()
            self.pTCount += 1
            self.mPTSC = self.playerTurnScreen()
            mSC.showturtle()
            self.pTB2["condition"]=False
            self.PlayerWinner(mSC)
        elif(self.AIMC and self.pTB3["value"]==None):
            result = self.checkpTBV()
            mSC.goto(result[0],result[1])
            self.pTB3["value"] = self.mPTSC[1]
            mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
            self.mPTSC[0].clear()
            self.pTCount += 1
            self.mPTSC = self.playerTurnScreen()
            mSC.showturtle()
            self.pTB3["condition"]=False
            self.PlayerWinner(mSC)
        elif(self.AIMC and self.pTB4["value"]==None):
            result = self.checkpTBV()
            mSC.goto(result[0],result[1])
            self.pTB4["value"] = self.mPTSC[1]
            mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
            self.mPTSC[0].clear()
            self.pTCount += 1
            self.mPTSC = self.playerTurnScreen()
            mSC.showturtle()
            self.pTB4["condition"]=False
            self.PlayerWinner(mSC)
        elif(self.AIMC and self.pTB5["value"]==None):
            result = self.checkpTBV()
            mSC.goto(result[0],result[1])
            self.pTB5["value"] = self.mPTSC[1]
            mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
            self.mPTSC[0].clear()
            self.pTCount += 1
            self.mPTSC = self.playerTurnScreen()
            mSC.showturtle()
            self.pTB5["condition"]=False
            self.PlayerWinner(mSC)
        elif(self.AIMC and self.pTB6["value"]==None):
            result = self.checkpTBV()
            mSC.goto(result[0],result[1])
            self.pTB6["value"] = self.mPTSC[1]
            mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
            self.mPTSC[0].clear()
            self.pTCount += 1
            self.mPTSC = self.playerTurnScreen()
            mSC.showturtle()
            self.pTB6["condition"]=False
            self.PlayerWinner(mSC)
        elif(self.AIMC and self.pTB7["value"]==None):
            result = self.checkpTBV()
            mSC.goto(result[0],result[1])
            self.pTB7["value"] = self.mPTSC[1]
            mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
            self.mPTSC[0].clear()
            self.pTCount += 1
            self.mPTSC = self.playerTurnScreen()
            mSC.showturtle()
            self.pTB7["condition"]=False
            self.PlayerWinner(mSC)
        elif(self.AIMC and self.pTB8["value"]==None):
            result = self.checkpTBV()
            mSC.goto(result[0],result[1])
            self.pTB8["value"] = self.mPTSC[1]
            mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
            self.mPTSC[0].clear()
            self.pTCount += 1
            self.mPTSC = self.playerTurnScreen()
            mSC.showturtle()
            self.pTB8["condition"]=False
            self.PlayerWinner(mSC)
        elif(self.AIMC and self.pTB9["value"]==None):
            result = self.checkpTBV()
            mSC.goto(result[0],result[1])
            self.pTB9["value"] = self.mPTSC[1]
            mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
            self.mPTSC[0].clear()
            self.pTCount += 1
            self.mPTSC = self.playerTurnScreen()
            mSC.showturtle()
            self.pTB9["condition"]=False
        self.AIMC += 1
        print(self.AIMC,"self.AIMC",resultPW,"resultPW")
        if(resultPW==False):
            self.AIMove(mSC,self.mPTSC)
        print("resultPW",resultPW)
        print(self.AIMC,"self.AIMC")
        return

    def demo(self):
        self.demoScreen = te.Screen()
        self.__screen = te.Turtle()
        self.__screen.penup()
        self.__screen.goto(-200,200)
        self.__screen.forward(100)
        self.__screen.right(-90)
        self.__screen.forward(15)
        self.__screen.pendown()
        self.__screen.forward(50)
        self.__screen.right(90)
        self.__screen.forward(100)
        self.__screen.right(90)
        self.__screen.forward(50)
        self.__screen.right(90)
        self.__screen.forward(100)
        self.__screen.right(90)
        self.__screen.forward(25)
        self.__screen.right(90)
        self.__screen.penup()
        self.__screen.forward(50)
        self.__screen.write("Demo",align="center",font=("ROBOTIC",10,"bold"))
        self.__screen.penup()
        self.__screen.goto(-200,200)
        self.__screen.pendown()
        self.__screen.forward(300)
        self.__screen.right(90)
        self.__screen.forward(300)
        self.__screen.right(90)
        self.__screen.forward(300)
        self.__screen.right(90)
        self.__screen.forward(300)
        self.__screen.right(90)
        self.__screen.forward(100)
        self.__screen.right(90)
        self.__screen.forward(300)
        self.__screen.right(-90)
        self.__screen.forward(100)
        self.__screen.right(-90)
        self.__screen.forward(300)
        self.__screen.right(90)
        self.__screen.penup()
        self.__screen.forward(100)
        self.__screen.right(90)
        self.__screen.forward(100)
        self.__screen.right(90)
        self.__screen.pendown()
        self.__screen.forward(300)
        self.__screen.penup()
        self.__screen.right(-90)
        self.__screen.forward(100)
        self.__screen.right(-90)
        self.__screen.pendown()
        self.__screen.forward(300)
        self.__screen.right(90)
        self.__screen.penup()
        self.__screen.forward(100)
        self.__screen.right(90)
        self.__screen.forward(300)
        self.__screen.right(-90)
        self.__screen.forward(50)
        self.__screen.right(-90)
        self.__screen.forward(100)
        self.__screen.pendown()
        self.__pTSC=self.playerTurnScreen()
        self.__screen.penup()
        self.__screen.hideturtle()
        self.__screen.goto(-200,200)
        self.__screen.goto(-150,150)
        self.__screen.write(f"{self.playersDict.get('Player1AI')}",align="center",font=("ROBOTIC",20,"bold"))        
        self.__pTSC[0].clear()
        self.pTCount+=1
        self.__pTSC = self.playerTurnScreen()
        self.__screen.goto(-150,50)
        self.__screen.write(f"{self.playersDict.get('Player2AI')}",align="center",font=("ROBOTIC",20,"bold"))
        self.__pTSC[0].clear()
        self.pTCount+=1
        self.__pTSC = self.playerTurnScreen()
        self.__screen.goto(-50,50)
        self.__screen.write(f"{self.playersDict.get('Player1AI')}",align="center",font=("ROBOTIC",20,"bold"))
        self.__pTSC[0].clear()
        self.pTCount+=1
        self.__pTSC = self.playerTurnScreen()
        self.__screen.goto(50,150)
        self.__screen.write(f"{self.playersDict.get('Player2AI')}",align="center",font=("ROBOTIC",20,"bold"))
        self.__pTSC[0].clear()
        self.pTCount+=1
        self.__pTSC = self.playerTurnScreen()
        self.__screen.goto(-50,150)
        self.__screen.write(f"{self.playersDict.get('Player1AI')}",align="center",font=("ROBOTIC",20,"bold"))
        self.__pTSC[0].clear()
        self.pTCount+=1
        self.__pTSC = self.playerTurnScreen()
        self.__screen.goto(50,-50)
        self.__screen.write(f"{self.playersDict.get('Player2AI')}",align="center",font=("ROBOTIC",20,"bold"))
        self.__pTSC[0].clear()
        self.pTCount+=1
        self.__pTSC = self.playerTurnScreen()
        self.__screen.goto(-50,-50)
        self.__screen.write(f"{self.playersDict.get('Player1AI')}",align="center",font=("ROBOTIC",20,"bold"))
        self.__pTSC[0].clear()
        self.pTCount+=1
        self.__screen.showturtle()
        self.__screen.goto(-150,-150)
        self.__screen.pendown()
        self.__screen.forward(200)
        self.__screen.right(90)
        self.__screen.forward(50)
        self.__screen.right(90)
        self.__screen.forward(200)
        self.__screen.right(90)
        self.__screen.forward(50)
        self.__screen.penup()
        self.__screen.goto(-50,-170)
        self.__screen.hideturtle()
        self.__screen.pendown()
        self.__screen.write(f"Player1AI {self.playersDict.get('Player1AI')} Winner",align="center",font=("ROBOTIC",10,"bold"))
        self.__screen.speed(10)
        time.sleep(5)
        self.__screen.penup()
        self.__screen.clear()
        return (self.__screen,self.demoScreen)

    def main(self):
        self.__mainScreen = te.Turtle()
        self.__mainScreen.penup()
        self.__mainScreen.goto(-200,200)
        self.__mainScreen.pendown()
        self.__mainScreen.forward(300)
        self.__mainScreen.right(90)
        self.__mainScreen.forward(300)
        self.__mainScreen.right(90)
        self.__mainScreen.forward(300)
        self.__mainScreen.right(90)
        self.__mainScreen.forward(300)
        self.__mainScreen.right(90)
        self.__mainScreen.forward(100)
        self.__mainScreen.right(90)
        self.__mainScreen.forward(300)
        self.__mainScreen.right(-90)
        self.__mainScreen.forward(100)
        self.__mainScreen.right(-90)
        self.__mainScreen.forward(300)
        self.__mainScreen.right(90)
        self.__mainScreen.penup()
        self.__mainScreen.forward(100)
        self.__mainScreen.right(90)
        self.__mainScreen.forward(100)
        self.__mainScreen.right(90)
        self.__mainScreen.pendown()
        self.__mainScreen.forward(300)
        self.__mainScreen.penup()
        self.__mainScreen.right(-90)
        self.__mainScreen.forward(100)
        self.__mainScreen.right(-90)
        self.__mainScreen.pendown()
        self.__mainScreen.forward(300)
        self.__mainScreen.right(90)
        self.__mainScreen.penup()
        self.__mainScreen.forward(100)
        self.__mainScreen.right(90)
        self.__mainScreen.forward(300)
        self.__mainScreen.right(-90)
        self.__mainScreen.forward(50)
        self.__mainScreen.right(-90)
        self.__mainScreen.forward(100)
        self.__mainScreen.penup()
        self.pTCount=1
        self.mPTSC=self.playerTurnScreen()
        self.busy = False
        self.__mSC = self.__mainScreen.getscreen()
        self.AIMove(self.__mainScreen,self.mPTSC)
        self.__mSC.onclick(lambda x,y:self.mainScreenCursor(x,y,self.__mainScreen))
        return self.__mainScreen

    def GameWinDraw(self,mSC):
        mSC.goto(-150,-150)
        mSC.pendown()
        mSC.forward(200)
        mSC.right(90)
        mSC.forward(50)
        mSC.right(90)
        mSC.forward(200)
        mSC.right(90)
        mSC.forward(50)
        mSC.penup()
        mSC.goto(-50,-170)
        mSC.hideturtle()
        mSC.pendown()
        return

    def PlayerWinner(self,mSC):
        if(((self.pTB1.get("condition")==False) or (self.pTB2.get("condition")==False) or (self.pTB3.get("condition")==False) or (self.pTB3.get("condition")==False) or (self.pTB4.get("condition")==False) or (self.pTB5.get("condition")==False) or (self.pTB6.get("condition")==False) or (self.pTB7.get("condition")==False) or (self.pTB8.get("condition")==False) or (self.pTB9.get("condition")==False)) and (self.GameOver == False)):                 
                if(((self.pTB1.get("value")=="X")and (self.pTB2.get("value")=="X") and (self.pTB3.get("value")=="X")) or ((self.pTB1.get("value")=="O") and (self.pTB2.get("value")=="O") and (self.pTB3.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)                
                    if(self.pTB1.get('value')==self.playersDict.get('Player1AI')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('Player1AI')
                    elif(self.pTB2.get('value')==self.playersDict.get('Player2AI')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('Player2AI')
                elif(((self.pTB4.get("value")=="X")and (self.pTB5.get("value")=="X") and (self.pTB6.get("value")=="X")) or ((self.pTB4.get("value")=="O") and (self.pTB5.get("value")=="O") and (self.pTB6.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB4.get('value')==self.playersDict.get('Player1AI')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('Player1AI')
                    elif(self.pTB5.get('value')==self.playersDict.get('Player2AI')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('Player2AI')
                elif(((self.pTB7.get("value")=="X")and (self.pTB8.get("value")=="X") and (self.pTB9.get("value")=="X")) or ((self.pTB7.get("value")=="O") and (self.pTB8.get("value")=="O") and (self.pTB9.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB7.get('value')==self.playersDict.get('Player1AI')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('Player1AI') 
                    elif(self.pTB7.get('value')==self.playersDict.get('Player2AI')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('Player2AI')
                elif(((self.pTB1.get("value")=="X")and (self.pTB4.get("value")=="X") and (self.pTB7.get("value")=="X")) or ((self.pTB1.get("value")=="O") and (self.pTB4.get("value")=="O") and (self.pTB7.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB1.get('value')==self.playersDict.get('Player1AI')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('Player1AI')                        
                    elif(self.pTB1.get('value')==self.playersDict.get('Player2AI')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('Player2AI')
                elif(((self.pTB2.get("value")=="X")and (self.pTB5.get("value")=="X") and (self.pTB8.get("value")=="X")) or ((self.pTB2.get("value")=="O") and (self.pTB5.get("value")=="O") and (self.pTB8.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB2.get('value')==self.playersDict.get('Player1AI')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('Player1AI') 
                    elif(self.pTB2.get('value')==self.playersDict.get('Player2AI')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('Player2AI')
                elif(((self.pTB3.get("value")=="X")and (self.pTB6.get("value")=="X") and (self.pTB9.get("value")=="X")) or ((self.pTB3.get("value")=="O") and (self.pTB6.get("value")=="O") and (self.pTB9.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB3.get('value')==self.playersDict.get('Player1AI')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('Player1AI') 
                    elif(self.pTB3.get('value')==self.playersDict.get('Player2AI')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('Player2AI')
                elif(((self.pTB1.get("value")=="X")and (self.pTB5.get("value")=="X") and (self.pTB9.get("value")=="X")) or ((self.pTB1.get("value")=="O") and (self.pTB5.get("value")=="O") and (self.pTB9.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB9.get('value')==self.playersDict.get('Player1AI')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('Player1AI')                        
                    elif(self.pTB9.get('value')==self.playersDict.get('Player2AI')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('Player2AI')
                elif(((self.pTB3.get("value")=="X")and (self.pTB5.get("value")=="X") and (self.pTB7.get("value")=="X")) or ((self.pTB3.get("value")=="O") and (self.pTB5.get("value")=="O") and (self.pTB7.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB7.get('value')==self.playersDict.get('Player1AI')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('Player1AI')                        
                    elif(self.pTB7.get('value')==self.playersDict.get('Player2AI')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('Player2AI')
                elif((self.pTB1.get("value")!=None) and (self.pTB2.get("value")!=None) and (self.pTB3.get("value")!=None) and (self.pTB4.get("value")!=None) and (self.pTB5.get("value")!=None) and (self.pTB6.get("value")!=None) and (self.pTB7.get("value")!=None) and (self.pTB8.get("value")!=None) and (self.pTB9.get("value")!=None)):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    self.GameOver = True
                if(self.PlayerWinner1.get('condition')):
                    mSC.write(f"Player1AI {self.PlayerWinner1.get('value')} WINNER",align="center",font=("ROBOTIC",10,"bold"))
                    self.GameOver = True
                    self.playNewGame(mSC)
                    mSC.penup()
                    self.exit(mSC)
                elif(self.PlayerWinner2.get('condition')):
                    mSC.write(f"Player2AI {self.PlayerWinner2.get('value')} WINNER",align="center",font=("ROBOTIC",10,"bold"))
                    self.GameOver = True
                    self.playNewGame(mSC)
                    mSC.penup()
                    self.exit(mSC)
                elif(self.GameOver == True):
                    mSC.write(f"Game Draw",align="center",font=("ROBOTIC",10,"bold"))
                    self.playNewGame(mSC)
                    mSC.penup()
                    self.exit(mSC)
        return self.GameOver

    def playNewGame(self,mSC):
        mSC.showturtle()
        mSC.penup()
        mSC.right(180)
        mSC.forward(50)
        mSC.right(90)
        mSC.forward(10)
        mSC.pendown()
        mSC.forward(100)
        mSC.right(-90)
        mSC.forward(40)
        mSC.right(-90)
        mSC.forward(100)
        mSC.right(-90)
        mSC.forward(40)
        mSC.right(-90)
        mSC.forward(50)
        mSC.right(-90)
        mSC.penup()
        mSC.forward(20)
        mSC.write("NewGame",align="center",font=("ROBOTIC",10,"bold"))
        mSC.penup()
        mSC.hideturtle()
        self.pNGCount+=1
        return

    def callBackPlayNewGame(self,mSC=None):
        mSC.clear()
        T3Game.Screen[0].deiconify()
        T3Game.Screen[1].pack_forget()
        T3Game.Screen[len(T3Game.Screen)-1].pack(fill="both",expand=True)
        return

    def exit(self,mSC):
        mSC.showturtle()
        mSC.goto(-50,-220)
        mSC.pendown()
        mSC.right(-90)
        mSC.forward(100)
        mSC.right(90)
        mSC.forward(40)
        mSC.right(90)
        mSC.forward(100)
        mSC.right(90)
        mSC.forward(40)
        mSC.penup()
        mSC.goto(-10,-245)
        mSC.write("Exit",align="center",font=("ROBOTIC",10,"bold"))
        mSC.hideturtle()
        return

    def cBExit(self,x=None,y=None,mSC=None,pEXit=None):
        self.demoScreen.bye()
        sys.exit()       
        return

    def mainScreenCursor(self,x,y,mSC):
        minX = -200
        maxX = 100
        minY = -100
        maxY = 200
        if self.busy:
            return
        self.busy = True

        try:
            '''
            if((x>minX and y>minY) and (x<maxX and y<maxY) and self.GameOver==False):
                if(-100>x and 100<y and self.pTB1.get("condition")):
                    mSC.hideturtle()
                    mSC.goto(-150,110)
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB1["value"] = self.mPTSC[1]
                    self.mPTSC[0].clear()
                    self.pTCount += 1
                    self.mPTSC = self.playerTurnScreen()
                    mSC.showturtle()
                    self.pTB1["condition"]=False
                    result = self.PlayerWinner(mSC)
                    if(result==False):
                        self.AIMove(mSC,self.mPTSC)
                elif(0>x and -100<x and 200>y and y>100 and self.pTB2.get("condition")):
                    mSC.hideturtle()
                    mSC.goto(-50,110)
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB2["value"] = self.mPTSC[1]
                    self.mPTSC[0].clear()
                    self.pTCount += 1
                    self.mPTSC = self.playerTurnScreen()
                    mSC.showturtle()
                    self.pTB2["condition"]=False
                    result = self.PlayerWinner(mSC)
                    if(result==False):
                        self.AIMove(mSC,self.mPTSC)
                elif(x>0 and y>100 and self.pTB3.get("condition")):
                    mSC.hideturtle()
                    mSC.goto(50,110)
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB3["value"] = self.mPTSC[1]
                    self.mPTSC[0].clear()
                    self.pTCount += 1
                    self.mPTSC = self.playerTurnScreen()
                    mSC.showturtle()
                    self.pTB3["condition"]=False
                    result = self.PlayerWinner(mSC)
                    if(result==False):
                        self.AIMove(mSC,self.mPTSC)
                elif(-100>x and y>0 and 100>y and self.pTB4.get("condition")):
                    mSC.hideturtle()
                    mSC.goto(-150,10)
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB4["value"] = self.mPTSC[1]
                    self.mPTSC[0].clear()
                    self.pTCount+=1
                    self.mPTSC = self.playerTurnScreen()
                    mSC.showturtle()
                    self.pTB4["condition"]=False
                    result = self.PlayerWinner(mSC)
                    if(result==False):
                        self.AIMove(mSC,self.mPTSC)
                elif(x>-100 and y<100 and x<0 and y>0 and self.pTB5.get("condition")):
                    mSC.hideturtle()
                    mSC.goto(-50,10)
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB5["value"] = self.mPTSC[1]
                    self.mPTSC[0].clear()
                    self.pTCount+=1
                    self.mPTSC = self.playerTurnScreen()
                    mSC.showturtle()
                    self.pTB5["condition"]=False
                    result = self.PlayerWinner(mSC)
                    if(result==False):
                        self.AIMove(mSC,self.mPTSC)
                elif(x<100 and y<100 and y>0 and x>0 and self.pTB6.get("condition")):
                    mSC.hideturtle()
                    mSC.goto(50,10)
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB6["value"] = self.mPTSC[1]
                    self.mPTSC[0].clear()
                    self.pTCount+=1
                    self.mPTSC = self.playerTurnScreen()
                    mSC.showturtle()
                    self.pTB6["condition"]=False
                    result = self.PlayerWinner(mSC)
                    if(result==False):
                        self.AIMove(mSC,self.mPTSC)
                elif(x<-100 and y<0 and self.pTB7.get("condition")):
                    mSC.hideturtle()
                    mSC.goto(-150,-90)
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB7["value"] = self.mPTSC[1]
                    self.mPTSC[0].clear()
                    self.pTCount+=1
                    self.mPTSC = self.playerTurnScreen()
                    mSC.showturtle()
                    self.pTB7["condition"]=False
                    result = self.PlayerWinner(mSC)
                    if(result==False):
                        self.AIMove(mSC,self.mPTSC)
                elif(x>-100 and y>-100 and y<0 and x<0 and self.pTB8.get("condition")):
                    mSC.hideturtle()
                    mSC.goto(-50,-90)
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB8["value"] = self.mPTSC[1]
                    self.mPTSC[0].clear()
                    self.pTCount+=1
                    self.mPTSC = self.playerTurnScreen()
                    mSC.showturtle()
                    self.pTB8["condition"]=False
                    result = self.PlayerWinner(mSC)
                    if(result==False):
                        self.AIMove(mSC,self.mPTSC)
                elif(x<100 and y>-100 and y<0 and x>0 and self.pTB9.get("condition")):
                    mSC.hideturtle()
                    mSC.goto(50,-90)
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB9["value"] = self.mPTSC[1]
                    self.mPTSC[0].clear()
                    self.pTCount+=1
                    self.mPTSC = self.playerTurnScreen()
                    mSC.showturtle()
                    self.pTB9["condition"]=False
                    result = self.PlayerWinner(mSC)
                    if(result==False):
                        self.AIMove(mSC,self.mPTSC)
            if(((self.pTB1.get("condition")==False) or (self.pTB2.get("condition")==False) or (self.pTB3.get("condition")==False) or (self.pTB3.get("condition")==False) or (self.pTB4.get("condition")==False) or (self.pTB5.get("condition")==False) or (self.pTB6.get("condition")==False) or (self.pTB7.get("condition")==False) or (self.pTB8.get("condition")==False) or (self.pTB9.get("condition")==False)) and (self.GameOver == False)):
                if(((self.pTB1.get("value")=="X")and (self.pTB2.get("value")=="X") and (self.pTB3.get("value")=="X")) or ((self.pTB1.get("value")=="O") and (self.pTB2.get("value")=="O") and (self.pTB3.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB1.get('value')==self.playersDict.get('Player1AI')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('Player1AI')
                    elif(self.pTB2.get('value')==self.playersDict.get('Player2AI')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('Player2AI')
                elif(((self.pTB4.get("value")=="X")and (self.pTB5.get("value")=="X") and (self.pTB6.get("value")=="X")) or ((self.pTB4.get("value")=="O") and (self.pTB5.get("value")=="O") and (self.pTB6.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB4.get('value')==self.playersDict.get('Player1AI')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('Player1AI')
                    elif(self.pTB5.get('value')==self.playersDict.get('Player2AI')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('Player2AI')
                elif(((self.pTB7.get("value")=="X")and (self.pTB8.get("value")=="X") and (self.pTB9.get("value")=="X")) or ((self.pTB7.get("value")=="O") and (self.pTB8.get("value")=="O") and (self.pTB9.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB7.get('value')==self.playersDict.get('Player1AI')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('Player1AI')
                    elif(self.pTB7.get('value')==self.playersDict.get('Player2AI')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('Player2AI')
                elif(((self.pTB1.get("value")=="X")and (self.pTB4.get("value")=="X") and (self.pTB7.get("value")=="X")) or ((self.pTB1.get("value")=="O") and (self.pTB4.get("value")=="O") and (self.pTB7.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB1.get('value')==self.playersDict.get('Player1AI')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('Player1AI')
                    elif(self.pTB1.get('value')==self.playersDict.get('Player2AI')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('Player2AI')
                elif(((self.pTB2.get("value")=="X")and (self.pTB5.get("value")=="X") and (self.pTB8.get("value")=="X")) or ((self.pTB2.get("value")=="O") and (self.pTB5.get("value")=="O") and (self.pTB8.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB2.get('value')==self.playersDict.get('Player1AI')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('Player1AI')
                    elif(self.pTB2.get('value')==self.playersDict.get('Player2AI')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('Player2AI')
                elif(((self.pTB3.get("value")=="X")and (self.pTB6.get("value")=="X") and (self.pTB9.get("value")=="X")) or ((self.pTB3.get("value")=="O") and (self.pTB6.get("value")=="O") and (self.pTB9.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB3.get('value')==self.playersDict.get('Player1AI')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('Player1AI')
                    elif(self.pTB3.get('value')==self.playersDict.get('Player2AI')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('Player2AI')
                elif(((self.pTB1.get("value")=="X")and (self.pTB5.get("value")=="X") and (self.pTB9.get("value")=="X")) or ((self.pTB1.get("value")=="O") and (self.pTB5.get("value")=="O") and (self.pTB9.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB9.get('value')==self.playersDict.get('Player1AI')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('Player1AI')
                    elif(self.pTB9.get('value')==self.playersDict.get('Player2AI')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('Player2AI')
                elif(((self.pTB3.get("value")=="X")and (self.pTB5.get("value")=="X") and (self.pTB7.get("value")=="X")) or ((self.pTB3.get("value")=="O") and (self.pTB5.get("value")=="O") and (self.pTB7.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB7.get('value')==self.playersDict.get('Player1AI')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('Player1AI')
                    elif(self.pTB7.get('value')==self.playersDict.get('Player2AI')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('Player2AI')
                elif((self.pTB1.get("value")!=None) and (self.pTB2.get("value")!=None) and (self.pTB3.get("value")!=None) and (self.pTB4.get("value")!=None) and (self.pTB5.get("value")!=None) and (self.pTB6.get("value")!=None) and (self.pTB7.get("value")!=None) and (self.pTB8.get("value")!=None) and (self.pTB9.get("value")!=None)):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    self.GameOver = True
                if(self.PlayerWinner1.get('condition')):
                    mSC.write(f"Player1AI {self.PlayerWinner1.get('value')} WINNER",align="center",font=("ROBOTIC",10,"bold"))
                    self.GameOver = True
                    self.playNewGame(mSC)
                    mSC.penup()
                    self.exit(mSC)
                elif(self.PlayerWinner2.get('condition')):
                    mSC.write(f"Player2AI {self.PlayerWinner2.get('value')} WINNER",align="center",font=("ROBOTIC",10,"bold"))
                    self.GameOver = True
                    self.playNewGame(mSC)
                    mSC.penup()
                    self.exit(mSC)
                elif(self.GameOver == True):
                    mSC.write(f"Game Draw",align="center",font=("ROBOTIC",10,"bold"))
                    self.playNewGame(mSC)
                    mSC.penup()
                    self.exit(mSC)
            '''
            pMinX=-160
            pMaxX =-60
            pMinY=-250
            pMaxY=-220
            eMinX = -50
            eMaxX = 50
            eMinY = -250
            eMaxY = -220
            if(self.PlayerWinner1.get('condition')):
                if((pMinX<x and pMaxX>x) and(pMinY<y and pMaxY>y)):
                    self.callBackPlayNewGame(mSC)
                elif((eMinX<x and eMaxX>x) and(eMinY<y and eMaxY>y)):
                    self.cBExit()
            elif(self.PlayerWinner2.get('condition')):
                if((pMinX<x and pMaxX>x) and(pMinY<y and pMaxY>y)):
                    self.callBackPlayNewGame(mSC)
                elif((eMinX<x and eMaxX>x) and(eMinY<y and eMaxY>y)):
                    self.cBExit()
            elif(self.GameOver == True):
                if((pMinX<x and pMaxX>x) and(pMinY<y and pMaxY>y)):
                    self.callBackPlayNewGame(mSC)
                elif((eMinX<x and eMaxX>x) and(eMinY<y and eMaxY>y)):
                    self.cBExit()
        finally:
            self.busy=False
        return

    def playGame(self,rTK):
        rTK.withdraw()
        self.demoSc = self.demo()
        self.moveCursor = self.demoSc[0].getscreen()
        self.mainSc = self.main()
        te.done()
        return


#open GUI
T3GUIG = tk.Tk()
T3GUIG.title("TicTacToe")

#object
T3G = T3Game()

#windowscreen
windowscreen = T3G.window(T3GUIG)
windowscreen.pack(fill="both",expand=True)

#playGame frame Player1AI
playGameScreen = T3G.window(T3GUIG)
#playGame Player1AI label
pGSLO = T3G.label(playGameScreen,"AITurn")
AIO = T3G.label(playGameScreen,"O")
AIX = T3G.label(playGameScreen,"X")
#playGame frame Player2AI
playGameScreenP2 = T3G.window(T3GUIG)
#playGame Player1AI label
pGSLO = T3G.label(playGameScreenP2,"AI2Turn")
#playGame Button
AI2O = T3G.label(playGameScreenP2,"O")
#playGame Button
AI2X = T3G.label(playGameScreenP2,"X")

#playGame Button
pGBnNt = T3G.button(playGameScreen,"Next",command=lambda:T3G.next(windowscreen,playGameScreen,playGameScreenP2),frame=None)

#playGame Button
pGBnBk = T3G.button(playGameScreen,"Back",command=lambda:T3G.back(windowscreen,playGameScreen),frame=None)

def Next(*arguments,elementFrame=None,text=None,classObject=None,frame=None):
    nT = classObject.button(element=elementFrame,text=text,command=lambda:classObject.next(*arguments),frame=frame)
    return nT

def Back(*arguments,elementFrame=None,text=None,classObject=None,frame=None):
    bK = classObject.button(element=elementFrame,text=text,command=lambda:classObject.back(*arguments),frame=frame)
    return bK

#GameScreen
gS = T3G.window(T3GUIG)
gSB = T3G.button(gS,"Play Game",command=lambda:T3G.playGame(T3GUIG),frame=None)
#playGame Buttonnt and Buttonbk
nTScreens = [windowscreen,playGameScreen,playGameScreenP2,gS]
bKScreens = [windowscreen,playGameScreen,playGameScreenP2]
pGBnNtP2 = Next(*nTScreens,elementFrame=playGameScreenP2,text="Next",classObject=T3G)
pGBnBkP2 = Back(*bKScreens,elementFrame=playGameScreenP2,text="Back",classObject=T3G)

#gameScreen Buttonbk
bKScreens+=[gS]
gSBBk = Back(*bKScreens,elementFrame=gS,text="Back",classObject =T3G)

#label creation
mainscreenlabel = T3G.label(windowscreen,"Tic Tac Toe")               

#button creation
buttoncreation = T3G.button(windowscreen,"New Game",command = lambda :T3G.newGame(windowscreen,playGameScreen),frame=None)
newGame = T3G.anotherNewGame(rTK=T3GUIG,windowScreen=windowscreen,gameScreen=gS)

#application running and responsive
T3GUIG.mainloop()
        

    

    

    

    
        

    

    
        
        

    
                
        
                
        

    
    

    

    

    
