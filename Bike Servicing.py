print("Welcome To Servicing Station ! ")
book = input("Please Keep Your Service Book Infront Of Sensor and PRESS OKAY ! ")
print("Please wait ! Collecting all data ")
name = input("Enter Owners Name ! ")
print("Welcome %s , To Our Servicing Station ! "%(name))
lr = ['NS 200','Pulsar 220F','CT 100','N160','NS 160','NS 125','Bajaj Dominar 250','Avenger','Pulsar 150','Pulsar 200']
bike = input("Enter your Bike Name ! ")
cc = input("Enter your Engine Capacity ! ")
if bike in lr :
    print("Yes we can service %s, Easier and Quicker ! "%(bike))
else :
    print("No We Dont Sell These Bikes So We Dont Service ! ")
avg = int(input("Enter your Bike Total Travelled Distance ! " ))
if avg >5000:
    print("Serviced Needed ! ")
else :
    print("No Service Requuired your %s, is in Good State ! "%(bike))
print("Hope You Waited Less ! ")
print("Please come After 5000 km Again or If there is any defect !")
print("Thank You")