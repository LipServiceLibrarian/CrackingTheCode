def two_arrays(array1, array2, value):
   flag = "YES"
   array1.sort()
   array2.sort(reverse=True)

   for i in range (0, len(array1)):
       if (int(array1[i]) + int(array2[i])) < value:
           flag = "NO"

   return flag

num_cases = int(raw_input())
for i in range (0, num_cases):
    length, value = raw_input().split()
    length, value = int(length), int(value)
    array1 = raw_input().split()
    array2 = raw_input().split()
    for i in range (0, len(array1)):
        array1[i] = int(array1[i])
        array2[i] = int(array2[i])

    print two_arrays(array1, array2, value)
