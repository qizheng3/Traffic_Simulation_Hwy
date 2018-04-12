class randTest:
    def tester(self, matrix):
        for i in range(len(matrix)):
            matrix[i] = i
            
            
sol = randTest()
m = [10, 20, 30, 40, 50]
sol.tester(m)
for i in m:
    print i