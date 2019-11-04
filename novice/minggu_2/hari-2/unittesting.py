
assert sum([1,2,3]) == 6 #the value should be 6

def tes_sum():
    assert sum([1,2,3,4]) == 10 #the values shouldbe ten

def tes_sum_tuple():
    assert sum((1,2,3))== 6 #the value should be six
    

if __name__=="__main__":
    tes_sum()
    tes_sum_tuple()
    print("everything passed")
