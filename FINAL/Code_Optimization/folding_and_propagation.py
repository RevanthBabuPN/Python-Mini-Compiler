'''
CODE LOGIC:
O(n) code
We loop through the quads,line by line, and see if the args are constants or can be reduced to 
constants (if already seen before i.e. in the dictionary) and replace them if the conditions
hold. We then push the result into a dictionary to store its value for further use in other
lines.
'''
fptr=open("non_optimized/show.tsv","r")
all_quads=fptr.readlines()[1:]
fptr.close()
all_quads = [(x[:-1].split("\t"))[1:] for x in all_quads]
di={'-':'-'}
for i in range(len(all_quads)):
	op,arg1,arg2,res=all_quads[i]
	if op=="LABEL" or op=="GOTO" or op=="IF" or '[' in arg1:
		continue
	if "addr" in arg1:
		continue
	if op=='=':
		if arg1 in di:
			di[res]=di[arg1]
			all_quads[i][1]=str(di[arg1])
		else:
			try:
				di[res]=int(arg1)
			except:
				di[res]=arg1
	elif op=="PRINT":
		if arg1 in di:
			all_quads[i][1]=str(di[arg1])
	else:
		if arg1 in di and arg2 in di:
			try:
				v1=int(di[arg1])
				v2=int(di[arg2])
				vr=0
				if op=='+':
					vr=v1+v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='*':
					vr=v1*v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='/':
					vr=v1/v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='//':
					vr=v1//v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='-':
					vr=v1-v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='==':
					vr=v1==v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='>':
					vr=v1>v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='<':
					vr=v1<v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='>=':
					vr=v1>=v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='<=':
					vr=v1<=v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
			except:#has to be a string
				if op=='+':
					di[res]=di[arg1]+di[arg2]
					all_quads[i]=["=",str(di[res]),"-",res]
				if op=='>=':
					di[res]=di[arg1]>=di[arg2]
					all_quads[i]=["=",str(di[res]),"-",res]
				if op=='<=':
					di[res]=di[arg1]<=di[arg2]
					all_quads[i]=["=",str(di[res]),"-",res]
				if op=='>':
					di[res]=di[arg1]>di[arg2]
					all_quads[i]=["=",str(di[res]),"-",res]
				if op=='<':
					di[res]=di[arg1]<di[arg2]
					all_quads[i]=["=",str(di[res]),"-",res]
				if op=='==':
					di[res]=di[arg1]<di[arg2]
					all_quads[i]=["=",str(di[res]),"-",res]
		else:
			try:
				v1=int(arg1)
				v2=int(arg2)
				vr=0
				if op=='+':
					vr=v1+v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='*':
					vr=v1*v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='/':
					vr=v1/v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='//':
					vr=v1//v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='-':
					vr=v1-v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='==':
					vr=v1==v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='>':
					vr=v1>v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='<':
					vr=v1<v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='>=':
					vr=v1>=v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
				if op=='<=':
					vr=v1<=v2
					di[res]=vr
					all_quads[i]=["=",str(vr),"-",res]
			except:
				pass
all_quads=["\t".join(i)+"\n" for i in all_quads]
all_quads=[str(i+1)+"\t"+all_quads[i] for i in range(len(all_quads))]
print(len(all_quads))
all_quads="".join(all_quads)
f=open("optimized/showfopr.tsv","w")
f.write("#\top\tA1\tA2\tRes\n")
f.write(all_quads)
f.close()