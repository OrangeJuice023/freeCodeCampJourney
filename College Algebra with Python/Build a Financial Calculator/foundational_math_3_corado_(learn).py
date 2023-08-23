# -*- coding: utf-8 -*-
"""Foundational Math 3_Corado (Learn).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15eBeNneH1SsNHXxB4lLXgBxo0boFZyQW

[![freeCodeCamp](https://cdn.freecodecamp.org/testable-projects-fcc/images/fcc_secondary.svg)](https://freecodecamp.org/)

**Learn Foundational Math 3 by Building a Financial App**<br>
Each of these steps will lead you toward the Certification Project. Once you complete a step, click to expand the next step.

# &darr; **Do this first** &darr;
Copy this notebook to your own account by clicking the `File` button at the top, and then click `Save a copy in Drive`. You will need to be logged in to Google. The file will be in a folder called "Colab Notebooks" in your Google Drive.

# Step 0 - Acquire the Testing Library

Please run this code to get the library file from FreeCodeCamp. Each step will use this library to test your code. You do not need to edit anything; just run this code cell and wait a few seconds until it tells you to go on to the next step.
"""

# You may need to run this cell at the beginning of each new session

!pip install requests

# This will just take a few seconds

import requests

# Get the library from GitHub
url = 'https://raw.githubusercontent.com/edatfreecodecamp/python-math/main/math-code-test-c.py'
r = requests.get(url)

# Save the library in a local working directory
with open('math_code_test_c.py', 'w') as f:
    f.write(r.text)

# Now you can import the library
import math_code_test_c as test

# This will tell you if the code works
test.step00()

"""# Step 1 - Graphing Inequalities

Learn Inequalities by Building Shaded Graphs. Notice how you set up the plot, like you learned in the last certification. Run the following code and you will see that the graph of y <u>></u> 2x is not quite right. Because y is greater, the shading should be above the line. The second two arguments in the `fill_between()` function give a range of y values to shade. Change just that part of the code to make the graph correct. (Hint: Think about the top of the graph.)
"""

import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = - 10
ymax = 10
points = 2*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

plt.title("y > 2x")

y1 = 2*x
plt.plot(x, y1)

# Only change code below this line
plt.fill_between(x, y1, ymax, color='gray', alpha=0.5)

plt.show()


# Only change code above this line
import math_code_test_c as test
test.step01(In[-1].split('# Only change code above this line')[0])

"""# Step 2 - Graphing inequalities - Part 2

The default graph will give you a solid line, but you can change the type of line and the color. As `'b'` is for a solid blue line, `'b--'` will be a dashed blue line and `'r--'` will display a dashed red line. Change the code to graph a dashed red line.
"""

import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = - 10
ymax = 10
points = 2*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

y1 = 2*x

# Only change the next line:
plt.plot(x, y1, 'r--')

plt.fill_between(x, y1, ymin)
plt.show()



# Only change code above this line
import math_code_test_c as test
test.step02(In[-1].split('# Only change code above this line')[0])

"""# Step 3 - Making Art with Graphs

Now plot four inequalities on the graph, in a pattern. Notice how you only need to define the x values once. In the `fill_between()` function notice a fourth argument, `facecolor=`, to indicate a different color for the shaded area. The color name in single quotes, like 'green' or 'yellow' or any common color name. Run the code to see the pattern, then reverse the order of the colors and run it again.
"""

import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = - 10
ymax = 10
points = 2*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# Only change the lines indicated below

# line 1
y1 = x+6
plt.plot(x, y1)
plt.fill_between(x, y1, 10, facecolor='red') # change this line

# line 2
y2 = x+3
plt.plot(x, y2)
plt.fill_between(x, y2, y1, facecolor='yellow') # change this line

# line 3
y3 = x-1
plt.plot(x, y3)
plt.fill_between(x, y3, y2, facecolor='green') # change this line

# line 4
y4 = x-4
plt.plot(x, y4)
plt.fill_between(x, y4, y3, facecolor='blue') # change this line

plt.show()



# Only change code above this line
import math_code_test_c as test
test.step03(In[-1].split('# Only change code above this line')[0])

