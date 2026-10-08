from datetime import datetime, timedelta

def create_records(func, num_records: int, date: datetime = None) -> list:
    records = []
    if date == None:
        for i in range(num_records):
            record = func(i)
            records.append(record)
    else:
        for i in range(num_records):
            record = func(i, date)
            records.append(record)
            date = date + timedelta(minutes=5)
    return records