def s2hms (segs):
    mins,segs = divmod(segs,60)
    hrs,mins = divmod(mins,60)
    print(f"{hrs} {mins} {segs}")

def hms2s (hrs, mins,segs):
    seg = hrs * 3600 + mins * 60 + segs
    print(f"{seg}")

s2hms (8000)
hms2s(2,13,20)