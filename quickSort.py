class InsertSortIt:

  def __init__(self, nums):
        self.num2sort = nums
        print("num to sort",self.num2sort)

  def InsertitionSort(self):

    l = len(self.num2sort)
    counter = 1
    while counter < l:

      key = self.num2sort[counter]

      for i in range(counter,0,-1):

        if key>self.num2sort[i-1]:
          break


        else:
          self.num2sort[i-1], self.num2sort[i] = self.num2sort[i], self.num2sort[i-1]

      counter+=1


    return self.num2sort