def vlrsParImpar():
    nums = []
    n1 = int(input("Digite o primeiro número: "))
    nums.append(n1)
    n2 = int(input("Digite o segundo número: "))
    nums.append(n2)
    if n1 % 2 == 0 and n2 % 2 == 0:
       return print(f"O menor número é {min(nums)}")
    else:
       return print(f"O maior número é {max(nums)}")
vlrsParImpar()
