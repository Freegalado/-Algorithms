#Project Euler Problem 39

L = 1000
triangles_max = 0
p_max = 0

perimeters = []

for p in range(2, L-1,2):
    t = 0
    for a in range(2, int(p/3)):
        
        if  p * (p - 2 * a) % (2 * (p - a)) == 0:
            t += 1
            if t >= triangles_max: 
                triangles_max =  t 
                p_max = p
                
print("The perimeter (p) below {} that maximizes the number of triangles is {}.".format(L,p_max))    
print ("The number of triangles withe optimal p is {}.".format(triangles_max))


