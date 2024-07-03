from math import *

#some source: https://forum.spaceengine.org/viewtopic.php?t=69

def c(n): #str hex to str dec converter
    return int(str(n),16)

#distance in parsecs from the SE universe center to AbsPosition
def DistFromCenter(x,y,z):
    return sqrt(c(x)**2+c(y)**2+c(z)**2)*(16**-20)

def XYZtoRADecDist(x,y,z):
    def sgn_func(n):
        if n>0: return 1
        elif n==0: return 0
        else: return -1

    if not (c(x)==0 and c(z)==0):
        RA  = degrees(atan2(c(x), c(z)))/15;
        if (RA<0): RA = RA + 24.0
        Dec = degrees(atan(c(y)/sqrt(c(x)**2+c(z)**2)))
    else:
        RA = "N/A"
        if c(y)!=0: Dec = sgn_func(c(y))*90.0
        else: Dec = "N/A"
    Dist = DistFromCenter(x,y,z)
    print("RA: "+str(RA))
    print("Dec: "+str(Dec))
    print("Dist: "+str(Dist)+" parsec(s)")

def main():
    calc_key=""
    while True:
        if calc_key.lower()!="q":
            print("XYZ to RA/Dec/Dist calculator\n1 block = 16^-20 parsecs\n")
            x=str(input("X: "))
            y=str(input("Y: "))
            z=str(input("Z: "))
            print("\nResult:")
            try: XYZtoRADecDist(x,y,z)
            except: print("\nN/A")
            calc_key=str(input("\nIf you want to quit, enter \"Q\" or \"q\": "))
            print("-------------------------------")
        else: break
    quit()

if __name__ == "__main__":
    main()
