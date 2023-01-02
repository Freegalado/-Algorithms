#function that get the sum by common multiples
def sum_factors(n1,n2,p1,p2):
    
    num_sum = 0
    lcm = p1*p2
    
    for n in range(n1,n2,p1):
        num_sum = num_sum + n
    for n in range(n1,n2,p2):
        num_sum = num_sum + n
    for n in range(n1,n2,lcm):
        num_sum = num_sum - n
    
    return num_sum


#function that get the sum by brute force
def brute_force_factors(n1,n2,p1,p2):
    
    num_sum = 0

    for i in range(n1,n2):
        if (i%p1==0) or (i%p2==0):
            num_sum = num_sum + i
            
    return num_sum



"""call the method and put the range of numbers for the problem
in this case and the method to solve it
1 = solve the problem by factors
2 = solve the problem by brute force
"""


method = 1
n1 = 0
p1=3
p2=5
n2= 1000


if method == 1:
    total_sum = sum_factors(n1, n2, p1, p2)
    
    print('The sum of all the multiples of 3 and 5 is {}.'.format(total_sum))
    
else:
    total_sum = brute_force_factors(n1, n2, p1, p2)
    
    print('The sum of all the multiples of 3 and 5 is {}.'.format(total_sum))
   



    