"""# Step 4 - Monomials

A <i>monomial</i> means "one thing" or one term. In a math equation, each term has a sign, a coefficient, and a variable to an exponent. Here are some examples: In the term -3x<sup>2</sup> you can see that the sign is negative, the coefficient is 3, the variable is x, the exponent is 2. The term x also has all of these parts: the sign is positive, the coefficient is 1, the variable is x, and the exponent is 1. In the term 5, the sign is positive, the coefficient is 5, the variable is still x, and the exponent is zero (notice that you don't need to write some of these parts, like x<sup>0</sup>). You can use `sympy` to display monomials nicely. Just run the code to see how this looks.
"""

from sympy import symbols, Eq

x = symbols('x')
eq1 = Eq(-2*x**3 , -16)
display(eq1)


# Just run this code
import math_code_test_c as test
test.step00()

"""# Step 5 - Polynomials

A "monomial" is one thing. A "binomial" is two things. A "trinomial" is three things. A "polynomial" is many things. In standard form, `x` is the variable; you put your terms in order from highest exponent to lowest; refer to the coefficients with letters in alphabetical order; and set all of this equal to `y` (because it is a function that you can graph). Example: y = ax<sup>4</sup> + bx<sup>3</sup> + cx<sup>2</sup> + dx + e <br>
Write code to prompt for integer input and display a polynomial. Remember to use the `**` for exponents. Parts of this are already done for you.
"""

from IPython.display import display, Math
from sympy import *

x,y = symbols('x y')

a = int(input("Enter coefficient A: "))
b = int(input("Enter coefficient B: "))
# continue this to prompt for variables c and d

# change the next line to display the full polynomial
y = a*x**3 + b*x**2

print("Here is your equation:")
display(Math("y = " + latex(y)))


# Only change code above this line
import math_code_test_c as test
test.step05(In[-1].split('# Only change code above this line')[0])

"""# Step 6 - Interactive Polynomial Graph

For this polynomial, y = ax<sup>2</sup> + bx + c, you can move the sliders to adjust the coefficients and see how that affects the graph. Notice how the `f()` function takes two arguments and the `interactive()` function defines two sliders. Run this code and interact with it. Then add the third coefficient ("c") by changing three things: the `def` line so that the function takes three arguments, the `plt.plot` line so that it includes "+ c", and the `interactive` line to include a third slider.
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np

# Change the function to take three coefficients: a, b, c
def f(a, b, c):  # Add 'c' as an argument
    plt.axis([-10, 10, -10, 10])  # window size
    plt.plot([-10, 10], [0, 0], 'k')  # blue x axis
    plt.plot([0, 0], [-10, 10], 'k')  # blue y axis
    x = np.linspace(-10, 10, 200)

    # Include the 'c' term in the equation
    plt.plot(x, a * x**2 + b * x + c)  # Include '+ c'
    plt.show()

# Add the third slider for coefficient 'c'
interactive_plot = interactive(f, a=(-9, 9), b=(-9, 9), c=(-9, 9))  # Add 'c' slider
display(interactive_plot)



# Only change code above this line
import math_code_test_c as test
test.step06(In[-1].split('# Only change code above this line')[0])

"""# Step 7 - Exponential Functions

The general formula for an `exponential function` is $y = a*b^{x}$ (where `a` and `b` are constants and `x` is the variable in the exponent). The shape of exponential graphs, especially when not drawn to scale, are very consistent, so the numerical values are more important to calculate. Things that grow exponentially include populations, investments, and other "percent increase" situations. Run this code and use the sliders to see the slight changes. Notice the scale. Then change the slider so that `a` has negative values from -9 to -1 and see how that changes the graph.
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = -100
ymax = 100

def f(a, b):
    plt.axis([xmin, xmax, ymin, ymax])  # window size
    plt.plot([xmin, xmax], [0, 0], 'k')  # x axis
    plt.plot([0, 0], [ymin, ymax], 'k')  # y axis
    x = np.linspace(xmin, xmax, 1000)
    plt.plot(x, a * b**x)
    plt.show()

# Modify the range for coefficient 'a' to include negative values
interactive_plot = interactive(f, a=(-9, -1), b=(1, 9))
display(interactive_plot)



# Only change code above this line
import math_code_test_c as test
test.step07(In[-1].split('# Only change code above this line')[0])

