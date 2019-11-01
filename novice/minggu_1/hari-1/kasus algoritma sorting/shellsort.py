def shellsort(alist):
    sublistcount = len(alist)//2
    while sublistcount >0:
        for star_position in range(sublistcount):
            gap_insertionsort(alist,star_position,sublistcount)
            
        print ("after increment of size",sublistcount,"the list is",nlist)

        sublistcount = sublistcount//2

def gap_insertionsort(nlist,start,gap):
    for i in range(start+gap,len(nlist),gap):

        current_value = nlist[i]
        position =1

        while position>= gap and nlist[position-gap]>current_value:
            nlist[position]=nlist[position-gap]
            position = position-gap
            nlist[position]=current_value
        
        
nlist =[15,98,7,65,46,34,25,13,8]
shellsort(nlist)
print(nlist)