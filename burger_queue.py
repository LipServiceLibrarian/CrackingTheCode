import operator

num_orders = int(raw_input())
orders = {}
for i in range(0, num_orders):
    start, end = raw_input().split()
    start, end = int(start),int(end)
    orders[i+1] = start + end
sorted_orders = sorted(orders.items(), key=lambda x:(x[1],x[0]))

output = ''
for k, v in sorted_orders:
    output = output + str(k) + ' '
print output
