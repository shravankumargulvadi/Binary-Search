
# coding: utf-8

# In[22]:


def search (sequence,elements):
    high=len(sequence)-1
    low=0
    



    def binary_search(sequence,low,high,element):#a is input sequence b is list of elements to search
        
            index= int((low+high)/2)
            #print(index)
            if sequence[index]==element:
                return index
            
            
                
            elif sequence[index]<element:
                if low==index:
                    return -1
                else:
                    low=index
                    return binary_search(sequence,low,high,element)
            
            else:
                if high==index:
                    return -1            
                else:
                    high=index
                    return binary_search(sequence,low,high,element)
            
        
            
    result=elements
    for i in range(len(elements)):
        result[i]=binary_search(sequence, low, high, elements[i])
    for r in result:
        print(r)
        
    
import sys    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    x = data[n + 2:]
        # replace with the call to binary_search when implemented
    print(search(a, x), end = ' ')
    


# In[24]:


r=[2,0,-1,0,-1]
str(r)

