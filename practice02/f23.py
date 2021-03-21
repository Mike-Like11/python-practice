def f23(x):
    r=[]
    for mini_x in x:
        res = []
        for val in mini_x:
            if val != None:
             res.append(val)
        r.append(res)
    s = []
    for i in r:
        if i not in s:
            s.append(i)
    e=[[row[i] for row in s] for i in range(len(s[0]))]
    s2 = []
    for i in e:
        if i not in s2:
            s2.append(i)
    s3= [[row[i] for row in s2] for i in range(len(s2[0]))]
    for min_s in s3:
        for rr in min_s:
            min_s[min_s.index(rr)]=rr.split("#")[0].replace("/",'-')
            if(rr.find("[")>0):
                min_s.append(rr.split("[")[0].split("#")[1])
            else:
                     if(rr.find(".")>-1):
                        min_s[min_s.index(rr)] =str(int(float(rr)*100.1))+"%"

    return s3