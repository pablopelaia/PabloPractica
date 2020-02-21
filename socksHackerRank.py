def sockMerchant(n,ar):
    parejas={}
    for media in ar:
        
        if parejas.has_key(media):
            continue
                     
        cantidad=ar.count(media)
                
        if cantidad%2==1:
            cantidad=cantidad-1
            
        parejas[media]=cantidad/2
                   
    cantidad=0
    for i in parejas:
        cantidad=cantidad+parejas[i]
        
    print(cantidad)
        
       
        
       
ar=[10,20,90,20,10,10,30,50,90,90,10,20,30]
n=len(ar)
sockMerchant(n, ar)
