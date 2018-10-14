def Binary_search(arr,search_num,start,last):
    arr.sort()
    while(last>=start):
        mid=start + int((last-start)/2)
        if(arr[mid]==search_num):
            return 1
        
        elif(arr[mid]>search_num):
            start=0
            last=mid-1
        else:
            start=mid+1
            last=last
    

arr=[14,2,8,9,4,7,0,5]
search_num=int(input("enter number "))
start=0
last=len(arr)-1
res=Binary_search(arr,search_num,start,last)
print("number found") if(res==1) else print("number not found")