from extract import extract_data
from transform import transform_data
from load import load_data


def main():
    """
    Punto de entrada principal del ETL.
    """
    raw = extract_data()
    transformed = transform_data(raw)
    load_data(transformed)


if __name__ == "__main__":
    main()
