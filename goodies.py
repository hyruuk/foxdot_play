# Instruments
## Melody

p1 >> pluck([5,5,5,2], amp=0.1, dur=1/2, oct=4, scale=Scale.chinese).every([5,3], "stutter") # melody
p2 >> gong([5,5,5,2], amp=0.2, dur=[1,1/2,1/2,2,1/4,1,3/4], oct=3, scale=Scale.chinese).every([13,7], "stutter") # bass


## Bass

p3 >> dub([7,5,4], dur=[3,2,2,1/2,1/2,1/2], amp=0.2, oct=4, scale=Scale.chinese)
p4 >> dub([4,5,7], dur=[3,2,2,1/2,1/2,1/2], amp=0.1, oct=6, scale=Scale.indian)



# Percs
## KD base

p5 >> play("[xX]-x-X-x-")

p5 >> play("")

p5 >> play("x{-x}")


## Galoppes

## Effects
p6 >> play("hhh[hh]", dur=1, sample=1, amp=0.2)


# Stops
p1.stop()
p2.stop()
p3.stop()
p4.stop()
p5.stop()
p6.stop()