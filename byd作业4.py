"""第一题"""
# num = int(input('随便输点:'))
# if num >= 90:
#     print('A')
# elif num >= 80:
#     print('B')
# elif num >= 70:
#     print('C')
# elif num >= 60:
#     print('D')
# else:
#     print('E')

"""第二题"""
# num = int(input('又随便输点:'))
# ret = 'A' if num >= 90 else 'B' if num >= 80 else 'C' if num >= 70 else 'D' if num >= 60 else 'E'
# print(ret)

"""第三题"""
# ret = 0
# count = 1
# while count <= 100:
#     ret += count
#     count += 1
# print(ret)
#
# ret = 0
# for i in range(1, 101):
#     ret += i
# print(ret)

"""第四题"""
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{j}*{i}={i*j}', end='\t')
#     print('\n')

"""第五题"""
# l = [1] * 2
# for i in range(1, 36):
#     n = l[-1] + l[-2]
#     l.append(n)
# for n, i in enumerate(l):
#     if n % 6 == 0:
#         print('\n')
#     print(i, end='\t')

"""第六题"""
# al, di, no, el = 0, 0, 0, 0
# s = input("再随便输点:")
# for i in list(s):
#     if i.isalpha():
#         al += 1
#     elif i.isdigit():
#         di += 1
#     elif i == ' ':
#         no += 1
#     else:
#         el += 1
# print(al, di, no, el)

"""第七题"""
# t = 10
# l = [100]
# s = [100]
# for i in range(0, t):
#     n1 = l[-1] /2
#     n2 = s[-1] + l[-1]
#     l.append(n1)
#     s.append(n2)
# print(l[t], s[t-1])

"""第八题"""
# year1 = int(input('随便输点1:'))
# year2 = int(input('随便输点2:'))
# l1 = []
# for i in range(year1, year2 + 1):
#     if i % 400 == 0 or i % 4 == 0 and i % 100 != 0:
#         l1.append(i)
# print(l1)

"""第九题"""
# year = int(input('双随便输点:'))
# mo = int(input('叒随便输点:'))
# da = int(input('叕随便输点:'))
# count = 0 + da
# for i in range(1, mo):
#     if i in [1, 3, 5, 7, 8, 10, 12]:
#         count += 31
#     elif i in [4, 6, 9, 11]:
#         count += 30
#     else:
#         if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#             count += 29
#         else:
#             count += 28
# print(count)

"""第十题"""
# n = int(input("真得再随便输点了:"))
# ret = 0
# for i in range(1, n + 1):
#     t = 1
#     for j in range(1, i + 1):
#         t *= j
#     ret += t
# print(ret)

"""第十一题"""
# n1 = int(input('随便输点v1.0:'))
# n2 = int(input('随便输点v2.0:'))
# (t1, t2) = (n1, n2) if n1 > n2 else (n2, n1)
# while t2:
#     x = t2
#     t2 = t1 % t2
#     t1 = x
# print(t1)

"""第十二题"""
# n = int(input('最后随便输点:'))
# i = 2
# lx = []
# while n / i >= i:
#     if n / i % 1 == 0.5 and i % 2 == 0:
#         ret = 0
#         j = 0
#         l = []
#         while ret < n and int(n / i) - j > 0 and int(n / i) + 1 + j < n:
#             ret += int(n / i) - j + (int(n / i) + 1 + j)
#             l.insert(0, int(n / i) - j)
#             l.append(int(n / i) + 1 + j)
#             j += 1
#         lx.append(l)
#     elif n / i % 1 == 0 and i % 2 == 1:
#         ret = n / i
#         j = 1
#         l = [int(n / i)]
#         while ret < n and n / i - j > 0 and n / i + j < n:
#             ret += n / i - j + (n / i + j)
#             l.insert(0, int(n / i - j))
#             l.append(int(n / i + j))
#             j += 1
#         lx.append(l)
#     i += 1
# print(lx)