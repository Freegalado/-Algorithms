# Multiple of 3 and 5

## The statement of the problem

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

------------------------
## Methodology

![multiple_of_3_and_5](https://user-images.githubusercontent.com/91080406/210271897-126e4080-4dad-495e-93db-8b4c902f2746.png)

The problem tries to find the sum of multiples of 3 and 5 in a range of positive integers. The solution can be found in two ways, the first is by obtaining the multiples of 3 and 5, but one must be careful with the least common multiple (lcm) since there will be a double counting, so the lcm is obtained and the sum of its multiples is subtracted. The second method is by brute force where it is verified that every number in the range of positive integers is divisible without any remainder, performing the sum of the numbers that meet this condition.

![time_process](https://user-images.githubusercontent.com/91080406/210273443-4ab3b22f-4c24-47ab-ad82-ae40da30d9ea.png)

It may seem that both solutions have similar computation time but the the above graph shows that as the range of positive integers increases method 1 where common multiples are used has a much small computation time. 

------------------------
## Result

The sum of all the multiples of 3 and 5 is **233168**.

