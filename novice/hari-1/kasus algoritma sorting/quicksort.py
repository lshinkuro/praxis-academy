def quicksort(data_list):
    quicksortH1p(data_list,0,len(data_list)-1)

def quicksortH1p(data_list,first,last):
    if first<last:

        splitpoint=partition(data_list,first,last)

        quicksortH1p(data_list,first,splitpoint-1)
        quicksortH1p(data_list,splitpoint+1,last)

def partition(data_list,first,last):
    pivotvalue = data_list[first]

    leftmark =first+1
    rightmark =last
    done = False
    while not done :
        while leftmark <= rightmark and data_list[leftmark] <= pivotvalue:
            leftmark=leftmark+1
        
        while data_list[rightmark]>=pivotvalue and rightmark >= leftmark:
            rightmark =rightmark-1
        
        if rightmark < leftmark:
            done= True
        else :
            temp =data_list[leftmark]
            data_list[leftmark]=data_list[rightmark]
            data_list[rightmark]=temp
    
    temp = data_list[first]
    data_list[first]=data_list[rightmark]
    data_list[rightmark]= temp

    return rightmark

data_list = [54,35,76,54,63,24,13,6,5,38,89]

quicksort(data_list)
print(data_list)



