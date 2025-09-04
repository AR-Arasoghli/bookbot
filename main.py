from stats import get_num_words, count_chars, sorted_list
import sys



def main():
    #x = 'books/frankenstein.txt'
    if len(sys.argv) == 2:
        x = sys.argv[1]
        g = get_num_words(x)
        y = count_chars(x)
        z = sorted_list(y)
        print(f'''============ BOOKBOT ============
Analysing book found at {x}...
----------- Word Count ----------
Found {g} total words
--------- Character Count -------''')
        for i in z:
            print(f'{i["char"]}: {i["num"]}')
        print('============= END ===============')
        print(sys.argv)
    else:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
        
    
#    a = sort_on(z)
#    print(a)
#    sort_on(sorted_list(count_chars('books/frankenstein.txt')))
#    final()
#    new_counts.sort(reverse=True, key=sort_on)  
#    print(new_counts)

main()