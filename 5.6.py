
import statistics
a = list()
number = int(input( "Enter the number of elements you want: "))
print ('Enter numbers: ')
for i in range(int(number)):
   n = input( "number : ")
   a.append ( int ( n ))
print("Given 'n' numbers: ")
print(a)
m = statistics.mean ( a )
v = statistics.variance ( a )
st = statistics.stdev ( a )
print( "Mean: ",m)
print( "Variance: ",v)
print( "Standard Deviation: ",st)
