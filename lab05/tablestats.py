def read_rows(lines):
    rows = []
    headers = []

    for data in lines:
        data = data.strip()
        if data=='': continue
        data = data.split(',')
        if len(data)==0: continue

        if len(headers)==0:
            headers = data
        else:
            if len(data)==len(headers):
                new_data = {}
                for i in range(0,len(headers)):
                    new_data[headers[i]] = data[i]

                rows.append(new_data)

    return rows

def count_types(rows):
    counts = {}

    for row in rows:
        kind = row["тип"]
        if kind not in counts:
            counts[kind] = 0
        counts[kind] += 1

    return counts


def total_minutes(rows, kind):
    total = 0.0

    for row in rows:
        if row["тип"] == kind:
            try:
                minutes = float(row["минуты"].replace(",", "."))
            except ValueError:
                continue
            total += minutes

    return round(total, 1)

def to_csv(counts: dict) -> str:
    result = "тип,количество\n"

    for kind in sorted(counts):
        result += kind + "," + str(counts[kind]) + "\n"

    return result

"""if __name__=='__main__':
    my_csv = [
    'дата,тип,минуты',
    '2026-03-01,запуск,1.5',
    '2026-03-03,проверка,2',
    '2026-03-03,выгрузка,11',
    '2026-03-03,проверка,2.49',
    ]"""
