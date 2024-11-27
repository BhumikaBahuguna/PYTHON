#count frequency of each character
arr=list(map(int,input().split()))         #map is a DS in which we can change the type of index as per your choice
print(arr)
m={}                                       #empty dictionary
for i in range(len(arr)):
    if arr[i] not in m:
        m[arr[i]]=0
    m[arr[i]]+=1
print(m)
