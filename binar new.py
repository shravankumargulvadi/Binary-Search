
# coding: utf-8

# In[9]:


def binary_search(sequence,low,high,element):#a is input sequence b is list of elements to search
        
            index=low+round((high-low)/2)
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
            
        
    
import sys  
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    high=len(a)
    low=0
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, low, high, x), end = ' ')


# In[7]:





# In[8]:


a=[1,2,3,4]
len(a)

