n=int(input("Enter number of elements:"))
print("Enter the input:")
inputs=[]
for i in range(0,n):
    ele=float(input())
    inputs.append(ele)
print(inputs)
print("Enter then weights:")
weights=[]
for i in range(0,n):
    ele=float(input())
    weights.append(ele)
print(weights)
b=float(input("Enter bais value:"))
print("The net input can be calculated as Yin=b+x1w1+x2w2:")
Yin=[]
for i in range(0,n):
    Yin.append(inputs[i]*weights[i])
print(round((sum(Yin)+b),3))





     
