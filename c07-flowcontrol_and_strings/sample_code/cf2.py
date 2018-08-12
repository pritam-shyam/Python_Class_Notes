# NOTE: You would never see such logic in a "real" program. This example
# simply illustrates the evaluation of a expression. For any if, or elif
# the Boolean expression must evalution to True for the associated block
# of code to run.

if True:
  print(True)
else:
  print(False)

if (10 == 10) == True:
  print(True)
elif (10 == 10) == False:
  print(False)
else:
  print(False)
