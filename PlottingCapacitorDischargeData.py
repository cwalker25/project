#Chris Walker
#01/28/2020
#plotting capacitor discharge data

import matplotlib.pyplot as plt
import numpy as np

#define data arrays
time_data=[]
voltage_data=[]

time_data1=[]
voltage_data1=[]

time_data2=[]
voltage_data2=[]

time_data3=[]
voltage_data3=[]

#read in the data
lines = np.loadtxt('CapData.txt', delimiter = ',')
for line in lines:
    #the first item in row is the time
    time_data.append(line[0])
    #the second item in a row is the voltage
    voltage_data.append(line[1])
    
lines1 = np.loadtxt('CapData1.txt', delimiter = ',')
for line1 in lines1:
    #the first item in row is the time
    time_data1.append(line1[0])
    #the second item in a row is the voltage
    voltage_data1.append(line1[1])
    
lines2 = np.loadtxt('CapData2.txt', delimiter = ',')
for line2 in lines2:
    #the first item in row is the time
    time_data2.append(line2[0])
    #the second item in a row is the voltage
    voltage_data2.append(line2[1])
    
lines3 = np.loadtxt('CapData3.txt', delimiter = ',')
for line3 in lines3:
    #the first item in row is the time
    time_data3.append(line3[0])
    #the second item in a row is the voltage
    voltage_data3.append(line3[1])
    
#exponential decay function
    def my_func(x,a,b):
        return a*np.exp(-b*x)
    
#have to do the following to use the time data in the exponential function
fit_time_data = np.array(time_data)
fit_time_data1 = np.array(time_data1)
fit_time_data2 = np.array(time_data2)
fit_time_data3 = np.array(time_data3)

#make a plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#make an xy scatter plot
plt.scatter(time_data,voltage_data,color='red',label='data 10k')
plt.scatter(time_data1,voltage_data1,color='red',label='data 1k')
plt.scatter(time_data2,voltage_data2,color='red',label='data 20k')
plt.scatter(time_data3,voltage_data3,color='red',label='data 30k')

#add the exponential curve with guesses for constants a and b:
plt.plot(fit_time_data,my_func(fit_time_data,3.3,95),color='black',label='my fit 10k')
plt.plot(fit_time_data1,my_func(fit_time_data1,3.3,95),color='black',label='my fit 1k')
plt.plot(fit_time_data2,my_func(fit_time_data2,3.3,95),color='black',label='my fit 20k')
plt.plot(fit_time_data3,my_func(fit_time_data3,3.3,95),color='black',label='my fit 30k')

#label the axes etc
ax.set_xlabel('Time(s)')
ax.setylabel('Voltage(v)')
ax.set_title('Capacitor Discharge')
plt.legend(loc='upper right')

ax.text(0.4,1.5,'Looks like exponential decay to me')
plt.savefig('CapDisch_all.png')


    
    
    




