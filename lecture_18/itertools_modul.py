from itertools import product, permutations, combinations, chain, cycle

# itertools.product
os = ['win', 'linux', 'mac']
browser = ['chrome', 'firefox', 'edge', 'safari', 'opera']
arch = ['x32', 'x64', 'arm']
output = product(os, browser, arch)
print(output)
for op_sys, web_browser, arc in output:
    print(op_sys, web_browser, arc)


# itertools.permutations
output2 = permutations((os+browser+arch), r=2)
print(output2)
for item in output2:
    print(item)

# itertools.combinations
output3 = combinations((os+browser+arch), r=3)
print(output3)
for item in output3:
    print(item)

# itertools.chain
output4 = chain(os, browser, arch)
print(output4)
for item in output4:
    print(item)

# itertools.cycle

output5 = cycle(output4)
print(output5)
# for i in output5:
#     print(i)