"""# Step 8 - Percent Increase

One formula for calculating a percent increase is <b>A = P(1 + r)<sup>t</sup></b> where `A` would be the `y` value on a graph and `t` would be the `x` value. `A` is the <i>annuity</i>, which is the amount you have at the end. `P` is the <i>principle</i>, which is the amount you have at the beginning. `R` (usually not capitalized) is the <i>rate</i>, a percent converted to a decimal. The exponent `t` represents <i>time</i>, usually in years. The code already prompts for `P`, `r` and `t`, so use those variables to calculate the annuity value.
"""

p = float(input("Starting amount = "))
r = float(input("Enter the percentage rate, converted to a decimal: "))
t = float(input("How many years will this investment grow? "))

# Change the next line to calculate the annuity
a = p*(1 + r)**t

print("The annuity is ", a)


# Only change code above this line
import math_code_test_c as test
test.step08(In[-1].split('# Only change code above this line')[0])

"""# Step 9 - Percent Decrease

The percent decrease formula is very similar, except you subtract the rate, so the formula is <b>A = P(1 - r)<sup>t</sup></b>. Some things that decrease by a percent include car values, decay of some elements, and sales discounts. Use the existing variables to calculate the final value (`a`).
"""

p = float(input("Starting amount = "))
r = float(input("Enter the percentage rate, converted to a decimal: "))
t = float(input("How many years will this decrease continue? "))

# Change the next line to calculate the final amount
a = p*(1 - r)**t

print("The final amount is ", a)

# Only change code above this line
import math_code_test_c as test
test.step09(In[-1].split('# Only change code above this line')[0])

"""#Step 10 - Compound Interest

When you use percent increase formulas for money in the bank, it's called <i>compound interest</i>. The amount of money you earn beyond the original principle is the interest. When the bank calculates the interest and adds it to the principle, that process is called <i>compounding</i> and it can happen any number of times per year. The formula is <b> A = P(1 + $\frac{r}{n}$)<sup>nt</sup></b> where <i>n</i> is the number of times the bank compounds the money per year. Notice that if n = 1 then this formula is the same as the formula from an earlier step. Write the code to calculate the annuity (hint: use extra parentheses).
"""

p = float(input("Starting amount: "))
r = float(input("Percentage rate, converted to a decimal: "))
t = float(input("Number of years this investment will grow: "))
n = int(input("Number of times compounded per year: "))

# Change the next line to calculate the annuity
annuity =  p*(1+(r/n))**(n*t)

print("The annuity is ", annuity)


# Only change code above this line
import math_code_test_c as test
test.step10(In[-1].split('# Only change code above this line')[0])

"""# Step 11 - Continuous Growth

In the first formula, A = P(1 + r)<sup>t</sup>, money is compounded annually.<br>
In the second formula, A = P(1 + $\frac{r}{n})^{nt}$, money is compounded `n` times per year.<br>
As `n` gets to be a really big number, you get a different formula, A = Pe$^{rt}$, for continuous growth.<br>
In this formula, `e` is a constant, about equal to 2.718281828. The following code already prompts for the four variables once. Use those variables to compare the annuity from the three formulas. Notice you need to `import math` to use `math.e` (the best approximation of e).
"""

import math

p = float(input("Principle: "))
r = float(input("Rate: "))
t = int(input("Time: "))
n = int(input("N: "))

# Only change the following three formulas:
a_annual = p*(1+r)**t
a_n_times = p*(1+r/n)**(n*t)
a_continuous = p*math.e**(r*t)

# Only change the code above this line

print("Compounded annually, anuity = ", a_annual)
print("Compounded ", n, "times per year, anuity = ", a_n_times)
print("Compounded continuously, anuity = ", a_continuous)


# Only change code above this line
import math_code_test_c as test
test.step11(In[-1].split('# Only change code above this line')[0])

"""# Step 12 - Investments

If you have an investment where you contrubute money every month and the value also increases by a consistent percentage, you can create a loop to calculate the accumulated value. In each iteration, use the <i>simple interest</i> formula: interest = principle * rate * time. (Hint: for one month, t = $\frac{1}{12}$ or you can just divide by 12.)
"""

p = float(input("Starting amount: "))
r = float(input("Annual percentage rate: "))
t = int(input("Number of years: "))
monthly = float(input("Monthly contribution: "))

# Hint: keep updating this annuity variable in the loop
annuity = p

# Each iteration of the loop represents one month
for a in range(12*t):
    annuity = annuity + monthly
    # Change the next line to calculate the interest
    interest = annuity * r / 12
    annuity = annuity + interest

