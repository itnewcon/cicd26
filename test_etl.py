from etl import transform

def test_transform():
    data = [1, 2, 3]
    result = transform(data)
    assert result == [2, 4, 6]