class Company:
    def __init__(self):
        self.__companyName = "Google"

    def dis(self):
        print(self.__companyName)

c1 = Company()
# print(c1.companyName)
c1.dis()

# If we are giving __ This it throws error
# bcaz Whenever We give __ this it Goes to private
# To access this use method