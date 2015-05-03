def service_lanes(lanes, entry, exit):
   subset = lanes[entry:exit+1]
   print subset
   return min(subset)

num_lanes, n = raw_input().split()
num_lanes, n = int(num_lanes), int(n)
lanes = raw_input().split()
''.join(lanes)
for i in range(1,n+1):
    entry, exit = raw_input().split()
    entry, exit = int(entry),int(exit)
    print service_lanes(lanes, entry, exit)
