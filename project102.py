print('--------------------------')
print('~ Help for math problems ~')
print('__________________________')
print(' ')
print(' ')
print('Select the formula to be used-')
print("(Note: '2' represents 'square'.)")
print(' ')
print('1) a2-b2')
print('2) (a+b)2')
print('3) (a-b)2')
print('--------------------------')
eq=int(input('Enter the the serial number of the equation you need :- '))
print(' ')
num1=int(input('Enter the first number, var a :- '))
num2=int(input('Enter the second number, var b :- '))
print(' ')
print('--------------------------')

#a2-b2
def func1():
    fig1=num1+num2
    fig2=num1-num2
    sum=fig1*fig2
    print('Your answer is - ')
    print(sum)

#(a+b)2
def func2():
    fig1=num1*num1
    fig2=2*num1*num2
    fig3=num2*num2
    sum=fig1+fig2+fig3
    print('Your answer is - ')
    print(sum)

#(a-b)2
def func3():
    fig1=num1*num1
    fig2=2*num1*num2
    fig3=num2*num2
    sum=fig1-fig2+fig3
    print('Your answer is - ')
    print(sum)

if eq==1:
    func1()
elif eq==2:
    func2()
elif eq==3:
    func3()
print('__________________________')