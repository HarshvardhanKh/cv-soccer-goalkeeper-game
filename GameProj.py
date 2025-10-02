import cv2
import mediapipe as mp
import time
import cvzone
import random

vid=cv2.VideoCapture(0)

ball=cv2.imread('soccerBall.png',cv2.IMREAD_UNCHANGED)
ball=cv2.resize(ball,(0,0),None,0.2,0.2)

keeper=cv2.imread('goalkeeper.png',cv2.IMREAD_UNCHANGED)
keeper=cv2.resize(keeper,(0,0),None,0.6,0.6)

mpPose=mp.solutions.pose
pose=mpPose.Pose()
mpDraw=mp.solutions.drawing_utils

def drawPose(frame,landmarkNo=None):
    global mpPose,pose,mpDraw
    imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=pose.process(imgRGB)
    landmark={}
    if results.pose_landmarks:
        mpDraw.draw_landmarks(frame,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        if landmarkNo!=None:
            for idd,lms in enumerate(results.pose_landmarks.landmark):
                temp=[]
                if idd in landmarkNo:
                    landmark[idd]=[lms.x,lms.y]
    if landmark!=None:
        return[frame,landmark]
    return [frame]

pTime=time.time()

##############################
endPositions=[[300,360],[200,360],[450,360],[100,360],[540,360]]
choices=[300,200,450,100,540]
startPosition=[310,540]
correctPosition=[[165,275],[75,165],[325,415],[0,75],[405,505]]
positions=random.choice(endPositions)

##############################
speed=30
x=0
y=0
z=0
roundno=0
complete=True
correct=0
mistakes=0
result=''
lost=False
done=False
##############################
waiting=False
ini=True
roundcom=False
##############################

def wait():
    global x,cTime,pTime,roundno,roundcom,bg,result,waiting
    x+=cTime-pTime

    if result=='win':
        win=cv2.imread('correct.png',cv2.IMREAD_UNCHANGED)
        win=cv2.resize(win,(0,0),None,0.6,0.6)
        bg = cvzone.overlayPNG(bg,win,[int((bg.shape[0]-win.shape[0])/2),int((bg.shape[1]-win.shape[1])/2)])
    if result=='lose':
        lose=cv2.imread('wrong.png',cv2.IMREAD_UNCHANGED)
        lose=cv2.resize(lose,(0,0),None,0.6,0.6)
        bg = cvzone.overlayPNG(bg,lose,[int((bg.shape[0]-lose.shape[0])/2),int((bg.shape[1]-lose.shape[1])/2)])
    if x>2:
        roundno+=1
        result=''
        waiting=False
        roundcom=True
    return bg

def checkPoint():
    global roundno, mistakes, info, bg, positions, correct, choices, result, speed

    a=0
    for i in choices:
        if i==positions[0]:
            break
        a+=1

    if roundno%10==0:
        if speed<15:
            speed-=5
    
    positions=random.choice(endPositions)
    #print(a)
    #print(positions[roundno])
    #print(correctPosition[a])
    #print(int(bg.shape[0]*(1-info[1][23][0])))
        
    if int(bg.shape[0]*(1-info[1][23][0]))<correctPosition[a][1] and int(bg.shape[0]*(1-info[1][23][0]))>correctPosition[a][0]:
        correct+=1
        result='win'
        return
    mistakes+=1
    result='lose'
    return

def ballAnimation(endPoint):
    global startPosition,cTime,pTime,x,bg,ball,y,z,complete,roundno,waiting,mistakes,roundcom,result,waiting,lost,done

    if mistakes>2:
        roundcom=False
        result=''
        waiting=False
        lost=True
        x=0
    
    x+=cTime-pTime
    change=[(endPoint[0]-310)/speed,(-180)/speed]
        
    if complete:
        bg = cvzone.overlayPNG(bg,ball,[int(310+y),int(540+z)])
    if x>0.05:
        y+=change[0]
        z+=change[1]
        x=0
        #print([int(310+y),int(540+z)])
    if 540+z<360:
        waiting=True
        roundcom=False
        checkPoint()
        y=0
        z=0
        x=0
    return bg


def Initialization():
    global x,cTime, pTime, bg, ini, roundcom, roundno
    
    x+=cTime-pTime

    if x<1:
        cv2.putText(bg,"5",(310,340),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),3)
    if x>1 and x<2:
        cv2.putText(bg,"4",(310,340),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),3)
    if x>2 and x<3:
        cv2.putText(bg,"3",(310,340),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),3)
    if x>3 and x<4:
        cv2.putText(bg,"2",(310,340),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),3)
    if x>4 and x<5:
        cv2.putText(bg,"1",(310,340),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),3)
    if x>5 and x<6:
        cv2.putText(bg,"Begin!!",(280,340),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)
    if x>6 and x<7:
        ini=False
        roundcom=True
        roundno+=1

    return bg
    

