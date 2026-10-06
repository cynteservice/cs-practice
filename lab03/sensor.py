threshold = float(input('ddtlbnt '))
n = int(input())
records = []

max_record, errors, threshold_crosses = 0,0,0
fea = 0

for i in range(n):
    r = input()
    if r!='error':
        value = float(r)
        records.append(float(r))
        if value>threshold:
            threshold_crosses += 1
    else:
        errors += 1

if len(records)==0:
    max_records = 0
else :
    max_record = max(records)
print(n)
print(errors)
print(threshold_crosses)
print(f"{max_record:.1f}")

if len(records)!=0:
    print(f"{sum(records)/len(records):.1f}")
else:
    print(False)
