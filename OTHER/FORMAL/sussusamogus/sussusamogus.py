import json,random;i=json.loads("".join(open("sussusamogus.json","r").readlines()));i=[i["among"],i["us"]];r=random.randint(0,len(i[0])-1)
for b,v in enumerate(i[0][r]):
    if v=="_" and i[0][r][b-1]!="/":del i[1][1]
    elif v=="!" and i[0][r][b-1]!="/":i[1][3]="are"
    elif v=="/" and i[0][r][b-1]!="/":i[1][2]+=""
    else:i[1][2]+=v
print(" ".join(i[1]))