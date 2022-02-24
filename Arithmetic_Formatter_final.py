# arithmetic_arranger function accepts math problems in the form ['5 + 5'] and arranges them vertically

def arithmetic_arranger (problems , solve = False):
  
    #represents the first,second, sum and dashed line 
    first = ''
    second = ''
    lines = ''
    sumx = ''
    string = ''
   
   # Max length of problem
    if len(problems) > 5 :
        return 'Error: Too many problems.'

        # Breaks down each problem by splittin the values
    for problem in problems:
        problem = problem.split(" ")
        firstnum = problem[0]
        operation = problem[1]
        secondnum = problem[2]
        
        # Max Lenght of Digits and only accepta digit values
        if len(firstnum) > 4 or len(secondnum) > 4: 
            return 'Error: Numbers cannot be more than four digits.'
        if not firstnum.isnumeric() or not secondnum.isnumeric():
            return 'Error: Numbers must only contain digits.'
        
        # finds the sum
        sum = ''
        if operation == '+':
            sum = str(int(firstnum) + int(secondnum))
        elif operation == '-':
            sum = str(int(firstnum) - int(secondnum))  
        else:
          return "Error: Operator must be '+' or '-'." 

        # Spacing of the problems
        length = max( len(firstnum) , len(secondnum) ) + 2
        top = str(firstnum).rjust(length)
        bottom = operation + str(secondnum).rjust(length - 1)
        solution = sum.rjust(length)
        line = ''
        for s in range(length):
            line += '-'

        # Sets up the lines for the problem and spacing if there is multiple problems
        if problem != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumx += solution + '    '
        else: 
            first += top 
            second += bottom
            lines += line 
            sumx += solution
    # rstrip is used to remove white spacing from the lines
    if solve: 
        string = first.rstrip() + '\n' + second.rstrip() + '\n' + lines.rstrip() + '\n' + sumx.rstrip()
    else: 
        string = first.rstrip() + '\n' + second.rstrip() + '\n' + lines.rstrip() 
    return string

print(arithmetic_arranger(['5 + 5']))