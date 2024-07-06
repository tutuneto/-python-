import os

ml = os.getcwd()

wenjian = os.listdir(ml)

for t in wenjian:
    t0 = t
    xin =  t.removeprefix("new_new_new_")
    os.rename(t0, xin)