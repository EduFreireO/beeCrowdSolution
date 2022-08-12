class Solution:
    def subtractProductAndSum(self, n):
        separados = [int(a) for a in list((str(n)))]
        def multiply(a, b):
            return a * b
        return reduce(multiply,separados) - sum(separados)

