import serial
import webbrowser
import time
from PyPDF2 import PdfFileReader
from pynput.keyboard import Key, Controller
from imusensor.filters import kalman
import numpy as np
import csv

########################################################################################
#                                     Functions                                        #
########################################################################################
# Receive information from Arduino through Serial Port
def GetArduinoData():
    list_in_floats = []
    list_values = []

    arduino = serial.Serial('com3', 9600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split('\t')

    for item in list_values: # item is string
        list_in_floats.append(float(item))

    arduino.close()
    print('Connection closed')
    print('<----------------------------->')

    return list_in_floats

# Turn page
def TurnPage(fb,num_turn):
    num_turn = int(num_turn)
    print('num_turn=',num_turn)
    if fb == 'f':
        for j in range (num_turn):
            print('j=',j)
            keyboard.press(Key.enter)  # Turn page forward
            time.sleep(0.01)
    else:
        for j in range(num_turn):
            print('j=', j)
            keyboard.press(Key.left)  # Turn page backward
            time.sleep(0.01)

########################################################################################
#                                         Main                                         #
########################################################################################
# Declare variables to be used
ts = 1 # sample period for Arduino data
p1 = ""
p2 = ""
p3 = ""
p4 = ""
p5 = ""
ax = []
ay = []
az = []
gx = []
gy = []
gz = []
mx = []
my = []
mz = []
pressed = "10"
total_press = 0
i = 0 # always starting on first page, index for number of notes
octave = [4,5,6]

# Open music sheet in PDF Reader
pdf = PdfFileReader(open('Set2.pdf', 'rb')) # read pdf
webbrowser.open_new(r"Set2.pdf")  # open pdf on browser
n = pdf.getNumPages() # display total number of pages
print('Number of Pages:\t'+str(n))
keyboard = Controller()
time.sleep(2)

# Open txt / csv file for page turning information
page_note = []
with open('numpresses.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        page_note.append(row)
########  Example  ########
# [numnote_turn, numnote_tot , forward/backward, numpage_turn #
# ['54', '66', 'f', '1']  #
# ['44', '55', 'f', '1']  #
# ['65', '68', 'f', '0']  #
###########################

# Get page note information
num_note_turn = int(page_note[i][0]) # number of notes pressed to turn
num_note_tot = int(page_note[i][1]) # number of notes in total for resetting total_presses
fb = page_note[i][2] # 'f' or 'b' to indicate forward or backward
num_page_turn = int(page_note[i][3]) # nume of pages turned forward / backward

# Octave information extraction
octave_pos = []
k = 0
with open('octave.csv',newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if k > 0:
            octave_pos.append(int(row[0]))
        k = k+1
########  Example  ########
# [octave position in order]   #
# [4,4,5,4,5,4,5,4,5,4,5,0...] #

counter = 0
prev_total_press = 0
R=[]
P=[]
Y=[]
# main loop
while True:
    # get data
    data = GetArduinoData() # get data (p1-p5, accel, gyro)
    # compute total presses
    if octave_pos[counter] in octave: # compute total presses only if wrist is in the right octave range
        ############################### Get Finger Sensor Values ########################################
        # if = normal data reception, else = when data gets lost
        if len(data) > 0:
            p1 = p1 + str(int(data[0]))
        else:
            p1 = p1 + p1[-1]
        if len(data) > 1:
            p2 = p2 + str(int(data[1]))
        else:
            p2 = p2 + p2[-1]
        if len(data) > 2:
            p3 = p3 + str(int(data[2]))
        else:
            p3 = p3 + p3[-1]
        if len(data) > 3:
            p4 = p4 + str(int(data[3]))
        else:
            p4 = p4 + p4[-1]
        if len(data) > 4:
            p5 = p5 + str(int(data[4]))
        else:
            p5 = p5 + p5[-1]
        total_press = p1.count(pressed) + p2.count(pressed) + p3.count(pressed) + p4.count(pressed) + p5.count(pressed)
        if prev_total_press < total_press: # if total_press increases
            counter = counter + 1  # go to the next note to find the right octave
            prev_total_press = total_press # set previous total press to current total press

    ############################### Get IMU Sensor Values ########################################
    if len(data)>5:
        ax.append(float(data[5]))
    else:
        ax.append(ax[-1])
    if len(data)>6:
        ay.append(float(data[6]))
    else:
        ay.append(ay[-1])
    if len(data) > 7:
        az.append(float(data[7]))
    else:
        az.append(az[-1])
    if len(data) > 8:
        gx.append(float(data[8]))
    else:
        gx.append(gx[-1])
    if len(data) > 9:
        gy.append(float(data[9]))
    else:
        gy.append(gy[-1])
    if len(data) > 10:
        gz.append(float(data[10]))
    else:
        gz.append(gz[-1])
    if len(data) > 11:
        mx.append(float(data[11]))
    else:
        mx.append(mx[-1])
    if len(data) > 12:
        my.append(float(data[12]))
    else:
        my.append(my[-1])
    if len(data) > 13:
        mz.append(float(data[13]))
    else:
        mz.append(mz[-1])
    ##########################################################################################
    sensorfusion = kalman.Kalman()

    # compute roll , pitch, yaw at 10Hz
    sensorfusion.computeAndUpdateRollPitchYaw(ax[-1],ay[-1],az[-1],gx[-1],gy[-1],gz[-1],mx[-1],my[-1],mz[-1],dt=0.1)
    roll = float(sensorfusion.roll)
    pitch = float(sensorfusion.pitch)
    yaw = float(sensorfusion.yaw)

    # printing
    #print('p1=', p1)
    #print('p2=', p2)
    #print('p3=', p3)
    #print('p4=', p4)
    #print('p5=', p5)
    print('total_press=', total_press)
    print('numnote_page', int(page_note[i][0]))
    print('numnote_total', int(page_note[i][1]))
    print('octave_pos:', octave_pos[counter])
    print('octave:', octave)
    #print("Roll: ", roll)
    #print("Pitch: ", pitch)
    #print("Yaw: ", yaw)

    # Computer linear accelration to approximate octave range
    lax = abs(ax[-1])-abs(roll)
    lay = abs(ay[-1]) - abs(pitch)
    laz = abs(az[-1]) - abs(yaw) - 2
    la = np.array([lax,lay,laz,4])
    if laz < -10:
        octave = [i+1 for i in octave] # octave range goes up
    if laz > 10:
        octave = [i-1 for i in octave] # octave range goes down
    print('lin. accel: ',laz)

    # turn page when total_press >= num_note_page
    if total_press >= num_note_turn:
        TurnPage(fb,num_page_turn)
        num_note_turn = 100000000 # to prevent this if statement to be entered once it's entered per page

    # reset fingering arrays when starting a new page
    if total_press >= num_note_tot: # reset total_press when total_press >= num_note_total
        p1 = ""
        p2 = ""
        p3 = ""
        p4 = ""
        p5 = ""
        i = i + 1
        if i >= n: # if i is out of the total number of pages
            print("You are done!")
            break
        num_note_turn = int(page_note[i][0])  # number of notes pressed to turn
        num_note_tot = int(page_note[i][1])  # number of notes in total for resetting total_presses
        fb = page_note[i][2]  # 'f' or 'b' to indicate forward or backward
        num_page_turn = int(page_note[i][3])  # nume of pages turned forward / backward





