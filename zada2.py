def spir(mat):
    r=[]
    while mat:
        r+=mat.pop(0)
        mat=list(zip(*mat))[::-1] if mat else []
        
    return r
print(spir([[1, 3, 7], [2, 4, 8], [9, 0, 5]]))