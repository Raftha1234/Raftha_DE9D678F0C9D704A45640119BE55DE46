# Raftha_DE9D678F0C9D704A45
#640119BE55DE46
f linearSearch(array, n, x):
for i in range(0, n):
if (array[i] == x):
return i return -1

array = [2, 4, 0, 1, 9]
x = 1n = len(array)
result = linearSearch(array, n, x)
if (result == -1): 
print("Element not found")else: print("Element found at index: ", result)


f CgpaCalc(marks, n):
grade = [0] * n Sum = 0
for i in range(n):
grade[i] = (marks[i] / 10)
for i in range(n):
Sum += grade[i] cgpa = Sum / n return cgpan = 5marks = [ 90, 80, 70, 80, 90 ] cgpa = CgpaCalc(marks, n)
print("CGPA = ", '%.1f' % cgpa)print("CGPA Percentage = ", '%.2f' % (cgpa * 9.5))
