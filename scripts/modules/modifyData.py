def smoothing(list, winsize, lenseq):
    smoothed_list=[]
    i=0
    while i<winsize:
        smoothed_list.append(sum(list[:i+1])/(i+1))
        i+=1
    while i< lenseq-winsize:
        smoothed_list.append(sum(list[i-int(winsize/2):i+int(winsize/2)])/winsize)
        i+=1
    while i<lenseq:
        smoothed_list.append(sum(list[i:])/(lenseq-i))
        i+=1

    return smoothed_list
