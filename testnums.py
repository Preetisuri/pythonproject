num = int(input('Enter a value between 1-1000 : '))
print('You entered %d' %num)
numval=''
numdict = {
    0:"",
    1:"ONE",
    2:"TWO",
    3:"THREE",
    4:"FOUR",
    5:"FIVE",
    6:"SIX",
    7:"SEVEN",
    8:"EIGHT",
    9:"NINE",
    10:"TEN",
    11:"ELEVEN",
    12:"TWELVE",
    13:"THIRTEEN",
    14:"FOURTEEN",
    15:"FIFTEEN",
    16:"SIXTEEN",
    17:"SEVENTEEN",
    18:"EIGHTEEN",
    19:"NINETEEN",
    20:"TWENTY",
    30:"THIRTY",
    40:"FORTY",
    50:"FIFTY",
    60:"SIXTY",
    70:"SEVENTY",
    80:"EIGHTY",
    90:"NINETY",
    100:"HUNDERED"
    }
if(num>0):
    temp=num%100
    if(temp<20):
        numval=numdict.get(temp)
    else:
        temp=num%10
        numval=numdict.get(temp)
        num-=temp
        temp=num%100
        numval=numdict.get(temp)+numval
    num-=temp
if(num>100):
    num/=100
    if(numval):
        numval=numdict.get(num)+" HUNDERED AND "+numval
    else:
        numval=numdict.get(num)+" HUNDERED"
print(numval)
