def cylinder_area(radius, height):
    pi = 3.14159
    area = pi*(radius**2)
    circumference = 2*pi*radius
    return 2*area + height*circumference

def hms(nsec):
    hh = nsec // 3600
    nsec = nsec % 3600
    mm = nsec // 60
    ss = nsec % 60
    return hh, mm, ss

def main():
    print('the area of a cylinder of radius 10 and height 5 is', cylinder_area(10, 5))
    hh,mm,ss = hms(100000)
    print('100000 seconds correspond to', hh, 'hours,', mm, 'minutes and', ss, 'seconds')

if __name__ == "__main__":
    main()
