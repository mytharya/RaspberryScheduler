num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
num_dict = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}

class conversion:

    def number2roman(num):

        roman = ''
        
        while num > 0:
            for i, r in num_map:
                while num >= i:
                    roman += r
                    num -= i
        return roman
    
    def roman2number(num):

        number = 0
        i = 0
        
        #varianta 1
        while i < len(num):
            pair = num[i:i+2]
            single = num[i]
            if pair in num_dict.keys():
                #  print('Pair found: ', pair, ':', num_dict[pair])
                 number = number + num_dict[pair]
                 i = i + 1
            else:
                # print('Single found: ', single, ':', num_dict[single])
                number = number + num_dict[single]
            i = i + 1
        return number
        
        #varianta 2
        # while len(num) > 0:
        #     for i, r in num_map:
        #         twol = num[:2]
        #         if twol == r:
        #             twol = num[:2]
        #             num = num[2:]
        #             number += i
        #         else:
        #             twol = num[:1]
        #             if twol == r:
        #                 num = num[1:]
        #                 number += i
        # return number
        
        #print(len(num))
        #print(range(len(num)))

# test 
# print(conversion.number2roman(2018))
print('2018 = ',conversion.roman2number('MMXVIII')) #2018
print('1994 = ',conversion.roman2number('MCMXCIV')) #1994
print('1924 = ',conversion.roman2number('MCMXXIV')) #1924
print('1669 = ',conversion.roman2number('MDCLXIX')) #1669
print('1487 = ',conversion.roman2number('MCDLXXXVII')) #1487
print('1199 = ',conversion.roman2number('MCXCIX')) #1199
print('2501 = ',conversion.roman2number('MMDI')) #2501
print('941 = ',conversion.roman2number('CMXLI')) #941
