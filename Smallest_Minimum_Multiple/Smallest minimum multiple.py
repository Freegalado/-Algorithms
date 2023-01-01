

#greatest common divisor 
def gcd(x,y):
    while y != 0:
        x,y = y, (x % y)
    return x    
    

#least common multiple 
def lcm(x,y):
   lcm = x * y / gcd(x,y)
   return lcm


#function to solve by force brute.
def brute_force_lcm(n1,n2):
    mod = True 
    n = 2
    
    while mod:
        dumm_list = []
    
        for i in range(n1,n2):
            res = n % i
            if res == 0:
                dumm_list.append(i)
        if len(dumm_list) == len(range(n1,n2)): 
            mod = False
            print(n)
        else:
            n += 1
            
     
#Function to choose the method to solve the problem
def method_SMM(n1,n2,method):
    if method == 1:
        for i in range(n1,n2):
            n1 = int(lcm(n1,i))   
        print(n1)
    else:
        brute_force_lcm(n1,n2)



"""call the method and put the range of numbers for the problem
in this case and the method to solve it
1 = solve the problem by lcm
2 = solve the problem by brute force
"""

method_SMM(1,21,1)








