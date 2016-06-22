#Written by Paul Wallace June 21st, 2016
#C.T.S = clockings time sum
print 'Hi, welcome to the clock in calculator :) \n'
print 'Please input your clockings (ex: 0748) (ex: 2100)'
user_input = 'y'
clock_list = []
count = int(raw_input("How many clockings did you have? \n(One clocking is one clock in and a corresponding clock out): "))
for n in range(0,count):
	c_time = (raw_input("Clock in %d: " % (n + 1)), raw_input("Clock out %d: " % (n + 1)))
	while (not(len(c_time[0]) == 4 and 
		len(c_time[1]) == 4 and 
		c_time[0].isdigit() and 
		c_time[1].isdigit() and 
		int(c_time[0]) < int(c_time[1]))):
		print "I'm sorry one (or both!) of your times was not a valid time,"
		print "or they were not a valid pair of times, please enter valid times."
		print "Also note that the times do not loop (sorry to you all-nighters)."
		c_time = (raw_input("Clock in %d: " % (n + 1)), raw_input("Clock out %d: " % (n + 1)))
	clock_list.append(c_time)
print 'Calculating...'

total = 0
workers_fine = False
for n in clock_list:
	hours1 = int(n[0][:2])
	mins1 = int(n[0][-2:])
	hours2 = int(n[1][:2])
	mins2 = int(n[1][-2:])
	hours1 = hours1 * 60 * 60
	mins1 = mins1 * 60
	seconds1 = hours1 + mins1
	hours2 = hours2 * 60 * 60
	mins2 = mins2 * 60
	seconds2 = hours2 + mins2
	total += (seconds2 - seconds1)
	if seconds2 - seconds1 > 18000:
		workers_fine = True
#convert back to hours
hours = total/60/60
minutes = (total/60)%60
print 'You worked %d hour(s) and %d minute(s) today' % (hours, minutes) 
if workers_fine:
	print 'Warning: You worked longer than 5 hours today without a break'
if hours == 8 and minutes > 0 or hours > 8:
	print 'You worked %d hour(s) and %d minute(s) overtime today' % ((hours - 8), (minutes))