# Keep this line:
print("Annuity = ", annuity)


# Only change code above this line
import math_code_test_c as test
test.step12(p,r,t,monthly,annuity)

"""# Step 13 - Mortgage Payments

When borrowing a large amount of money over a long period of time, the formula to calculate monthly payments gets complicated. Here it is:<br>
 monthly payment = P$\frac{\frac{r}{12}(1 + \frac{r}{12})^{12t}}{(1 + \frac{r}{12})^{12t} - 1}$ where, as usual, `P` is the principle, `r` is the annual interest rate (as a decimal), and  `t` is the time in years. Write the code to prompt for these variables and calculate the monthly payment. Hint: Use other variables and do this in steps.
"""

p = float(input("Amount borrowed: "))
r = float(input("Annual percentage rate: "))
t = float(input("Number of years: "))

# Write your code here and change the pmt variable
mult = 1 + r / 12
exp = 12 * t
top = r / 12 * mult ** exp
bot = (mult ** exp) - 1
pmt = top / bot

print("Monthly payment = $", pmt)


# Only change code above this line
import math_code_test_c as test
test.step13(p,r,t,pmt)

"""# Step 14 - Exponents and Logarithms

Exponential functions and logarithmic functions are inverses of each other. Here is an example: <b>2<sup>4</sup> = 16</b> and <b>log<sub>2</sub>16 = 4</b>. Both have the same information rearranged in different ways. If you had 2<sup>4</sup> = x you would be able to do that easily, but if you had 2<sup>x</sup> = 16 it would be more difficult. You could write that last equation as a logarithm: log<sub>2</sub>16 = x. In Python, you would write this as `math.log(16,2)`. In both cases, you would read it as "the log, base 2, of 16" and the answer would be an exponent. The logarithm is especially useful when the exponent is not a nice integer. Write code to prompt for the base and the result, then use logarithms to calculate the exponent.
"""

import math

base = float(input("base: "))
result = float(input("result: "))

# Just change the next line:
exp = math.log(result, base)

print("exponent = ", exp)


# Only change code above this line
import math_code_test_c as test
test.step14(In[-1].split('# Only change code above this line')[0])

"""# Step 15 - Natural Logs

If you know the rate, how long will it take for something to double?
Start with the continuous growth formula:<br>
A = Pe<sup>rt</sup><br>
If annuity is two times the principle, divide both sides by P
and get this:<br>
2 = e<sup>rt</sup><br>
Because of the base <i>e</i>, take the natural log of both sides and get this:<br>
ln(2) = rt<br>
Then divide by r to solve for t or divide by t to solve for r. In Python, use `math.log()` with one argument and no base to calculate natural log (which is a logarithm with base e). So the natural log of 2 is `math.log(2)`. Just run the code to see this example.
"""

import math

r = float(input("Enter the annual rate as a decimal: "))
t = math.log(2) / r
print("Your money will double in", t, "years")


# Just run this code
import math_code_test_c as test
test.step00()

"""# Step 16 - Common Logs

The <i>common log</i> is base 10, because that is our number system. Run this code a few times to see how the exponents relate to moving the decimal point to get the resulting number. Notice the floor function. Then take out the floor function to see the exact logarithm.
"""

import math

n = input('Enter a number with several digits or several decimal places: ')
n = float(n)

exp = math.log(n, 10)

if n == 1000:
    exp = 3

print("exponent =", exp)



# Only change code above this line
import math_code_test_c as test
test.step16(In[-1].split('# Only change code above this line')[0])

"""# Step 17 - Scientific Notation

<i>Scientific Notation</i> is a way of writing very large or very small numbers without all of the zeros or decimal places. For example, 45,000,000 could be written as 4.5 x 10<sup>7</sup> in scientific notation and 0.00000045 could be written as 4.5 x 10<sup>-7</sup>. The notation requires base 10, so it will always use the structure <b>n $*$ 10<sup>x</sup></b> where n is one digit then the decimal point. Change the code below to print each number in scientific notation. Determine the value of each variable by counting (not writing code). You will automate this process in the next step.
"""

a = 156000000000
b = 0.000000000413

# Determine the values for the scientific notation
a1 = 1.56
a2 = 11
b1 = 4.13
b2 = -10

print(a, " = ", a1, "* 10^", a2)
print(b, " = ", b1, "* 10^", b2)



