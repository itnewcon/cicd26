def extract_data():
    print("Extracting data")


def transform_data():
    print("Transforming data")


def load_data():
    print("Loading data")

def transform(data):
    print("Transforming data")
    return [value * 2 for value in data]
    
if __name__ == "__main__":
    extract_data()
    transform_data()
    load_data()

    