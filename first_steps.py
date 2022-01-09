p1 >> blip([0,1,2,[(3,12),5,(7,11),(9,11,3)]], scale=Scale.chinese, oct=3).every([6, 2], "stutter")
p3 >> play("x-ox-ox[ox]--ox-o---x-ox-ox[ox]ox-o---x-ox-o[xx]x--ox-o---x-ox-oxox-o---", sample=[0,0,1,0,0,1,1,0,1,0,0,1]) # actually dope
p4 >> creep([0,2,0,1], scale=Scale.indian, delay=[0, 0, (0, 1.5)], echo=0.00125, amp=0.06, glidedelay = [7,-7]) # tingling fx


p4.stop()

p5 >> play("[xX]-x-X-x-x-x-x-x-x-x-x-x-x-x-x-x{x-}", sample=[5,7])

bs >> pulse(primes[7:12], oct=1, scale=Scale.chinese)


ts >> pluck(P[1,2,3,4].reverse())


ts.stop()

p1 >> play("x{-x}")


Scale.default = "major"



p2.stop()



p5.stop()
bs.stop()
p1.stop()
p2.stop()
p3.stop()



# Check available synths
print(SynthDefs)

# Check available scales
print(Scale.names())

# Primes
noprimes = set(j for i in range(2, 8) for j in range(i*2, 50, i))
primes = [x for x in range(2, 50) if x not in noprimes]
print(primes)

################
