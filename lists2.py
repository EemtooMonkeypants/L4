import random
marks = []
Failures = []
StillFailures = []
Average = []
count = 0
while count <=19:
    inputs = random.randint(1,100)
    marks.append(inputs)
    count +=1
for mark in marks:
    if mark <=30:
        Failures.append(mark)
    if mark >=31 and mark <=69:
        StillFailures.append(mark)
    if mark >=70:
        Average.append(mark)
print(Failures)
print(StillFailures)
print(Average)