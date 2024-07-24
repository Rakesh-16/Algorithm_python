def Gcd(m,n):
   if (m == n):
   	return m;
   elif(m > n):
   	return Gcd(m-n, n);
   else:
   	return Gcd(m, n-m);
def F_gcd(num):
   fib1 = 1
   fib2 = 1
   i = 0
   while(i != num):
   	fib1, fib2 = fib2, fib1 + fib2
   	i += 1
   return i	
   	
   	 	
   			
m = input("Enter the number")
m = int(m)

n = input("Enter the number")
n = int(n)

result1 = Gcd(m, n)
print("Gcd is: ",result1)

result2 = Gcd(F_gcd(m), F_gcd(n))
print("fib_num is : ", result2)

result3 = F_gcd(result2)

if(result1 == result3):
   print("it is verified")

result = F_gcd(5)

print(result)  	
