# Triangle perimeter
----------------------------
## Statement

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

----------------------------

## Methodology


The problem states that the sum of the sides of the triangle is 120, so we can say that:

![Diagrama sin título drawio](https://user-images.githubusercontent.com/91080406/211056522-9e4ce3f8-75a4-4a2a-9d96-99aa716c9a37.png)


![functions_solve_trian-0 drawio](https://user-images.githubusercontent.com/91080406/211053871-d602ab15-c435-4bbf-9998-50c786196943.png)

The Pythagorean theorem will be used in conjunction with the above formulation to obtain the larger leg (*b*). The first step would be to formulate the hypotenuse (*c*) with the variables *a*, *b* and *p*.

![functions_solve_trian-1 drawio](https://user-images.githubusercontent.com/91080406/211056650-a0539e58-42a7-4dc2-aa6f-109791f71e33.png)

Performing a simplification on the function we find *b* in terms of *p* and *a*. We know the value of *p* but we do not have the value of *a* which will be determined later.

![functions_solve_trian-2 drawio](https://user-images.githubusercontent.com/91080406/211057974-8ec550ff-472c-4e16-bb9b-d4d7a0a14b43.png)

The last step is determine *a* where we know that is less than or equal to *b* which is less than *c*, with this we can say that a is less than or equal to one third of the length of p.

![functions_solve_trian-3 drawio](https://user-images.githubusercontent.com/91080406/211059460-55c33048-37fc-4e81-8634-87fbaad2c71d.png)

Finally there are some restrictions that we can put on the function, the sum of the sides whether they are even or odd positive integers add up to an even number. Reviewing the Pythagorean theorems we find the Pythagorean triples where the same behavior is shown, so we can disregard looking among the odd values of *p*.


-------------------
## Results

The perimeter (p) below 1000 that maximizes the number of triangles is 840.
The number of triangles withe optimal p is 9.

