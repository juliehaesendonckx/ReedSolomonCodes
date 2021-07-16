def GCD(a,b):
    c = a%b
    
    if (c == 0):
        return b
    else:
        return GCD(b,c)



def ModularInverse(a, p):
    if (GCD(a,p) == 1):    
        t = 0
        nt = 1
        r = p
        nr = a

        while (nr != 0):
            s = r // nr
            oT = t
            oR = r
            t = nt
            r = nr

            nt = oT - (s*nt)
            nr = oR - (s*nr)     
        
        if (r > 1):
            return 0
        if(t < 0):
            return t + p
        else:
            return t
        
    return 0