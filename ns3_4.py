#! /usr/bin/env python
#encoding=utf8
import sys,os
DISTANCES=[25,50,75,100,125,145,147,150,152,155,157,160,162,165,167,170,172,175,177,180]
TRIALS=[1,2,3,4,5]

print " WiFi Experiment Example"
try:
    import sqlite3
except ImportError as e:
    print "ERROR: This script requires sqlite3 (wifi-example-sim does not)."
    sys.exit(0)

#try:
    #os.system("gnuplot")
#except:
    #print "ERROR: This script requires gnuplot (wifi-example-sim does not)."
    #sys.exit(0)

os.system(r"export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:bin/")
if os.path.exists(r"/ns3/ns-allinone-3.29/ns-3.29/data.db"):
    answer=str(input("Kill data.db? (y/n)"))
    if answer=="y"or answer=="yes":
        print "Deleting database"
        os.remove(r"/ns3/ns-allinone-3.29/ns-3.29/data.db")


for trial in TRIALS:
    for distance in DISTANCES:
        print "第%s次实验,距离是%s"%(trial,distance)
        os.system(r'../../waf --run "wifi-example-sim --format=db --distance=%d --run=run-%d-%d"'%(distance,distance,trial))


# Another SQL command which just collects raw numbers of frames received.
#
# CMD="select Experiments.input,avg(Singletons.value) \
#    from Singletons,Experiments \
#    where Singletons.run = Experiments.run AND \
#          Singletons.name='wifi-rx-frames' \
#    group by Experiments.input \
#    order by abs(Experiments.input) ASC;"

os.system(r"mv ../../data.db .")
CMD="select exp.input,avg(100-((rx.value*100)/tx.value)) \
    from Singletons rx, Singletons tx, Experiments exp \
    where rx.run = tx.run AND \
          rx.run = exp.run AND \
          rx.variable='receiver-rx-packets' AND \
          tx.variable='sender-tx-packets' \
    group by exp.input \
    order by abs(exp.input) ASC;"
os.system(r'sqlite3 -noheader data.db "%s" > wifi-default.data'%CMD)


def alter(file,old_str,new_str):
    """
    替换文件中的字符串
    file:文件名
    old_str:旧字符串
    new_str:新字符串
    """
    file_data = ""
    with open(file, "r") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w") as f:
        f.write(file_data)
alter("wifi-default.data", "|", " ")

os.system(r"rm wifi-default.data.bak")

import matplotlib.pyplot as plot
x,y=[],[]
f=open("wifi-default.data",'r')
for line in f:
    a=0
    while line[a]!=" ":
        a+=1
    x.append(float(line[:a]))
    y.append(float(line[(a+1):].strip()))
plot.title("WiFi Defaults")
plot.xlabel('Distance(m)')
plot.ylabel("% Packet Loss --- average of 5 trials per distance")
plot.plot(x,y,linewidth=1.0)
plot.show()
plot.savefig("")
print("Done; data in wifi-default.data, plot in wifi-default.png")