# Only change code above this line
import math_code_test_c as test
test.step17(b1,b2)

"""#Step 18 - Logs and Scientific Notation

Writing code for scientific notation, you will make use of logarithms with base 10. Remember that scientific notation is in the form n $*$ 10<sup>x</sup> where `n` is one digit and then a decimal. To convert a number to scientific notation, take the log of the number and use the `floor()` function to get the expoenent (just as you did in a previous step). Divide the original number by 10 to that exponent and you get `n` (hint: dividing by 10<sup>x</sup> is the same as multiplying by 10<sup>-x</sup>). Rounding is usually necessary. Write the code to convert numbers to scientific notation.
"""

import math

a = 0.00000000000234
b = 12300000000000

# Use these three lines as a model
x1 = math.floor(math.log(a, 10))
n1 = round(a * 10**(-x1), 2)
print("a =", n1, "* 10^", x1)

# Calculate the values for 'b' in scientific notation
x2 = math.floor(math.log(b, 10))
n2 = round(b*10**(-x2),2)
print("b =", n2, "* 10^", x2)



# Only change code above this line
import math_code_test_c as test
test.step18(In[-1].split('# Only change code above this line')[0])

"""# Step 19 - Scientific Notation Conversion

Now ask for a number as input, and write the code to convert that number into scientific notation. You can re-use code you used in the previous step, using `n` and `x` as variables to print n * 10^x.
"""

import math

a = float(input('Enter a number to convert to scientific notation: '))

# Calculate the values for scientific notation
x = math.floor(math.log(a, 10))
n = round(a*10**(-x),2)

# Print the number in scientific notation
print(a, " = ", n, "* 10^", x)


# Only change code above this line
import math_code_test_c as test
test.step19(In[-1].split('# Only change code above this line')[0])

"""# Step 20 - Graphing Exponents and Logs

When not writing code, the <i>natural log</i> is written as "ln" and it means a logarithm with base e. Like any pair of inverse functions, the line y = e<sup>x</sup> and the line y = ln(x) are mirrored over the line y = x.  Because of the `np.linspace()` function in this code, `np.log()` works, but `math.log()` does not work here. Both log() functions in Python use e as the base by default. When using the `numpy` library, use `np.log10()` for base 10, `np.log2()` for base 2, etc. Because log functions can only have positive x values, the np.linspace() function will define a positive range for the log() function. Run this code, then change the blue line function to graph y = 2<sup>x</sup> and change the green line function to graph y = log<sub>2</sub>x and notice the similarities between the graphs.
"""

import matplotlib.pyplot as plt
import numpy as np
import math

xmin = -10
xmax = 10
ymin = -10
ymax = 10
plt.axis([xmin, xmax, ymin, ymax])  # window size
plt.plot([xmin, xmax], [0, 0], 'k')  # x axis
plt.plot([0, 0], [ymin, ymax], 'k')  # y axis

# Same x values for two lines
x1 = np.linspace(xmin, xmax, 1000)

# Blue line for y = 2x
plt.plot(x1, 2 * x1, 'b')

# Red line for y = x
plt.plot(x1, x1, 'r')

# Different x values for y = log(x) because x > 0
x2 = np.linspace(.001, xmax, 500)

# Green line for y = log2(x)
plt.plot(x2, np.log2(x2), 'g')

plt.show()

"""# Step 21 - Log Application - pH Scale

The pH scale, for measuring acids and bases, is a logarithmic scale. The negative log of the hydrogen concentration is the pH. Example: if the hydrogen concentration is .007 then that would be 7 * 10<sup>-3</sup> and therefore a pH of 3. Write the code to prompt for hydrogen concentration and then print the pH. Hint: the <i>ceiling</i> function (`math.ceil()`) works better than rounding here.
"""

import math

decimal = float(input("Enter the hydrogen concentration as a decimal number: "))

# Calculate pH using the formula pH = -log10(concentration)
h = -math.log10(decimal)

print("pH =", h)

"""# Step 22 - Functions for the Project

Define a function for calculating mortgage payments and a function for calculating investment balance. Use code you wrote in earlier steps. Each function should prompt for input and print the output.
"""

import math

