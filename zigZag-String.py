# leet code problem --> https://leetcode.com/problems/zigzag-conversion/
#  Zigzag Conversion -- question
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000


class Solution:


    def sizeFORzigzag(self, str, rows):

        # size of list for the string-zigzag
        l = len(str)
        sum=0               # to track string accumulation in while loop
        diag = "False"
        num_cols = 0

        # returns the size of 2-D list for the zig-zag pattern
        while sum<l:

            if diag == "False":       # for non-diagonal
                num_cols+=1
                sum += rows
                diag = "True"

            elif (l-sum)<rows-2 and diag == "True":    # applicable for last row(# char left less than diagonal size)
                num_cols+=l-sum # num characters equals number of columns left
                sum+=(l-sum)

            else:                                       # for standard diagnols
                num_cols+=rows-2
                sum+=rows-2
                diag = "False"


        return num_cols


    def convert(self, s: str, numRows: int) -> str:
        self.strSeq = s
        self.num_rows = numRows
        l = len(self.strSeq)
        p=l
        num_cols = self.sizeFORzigzag(self.strSeq,self.num_rows)

        # initialize an empty list to save this
        empty_list = [[0 for _ in range(num_cols)] for _ in range(self.num_rows)]

        diag = False

        for j in range(num_cols):

            for i in range(self.num_rows):
                # this loop can help us populate all the cells of the matrix
                if diag == False and l!=0:
                    empty_list[i][j] = self.strSeq[p-l]
                    #empty_list[i][j] = self.strSeq[l-1]
                    l-=1  # decrement the total
                    if i==(self.num_rows-1): # checks if last row is populated | we need to switch to filling diagonals
                        diag = True
                        break

                if diag == True and l!=0:
                    if (i+j)%(self.num_rows - 1)==0: # this is the condition for diagonal
                        empty_list[i][j]=self.strSeq[p-l]
                        #empty_list[i][j] = self.strSeq[l-1]
                        l-=1
                        if i == 1:      # switch back filling rows
                            diag = False
                            break
                    else:
                        pass
        

        strList2ret = []

        for i in range(self.num_rows):
            for j in range(num_cols):
                if empty_list[i][j] != 0:
                    strList2ret.append(f"{empty_list[i][j]}")

        result = ''.join(strList2ret)

        return result