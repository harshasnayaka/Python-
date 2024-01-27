name = input("Enter The User Name ! ")

print("Welcome %s , to Bajaj Showroom ! "%(name))

buy = input("Do You Wanna Take A Bike ? ")

test = input("Wana Test Ride It ? ")

print("Okay Which Vechile You Wanna Ride ? ")

select = input("Select Vechile ")

vehicle = ['NS 200', 'Pulsar', 'Dominar', 'CT 100', 'KTM']
if select in vehicle :
    print("Yes You Can Test It Please wait Sir ! ")

else :
    print("Stock Not Available ! ")


print("Thank You ! ")