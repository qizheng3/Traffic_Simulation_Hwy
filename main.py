import vehicle
import MultiLane
import Lane

def main():

	highwayLength = 50000
	vMax = 40
	nLane = 5
	highway = MultiLane.MultiLane(highwayLength, nLane, vMax)

	iteration = 200

	for i in range(iteration):

		#highway.printSpeed();
		highway.updateSpeed()
		highway.updatePosition()
		highway.checkChangeLaneLeft()
		highway.checkChangeLaneRight()
		highway.enterAtStart(0.5)
		highway.exitAtEnd()
		highway.entranceEvent(0.3, 0.4)

if __name__ == '__main__':
	main()