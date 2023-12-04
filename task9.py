#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
#You are given  scores.
#Store them in a list and find the score of the runner-up.

def runnerUp(n):
    d = [int(input()) for _ in range(n)]
    
    # now we will iterate through the array
    for i in range(len(d)-1):
       if d[i]>d[i+1]:
            first = d[i]
       else:
            first = d[i+1]
    d.pop(first)
       
    for i in range(len(d)-1):
       if d[i]>d[i+1]:
            rUP = d[i]
       else:
            rUP = d[i+1]
        
    print(rUP)


print(runnerUp(5))