
process_queue = []
total_wtime = 0
n = int(input('Enter the total no of processes: '))
for i in range(n):
     process_queue.append([])                                #append a list object to the list
     process_queue[i].append(input('Enter p_name: '))
     process_queue[i].append(int(input('Enter p_arrival: ')))
     process_queue[i].append(int(input('Enter p_bust: ')))
     process_queue[i].append(int(0))
     process_queue[i].append(True)
for i in range(n):
	for j in range(n):
		temp = process_queue[i]
		if(temp[1] <= process_queue[j][1] and temp[2] <= process_queue[j][2]):
			process_queue[i]=process_queue[j]
			process_queue[j]=temp

total_wtime=process_queue[0][1]
print ('ProcessName\tArrivalTime\tBurstTime')
count = process_queue[0][2]
for i in range(len(process_queue)):
        for j in range(len(process_queue)):
                 
                if(process_queue[i][4]==True and process_queue[j][4]==True and process_queue[i][1]<=count and process_queue[j][1] <=count and process_queue[i][2]<=process_queue[j][2]):
                        if(process_queue[i][1]<=process_queue[j][2]):
                                print(i,'if ',j)
                                process_queue[i][4]=False                                
                                print (process_queue[i][0],'\t\t',process_queue[i][1],'\t\t',process_queue[i][2])
                                process_queue[i][3]=total_wtime  - process_queue[i][1]
                                print (process_queue[i][0],': Total waiting time: ',process_queue[i][3])
                                total_wtime=total_wtime+process_queue[i][2]
                                count=count+process_queue[i][2]
                                break
                        else:
                                print(i,'else')
                                 
                                process_queue[j][4]=False                                
                                print (process_queue[j][0],'\t\t',process_queue[j][1],'\t\t',process_queue[j][2])
                                process_queue[j][3]=total_wtime  - process_queue[j][1]
                                print (process_queue[j][0],': Total waiting time: ',process_queue[j][3])
                                total_wtime=total_wtime+process_queue[j][2]
                                count=count+process_queue[j][2]
                                break
total_wtime=0
for i in range(n):
	total_wtime=total_wtime+process_queue[i][3]
print ('Average waiting time: ',total_wtime/n)
