import serial
import matplotlib.pyplot as plt
import numpy as np


def plotClose(evt):
	quit()

initTimeOut = 100
dataLength = 1000

ser = serial.Serial('COM4', 115200)

nChannels = 1
channelData = []
channelNames = []

yMin = -1
yMax = 1

for i in range(initTimeOut):
	data = ser.readline().decode().strip().split()
	if data[0] == "N":
		nChannels = len(data)-1
		print(nChannels)
		channelData = np.zeros((dataLength, nChannels+1))
		channelNames.append(data[1:nChannels+1])
		print(channelNames[0])

	if data[0] == "L":
		yMin = data[1]
		yMax = data[2]

	if data[0] == "!":
		break

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylim([-1, 1])
fig.canvas.mpl_connect('close_event', plotClose)

plotLines = []
colors = ['r-', 'b-', 'g-']
for iChan in range(1, nChannels+1):
	plotLine, = ax.plot(channelData[:,0], channelData[:,iChan], colors[iChan%3])
	plotLines.append(plotLine)
	print(iChan)

ax.legend(channelNames[0])
	

pointer = 0
while True:
	serialData = ser.readline().decode().strip().split()
	if (serialData[0] == "D") & (len(serialData) == nChannels+2):
		serialData = serialData[1:]
		for iChan in range(nChannels+1):
			channelData[pointer,iChan] = float(serialData[iChan])
			

		for iChan in range(1, nChannels+1):
			xData = np.append(channelData[pointer+1:dataLength,0], channelData[0:pointer+1,0])
			yData = np.append(channelData[pointer+1:dataLength,iChan], channelData[0:pointer+1,iChan])
			plotLines[iChan-1].set_ydata(yData)
			plotLines[iChan-1].set_xdata(xData)
			ax.set_xlim([min(xData), max(xData)])

		if pointer % 10 == 0:
			fig.canvas.draw()

		pointer = (pointer + 1)%dataLength

	