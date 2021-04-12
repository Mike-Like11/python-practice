import random
def str_int(a):
    return [int(x) for x in a]
def kolvo_razl_el(a):
    return len(set(a))
def reversik(a):
    return list(reversed(a))
def spisok_indexsov(a,x):
    return [i for i in range(0,len(a)) if a[i]==x]
def sum_chet_indexsov(a):
    return sum([a[i] for i in range(0,len(a)) if i%2==0 ])
def max_len_posl(a):
    return max(j for j in a if len(j)==max(len(i) for i in a))
def shorten(i):
    return "mcwuoocdwhe"[i::3]
def transpose_zip(a):
    return [*zip(*a)]
def doklad():
    chast_1=('Коллеги,','В то же время,','Однако,','Тем не менее,','Следовательно,','Соответственно,','Вместе с тем,','С другой стороны,')
    chast_2 = ('парадигма цифровой экономики', 'контeкст цифровой трансформации', 'диджитализация бизнeс-процессов', 'прагматичный подход к цифровым платформам', 'совокупность сквозных тeхнологий', 'программа прорывных исслeдований','ускорeниe блокчeйн-транзакций', 'экспоненциальный рост Big Data')
    chast_3 = ["открывает новые возможности для", "выдвигает новые требования", "несёт в себе риски",
              "расширяет горизонты", "заставляет искать варианты",
              "не оставляет шанса для", "повышает вероятность", "обостряет проблему"]
    chast_4 = ["дальнейшего углубления", "бюджетного финансирования", "синергетического эффекта",
               "компрометации конфиденциальных", "универсальной коммодитизации",
               "несанкционированной кастомизации", "нормативного регулирования", "практического применения"]
    chast_5 = ["знаний и компетенций.", "непроверенных гипотез.", "волатильных активов.",
               "опасных экспериментов.", "государственно-частных партнёрств.",
               "цифровых следов граждан.", "нежелательных последствий.", "внезапных открытий."]
    return random.choice(chast_1)+" "+random.choice(chast_2)+" "+random.choice(chast_3)+" "+random.choice(chast_4)+" "+random.choice(chast_5)
def groups():
    letter = ['K', 'В', 'Н']
    maxCount = [25, 13, 10]
    return [letter[i] + str(j + 1)  for i in range(len(letter)) for j in range(maxCount[i])]

print(str_int(['1','2','3','4','5']))
print(kolvo_razl_el(['1','2','3','1','4','5','3']))
print(reversik(['1','2','3','4','5']))
print(spisok_indexsov(['1','2','3','1','4','5','3'],'1'))
print(sum_chet_indexsov([1,2,3,4,5]))
print(max_len_posl(["aaa","a","aaaaa","aaaaaaa","aa"]))
print(transpose_zip([['a','b','c'],['d','e','f'],['g','h','i']]))
print(doklad())
print(groups())
print(shorten(0))


