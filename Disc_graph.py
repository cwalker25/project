
#Chris Walker
#02/12/2020
#plotting battery discharge data

import matplotlib.pyplot as plt
import numpy as np

#define data arrays
time_data=[]
voltage_data=[]
I_data=[]

#read in the data
lines = np.loadtxt('Voltage_data.txt', delimiter = ',')
for line in lines:
    #the first item in row is the time
    time_data.append(line[0])
    #the second item in a row is the voltage
    voltage_data.append(line[1])
    #the third item in a row is the current
    I_data.append(line[2])


    
#have to do the following to use the time data in the exponential function
fit_time_data = np.array(time_data)

#make a plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#make an xy scatter plot
plt.scatter(time_data,voltage_data,color='red',label='data 10k')
#add the exponential curve with guesses for constants a and b:
# plt.plot(fit_time_data,my_func(fit_time_data,3.3,95),color='black',label='my fit 10k')
#label the axes etc
ax.set_xlabel('Time(hours)')
ax.set_ylabel('Voltage(v)')
ax.set_title('Battery Discharge')
plt.legend(loc='upper right')


plt.savefig('VoltageDisch_all.png')

#have to do the following to use the time data in the exponential function
fit_time_data = np.array(time_data)

#make a plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#make an xy scatter plot
plt.scatter(time_data,voltage_data,color='blue',label='data 10k')
#add the exponential curve with guesses for constants a and b:
# plt.plot(fit_time_data,my_func(fit_time_data,3.3,95),color='black',label='my fit 10k')
#label the axes etc
ax.set_xlabel('Time(hours)')
ax.set_ylabel('Current(mA)')
ax.set_title('Current Discharge')
plt.legend(loc='upper right')

# this for loop calculates the charge that the battery output
for n in range(len(time_data)):
    q=I_data[n]*(time_data[n-1]-time_data[n])+q
print(q)


plt.savefig('CurrentDisch_all.png')

