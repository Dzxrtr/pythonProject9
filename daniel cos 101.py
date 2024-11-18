print('one')
def calculate_pressure():
    force=float(input('what is the value for mass'))

    area = float(input('what is the value for area'))

    pressure = force / area

    print('pressure is', pressure,)
calculate_pressure()
print('two')
def calculate_area_of_trapezium():

    a = int(input("Enter a of trapezium ") )
    b = int(input(" Enter b of trapezium "))
    height = int(input(" Enter of height of trapezium "))
    area = ( (1/2) * (a + b ) * height )
    print("area is" , area )
calculate_area_of_trapezium()
print('three')
def calculate_area_of_triangle():

    base=float(input('what is the value of base'))
    height=float(input('what is the value of height'))

    area=(base*height)/2
    print('area is',area)
calculate_area_of_triangle()
print('four')
def calculate_power():

    work = float(input("Enter value of work") )
    time = float(input(" Enter value of time "))
    power=work/time
    print("power is" , power)
calculate_power()
print('five')
def calculate_work():

    force=float(input('what is the value of force'))
    displacement=float(input('what is the value of displacement'))
    work= force * displacement

    print('work is',work,'j(joules)')
calculate_work()
