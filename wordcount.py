def wordcount(str):
    words = str.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    print("단어\t\t빈도수")
    print("=====================")
    for word, count in word_count.items():
        print(f"{word}\t\t{count}")
    
if __name__ == "__main__":
    str = input("문자열을 입력하세요: ")
    wordcount(str)