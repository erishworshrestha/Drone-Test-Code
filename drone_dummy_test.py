# import pyqtgraph.examples
# pyqtgraph.examples.run()

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from time import perf_counter
from pyqtgraph.dockarea import *
import serial
import serial.tools.list_ports


app = pg.mkQApp("DockArea Example")
win = QtGui.QMainWindow()
area = DockArea()
win.setCentralWidget(area)
win.resize(1000,500)
win.setWindowTitle('Benchmark Test')

d1 = Dock("Dock1", size=(1, 1))  
d3 = Dock("PWM", size=(500,400))
d4 = Dock("RPM", size=(500,200))
d5 = Dock("Voltage", size=(500,200))
d6 = Dock("Current", size=(500,200))
d7 = Dock("Torque", size=(500,200))
d8 = Dock("Thrust", size=(500,200))

area.addDock(d1, 'left')  
area.addDock(d3, 'bottom', d1)
area.addDock(d4, 'right')  
area.addDock(d5, 'top', d4) 
area.addDock(d6, 'top', d4) 
area.addDock(d7, 'top', d4) 
area.addDock(d8, 'top', d4) 


# area.moveDock(d4, 'top', d2)     ## move d4 to top edge of d2
area.moveDock(d5, 'above', d4)   ## move d6 to stack on top of d4
area.moveDock(d6, 'above', d4)   ## move d6 to stack on top of d4
area.moveDock(d7, 'above', d4)   ## move d6 to stack on top of d4
area.moveDock(d8, 'above', d4)   ## move d6 to stack on top of d4
# area.moveDock(d5, 'top', d2)     ## move d5 to top edge of d2


ports = list(serial.tools.list_ports.comports())

for port in ports:
    # if "USB-SERIAL" in port.description:
        # print(port)
        if __name__ == '__main__':
            try:
                ser = serial.Serial(str(port[0]), 9600, timeout=1)
                ser.flush()
            except serial.SerialException as e:
                continue
            except OSError:
                continue
        ser.close()



d1.hideTitleBar()
w1 = pg.LayoutWidget()
label = QtGui.QLabel(""" Hello""")
saveBtn = QtGui.QPushButton('Save')
restoreBtn = QtGui.QPushButton('Restore')
restoreBtn.setEnabled(False)
w1.addWidget(label, row=0, col=0)
w1.addWidget(saveBtn, row=1, col=0)
w1.addWidget(restoreBtn, row=2, col=0)
d1.addWidget(w1)
state = None
def save():
    global state
    state = area.saveState()
    restoreBtn.setEnabled(True)
def load():
    global state
    area.restoreState(state)

saveBtn.clicked.connect(save)
restoreBtn.clicked.connect(load)


data1 = np.random.normal(size=1)
data2 = np.random.normal(size=1)
ptr1 = 0
w3 = pg.PlotWidget(title="time vs PWM")
curve1 = w3.plot(data1)
d3.addWidget(w3)
data = []
data_ = []

w3.setLabel('bottom', 'Time', 's')
w3.setLabel('left', 'P W M')
def update1():
    global data1, ptr1
    splitted_data = dataSerial.split(",")
    if(splitted_data != [""]):
        data1[:-1] = data1[1:]
        data1[-1] =splitted_data[0]
        data2[:-1] = data2[1:]
        data2[-1] =splitted_data[1]
        data.append(data1[-1])
        data_.append(data2[-1])
        curve1.setData(data,data_)
        ptr1 += 1


data3 = np.random.normal(size=1)
data4 = np.random.normal(size=1)
ptr2 = 0
w4 = pg.PlotWidget(title="time vs RPM")
curve2 = w4.plot(data1)
d4.addWidget(w4)
dataListX2 = []
dataListY2 = []

w4.setLabel('bottom', 'Time', 's')
w4.setLabel('left', 'R P M')

