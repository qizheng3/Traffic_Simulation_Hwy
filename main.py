import vehicle
import MultiLane
import Lane
import UI
import threading

def main():

	GUI = UI.UI()

	def run():

		highwayLength = 50000
		vMax = 40
		nLane = 5
		highway = MultiLane.MultiLane(highwayLength, nLane, vMax)

		iteration = 200

		# print len(highway.lanes)
		# print len(highway.lanes[0].cells)

		for i in range(iteration):
			#highway.printSpeed();
			highway.updateSpeed()
			highway.updatePosition()
			highway.checkChangeLaneLeft()
			highway.checkChangeLaneRight()
			highway.enterAtStart(0.5)
			highway.exitAtEnd()
			highway.entranceEvent(0.3, 0.4)

			#send msg to UI
			GUI.drawFrame(i)

	workerThread = threading.Thread(target = run)
	workerThread.setDaemon(True)
	workerThread.start()

	GUI.mainloop()



if __name__ == '__main__':
	main()
