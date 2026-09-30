threshold = float(input())
n = int(input())
records = []

max_record, errors, threshold_crosses = 0,0,0

for i in range(n):
    r = input()
    if r!='error':
        value = float(r)
        records.append(float(r))
        if value>threshold:
            threshold_crosses += 1
    else:
        errors += 1

max_record = max(records)
print(n)
print(errors)
print(threshold_crosses)
print(f"{max_record:.1f}")
print(f"{sum(records)/len(records):.1f}")