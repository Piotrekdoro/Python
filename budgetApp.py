'''
Complete the Category class in budget.py. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment.
When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list. The class should
also contain the following methods:
    - A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to
      the ledger list in the form of {"amount": amount, "description": description}.
    - A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds,
      nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
    - A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    - A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to
      [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description
      "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should
      return True if the transfer took place, and False otherwise.
    - A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
      This method should be used by both the withdraw method and transfer method.

When the budget object is printed it should display:

    - A title line of 30 characters where the name of the category is centered in a line of * characters.
    - A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount.
      The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
    - A line displaying the category total.

Here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96

Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that
is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits.
Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down
to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should
be a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     

'''

import re
import inspect
import collections
import math

class Category:
    categoriesList=[]

    def __init__(self,name):
        self.name=name
        self.ledger=[]
        self.categoriesList.append(self)
    def __str__(self):
        returnStr=''
        #First line
        if len(self.name)%2==0:
            returnStr=returnStr+'*'*(15-int(len(self.name)/2))+self.name.capitalize()+'*'*(15-int(len(self.name)/2))+'\n'
        else:
            returnStr=returnStr+'*'*(14-int((len(self.name)-1)/2))+self.name.capitalize()+'*'*(15-int((len(self.name)-1)/2))+'\n'
        #All the other lines except for last one
        for i in range(len(self.ledger)):
            #Description
            if len(self.ledger[i]['description'])<=23:
                returnStr=returnStr+self.ledger[i]['description']
            else:
                returnStr=returnStr+''.join([*self.ledger[i]['description'][:23]])
            #Spaces
            if bool(re.search('\.[0-9]$',str(float(self.ledger[i]['amount'])))) and len(self.ledger[i]['description'])<=23:
                returnStr=returnStr+' '*(30-len(self.ledger[i]['description'])-len(str(float(self.ledger[i]['amount'])))-1)
            if bool(re.search('\.[0-9]$',str(float(self.ledger[i]['amount'])))) and len(self.ledger[i]['description'])>23:
                returnStr=returnStr+' '*(30-23-len(str(float(self.ledger[i]['amount'])))-1)
            if bool(re.search('\.[0-9]$',str(float(self.ledger[i]['amount']))))==False and len(self.ledger[i]['description'])<=23:
                returnStr=returnStr+' '*(30-len(self.ledger[i]['description'])-len(str(float(self.ledger[i]['amount']))))
            if bool(re.search('\.[0-9]$',str(float(self.ledger[i]['amount']))))==False and len(self.ledger[i]['description'])>23:
                returnStr=returnStr+' '*(30-23-len(str(float(self.ledger[i]['amount']))))
            #Amount
            if bool(re.search('\.[0-9]$',str(float(self.ledger[i]['amount'])))):
                returnStr=returnStr+str(float(self.ledger[i]['amount']))+'0\n'
            else:
                returnStr=returnStr+str(float(self.ledger[i]['amount']))+'\n'
        #Last line
        if bool(re.search('\.[0-9]$',str(float(self.get_balance())))):
            returnStr=returnStr+'Total: '+str(float(self.get_balance()))+'0\n'
        else:
            returnStr=returnStr+'Total: '+str(float(self.get_balance()))+'\n'
        returnStr=returnStr.rstrip('\n')
        return returnStr
            

    def deposit(self,amount,description=''):
        self.ledger.append({"amount": amount, "description": description})
    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    def get_balance(self):
        self.ledger
        balance=0
        for i in range(len(self.ledger)):
            balance=balance+self.ledger[i]['amount']
        return balance
    def transfer(self,amount,category):
        if self.withdraw(amount,'Transfer to '+category.name.capitalize()):
            category.deposit(amount,'Transfer from '+self.name.capitalize())
            return True
        else:
            return False
    def check_funds(self,amount):
        if amount>self.get_balance():
            return False
        else:
            return True



def create_spend_chart(*categories):
    #Title
    #print(locals()['categories'])
    chartStr='Percentage spent by category\n'
    #Calculating percentage spent for each category
    percentagesSpent=[]
    totalSpent=0
    labelLength=[]
    longestLabelLength=0
    for i in range(len(locals()['categories'])):
        spentInCategory=0
        for j in range(len(locals()['categories'][i].ledger)):
            if locals()['categories'][i].ledger[j]['amount']<0:
                spentInCategory=spentInCategory+abs(locals()['categories'][i].ledger[j]['amount'])
        percentagesSpent.append(spentInCategory)
        totalSpent=totalSpent+spentInCategory
    for i in range(len(percentagesSpent)):
        percentagesSpent[i]=int((percentagesSpent[i]/totalSpent)*10)*10
    #print(percentagesSpent)
    #Body of chart
    for i in range(10,-1,-1):
        #Spaces before y axis labels
        labelNumbersLength=len(str(i*10))
        if labelNumbersLength==2:
            chartStr=chartStr+' '
        elif labelNumbersLength==1:
            chartStr=chartStr+'  '
        #y axis numbers and y axis itself
        chartStr=chartStr+str(10*i)+'|'+' '
        #chart bars
        for j in range(len(percentagesSpent)):
            if percentagesSpent[j]<i*10:
                chartStr=chartStr+''*3
            else:
                chartStr=chartStr+'o'+' '*2
            #print('i: '+str(i)+'    '+'j: '+str(j))
        chartStr=chartStr+'\n'
    #x axis
    chartStr=chartStr+' '*4+'-'
    for i in range(len(percentagesSpent)):
        chartStr=chartStr+'-'*3
    chartStr=chartStr+'\n'
    #x axis labels
    #calculating max label length
    for i in range(len(locals()['categories'])):
        labelLength.append(len(locals()['categories'][i].name))
    longestLabelLength=max(labelLength)
    #print('Longest label: '+str(longestLabelLength))
    #printing labels themselves
    for i in range(longestLabelLength):
        for j in range(len(percentagesSpent)):
            #print(locals()['categories'][j].name[i]+'    i: '+str(i)+'    j: '+ str(j))
            chartStr=chartStr+' '*5
            #if labelLength[j]<i:
            try:
                chartStr=chartStr+locals()['categories'][j].name[i]+' '*2
            #else:
            except:
                chartStr=chartStr+' '*3
    
    
    
    print(chartStr)




foodCat=Category('food')
entertainmentCat=Category('entertainment')
businessCat=Category('business')

foodCat.deposit(900, "deposit")
entertainmentCat.deposit(900, "deposit")
businessCat.deposit(900, "deposit")

foodCat.withdraw(105.55)
entertainmentCat.withdraw(33.4)
businessCat.withdraw(10.99)

create_spend_chart(businessCat,foodCat,entertainmentCat)

print('\n\n')
print('Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ')
#Wrong order of arguments, right now they are drawn in order of instantiation and not in order in which they were called
#Copy the list of arguments and sort it
#Labels are wrong, make a list of them and try to pad them with spaces and just looping through them appending them to charStr