from datetime import datetime
from guizero import App, Text, PushButton, Drawing, Window, Picture

import os
import time
import math
from random import randint

MainTextMode = 'hour'

def hdat_Pressed():
   global MainTextMode
   MainTextMode = 'hdat'

def mindat_Pressed():
   global MainTextMode
   MainTextMode = 'mindat'

def Hour_Pressed():
   global MainTextMode
   MainTextMode = 'hour'
   OBC.show()
   OBC.focus()

def Date_Pressed():
   global MainTextMode
   MainTextMode = 'date'

def Temp_Pressed():
   global MainTextMode
   MainTextMode = 'temp'

def Memo_Pressed():
   global MainTextMode
   MainTextMode = 'memo'

def TrackMode_Pressed():
   OBC.hide()
   TRACK.show()
   TRACK.focus()
   
def OBCMode_Pressed():
   global MainTextMode
   MainTextMode = ''
   TRACK.hide()
   OBC.show()
   OBC.focus()

def OBC_Data():
    if MainTextMode == '':
      OBCMainText.value = (datetime.now()).strftime("%I:%M:%S %p")
    if MainTextMode == 'hdat':
      OBCMainText.value = 'h/Dat'
    if MainTextMode == 'mindat':
      OBCMainText.value = 'min/Dat'
    if MainTextMode == 'hour':
      OBCMainText.value = (datetime.now()).strftime("%I:%M:%S %p")
    if MainTextMode == 'date':
      OBCMainText.value = (datetime.now()).strftime("%m/%d/%y")
    if MainTextMode == 'temp':
      OBCMainText.value = (((os.popen("vcgencmd measure_temp").readline()).replace("temp=","")).strip())
    if MainTextMode == 'memo':
      OBCMainText.value = 'Memo'
      
def Track_Data():
    global radius
    """
    if Q1TargetP <= 100:
        Q1TargetP = Q1TargetP + randint(1,5)
    else:
        Q1TargetP = 0
    """
    #Q1 Gauge
    global Q1xc
    global Q1yc
    global Q1Needle
    global Q1TargetP
    global Q1Min
    global Q1Max
    global Q1MainReading
    Q1TargetP = float((((os.popen("vcgencmd measure_temp").readline()).replace("temp=","")).strip()).replace("'C",""))
    GaugeCluster.delete(Q1Needle)
    GaugeCluster.delete(Q1MainReading)
    Q1Needle = GaugeCluster.line(Q1xc, Q1yc,Q1xc + (math.cos((((Q1TargetP - Q1Min) * ((3.141592 * 1.25) - 0)) / (Q1Max - Q1Min))-(3.141592 / .75)) * radius), Q1yc + (math.sin((((Q1TargetP - Q1Min) * ((3.141592 * 1.25) - 0)) / (Q1Max - Q1Min))-(3.141592 / .75)) * radius), color="black", width=5)
    Q1MainReading = GaugeCluster.text(Q1xc , Q1yc+35, text = Q1TargetP,size=15)
    
    #Q2 Gauge
    global Q2xc
    global Q2yc
    global Q2Needle
    global Q2TargetP
    global Q2Min
    global Q2Max
    global Q2MainReading
    Q2TargetP = float((((os.popen("vcgencmd measure_temp").readline()).replace("temp=","")).strip()).replace("'C",""))
    GaugeCluster.delete(Q2Needle)
    GaugeCluster.delete(Q2MainReading)
    Q2Needle = GaugeCluster.line(Q2xc, Q2yc,Q2xc + (math.cos((((Q2TargetP - Q2Min) * ((3.141592 * 1.25) - 0)) / (Q2Max - Q2Min))-(3.141592 / .75)) * radius), Q2yc + (math.sin((((Q2TargetP - Q2Min) * ((3.141592 * 1.25) - 0)) / (Q2Max - Q2Min))-(3.141592 / .75)) * radius), color="black", width=5)
    Q2MainReading = GaugeCluster.text(Q2xc , Q2yc+35, text = Q2TargetP,size=15)
    
    #Q3Gauge
    global Q3xc
    global Q3yc
    global Q3Needle
    global Q3TargetP
    global Q3Min
    global Q3Max
    global Q3MainReading
    Q3TargetP = float((((os.popen("vcgencmd measure_temp").readline()).replace("temp=","")).strip()).replace("'C",""))
    GaugeCluster.delete(Q3Needle)
    GaugeCluster.delete(Q3MainReading)
    Q3Needle = GaugeCluster.line(Q3xc, Q3yc,Q3xc + (math.cos((((Q3TargetP - Q3Min) * ((3.141592 * 1.25) - 0)) / (Q3Max - Q3Min))-(3.141592 / .75)) * radius), Q3yc + (math.sin((((Q3TargetP - Q3Min) * ((3.141592 * 1.25) - 0)) / (Q3Max - Q3Min))-(3.141592 / .75)) * radius), color="black", width=5)
    Q3MainReading = GaugeCluster.text(Q3xc , Q3yc+35, text = Q3TargetP,size=15)
    
    #Q4Gauge
    global Q4xc
    global Q4yc
    global Q4Needle
    global Q4TargetP
    global Q4Min
    global Q4Max
    global Q4MainReading
    Q4TargetP = float((((os.popen("vcgencmd measure_temp").readline()).replace("temp=","")).strip()).replace("'C",""))
    GaugeCluster.delete(Q4Needle)
    GaugeCluster.delete(Q4MainReading)
    Q4Needle = GaugeCluster.line(Q4xc, Q4yc,Q4xc + (math.cos((((Q4TargetP - Q4Min) * ((3.141592 * 1.25) - 0)) / (Q4Max - Q4Min))-(3.141592 / .75)) * radius), Q4yc + (math.sin((((Q4TargetP - Q4Min) * ((3.141592 * 1.25) - 0)) / (Q4Max - Q4Min))-(3.141592 / .75)) * radius), color="black", width=5)
    Q4MainReading = GaugeCluster.text(Q4xc , Q4yc+35, text = Q4TargetP,size=15)

