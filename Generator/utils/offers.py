def get_id(existing_records: list, id_field: str):
    if existing_records == []:
        record_id = 1
    else:
        record_id = existing_records[-1][id_field] + 1
    return record_id