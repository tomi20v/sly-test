from decimal import Decimal

def to_json_serializable(row):
    """
    Converts non-serializable types in a single dictionary (row) to JSON-serializable formats.
    """
    if not isinstance(row, dict):
        return row

    new_row = row.copy()
    for k, v in new_row.items():
        if isinstance(v, Decimal):
            new_row[k] = float(v)
    return new_row

def to_json_serializable_array(rows):
    """
    Iterates over a list of dictionaries (rows) and converts non-serializable
    types to JSON-serializable formats using to_json_serializable.
    """
    if not isinstance(rows, list):
        return rows

    return [to_json_serializable(r) for r in rows]
