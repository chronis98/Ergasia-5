harshad=[]
table2=[]
for i in range(1000):
  if i<=9:
    if i>0:
      harshad.append(i)
      table2.append(i)
  elif i<=99:
      if i%(i%10+i/10)==0:
          harshad.append(i)
      if i%10*i/10>0:
        if i%(i%10*i/10)==0:
          table2.append(i)
  elif  i<=999:
     if i%(i%10+(i/10)%10+i/100)==0:
        harshad.append(i)
     if i%10*(i/10)%10*i/100>0:
       if i%(i%10*((i/10)%10)*i/100)==0:
          table2.append(i)
  else:
        harshad.append(i)
print "arithmoi harshad mexri to 1000:",harshad
print "arithmoi pou to ginomeno twn pshfiwn tous diairei ton idio ton arithmo:",table2
