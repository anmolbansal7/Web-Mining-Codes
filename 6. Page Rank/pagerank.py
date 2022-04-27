#Anmol Bansal 19BCE0630

import numpy as np
import pandas as pd


def calculate_PageRank(df, tup, OD, total, it):
    size = df.shape[0]

    old_page_ranks = [1 for i in range(size)]
    new_page_ranks = [1/size for i in range(size)]

    if it == 1:
        print()
        print('Initial page ranks: ')
        print(new_page_ranks)

    for _ in range(it):
        temp = 0
        c = 0
        for q, r in tup:
            old_page_ranks[q] = new_page_ranks[q]
        for x, y in tup:
            if total[x] > 1:
                temp += old_page_ranks[y]/OD[y]
                c += 1
                if(c == total[x]):
                    new_page_ranks[x] = round(temp, 4)
                    c = 0
                    temp = 0
                    continue
            else:
                temp = old_page_ranks[y]/OD[y]
                new_page_ranks[x] = round(temp, 4)
                temp = 0
    return new_page_ranks


n = int(input('Enter the size of the matrix:\t'))
outlinks = []
for i in range(n*n):
    temp = int(input('Enter the element:\t'))
    outlinks.append(temp)

outlinks = np.reshape(outlinks, (n, n))

it = int(input('Enter the number of iterations to be performed: '))

df = pd.DataFrame(outlinks)

OD = []

df2 = df.copy()

df["sum_1"] = df.apply(lambda row: sum(row[0:n] == 1), axis=1)

OD = np.array(df["sum_1"])

total = []
for i in range(0, n):
    total.append(df[i].sum())

df3 = np.array(df2)
df4 = np.transpose(df3)
df5 = pd.DataFrame(df4)
m, n = np.where(df5.values == 1)
index = df2.index
condition = df2.values == 1
row_index = index[m]
row_index_list = row_index.tolist()
column_index = index[n]
column_index_list = column_index.tolist()


def merge(list1, list2):
    merged_list = tuple(zip(list1, list2))
    return merged_list


tup = merge(row_index_list, column_index_list)

for i in range(1, it+1):
    page_ranks = calculate_PageRank(df, tup, OD, total, i)
    print()
    print('The converged page rank after', i, 'iteratios is:')
    print(page_ranks)
    sums = 0
    for j in page_ranks:
        sums += j
    print('The sum of page ranks after', i, 'iterations is: ', round(sums, 4))
