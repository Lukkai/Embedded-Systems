from collections import Counter

def repcounter():
    # chars = chars.lower()
    a = [1, 2, 3, 4, 1, 4, 1]
    
    ##1
    # repetition_dict = Counter(a)
    
    ##2
    # repetition_dict = dict((i, a.count(i)) for i in set(a))

    ##3
    # d = {}
    # for i in a:
    #     if i in d:
    #         d[i] = d[i]+1
    #     else:
    #         d[i] = 1
    # return d

    ##4
    # d = {}
    # for i in a:
    #     if i in d:
    #         d[i] = d[i]+1
    #     else:
    #         d[i] = 1
    # return dict(d)
    
    ##5
    # repetition_dict = {}
    # for char in set(chars):
        # repetition_dict[char] = chars.count(char)

    repetition_dict = dict(map(lambda x  : (x , list(a).count(x)) , a))
    return repetition_dict

# if __name__ == "__main__":
# chars = input("Input a set of characters: ")
print(repcounter())

print(3/2)