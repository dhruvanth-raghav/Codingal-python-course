class PairElements:
    def __init__(self, numbers_list):
        self.numbers_list= numbers_list
        self.target = int(input("Enter the sum of 2 nums that you want to look for:"))

    def find_elements(self):
        lookup={}        
        for index, number in enumerate(self.numbers_list):
            if self.target - number in lookup:
                return(lookup[self.target-number], index)

            lookup[number]=index   

        return False, False    

    def answer(self):
        print(f"The 2 nums that add up to {self.target} are ")
        index1, index2=self.find_elements()
        if not index1 and not index2:
            print("Sorry.. No 2 numbers add up to the target!")
        else:
            print(self.numbers_list[index1])
            print(self.numbers_list[index2])





#==================================================================================
number_list=[3,5,1,7,10,2]
two_sum=PairElements(number_list)
two_sum.answer()