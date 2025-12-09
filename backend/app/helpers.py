from decimal import Decimal

def to_json_serializable(rows):
    """
    Iterates over a list of dictionaries (rows) and converts non-serializable
    types to JSON-serializable formats. Returns a new list with the converted data.
    """
    # Create a new list containing shallow copies of the dictionaries
    new_rows = [r.copy() for r in rows]
    for r in new_rows:
        for k, v in r.items():
            if isinstance(v, Decimal):
                r[k] = float(v)
    return new_rows
