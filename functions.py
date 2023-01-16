from itertools import *
import re
import string
import requests


def combinations(st):
    combination = []
    for i in permutations(st):
        combination.append(i)
        print(i, end=' ')
    print()
    return combination


# Функция для замены двух символов в массиве символов
def swap(ch, i, j):
    temp = ch[i]
    ch[i] = ch[j]
    ch[j] = temp


# Рекурсивная функция для генерации всех перестановок строки
tr1 = []


def permutations(ch, curr_index=0):
    global tr1
    if curr_index == len(ch) - 1:
        tr1.append(''.join(ch))

    for i in range(curr_index, len(ch)):
        swap(ch, curr_index, i)
        permutations(ch, curr_index + 1)
        swap(ch, curr_index, i)
    return tr1


def С(n, k):
    if 0 <= k <= n:
        nn = 1
        kk = 1
        for t in range(1, min(k, n - k) + 1):
            nn *= n
            kk *= t
            n -= 1
        return nn // kk
    else:
        return 0


def print_combination(k, n):
    comb_ls = []
    kek = []
    for i in range(k):
        comb_ls.append(i)
    comb_ls.append(n)
    comb_ls.append(0)
    while True:
        print(comb_ls[0:k])
        kek.append(comb_ls[0:k])
        for j in range(len(comb_ls) - 1):
            if comb_ls[j] + 1 == comb_ls[j + 1]:
                comb_ls[j] = j
            else:
                break
        if j < k:
            comb_ls[j] += 1
        else:
            break
    return kek


class Triangle:
    def __init__(self, count):
        self.countLines = int(count)

    def generateLine(self, n):
        line = []
        for i in range(n):
            if i == 0 or i == n - 1:
                line.append(1)
            else:
                prevLine = self.lines[n - 2]
                line.append(prevLine[i - 1] + prevLine[i])
        self.lines.append(line)

    def generate(self):
        self.lines = []
        for i in range(self.countLines):
            self.generateLine(i + 1)


def frequency_words(text_string):
    frequency = {}
    text_string = text_string.lower()
    match_pattern = re.findall(r"(\w+)", text_string)

    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1
    frequency_list = frequency.keys()
    return frequency


def print_rev(namefile):
    # получим объект файла
    file1 = open(namefile, "r")
    file2 = open("23.txt", "w")

    while True:
        # считываем строку
        line = file1.readline()
        reversed = []
        for i in line.strip():
            reversed.append(i)
        # прерываем цикл, если строка пустая
        new_line = "".join(reversed[::-1])
        if not line:
            break
        file2.write(new_line + '\n')
    # закрываем файл
    file1.close()
    file2.close()
    return True


def frequency_letters(text):
    letters = clear_text(text)
    frequency = {}
    for letter in letters:
        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter] += 1
    return frequency
    # print_results(frequency)


def clear_text(a_text):
    lower_text = a_text.lower().strip(string.punctuation)
    pattern = '[0-9]+'
    no_digits_text = re.sub(pattern, '', lower_text)
    words = no_digits_text.split()
    cleared_words = list()
    for word in words:
        cleared_words.append(word.strip(string.punctuation).replace('\'', ''))
    list_letters = list(''.join(cleared_words))
    return list_letters


def remove_img_tags(url):
    r = requests.get(url)  # url - ссылка
    html = r.text
    f = open('del_img.html', 'w')
    p = re.compile(r'<img.*?/>')
    f.write(p.sub('', html))
    f.close()
    return True


def absuoluteUrl(src, url):
    if 'https' not in src:
        return url + src
    else:
        return src


def imgSrc(img, url):
    return absuoluteUrl(re.findall(r'src=".*?"', img)[0], url)


def change_absol(url):
    str = requests.get(url).text
    imgList = re.findall(r'<img.*?>', str)

    for image in imgList:
        image = re.sub(r'src=".*?"', imgSrc(image, url), image)

    with open('urls_absol.html', 'w', encoding="utf-8") as output_file:
        output_file.write(''.join(imgList))
    return True

def del_tag(url):
   r = requests.get(url)  # url - ссылка
   html = r.text
   f = open('del_tag.html', 'w')
   html_without_tag = re.sub('<[^>]*>', '', html)
   f.write(html_without_tag)
   f.close()
   return True
