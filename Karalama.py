def makeArrayConsecutive2(statues):
    a = sorted(statues)
    b = []
    for i in range(len(a)):
        if a[i] != a[-1] and a[i] != a[i+1] -1:
            a.insert(i, a[i])
            b.append((a[i]+1))
        else:
            continue
    return len(b) , b

print(makeArrayConsecutive2([6, 3]))