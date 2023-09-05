# Import libraries
import pysicktim as lidar
import time
import math
import matplotlib.pyplot as plot

# Set parameters
d_max = 2.0				# Maximum distance to measure in meters
circumference_chord = 1 # Chord length desired of the circumference a d_max distance

# Compute alpha
alpha_rad = math.asin(circumference_chord / (2 * d_max))
alpha_deg = round(math.degrees(alpha_rad),0)
alpha_deg=int(alpha_deg)

# Parameters for plot
d_average=[]
average=0

try:
	while True:
		
		lidar.scan()	# Requests and returns list of LiDAR
						# distance data in meters

		d = lidar.scan.distances[135-alpha_deg:135+alpha_deg]
		for i in range(len(d)):
			if d[i]>d_max:
				d[i]=0		# Delete values greater than d_max
							# to avoid errors in the average
			
		# Compute average 
		n=0 	#number of elements
		s=0 	#sum of elements

		for i in d:
			if i!=0:
				n=n+1
				s=s+i
		if n!=0:
			average=s/n
		else:
			average=0
			
		if average<0.0001:
			print("Free space")
		elif average<=(d_max/2):
			print(f"WARNING, Nearby obstacle: {average} meters")
		else: # Between d_max/2 and d_max
			print(f"Approaching obstacle: {average} meters")
		
		# Update values for plot
		d_average.append(average)

		# Wait 0.5 seconds
		time.sleep(0.5)

except KeyboardInterrupt:
    print('\nInterrupted!')

# Plot
plot.plot(d_average)
plot.title('LaserScanner data')
plot.ylabel('Distance [m]')
plot.xlabel('Time [s]')
plot.show()
