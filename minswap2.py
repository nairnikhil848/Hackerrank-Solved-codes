

def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    count = -0
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            count += 1
    print(count)


if __name__ == "__main__":
    main()


# #second method using hash table

# def minimumSwaps(arr):

#     swap=0
#     temp=[0]*n
#     for index,value in enumerate(arr):
#         temp[value-1]=index

#     for i in range(0,n):
#         if(arr[i]!=(i+1)):
#             swap+=1
#             t=arr[i]
#             arr[temp[i]]=arr[i]
#             temp[arr[i]-1]=temp[i]
#             arr[i]=i+1
#             temp[i]=i
#     #print(arr)
#     #print(temp)

#     return(swap)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     arr = list(map(int, input().rstrip().split()))

#     res = minimumSwaps(arr)
