#opening the mission file 
#pwd
myfile=open("c:\\Users\\Houriyeh Majditehran\\Desktop\\Spring_2019\\hard.txt")
#why it does NOt work! vali akhe file e k unja nis
#with open ('./hard.txt') as myfile:
#with open( 'hard.txt', mode = 'r') as myfile:

#for line in myfile.readlines():

content = myfile.read()
content

inLined=content.splitlines( )
inLined
# linebelineshode=content.splitlines()
#linebelineshode
n=len(inLined)
n
indexcount=0
#for items in inLined:
    
    #if index_count==n:
    #break
    # station
    #not needed but I did!
eachline=[]
for i in range(len(inLined)):
    eachline.append(inLined[i])
       # i+=1
   # if i==5:
       # break 
    print(eachline)
    eachline

#---------------------------------------------------------------------------
result=[]
r1='Null'
r2="Null"
r3="Null"
r31='Null'
r32='Null'
r33='Null'
R3=[r31,r32,r33]
if len(eachline[j])==17:
        result={"station":r1, "types":r2, "DesiredPosition":[r31,r32,r33]}
       
        result
else:
        result1={"station":r1, "types":r2, "DesiredPosition":r3}  
        result

eachline=['AV1 +180','FV3 1','CV1 +90','DA B1 U B2 D B3 D']
for j in range(len(eachline)):
#j=0
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
        #result={"station":r1, "types":r2, "DesiredPosition":[r31,r32,r33]}
         

        result={"station":r1, "types":r2, "DesiredPosition":[r31,r32,r33]}
        #result.update({"station":r1, "types":r2, "DesiredPosition":[r31,r32,r33]})
        #result["station","types","DesiredPosition"].append(r1,r2,[r31,r32,r33])
        result
    else:
        #result.update({"station":r1, "types":r2, "DesiredPosition":r3})

        result2={"station":r1, "types":r2, "DesiredPosition":r3} 
        result2_sorted = {i:result2[i] for i in result1.keys()}

        keys = result1.keys()
        values = zip(result1.values(), result2_sorted.values())
        result=dictionary = dict(zip(keys, values))
        result1=result
        #d.setdefault(key,[]).append(result[key]) 
        #result="string":()
        #result["station"]=r1
        #result["types"]=r2
        #result["DesiredPosition"]=r3
        
       # result["station","types","DesiredPosition"].append(r1,r2,r3)
        result
        result1


print (result)
           






# Another way to find out stations which I did not use here
#station=[]
#while indexcount< n-1:  
  #  station[indexcount] = inLined[indexcount][0] 
 #   station
#    indexcount+=1  
#station 

#First_letter = []
#For str in inLined
 #   First_letter.append(str[0])

#Contetnt_lines = [x.strip() for x in content]
#Contetnt_lines
#line_split = line.split(' ') 
#station_type = line_split[0] 
#station = station_type[0] 
#type_ = station_type[1]
#Operation = {'V': 'valve', 'B': 'breaker'}
#word='abcd'
#for item in enumerate(word):
#print(item)