#******************************************
#----------------OBC MENU----------------
#******************************************
OBC = App(title="OBC", layout="grid")
OBC.bg = "#5E0000"
spacer = Text(OBC, text = "                                                                                                        ", font="digital-7", height="1", size=9, color="orange", grid=[0,0])
spacer = Text(OBC, text="", grid=[0,1])
OBCMainText = Text(OBC, text = "Loading", font="digital-7", height="2", size=50, color="orange", grid=[0,2])
OBCMainText.repeat(250, OBC_Data)
spacer = Text(OBC, text="", grid=[0,3])
spacer = Text(OBC, text="", grid=[0,4])
spacer = Text(OBC, text="", grid=[0,5])
spacer = Text(OBC, text="", grid=[0,6])
OBChdat = PushButton(OBC, command=hdat_Pressed, text="h/dat        ", align="left", width="fill", grid=[0,7])
OBChdat.bg = "white"
OBCmindat = PushButton(OBC, command=mindat_Pressed, text="        min/dat", align="right", width="fill", grid=[0,7])
OBCmindat.bg = "white"
spacer = Text(OBC, text="", grid=[0,8])
spacer = Text(OBC, text="", grid=[0,9])
OBChour = PushButton(OBC, command=Hour_Pressed, text="Hour        ", align="left", width="fill", grid=[0,10])
OBChour.bg = "white"
OBCdate = PushButton(OBC, command=Date_Pressed, text="        Date", align="right", width="fill", grid=[0,10])
OBCdate.bg = "white"
spacer = Text(OBC, text="", grid=[0,11])
spacer = Text(OBC, text="", grid=[0,12])
OBCtemp = PushButton(OBC, command=Temp_Pressed, text="Temp        ", align="left", width="fill", grid=[0,13])
OBCtemp.bg = "white"
OBCmemo = PushButton(OBC, command=Memo_Pressed, text="        Memo", align="right", width="fill", grid=[0,13])
OBCmemo.bg = "white"
TrackMode= PushButton(OBC, command=TrackMode_Pressed, text="TRACK", width="fill", grid=[0,13])
TrackMode.bg = "white"
#******************************************
#----------------TRACK MENU----------------
#******************************************
#TRACK = App(title="TRACK")
TRACK = Window(OBC, title = "TRACK")
TRACK.bg = "BLACK"

