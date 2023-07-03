"""
Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:
 
      235
    +  52
    -----

Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should
optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Example
Function Call:
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

Output:
       32      3801      45      123
    + 698    -    2    + 43    +  49
    -----    ------    ----    -----

Function Call:
    arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

Output:
      32         1      9999      523
    +  8    - 3801    + 9999    -  49
    ----    ------    ------    -----
      40     -3800     19998      474

Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is
meaningful to the user.

Situations that will return an error:
    - If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
    - The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned
      in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
    - Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
    - Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:
      Error: Numbers cannot be more than four digits.
If the user supplied the correct format of problems, the conversion you return will follow these rules:
    - There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both
      operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
    - Numbers should be right-aligned.
    - There should be four spaces between each problem.
    - There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. 
      (The example above shows what this should look like.)
"""

import re

def arithmetic_arranger(problems, display=False):
    
    operators=[]
    operands=[]
    results=[]
    maxLength=[]
    arranged_problems=''
    arranged_list=[]
    arranged_str=''

    for item in problems:
        # Checking if input formatting is correct
        if len(problems)>5:
            print('Error: Too many problems.')
            return 'Error: Too many problems.'
        if bool(re.search(' *[\+-] *',item.strip()))==False:
            print('Error: Operator must be \'+\' or \'-\'.')
            return 'Error: Operator must be \'+\' or \'-\'.'
        if bool(re.search('^[0-9]+ *[\+-]',item.strip()))==False or bool(re.search('[\+-] *[0-9]+$',item.strip()))==False:
            print('Error: Numbers must only contain digits.')
            return 'Error: Numbers must only contain digits.'
        if bool(re.search('^[0-9]{1,4} *[\+-]',item.strip()))==False or bool(re.search('[\+-] *[0-9]{1,4}$',item.strip()))==False:
            print('Error: Numbers cannot be more than four digits.')
            return 'Error: Numbers cannot be more than four digits.'
        if bool(re.search('^[0-9]{1,4} *[+-] *[0-9]{1,4}$',item.strip()))==False:
            print('Error: Wrong input.')
            return 'Error: Wrong input'
        
        #Set up operands, operators, results and their max length
        operands.append(re.split('[\+-]',item))
        if bool(re.search('\+',item)):
            operators.append('add')
        else:
            operators.append('substract')

    for i in range(len(problems)):
        operands[i][0]=int(operands[i][0].strip())
        operands[i][1]=int(operands[i][1].strip())
    
    for i in range(len(problems)):
        if operators[i]=='add':
            results.append((operands[i][0])+(operands[i][1]))
        else:
            results.append((operands[i][0])-(operands[i][1]))

    for i in range(len(problems)):
        #maxLength.append(len(str(max(abs(operands[i][0]),abs(operands[i][1]),abs(results[i])))))
        maxLength.append(len(str(max(abs(operands[i][0]),abs(operands[i][1])))))

    #Constructing returned string 1st line
    for i in range(len(problems)):
        if i!=len(problems)-1:
            arranged_problems=arranged_problems+' '*2+' '*(maxLength[i]-len(str(abs(operands[i][0]))))+str(operands[i][0])+' '*4
        else:
            arranged_problems=arranged_problems+' '*2+' '*(maxLength[i]-len(str(abs(operands[i][0]))))+str(operands[i][0])
    
    arranged_problems=arranged_problems+'\n'
    
    #Constructing returned string 2nd line
    for i in range(len(problems)):
        if operators[i]=='add':
            arranged_problems=arranged_problems+'+'
        else:
            arranged_problems=arranged_problems+'-'
        if i!=len(problems)-1:
            arranged_problems=arranged_problems+' '+' '*(maxLength[i]-len(str(abs(operands[i][1]))))+str(operands[i][1])+' '*4
        else:
            arranged_problems=arranged_problems+' '+' '*(maxLength[i]-len(str(abs(operands[i][1]))))+str(operands[i][1])

    arranged_problems=arranged_problems+'\n'

    #Constructing returned string 3rd line
    for i in range(len(problems)):
        if i!=len(problems)-1:
            arranged_problems=arranged_problems+'--'+'-'*maxLength[i]+' '*4
        else:
            arranged_problems=arranged_problems+'--'+'-'*maxLength[i]
    
    #Constructing returned string 4th line
    if display==True:
        arranged_problems=arranged_problems+'\n'
        for i in range(len(problems)):
            if results[i]>=0:
                if i!=len(problems)-1:
                    #arranged_problems=arranged_problems+' '*2+' '*(maxLength[i]-len(str(abs(results[i]))))+str(results[i])+' '*4
                    arranged_problems=arranged_problems+' '*(2-len(str(abs(results[i])))+maxLength[i])+str(results[i])+' '*4
                else:
                    #arranged_problems=arranged_problems+' '*2+' '*(maxLength[i]-len(str(abs(results[i]))))+str(results[i])
                    arranged_problems=arranged_problems+' '*(2-len(str(abs(results[i])))+maxLength[i])+str(results[i])
            else:
                if i!=len(problems)-1:
                    #arranged_problems=arranged_problems+' '+' '*(maxLength[i]-len(str(abs(results[i]))))+str(results[i])+' '*4 
                    arranged_problems=arranged_problems+' '*(1-len(str(abs(results[i])))+maxLength[i])+str(results[i])+' '*4
                else:
                    #arranged_problems=arranged_problems+' '+' '*(maxLength[i]-len(str(abs(results[i]))))+str(results[i])
                    arranged_problems=arranged_problems+' '*(1-len(str(abs(results[i])))+maxLength[i])+str(results[i])

    #Convert arranged_results into a code that would be needed to print it
    arranged_list=[*arranged_problems]
    for i in range(len(arranged_list)):
        if arranged_list[i]=='\n':
            arranged_list[i]='\\n'
        arranged_str=arranged_str+str(arranged_list[i])

    #print(operators)
    #print(operands)
    #print(results)
    #print(maxLength)
    print (arranged_problems+'\n')
    #print(arranged_list)
    print(arranged_str+'\n')

    return arranged_problems


#Testing
arithmetic_arranger(["3 + 855", "988 + 40"], True)
print('    3      988\n+ 855    +  40\n-----    -----\n  858     1028'+'\n')
print('    3      988\\n+ 855    +  40\\n-----    -----\\n  858     1028')