#opening the mission file 
#myfile=open("c:\\Users\\Houriyeh Majditehran\\Desktop\\Spring_2019\\hard.txt")
#content = myfile.read()
#eachline=content.splitlines()

eachline=['AV1 +180','FV3 1','CV1 +90','DA B1 U B2 D B3 D'] #for testing without file

mission = {"time": 0, "tasks": []}
for j in range(len(eachline)):
    r1=eachline[j][0]
    if eachline[j][1]=="V" and eachline[j][2]=="1":
        r2='Gate Value'
        r3=eachline[j][4:]
    if eachline[j][1]=="V" and eachline[j][2]=="2":
        r2='Large Valve'
        r3=eachline[0][4:]
    if eachline[j][1]=="V" and eachline[j][2]=="3":
        r2='shutlecook'
        if eachline[j][4]==0:
            r3='Open'
        if eachline[j][4]==1:
            r3='closed'
    if eachline[j][1]=="A":
        r2='BreakerBox A'
        if eachline[j][6]=="U":
            r31='Up'
        else:
            r31='Down'
        if eachline[j][11]=="U":
            r32='Up'
        else:
            r32='Down'
        if eachline[j][16]=="U":
            r33='Up'
        else:
            r33='Down'    
    if eachline[j][1]=="B":
        r2='BreakerBox B' 
        if eachline[j][6]=="U":
            r31='Up'
        else:
            r31='Down'
        if eachline[j][11]=="U":
            r32='Up'
        else:
            r32='Down'
        if eachline[j][16]=="U":
            r33='Up'
        else:
            r33='Down'

    if len(eachline[j])==17:
        result={"station":r1, "types":r2, "desiredPosition":[r31,r32,r33]}
    else:
        result={"station":r1, "types":r2, "desiredPosition":r3}
    mission["tasks"].append(result)

print mission