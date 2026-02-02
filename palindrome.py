def palindrom(s):
    left=0
    n=len(s)
    right=n-1
    while(left<=right):
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True
if __name__=="__main__":
    s=input()
    print(palindrom(s))