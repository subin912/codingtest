_list = list(map(int, input().split()))
song = [1,2,3,4,5,6,7,8]

if _list== song:
    print('ascending')
elif _list == song[::-1]:
    print('descending')
else:
     print('mixed')