def isLUN(year):
    if year%100==0:
        if year%400==0:
            return 1
    else:
        if year%4==0:
            return 1
    return 0

def dijitian(YEAR,Month,day):
    ret=0
    ping=[31,28,31,30,31,30,31,31,30,31,30,31]
    lun=[31,29,31,30,31,30,31,31,30,31,30,31]
    if isLUN(YEAR):
        for i in range(Month-1):
            ret=ret+lun[i]
    else:
         for i in range(Month-1):
            ret=ret+ping[i]
    return ret+day       

def jiejiari(YEAR,Month,day):
    '返回 1代表周末 0代表周一和周五 '
    S=(YEAR+(YEAR-1)//4-(YEAR-1)//100+(YEAR-1)//400)%7
    days=(dijitian(YEAR,Month,day)+S-1)%7
    #return days
    if days==0 or days==6:
        return 1
    else :
        return 0


if __name__ == "__main__":
    print(jiejiari(2020,8,1))

    
    import time
    tm=time.strptime("20201028",'%Y%m%d')
    print(time.asctime(tm).startswith("Sat") or time.asctime(tm).startswith("Sun"))