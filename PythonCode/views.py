def isDisariumNumber(a):
    dummy=a
    summ=0
    l=len(str(a))
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**l
        l-=1
    if summ==a:
        return True
    else:
        return False
if __name__=='__main__':
    ll=int(input('Enter lower limit='))
    ul=int(input('Enter upper limit='))
    for a in range(ll,ul+1):
        if isDisariumNumber(a):
            print(a,' ',end='')