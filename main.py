import string,random

if __name__ == "__main__":
    s1=string.ascii_letters
    
    s3=string.digits
    s4=string.punctuation
    while True:
        passLen=input('Enter password length:')
        if passLen.isdigit():
            s=[]
            s.extend(list(s1))
            
            s.extend(list(s3))
            s.extend(list(s4))
            random.shuffle(s)
            # or
            # random.sample(s,passLen)

            print('Your Password is:'+'\n'+''.join(s[0:int(passLen)]))
            break
            
        else:
            print('Please enter digits only')
            
        
            

                
            
        
            
        
        
        
            
            

    
    


    