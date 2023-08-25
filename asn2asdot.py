import sys

def asplain_to_asdot(asplain):
    high_order = asplain >> 16
    low_order = asplain & 0xffff
    return f"{high_order}.{low_order}"

def asdot_to_asplain(asdot):
    high_order, low_order = map(int, asdot.split('.'))
    asplain = (high_order << 16) + low_order
    return asplain

def main():
    if len(sys.argv) != 2:
        print("Usage: python asn2asdot.py <ASN or ASDOT>")
        return

    input_value = sys.argv[1]

    try:
        if '.' in input_value:  # Check if input is in ASDOT notation
            result = asdot_to_asplain(input_value)
        else:  # Input is assumed to be in ASN format
            result = asplain_to_asdot(int(input_value))
        print(result)
    except ValueError:
        print("Invalid input. Please provide a valid ASN or ASDOT.")

if __name__ == "__main__":
    main()