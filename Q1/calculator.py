class calculator:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
    def addition(self):
        answer = self.input1 + self.input2
        return answer
    def subtraction(self):
        answer = self.input1 - self.input2
        return answer
    def multiplication(self):
        answer = self.input1 * self.input2
        return answer
    def divison(self):
        answer = self.input1 / self.input2
        return answer
input1 = int(input("Enter Input 1: "))
input2 = int(input("Enter Input 2: "))
output = calculator(input1, input2)
option = int(input("Choose the operation: 1.Add 2.Sub 3.Multiply 4.Divide\n"))
if option == 1:
    print(output.addition())
elif option == 2:
    print(output.subtraction())
elif option == 3:
    print(output.multiplication())
elif option == 4:
    print(output.divison())
else:
    print("Choose an operation")