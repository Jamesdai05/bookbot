from stats import get_num_words, get_char_count,sort_on,check_file
import sys
# def get_book_text_to_list():
#     with open("./books/frankenstein.txt","r") as f:
#         text= f.read()
#     word_count=len(text.split())
#     return word_count




def main():
    count= get_num_words(book_path=check_file())
    char_count= get_char_count(book_path=check_file())
    sorted_res= sort_on(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at sys.argv[1]...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for k in sorted_res.items():
        print(f"{k[0]}: {k[1]}")
    # print(sorted_res)
    print("============= END ===============")


if __name__ == "__main__":
    main()


