try:
    inp = raw_input ("Enter Hours:")
    hours = float(inp)
    inp = raw_input ("Enter Rate:")
    rate = float (inp)
except:
    print "Error, please enter numeric input"
    quit()
#print hours, rate
if hours <= 40:
    pay = hours*rate
else:
    pay = hours*rate+(rate*1.5*(hours-40))
print pay
