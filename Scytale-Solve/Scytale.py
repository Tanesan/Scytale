#!/usr/bin/env python
# coding: utf-8

import sympy
import statistics
#大文字を小文字にするもの
import string
import math

#　言語ファイルの読み込み
file_name = "words_alpha.txt"

#　そのファイルを開く
with open(file_name, encoding="utf-8") as f:
    data_lines = f.read()
data_lines = data_lines.split('\n')
#重複を消す
namelist = list(set(data_lines))

# Enter the password
password = input("パスワードを英字で入力してください")
# A string of rounds n(Number)
#First,range of the password
#Imagine the n from password length　約数
n = sympy.divisors(len(password))
#メジアンで中央値を探す
median = statistics.median(n)
#リストに中央値が入っていれば
if n.count(median) != 0:
    mediun_ud = n.count(median)
    min_list = n[:mediun_ud]
    max_list = n[mediun_ud:]
else:
    list_len = int(len(n)/2)
    min_list = n[:list_len]
    max_list = n[list_len:]
    
min_list = sorted(min_list, reverse=True)
max_list = sorted(max_list)

print(max_list,min_list)
#maxの一番目,minの1,max2,min2,..
answers_k = []
answers_lenge = []
answers_aps = []
# sは何番目か
# kはパスワードをk個のブロックに分けて考える
for s in range(len(n)):
    if s % 2 == 1:
        k = max_list[math.floor(s/2)]
    else:
        k = min_list[round(s/2)]
        
        
    #パスワードをリストにする
    password_list = list(password)
    #リストをn回分割する
    result = [password_list[idx:idx + k] for idx in range(0,len(password_list), k)]
    #リストの一番目を縦に並べる
    #for y in range(int(len(password)/n)):
    answer_list =[]
    # リストを縦に並べる
    for y in range(k):
        # リストを横に並べる
        for i in range(int(len(password)/k)):
            #リストの向きを変えたものを入れる
            answer_list.append(result[i][y])
    #リストを文字列へ
    aps = "".join(answer_list)
    lists = []
    #言語ファイルから一致する単語を探す
    for x in range(len(namelist)):  
        #一致すると-1以外を返す
            if aps.lower().find(namelist[x]) != -1:
                #一致したものをリストへ
                lists.append(namelist[x])
                
    answers_k.append(k)
    answers_lenge.append(len(lists))
    answers_aps.append(aps)
answer_number = answers_lenge.count(max(answers_lenge))
print("The result is n=",answers_k[answer_number],"The sentence is",answers_aps[answer_number])


for n in range(1,6):
    #パスワードをリストにする
    password_list = list(password)
    #リストをn回分割する
    result = [password_list[idx:idx + n] for idx in range(0,len(password_list), n)]
    #リストの一番目を縦に並べる
    #for y in range(int(len(password)/n)):
    print(result)
    # リストを縦に並べる
    for y in range(5):
        # リストを横に並べる
        for i in range(int(len(password)/n)):
            #リストの向きを変えたものを入れる
            print(result,i,y,answer_list)
            answer_list.append(result[i][y])
    #リストを文字列へ
    aps = "".join(answer_list)
    answers = []
    lists = []
    #言語ファイルから一致する単語を探す
    for x in range(len(namelist)):  
        #一致すると-1以外を返す
            if aps.lower().find(namelist[x]) != -1:
                #一致したものをリストへ
                lists.append(namelist[x])
    print(len(lists))

