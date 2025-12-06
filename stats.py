import sys

def check_file():
    book_path=""
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path=sys.argv[1]
    return book_path



def get_num_words(book_path):
    res={}
    with open(book_path,"r") as f:
        text= f.read()

    string_text=text.lower()
    word_count=len(string_text.split())
    return word_count

def get_char_count(book_path):
    res={}
    with open(book_path,"r") as f:
        text= f.read()
    string_text=text.lower()
    word=string_text.split()
    for w in word:
        for char in w:
            if char in res:
                res[char]+=1
            else:
                res[char]=1
    return res

# dic=get_char_count()
# for k in dic.items():
#     print(f"{k[0]}: {k[1]}")

def sort_on(dic):
    return dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

# print(get_num_words())
# print(get_char_count())
# print(sort_on(dic))