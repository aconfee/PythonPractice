# See two sum.
# Can either call a 2 sum algorithm for every N -- basically, I have one number, what pair exists to provide the difference?
# If calling the 2 sum, note that the hash implementation is way faster, but at the cost of memory.
# OR if no additional memory is allowed, the algorithm can look like:

# for each i in N
#   for each j in N
#     diff = target - (valI + valJ)
#     third = binarySearch(diff)

# this runs at N^2(logN), or O(n^2)

# using N = 64, calling hash would result in 8192, this would result in 28672, and calling two ptr results in 30720. So this is the
# fastest implementation that doesn't use additional memory.
