def pLDDT_dict(uniprotid):
    dict={}
    fd=open(uniprotid+".pdb","r")
    for line in fd:
        line2=line.split()
        if line2[0]=="ATOM" and line2[2]=="CA":
            dict[int(line2[5])]=float(line2[10])

    return dict