def calculate_mortgage_payment():
    p = float(input("Amount borrowed: "))
    r = float(input("Annual percentage rate: "))
    t = float(input("Number of years: "))
    n = int(input("Number of times compounded per year: "))

    numerator = p * r / n * (1 + r / n)**(n * t)
    denominator = (1 + r / n)**(n * t) - 1
    pmt = numerator / denominator

    print("Monthly payment =", pmt)

def calculate_investment_balance():
    p = float(input("Starting amount: "))
    r = float(input("Annual percentage rate: "))
    t = int(input("Number of years: "))
    n = int(input("Number of times compounded per year: "))

    balance = p * (1 + r / n)**(n * t)

    print("Investment balance =", balance)

# Main program
choice = input("Choose an option (1 - Mortgage Payment, 2 - Investment Balance): ")

if choice == "1":
    calculate_mortgage_payment()
elif choice == "2":
    calculate_investment_balance()
else:
    print("Invalid choice.")

"""# Step 23 - More Functions

Create a function that produces an interactive polynomial graph (with sliders). Use code from an earlier step.
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np

def interactive_polynomial_graph():
    def f(a, b, c):
        xmin = -10
        xmax = 10
        ymin = -10
        ymax = 10
        plt.axis([xmin, xmax, ymin, ymax])  # window size
        plt.plot([xmin, xmax], [0, 0], 'k')  # x axis
        plt.plot([0, 0], [ymin, ymax], 'k')  # y axis
        x = np.linspace(xmin, xmax, 200)
        plt.plot(x, a * x**2 + b * x + c)
        plt.show()

    interactive_plot = interactive(f, a=(-9, 9), b=(-9, 9), c=(-9, 9))
    display(interactive_plot)

# Call the function to display the interactive graph
interactive_polynomial_graph()

"""# Step 24 - New Function

Create a function to print the time required for money to double, given the rate. Use the continuous growth formula from an earlier step.
"""

import math

def time_to_double_money(rate):
    t = math.log(2) / rate
    print("Time required for money to double:", t, "years")

# Call the function with the desired rate
rate = float(input("Enter the annual rate as a decimal: "))
time_to_double_money(rate)

"""# Step 25 - Certification Project 3

Build a financial app that calculates all of the following:<br>
<ul>
<li>Mortgage payment - given principle, rate, time</li>
<li>Retirement account balance at time of retirement</li>
<li>Time required for money to double - given the rate</li>
<li>Rate of growth - given starting value, time, and ending value</li>
</ul>
"""

import math

class FinancialApp:
    def __init__(self):
        self.choices = {
            "1": self.calculate_mortgage_payment,
            "2": self.calculate_retirement_balance,
            "3": self.calculate_time_to_double_money,
            "4": self.calculate_rate_of_growth,
            "5": self.exit_app
        }

    def calculate_mortgage_payment(self):
        p = float(input("Amount borrowed: "))
        r = float(input("Annual percentage rate: "))
        t = float(input("Number of years: "))
        n = int(input("Number of times compounded per year: "))
        numerator = p * r / n * (1 + r / n)**(n * t)
        denominator = (1 + r / n)**(n * t) - 1
        pmt = numerator / denominator
        print("Monthly payment =", pmt)

    def calculate_retirement_balance(self):
        p = float(input("Starting amount: "))
        r = float(input("Annual percentage rate: "))
        t = int(input("Number of years: "))
        n = int(input("Number of times compounded per year: "))
        balance = p * (1 + r / n)**(n * t)
        print("Retirement account balance =", balance)

    def calculate_time_to_double_money(self):
        rate = float(input("Enter the rate as a decimal: "))
        time_to_double = math.log(2) / rate
        print("Time required for money to double:", time_to_double, "years")

    def calculate_rate_of_growth(self):
        starting_value = float(input("Enter the starting value: "))
        ending_value = float(input("Enter the ending value: "))
        t = float(input("Enter the time in years: "))
        rate_of_growth = (ending_value / starting_value)**(1 / t) - 1
        print("Rate of growth =", rate_of_growth)

      def exit_app(self):
        print("Exiting the app.")
        quit()  # Exit the script

    def run(self):
        print("Financial App")
        while True:
            print("\nChoose an option:")
            print("1 - Calculate Mortgage Payment")
            print("2 - Calculate Retirement Account Balance")
            print("3 - Calculate Time to Double Money")
            print("4 - Calculate Rate of Growth")
            print("5 - Exit")
            choice = input("Enter option number: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    app = FinancialApp()
    app.run()