#Gauge Face Cluster
DrawingWidth = 300
DrawingHeight = 400
NumberOfGauges = 4
GaugeWidth = DrawingWidth
GaugeHeight = 300
WarningWidth = DrawingWidth
WarningHeight = 100
GaugeCluster = Drawing(TRACK, width=DrawingWidth, height=DrawingHeight)
GaugeCluster.oval(0, 0, GaugeWidth/(NumberOfGauges/2), GaugeHeight/(NumberOfGauges/2), color="white", outline=True)
GaugeCluster.oval(GaugeWidth/(NumberOfGauges/2), 0, GaugeWidth, GaugeHeight/(NumberOfGauges/2), color="white", outline=True)
GaugeCluster.oval(0, GaugeHeight, GaugeWidth/(NumberOfGauges/2), GaugeHeight/(NumberOfGauges/2), color="white", outline=True)
GaugeCluster.oval(GaugeWidth/(NumberOfGauges/2), GaugeHeight, GaugeWidth, GaugeHeight/(NumberOfGauges/2), color="white", outline=True)
#Gauge Needles
radius = GaugeWidth/4
#Q1 Gauge
Q1xc = radius
Q1yc = radius
Q1x = radius
Q1y = 0
#///Q1 VARIABLES////
Q1Min = 0
Q1Max = 100
Q1Title = "O Temp"
Q1TitleSize = 13
#///////////////////
Q1TargetP = 0
Q1Needle = GaugeCluster.line(Q1xc, Q1yc, Q1x, Q1y, color="red", width=5)
Q1MainText = GaugeCluster.text(Q1xc , Q1yc+10, text = Q1Title,size=Q1TitleSize)
Q1MainReading = GaugeCluster.text(Q1xc , Q1yc+35, text = "0",size=14)
Q1MinText = GaugeCluster.text(Q1xc-30 , Q1yc+55, text = Q1Min,size=10)
Q1MaxText = GaugeCluster.text(Q1xc+50, Q1yc-10, text = Q1Max,size=10)
Q1Max1 = GaugeCluster.line(Q1xc, Q1yc,Q1xc + (math.cos((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q1yc + (math.sin((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="red", width=4)
Q1Min1 = GaugeCluster.line(Q1xc, Q1yc,Q1xc + (math.cos((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q1yc + (math.sin((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="blue", width=4)
Q1MaxRadius = GaugeWidth/6
for i in range(1, 10):
    Q1Dashes = GaugeCluster.line(Q1xc, Q1yc,Q1xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q1yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="black", width=2)
for i in range(0, 11):
    Q1DashCover = GaugeCluster.line(Q1xc, Q1yc,Q1xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q1MaxRadius), Q1yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q1MaxRadius), color="white", width=5)
#Q2 Gauge
Q2xc = radius*3
Q2yc = radius
Q2x = radius*2
Q2y = 0
#///Q2 VARIABLES////
Q2Min = 10
Q2Max = 90
Q2Title = "C Temp"
Q2TitleSize = 13
#///////////////////
Q2TargetP = 0
Q2Needle = GaugeCluster.line(Q2xc, Q2yc, Q2x, Q2y, color="red", width=5)
Q2MainText = GaugeCluster.text(Q2xc , Q2yc+10, text = Q2Title,size=Q2TitleSize)
Q2MainReading = GaugeCluster.text(Q2xc , Q2yc+35, text = "0",size=14)
Q2MinText = GaugeCluster.text(Q2xc-30 , Q2yc+55, text = Q2Min,size=10)
Q2MaxText = GaugeCluster.text(Q2xc+50, Q2yc-10, text = Q2Max,size=10)
Q2Max1 = GaugeCluster.line(Q2xc, Q2yc,Q2xc + (math.cos((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q2yc + (math.sin((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="red", width=4)
Q2Min1 = GaugeCluster.line(Q2xc, Q2yc,Q2xc + (math.cos((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q2yc + (math.sin((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="blue", width=4)
Q2MaxRadius = GaugeWidth/6
for i in range(1, 10):
    Q2Dashes = GaugeCluster.line(Q2xc, Q2yc,Q2xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q2yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="black", width=2)
for i in range(0, 11):
    Q2DashCover = GaugeCluster.line(Q2xc, Q2yc,Q2xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q2MaxRadius), Q2yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q2MaxRadius), color="white", width=5)
#Q3 Gauge
Q3xc = radius
Q3yc = radius*3
Q3x = radius
Q3y = 0
#///Q3 VARIABLES////
Q3Min = 20
Q3Max = 80
Q3Title = "O Press"
Q3TitleSize = 13
#///////////////////
Q3TargetP = 0
Q3Needle = GaugeCluster.line(Q3xc, Q3yc, Q3x, Q3y, color="red", width=5)
Q3MainText = GaugeCluster.text(Q3xc , Q3yc+10, text = Q3Title,size=Q3TitleSize)
Q3MainReading = GaugeCluster.text(Q3xc , Q3yc+35, text = "0",size=14)
Q3MinText = GaugeCluster.text(Q3xc-30 , Q3yc+55, text = Q3Min,size=10)
Q3MaxText = GaugeCluster.text(Q3xc+50, Q3yc-10, text = Q3Max,size=10)
Q3Max1 = GaugeCluster.line(Q3xc, Q3yc,Q3xc + (math.cos((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q3yc + (math.sin((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="red", width=4)
Q3Min1 = GaugeCluster.line(Q3xc, Q3yc,Q3xc + (math.cos((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q3yc + (math.sin((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="blue", width=4)
Q3MaxRadius = GaugeWidth/6
for i in range(1, 10):
    Q3Dashes = GaugeCluster.line(Q3xc, Q3yc,Q3xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q3yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="black", width=2)
for i in range(0, 11):
    Q3DashCover = GaugeCluster.line(Q3xc, Q3yc,Q3xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q3MaxRadius), Q3yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q3MaxRadius), color="white", width=5)
#Q4 Gauge
Q4xc = radius*3
Q4yc = radius*3
Q4x = radius*3
Q4y = radius*2
#///Q4 VARIABLES////
Q4Min = 30
Q4Max = 70
Q4Title = "O2"
Q4TitleSize = 13
#///////////////////
Q4TargetP = 0
Q4Needle = GaugeCluster.line(Q4xc, Q4yc, Q4x, Q4y, color="red", width=5)
Q4MainText = GaugeCluster.text(Q4xc , Q4yc+10, text = Q4Title,size=Q4TitleSize)
Q4MainReading = GaugeCluster.text(Q4xc , Q4yc+35, text = "0",size=14)
Q4MinText = GaugeCluster.text(Q4xc-30 , Q4yc+55, text = Q4Min,size=10)
Q4MaxText = GaugeCluster.text(Q4xc+50, Q4yc-10, text = Q4Max,size=10)
Q4Max1 = GaugeCluster.line(Q4xc, Q4yc,Q4xc + (math.cos((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q4yc + (math.sin((((100 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="red", width=4)
Q4Min1 = GaugeCluster.line(Q4xc, Q4yc,Q4xc + (math.cos((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q4yc + (math.sin((((0 - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="blue", width=4)
Q4MaxRadius = GaugeWidth/6
for i in range(1, 10):
    Q4Dashes = GaugeCluster.line(Q4xc, Q4yc,Q4xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), Q4yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * radius), color="black", width=2)
for i in range(0, 11):
    Q4DashCover = GaugeCluster.line(Q4xc, Q4yc,Q4xc + (math.cos(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q4MaxRadius), Q4yc + (math.sin(((((i*10) - 0) * ((3.141592 * 1.25) - 0)) / (100 - 0))-(3.141592 / .75)) * Q4MaxRadius), color="white", width=5)
#Warning Bars
WB1x1 = 0
WB1y1 = 300
WB1x2 = 100
WB1y2 = 400
WB1Color = "red"
WB1 = GaugeCluster.rectangle(WB1x1, WB1y1, WB1x2, WB1y2, color=WB1Color)

WB2x1 = 100
WB2y1 = 300
WB2x2 = 200
WB2y2 = 400
WB2Color = "orange"
WB2 = GaugeCluster.rectangle(WB2x1, WB2y1, WB2x2, WB2y2, color=WB2Color)

WB3x1 = 200
WB3y1 = 300
WB3x2 = 300
WB3y2 = 400
WB3Color = "red"
WB3 = GaugeCluster.rectangle(WB3x1, WB3y1, WB3x2, WB3y2, color=WB3Color)

GaugeCluster.repeat(250, Track_Data)
OBCMode= PushButton(TRACK, command=OBCMode_Pressed, text="OBC", width="20")
OBCMode.bg = "white"

OBC.display()
TRACK.display()