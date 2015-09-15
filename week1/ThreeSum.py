class ThreeSum:
    def count(self, a):
        N = len(a)
        count = 0
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    if a[i] + a[j] + a[k] == 0:
                        count += 1
        return count

ts = ThreeSum()
a = raw_input('plz input the numbers\n')
temp = [int(i) for i in a.split(' ')]
print ts.count(temp)

