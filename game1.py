#snake game by musfira ansari and fizza tariq
#using tkinter

from tkinter import *
import random,time
#snake game window
class Snake(Tk):
    #initial set up function to make a window
    def __init__(self,*arge,**kwargs):
        Tk.__init__(self,*arge,**kwargs)
        self.initialSetup()
    #iitilaized score 
    def initialSetup(self):
        #canvas use to set the width,height and background colour of the window
        self.base=Canvas(self,width=500,height=500,bg='black')
        self.base.pack(padx=10,pady=10)
        #snake body create 
        self.snake=self.base.create_rectangle(1,1,21,21,fill="green")
        #score
        self.score=0
        self.scoreDisplay=Label(self,text="Score:{}".format(self.score),font=('arial',20,'bold'))
        self.scoreDisplay.pack(anchor='n')
        self.length=3
        self.target=None
        self.gameStatus=1
        self.x=20
        self.y=0
        self.bodycoords=[(0,0)]    
        self.bind('<Any-KeyPress>',self.linkKeys)
        return
    #sanke cords
    def check_snake_coords(self):
        self.base.move(self.snake,self.x,self.y)
        i,j,ii,jj=self.base.coords(self.snake)
        if i<=0 or j<=0 or ii>=500 or jj>=500:
            self.x=0
            self.y=0
            #gameover
            self.base.create_text(220,220,text="GAME OVER",font=('arial',40,'bold'),fill='red')
            self.gameStatus=0
        return
    #movement of snake
    def move_snake(self):
        pass

    
    #snake food    
    def food(self):
        pass
    #update score if snake ate food  
    def updateScore(self):
        pass
    #use link key to change the diection of snake 
    def linkKeys(self,event=None):
       pass
    #game over than start the process again
    def manage(self):
        pass
#snake game title
snakeobj=Snake(className="Snake game")
while True:
    snakeobj.update()
    snakeobj.update_idletasks()
    snakeobj.manage()
    time.sleep(0.4)

