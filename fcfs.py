process_queue = []
total_wtime = 0
n = int(input('Enter the total no of processes: '))
for i in range(n):
	process_queue.append([])                                #append a list object to the list
	process_queue[i].append(input('Enter p_name: '))
	process_queue[i].append(int(input('Enter p_arrival: ')))
	process_queue[i].append(int(input('Enter p_bust: ')))
	process_queue[i].append(int(0))
for i in range(n):
	for j in range(n):
		temp = process_queue[i]
		if(temp[1] < process_queue[j][1]):
			process_queue[i]=process_queue[j]
			process_queue[j]=temp

total_wtime=process_queue[0][1]
process_queue[0][3]=process_queue[0][1]
print ('ProcessName\tArrivalTime\tBurstTime')
for i in range(n):
	print (process_queue[i][0],'\t\t',process_queue[i][1],'\t\t',process_queue[i][2])
	process_queue[i][3]=total_wtime - process_queue[i][1]
	print (process_queue[i][0],': Total waiting time: ',process_queue[i][3])
	total_wtime=total_wtime+process_queue[i][2]
total_wtime=0
for i in range(n):
	total_wtime=total_wtime+process_queue[i][3]
print ('Average waiting time: ',total_wtime/n)
