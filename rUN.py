from tkinter import *
import subprocess
from PIL import ImageTk, Image
import mysql.connector as mysql

root=Tk()
root.title('Soccer Game Startup')
root.resizable(False,False)

bg=Image.open('BG1.png')
bg = bg.resize((600, 600), Image.LANCZOS)
bg = ImageTk.PhotoImage(bg)
panel = Label(root, image = bg)

panel.grid(row=0,column=0,rowspan=6,columnspan=4)

label=Label(root,text=None,font=('Arial',2))
#label.config(background="none", bg="#00000000")
label.grid(row=0,column=0,columnspan=4,pady=40)

#Function to Start the Game
def startGame():
    subprocess.run(['python','SoccerGame.py'])

#Function to Refresh the Leaderboard
def refreshLeaderboard():
    global top

    string=''
    conn=mysql.connect(host='localhost',user='root',passwd='harshkh@1202',database='hvk')
    cursor=conn.cursor()
    cursor.execute('select * from soccerScore order by score desc;')
    data=cursor.fetchall()
    if len(data)==0:
        string='1# \n2# \n3#'
    if len(data)==1:
        string='1# '+str(data[0][0])+' - '+str(data[0][1])+'\n2# \n3#'
    if len(data)==2:
        string='1# '+str(data[0][0])+' - '+str(data[0][1])+'\n2# '+str(data[1][0])+' - '+str(data[1][1])+'\n3#'
    if len(data)>2:
        string='1# '+str(data[0][0])+' - '+str(data[0][1])+'\n2# '+str(data[1][0])+' - '+str(data[1][1])+'\n3# '+str(data[2][0])+' - '+str(data[2][1])
        
    top.grid_remove()
    top=Label(root,text=string,font=('Arial',12))
    top.grid(row=3,column=1,columnspan=2)
    
    conn.close()


#Play Game Button
Button(root,text='Play Game',font=('Arial',16),command=startGame,width=30,height=2).grid(row=1,column=1,columnspan=2)
#Leaderboard Heading
Label(root,text='Leaderboard',font=('Arial',16)).grid(row=2,column=1,columnspan=2)
#Refresh Button
Button(root,text='Refresh',font=('Arial',12),command=refreshLeaderboard).grid(row=5,column=1,columnspan=2)

top=Label(root,text='1# \n2# \n3#',font=('Arial',12))
top.grid(row=3,column=1,columnspan=2)

refreshLeaderboard()

root.mainloop()
