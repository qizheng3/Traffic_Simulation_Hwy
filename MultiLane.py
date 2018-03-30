import vehicle
import random
import Lane
class MultiLane:
	def __init__(self, l, nLane, vMax):
		self.nLane = nLane;
		self.lanes = [];
		for i in range(nLane):
			self.lanes.append(Lane.Lane(l,vMax))

	# Every second, update vehicles speed of all lanes
	# if speed is lower than the previous vehicle and lower than max speed, then speed up; 
	# if speed is higher than the previous vehicle and their distance < 200 meters, then speed = preSpeed;
	def updateSpeed(self):
		for lane in self.lanes:
			prePos = lane.size - 1;
			while (lane.cells[prePos] == None and prePos >= 0):
				prePos = prePos - 1;                     # find the vehicle which is closest to the exit of this lane
			firstCar = lane.cells[prePos];
			if firstCar != None:
				firstCar.speed = min(firstCar.speed + 5, firstCar.vMax, lane.vMax); # speed up the first car if possible
			start = prePos - 1;
			for i in range(start, -1, -1):
				if lane.cells[i] != None:
					preCar = lane.cells[prePos];
					currCar = lane.cells[i];
					if currCar.speed <= preCar.speed - 1:
						currCar.speed = min(currCar.vMax, lane.vMax, preCar.speed);
					elif currCar.speed > preCar.speed and abs(i - prePos) <= 20:
						currCar.speed = preCar.speed;
					prePos = i;

	def updatePosition(self):
		for lane in self.lanes:
			for i in range(lane.size - 1, -1, -1):
				if lane.cells[i] != None:
					car = lane.cells[i];
					speed = car.speed;
					newPos = i + int(speed/10);  # calculate which cell this vehicle will move to
					if newPos >= lane.size:
						# deal with the situation if this car exits
						pass
					elif lane.cells[newPos] == None:
						lane.cells[newPos] = car;
					lane.cells[i] = None;

	def checkChangeLaneLeft(self):
		for i in range(1, len(self.lanes)):
			lane = self.lanes[i]
			for j in range(len(lane.cells)):
				if lane.cells[j] is not None:
					car = lane.cells[j]
				else:
					continue
				if car.speed <= 0.7 * car.vMax: # this car has the requirment to switch the lane 
					leftLaneIsEmpty = True
					for k in range(-20,20):
						if self.lanes[i-1].cells[j+k] is not None: #if there is no vehicle between 100m behind and ahead
							leftLaneIsEmpty = False
							break
					if leftLaneIsEmpty:
						lane.RemoveCar(j)
						self.lanes[i-1].addCar(car, j)

	def checkChangeLaneRight(self):
		for i in range(len(self.lanes) - 1):
			lane = self.lanes[i]
			for j in range(len(lane.cells)):
				if lane.cells[j] is not None:
					car = lane.cells[j]
				else:
					continue
				if car.speed <= 0.7 * car.vMax: # this car has the requirment to switch the lane 
					rightLaneIsEmpty = True
					for k in range(-20,20):
						if j + k >= 0 and j + k < len(self.lanes[i+1].cells) and self.lanes[i+1].cells[j+k] is not None:  #if there is no vehicle between 100m behind and ahead
							rightLaneIsEmpty = False
							break
					if rightLaneIsEmpty:
						lane.RemoveCar(j)
						self.lanes[i+1].addCar(car, j)

	def enterAtStart(self, prob):
		for lane in self.lanes:
			for i in range(10):
				if lane.cells[i] == None:
					if random.random() < prob:
						lane.addCar(vehicle.Vehicle(),i)
						break

	def exitAtEnd(self):
		for lane in self.lanes:
			for i in range(len(lane.cells) - 10):
				if lane.cells[i] != None:
					lane.RemoveCar(i)

	def entranceEvent(self, probExit, probEnter):
		lastLane = self.lanes[-1]
		for i in range(1000, 1000, len(lastLane.cells)):
			j = -1
			while j > -20:
				if lastLane.cells[i+j] is None:
					j -= 1
				else:
					rand = random.random()
					if rand < probExit:
						lastLane.RemoveCar(i+j)
					break
			rand = random.random()
			if rand < probEnter:
				lastLane.addCar(vehicle.Vehicle(), i)



	def printSpeed(self):
		for lane in self.lanes:
			for i in range(lane.size):
				if lane.cells[i] == None:
					print "*",
				else:
					print lane.cells[i].speed,
			print;