def update2():
    global data3,data4, ptr2
    splitted_data = dataSerial.split(",")
    if(splitted_data != [""]):
        data3[:-1] = data3[1:]
        data3[-1] =splitted_data[0]
        data4[:-1] = data4[1:]
        data4[-1] =splitted_data[4]
        dataListX2.append(data3[-1])
        dataListY2.append(data4[-1])
        curve2.setData(dataListX2,dataListY2)
        ptr2 += 1


data5 = np.random.normal(size=1)
data6 = np.random.normal(size=1)
ptr3 = 0
w5 = pg.PlotWidget(title="time vs Voltage")
curve3 = w5.plot(data5)
d5.addWidget(w5)
dataListX3 = []
dataListY3 = []

w5.setLabel('bottom', 'Time', 's')
w5.setLabel('left', 'Voltage')

def update3():
    global data5,data6, ptr3
    splitted_data = dataSerial.split(",")
    if(splitted_data != [""]):
        data5[:-1] = data5[1:]
        data5[-1] =splitted_data[0]
        data6[:-1] = data6[1:]
        data6[-1] =splitted_data[2]
        dataListX3.append(data5[-1])
        dataListY3.append(data6[-1])
        curve3.setData(dataListX3,dataListY3)
        ptr3 += 1

data7 = np.random.normal(size=1)
data8 = np.random.normal(size=1)
ptr4 = 0
w6 = pg.PlotWidget(title="time vs Current")
curve4 = w6.plot(data7)
d6.addWidget(w6)
dataListX4 = []
dataListY4 = []

w6.setLabel('bottom', 'Time', 's')
w6.setLabel('left', 'Current')

def update4():
    global data5,data6, ptr4
    splitted_data = dataSerial.split(",")
    if(splitted_data != [""]):
        data7[:-1] = data7[1:]
        data7[-1] =splitted_data[0]
        data8[:-1] = data8[1:]
        data8[-1] =splitted_data[3]
        dataListX4.append(data7[-1])
        dataListY4.append(data8[-1])
        curve4.setData(dataListX4,dataListY4)
        ptr4 += 1



data9 = np.random.normal(size=1)
data10 = np.random.normal(size=1)
ptr5 = 0
w7 = pg.PlotWidget(title="time vs Torque")
curve5 = w7.plot(data9)
d7.addWidget(w7)
dataListX5 = []
dataListY5 = []

w7.setLabel('bottom', 'Time', 's')
w7.setLabel('left', 'torque')

def update5():
    global data9,data10, ptr5
    splitted_data = dataSerial.split(",")
    if(splitted_data != [""]):
        data9[:-1] = data9[1:]
        data9[-1] =splitted_data[0]
        data10[:-1] = data10[1:]
        data10[-1] =splitted_data[5]
        dataListX5.append(data9[-1])
        dataListY5.append(data10[-1])
        curve5.setData(dataListX5,dataListY5)
        ptr5 += 1



data11 = np.random.normal(size=1)
data12 = np.random.normal(size=1)
ptr6 = 0
w8 = pg.PlotWidget(title="time vs Thrust")
curve6 = w8.plot(data11)
d8.addWidget(w8)
dataListX6 = []
dataListY6 = []

w8.setLabel('bottom', 'Time', 's')
w8.setLabel('left', 'thrust')

def update6():
    global data11,data12, ptr6
    splitted_data = dataSerial.split(",")
    if(splitted_data != [""]):
        data11[:-1] = data11[1:]
        data11[-1] =splitted_data[0]
        data12[:-1] = data12[1:]
        data12[-1] =splitted_data[6]
        dataListX6.append(data11[-1])
        dataListY6.append(data12[-1])
        curve6.setData(dataListX6,dataListY6)
        ptr6 += 1



def update():
    global dataSerial
    if(ser.isOpen() == False):
        ser.open()
    dataSerial = ser.readline().decode('utf-8').rstrip()
    update1()
    update2()
    update3()
    update4()
    update5()
    update6()

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

win.show()

if __name__ == '__main__':
    pg.exec()
 