class Solution:
    def numberToWords(self, num: int) -> str:
        aplhabeth =""
        
        ones = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]
        tens = ["Ten","", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety" ]
        teens =["","Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        def ones_(num):
            return ones[num]
        
        def tens_(num):
            if str(num)[1]== "0":
                return tens[int(str(num)[0])]
            else:
                return tens[int(str(num)[0])] + " "+ ones_(int(str(num)[1]))
            
        def teens_(num):
            return teens[int(str(num)[1])]
        
        def hundreds_(num):
            print(num,",,")
            n = int(str(num)[0])
            ans = ""+ ones_(n) + " Hundred"
            n = int(str(num)[1:])
            if n < 1:
                return ans
            if n<=10:
                ans += " " + ones_(n)
            elif n < 20:
                print(n)
                ans+= " "+ teens_(n)
            elif n <100:
                ans+= " "+ tens_(n)
            print("jndc", n)                
            return ans
        
        def thousands_(num):
            print("thousands")
            n = str(num)[:len(str(num))-3]
            if(len(str(num))==6):
                ans = ""+ hundreds_(int(n))+ " Thousand" 
                print(ans)
                n = int(str(num)[3:])
                if n <1:
                    return ans
                elif n <=10:
                    ans += " "+ ones_(n)
                elif n < 20:
                    ans += " " + teens_(n)
                elif n < 100:
                    ans += " " + tens_(n)
                elif n >= 100:
                    ans+= " " + hundreds_(n)
                return ans
            
            elif(len(str(num))==5):
                ans =""
                n = int(str(num)[0:2])
                print(n)
                if n <= 10:
                    ans += ones_(n) + " Thousand"
                elif n < 20:
                    ans += teens_(n) + " Thousand"
                    print(ans)
                elif n < 100:
                    ans += tens_(n) + " Thousand"
                else:
                    if str(num)[1] == "0":
                        ans += tens_(n) +" Thousand"
                    else: 
                        ans += tens_(int(str(num)[0:2])) + " "+ ones_(int(str(num)[1:2])) +" Thousand"
                n = int(str(num)[2:])
                if n == 0:
                    return ans
                ans += " "
                if n < 10:
                    ans += ones_(int(str(num)[2:]))
                elif n <20:
                    ans += teens_(int(str(num)[2:]))
                elif n < 100:
                    ans += tens_(int(str(num)[2:]))
                else:
                    ans += hundreds_(int(str(num)[2:]))
                return ans
            
            elif(len(str(num))==4):
                ans =""
                n = int(str(num)[0])
                if n < 10:
                    ans += ones_(int(str(num)[0])) + " Thousand"
                n = int(str(num)[1:])
                if n == 0:
                    return ans
                ans += " "
                if n <=10:
                    ans += ones_(n)
                elif n <20:
                    ans += teens_(n)
                elif n < 100:
                    ans += tens_(n)
                else:
                    ans += hundreds_(n)
                return ans
      
        def millions_(num):
            print("millions")
            if(len(str(num))==7):
                n = str(num)[0]
                ans = "" + ones_(int(n)) + " Million"
                n = int(str(num)[1:])
                if n == 0:
                    return ans
                ans += " "
                if n <=10:
                    ans += ones_(n)
                elif n <20:
                    ans += teens_(n)
                elif n < 100:
                    ans += tens_(n)
                elif n < 1000:
                    ans += hundreds_(n)
                else:
                    ans += thousands_(n)
                return ans

            elif(len(str(num))==8):
                n = int(str(num)[0:2])
                if n <=10:
                    ans = "" + ones_(int(n)) + " Million"
                elif n < 20:
                    ans = "" + teens_(int(n)) + " Million"
                elif n < 100:
                    ans = "" + tens_(int(n)) + " Million"
                n = int(str(num)[2:])
                if n == 0:
                    return ans
                ans += " "
                if n <=10:
                    ans += ones_(n)
                elif n <20:
                    ans += teens_(n)
                elif n < 100:
                    ans += tens_(n)
                elif n < 1000:
                    ans += hundreds_(n)
                else:
                    print("...")
                    ans += thousands_(n)
                return ans
            elif(len(str(num))==9):
                n = int(str(num)[0:3])
                ans = "" + hundreds_(int(n)) + " Million"
                n = int(str(num)[3:])
                if n <= 0:
                    return ans
                if n <=10:
                    ans += " "+ ones_(n)
                elif n <20:
                    ans += " "+teens_(n)
                elif n < 100:
                    ans += " "+tens_(n)
                elif n < 1000:
                    ans += " "+hundreds_(n)
                else:
                    print("...")
                    ans += " "+ thousands_(n)
                return ans

        #start here
        if len(str(num)) == 1:
            #print("ones")
            return ones_(num) 
        elif len(str(num)) == 2:
            print("teens")
            if num ==10:
                return ones_(num)
            if num < 20:
                return teens_(num)
            else: 
                return tens_(num) 
            
        elif len(str(num)) == 3:
            #print("hundreds")
            return hundreds_(num)
        elif len(str(num)) > 3 and len(str(num))<=6:
            return thousands_(num)
        elif len(str(num)) > 6 and len(str(num))<=9:
            return millions_(num)
        elif len(str(num)) > 9:
            print("billions")
            n = int(str(num)[0])
            ans = "" + ones_(n) + " Billion"
            n = int(str(num)[1:])
            print(n)
            if n <= 0:
                return ans
            if n <=10:
                ans += " "+ ones_(n)
            elif n <20:
                ans += " "+teens_(n)
            elif n < 100:
                ans += " "+tens_(n)
            elif n < 1000:
                ans += " "+hundreds_(n)
            elif n < 1000000:
                print("...")
                ans += " "+ thousands_(n)
            else:
                print("...")
                ans += " "+ millions_(n)
            return ans
            
            
            
