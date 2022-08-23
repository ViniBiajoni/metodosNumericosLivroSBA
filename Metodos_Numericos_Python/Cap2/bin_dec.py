


def binTOdec(val_bin):
    val_dec = 0
    i=len(val_bin)-1
    for k in val_bin:
        val_dec= val_dec+2**k
        i=i-1
    return val_dec    


print(binTOdec([1,1,1,0,1,1,1]))    
print(binTOdec([1,1,1,1,1,1,1])) 
   