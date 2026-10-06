# def missing_number(l):
#     ncount=set()
#     for i in l:
#         if i not in ncount:
#             ncount.add(i)
#         else:
#             rnum=i
#             print(f"Repeated number:{rnum}")
#
#     for i in range(1,len(l)+1):
#         if i not in ncount:
#             mnum=i
#             print(f"Missing number:{mnum}")
#             break
#
#     return mnum+rnum

# num_list=[1,1,3,4]
# print(missing_number(num_list))

# def num(numlist):
#     repeated=0
#     missing=0
#     for i in range(1,max(numlist)+1):
#         if numlist.count(i)>1:
#             repeated=i
#         if numlist.count(i)==0:
#             missing=i
#     sum=repeated+missing
#     print(sum)
# num([1,4,3,4])
import math
