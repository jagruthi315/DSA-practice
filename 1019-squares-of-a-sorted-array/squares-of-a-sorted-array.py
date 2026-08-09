class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        
        pos=[]
        neg=[]
        main=[]
      
        
    
        for i in range (len(nums)):
            if nums[i]>=0:
               pos.append(nums[i])
            
            if nums[i]<0:
               neg.append(nums[i])
            
        if len(pos)==0:
            for i in range(len(neg)):
                val = lambda x: x * x
                main.append(val(neg[i]))
                i+=1
                  
            main = main[::-1]
            return main 
            
        if len(neg)==0:
            for i in range(len(pos)):
                val = lambda x: x * x
                main.append(val(pos[i]))
                i+=1
            return main


            # if len(neg) and len(pos)!=0:
        else:
            neg = [x*x for x in neg][::-1]
            pos = [x*x for x in pos]


               

                  
        m =len(neg)
        n = len(pos)
        i = j = 0
           

        while(i<m and j<n):
            
            if neg[i]<= pos[j]:
                        
                main.append(neg[i])
                i+=1
                    
            else:
                       
                main.append(pos[j])
                j+=1
                    

        while(j<n):
                
            main.append(pos[j])
            j+=1
                

        while(i<m):
                
            main.append(neg[i])
            i+=1

           
        return main       

        



        
                
               

                
                
                   
