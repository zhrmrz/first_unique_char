import collections
class Sol:
    def first_unique_char(self,s):
        c=collections.Counter(s)
        idx=0
        for char in s:
            if c[char]==1:
                return idx
            else:
                idx+=1
        return -1

if __name__ == '__main__':
    p1=Sol()
    print(p1.first_unique_char('anaconda'))
