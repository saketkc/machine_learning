#Hamming Code is a  regression model for finding the similarity between the
#texts. Returns the minimum number of substitutions required for transforming
#two strings to onen another. E.G. python parrot : 0+1+1+1+0+1 = 4

def hamming(s1,s2):
    if not (len(s1)==len(s2)):
        return false
    return sum(a1 != a2 for a1, a2 in zip(s1,s2))

if __name__ == "__main__":
    print hamming("toned","roses")

