#3. Сформувати функцію для обчислення індексу максимального елемента масиву
#n*n, де 1<=n<=5.
#Наральник Богдан
import timeit
d=int(input())
def b(a):
    if a<=9:
        return a
    else:
        return b(a//10)+a%10
def c(a):#у даному блоку коду ми перервіряємо, чи дане число не є однозначним
    if a<=9:
        return a
    else:
        return c(b(a))
print(c(d))
