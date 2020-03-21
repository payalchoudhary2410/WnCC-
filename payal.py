import math

file = open("timestat.txt")
n = 0
real = []
totalr = float(0)
squarer = float(0)
user = []
totalu = float(0)
squareu = float(0)
sys = []
totals = float(0)
squares = float(0)
for x in file:
    if n % 4 == 0:
        n += 1
    else:
        y = x.split()
        l = list(y)
        s = l[1]
        t = (float(s[0]) * 60)
        t += (float(s[2:7]))
        if n % 4 == 1:
            real += [t]
            totalr += t
            squarer += t * t
            n += 1
        elif n % 4 == 2:
            i = 3
            user += [t]
            totalu += t
            squareu += t * t
            n += 1
        else:
            i = 0
            sys += [t]
            totals += t
            squares += t * t
            n += 1
avgr = float(totalr) / 100
avgu = float(totalu) / 100
avgs = float(totals) / 100
sdr = math.sqrt(float(squarer) / 100 - avgr * avgr)
sdu = math.sqrt(float(squareu) / 100 - avgu * avgu)
sds = math.sqrt(float(squares) / 100 - avgs * avgs)
nr = 0
nu = 0
ns = 0
for x in real:
    if avgr - sdr <= x <= avgr + sdr:
        nr += 1
for x in user:
    if avgu - sdu <= x <= avgu + sdu:
        nu += 1
for x in sys:
    if avgs - sds <= x <= avgs + sds:
        ns += 1
print("Average Time statistics")
print("real ", avgr, "user ", avgu, "sys ", avgs)
print("Standard deviation of Time statistics")
print("real ", sdr, "user ", sdu, "sys ", sds)
print("Number of runs within (average - standard deviation) to (average + standard deviation)")
print("real ", nr, "user ", nu, "sys ", ns)
