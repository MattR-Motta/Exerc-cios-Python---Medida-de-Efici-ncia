nums = []
def numeros():
    for i in range(1,6):
        num = float(input(f"Digite o {i}º número: "))
        nums.append(num)
    return nums
def maior(nums):
    return max(nums)
def menor(nums):
    return min(nums)
n = numeros()
print(f"O maior número é: {maior(n)}")
print(f"O menor número é: {menor(n)}")