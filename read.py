data =[]
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        count += 1
        if count % 1000 == 0: # %求餘數
            print(len(data))
print('檔案讀取完畢，總共', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len += len(d)
print('留言平均長度', sum_len / len(data), '字')


new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('有', len(new), '筆留言小於100字')
print(new[0])
print(new[1])


good =[]
good = [d for d in data if 'good' in d] # 如果d有包含good就把d裝進清單
# for d in data:
#     if 'good' in d:
#         good.append(d)
print('有', len(good), '筆留言提到good')


# good = [1 for d in data if 'good' in d] # 如果d有包含good就把1裝進清單
# bad = ['bad' in d for d in data] # 把d有沒有包含bad的運算結果(True/False)裝進清單


# 文字計數
wc = {} # word_count
for d in data:
    words = d.split() # split()預設值為空白鍵，且遇連續空白鍵切割完不會產生空字串
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 # 新增word進wc字典
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
    word = input('請問你想查什麼字：')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過次數：', wc[word])
    else:
        print('這個字沒有出現過！')
print('感謝使用本查詢功能')