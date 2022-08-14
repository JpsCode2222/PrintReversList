# 1] list reverse  2 methods (simple call reverse())
List=[10,20,30,40,50,60,70,80,90,100]
print('Reverse list is : ')
List.reverse()
print(List)

# 2] Input list from User
A=int(input('Enter how many Number you want in your list: '))
for i in range(A):
    data=int(input())
    List.append(data)
print("Entered list is: ",List)
List.reverse()
print("Reversed list is: ",List)