while True:
    bg=cv2.imread('BG1.png')
    bg=cv2.resize(bg,(700,700))
    
    sucess,frame=vid.read()

    info=drawPose(frame,[23])

    cTime=time.time()
    fps=1/(cTime-pTime)
    

    bgres=[bg.shape[0],bg.shape[1]]
    ballres=[ball.shape[0],ball.shape[1]]

    if len(info[1])!=0:
        if float(info[1][23][0])<1 and float(info[1][23][1])<1:
            bg = cvzone.overlayPNG(bg,keeper,[int(bg.shape[0]*(1-info[1][23][0])),300])
            #int(bg.shape[1]*info[1][23][1])

    if ini:
        bg=Initialization()
        
    if waiting:
        bg = wait()
            
    if roundcom:
        bg= ballAnimation(positions)   

    if lost:
        lostImg=cv2.imread('Losing.png',cv2.IMREAD_UNCHANGED)
        lostImg=cv2.resize(lostImg,(0,0),None,2,2)
        #bg = cvzone.overlayPNG(bg,lostImg,[int((bg.shape[0]-lostImg.shape[0])/2),int((bg.shape[1]-lostImg.shape[1])/2)])
        bg = cvzone.overlayPNG(bg,lostImg,[75,275])
        x+=cTime-pTime
        if x>5:
            break
    

    if done:
        winImg=cv2.imread('Winning.png',cv2.IMREAD_UNCHANGED)
        winImg=cv2.resize(winImg,(0,0),None,2,2)
        #bg = cvzone.overlayPNG(bg,lostImg,[int((bg.shape[0]-lostImg.shape[0])/2),int((bg.shape[1]-lostImg.shape[1])/2)])
        bg = cvzone.overlayPNG(bg,winImg,[75,275])
        x+=cTime-pTime
        if x>5:
            break
    
    pTime=cTime

    #print(int(bg.shape[0]*(1-info[1][23][0])))
        
    cv2.putText(bg,'Penalty '+str(roundno),(280,670),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),3)
    cv2.putText(bg,'Goals Stopped: '+str(correct),(10,670),cv2.FONT_HERSHEY_PLAIN,1.5,(0,0,0),2)
    cv2.putText(bg,'Misses: '+str(mistakes),(550,670),cv2.FONT_HERSHEY_PLAIN,1.5,(0,0,0),2)
    
    #cv2.namedWindow('Soccer Goalkeeping', cv2.WINDOW_NORMAL)
    #cv2.setWindowProperty('Soccer Goalkeeping', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Soccer Goalkeeping',bg)

    cv2.putText(info[0],str(int(fps)),(50,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv2.imshow('Webcam',info[0])
    
    cv2.waitKey(1)

vid.release()
cv2.destroyAllWindows()

import mysql.connector as mysql
from tkinter import *

root=Tk()

def addData():
    global root,e
    conn=mysql.connect(host='localhost',user='root',passwd='harshkh@1202',database='hvk')
    cursor=conn.cursor()
    cursor.execute('insert into soccerScore values(%s,%s)',(e.get(),correct))
    root.destroy()
    conn.commit()
    conn.close()

Label(root,text='Hope You Had Fun Playing!!!!',font=('Arial',18)).grid(row=0,column=1,pady=10,padx=10)
Label(root,text='Your Score: '+str(correct),font=('Arial',18)).grid(row=2,column=1,pady=10,padx=10)
Label(root,text='Enter your Player Name:',font=('Arial',12)).grid(row=3,column=1)
e=Entry(root)
e.grid(row=4,column=1,pady=2)
Button(root,text='Done',font=('Arial',10),command=addData).grid(row=5,column=1,pady=5)

root.mainloop()
