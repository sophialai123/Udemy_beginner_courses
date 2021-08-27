import math

""""
https://docs.python.org/3/library/math.html
https://www.notion.so/zarkom/Introduction-to-Git-ac396a0697704709a12b6a0e545db049
"""

#math.ceil(num) _return a round up int
num = 31.23
num_round_up_int = math.ceil(num) #
print(num_round_up_int)

#math.floor(num)¶ return a round down int
num_round_down_int = math.floor(num)
print(num_round_down_int)


#math.abs(num) , absolute number 绝对数, 负数变绝对数
abs_num = -12
print(abs(abs_num))


#math.factorial(x) x = 4*3*2*1 阶乘公式: 乘以本身的数字和比本身小的数字到1 int only
num_fac = 4
print(math.factorial(num_fac))


#Return the absolute value of x. with a float type
float_abs_num = math.fabs(-12)
print(type(float_abs_num))


#math.sqrt(x) Return the square root of x. 平方根: 一个数字乘以它本身的值 eg: 9*9 = 81, 81 sqrt is 9.0, is a float
#Square root, in mathematics, a factor of a number that, when multiplied by itself, gives the original number.
print(math.sqrt(81))  # output = 9.0


#power 是函数 比如POWER（2，3）表示2的3次方 == 2*2*2
print(math.pow(2, 3))

# log 对数函数???
print(math.log(10))



# math.remainder(x, y), The remainder r = remainder(x, y) thus always satisfies abs(r) <= 0.5 * abs(y).??
x = 125
y = 22
print(math.remainder(x, y))




