# import turtle            # set up alex
# wn = turtle.Screen()
# alex = turtle.Turtle()

# for i in [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 ,19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]:   # repeat four times
#     alex.backward(50)
#     alex.right(90)

# wn.exitonclick()

'''def filter_mult5(numbers):
    for n in numbers:
        if n%2 == 1:
            return 

print(filter_mult5(list(range(11))))
[1, 2, 3, 4, 6, 7, 8, 9, 11]  

print(filter_mult5([7]))
print(filter_mult5([0, 1, 0]))
print(filter_mult5([0, 1, 0, 1, 0]))'''


def check_point_belongs_rect(a, c, b):
    # if a[0] <= c[0] <= b[0] and a[1] <= c[1] <= b[1]:
        # print("Belongs to  axis")
        # return True
    x1, y1 = a
    x2, y2 = b
    x, y = c
    return x1 <= x <= x2 and y1 <= y <= y2

print(check_point_belongs_rect((2,3), (3, 4), (6, 6)))