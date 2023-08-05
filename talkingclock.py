class Solution:    
    def ClockTalker(self, input_time):
            first_dict = {"00":"twelve:am","01": "one:am", "02":"two:am", "03":"three:am", "04":"four:am", "05":"five:am", "06":"six:am", "07":"seven:am", "08":"eight:am", "09":"nine:am","l0":"ten:am","11":"eleven:am","12":"twelve:pm","13":"one:pm","14":"two:pm","15":"three:pm","16":"four:pm","17":"five:pm","18":"six:pm","19":"seven:pm","20":"eight:pm","21":"nine:pm","22":"ten:pm","23":"eleven:pm","24":"twelve:am"}
            ty_case = {"0":"oh", "2":"twenty", "3":"thirty", "4":"fourty", "5":"fifty"}
            teen_case={"0":"ten","1":"eleven","2":"twelve","3":"thirteen","4":"fourteen","5":"fifteen"}
            normal = {"0":"","1":" one","2":" two","3":" three","4":" four","5":" five","6":" six","7":" seven","8":" eight","9":" nine"}
            second_section = 0
            #type input_time: string
            #return type: string
            print(type(input_time))
            firstpart, secondpart = input_time.split(":")
            print(firstpart,secondpart)
            correctpart = first_dict[firstpart]
            firstime, timestamp = correctpart.split(":")
            appendingstring = 0
            if secondpart[0] == "0" and secondpart[1] == "0":
                appendingstring = ""
                return "It's " + firstime + " " + timestamp
            elif secondpart[0] == "0":
                appendingstring = "oh" + normal[secondpart[1]]
            elif secondpart[0] == "1":
                appendingstring = teen_case[secondpart[1]]
            else:
                appendingstring  = ty_case[secondpart[0]] + normal[secondpart[1]]

            result = "It's " + firstime + " " + appendingstring  + " " + timestamp
            return result
            
                
            
            
            #TODO: Write code below to return a string with the solution to the prompt.
            pass

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()
        
