import pathlib
import re

file = r"C:\Users\tobias.bowers\Desktop\2015_aoc2.txt"
data = pathlib.Path(file).read_text()
#mod_data = data.split('x')
total = 0
index = 1000
i = 0

while i <= index:
    for d in data:
        mod_data = re.split(r"[x\n]",data)
        mod_data = list(map(int,mod_data))
        sub_mod = mod_data[i:i+3]
        #dimentions of each gift
        for lwh in sub_mod:
            print(sub_mod)
            l = sub_mod[0]
            w = sub_mod[1]
            h = sub_mod[2]
            sqft=(2*l*w + 2*w*h + 2*h*l)
            #extra paper
            if l*w < w*h:
                if l*w < l*h:
                    extra = l*w
                else:
                    extra = l*h
            else:
                extra = w*h
            #total wrapping paper
            sub_total = sqft + extra
            print(sub_total)
            total = total + sub_total
            print(total)
            i += 3 

#print(mod_data)
print(sub_total)
print(total)
#print(l)
#print(w)
#print(h)