def gen_integers(start=0, count=None):
    i = start
    while True:
        yield i
        i = i + 1
        if count!=None:
            if i > start+count:
                return

def fv_table(PV, r, start=0, count=30):
    for i in gen_integers(start,count):
        FV = PV*(1+r)**i
        yield FV


for balance in fv_table(100000, .07, start=0, count=10):
    print('${:,.2f}'.format(balance))
