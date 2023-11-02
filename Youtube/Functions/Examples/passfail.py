def pass_or_fail(score):
    if(score>=35):
        print("Pass")
    else:
        print("Fail")

score = int(input("Marks:"))
pass_or_fail(score)