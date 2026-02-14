from utils.distances import euclidean

def test_euclidean():
    # Basit bir test: [0,0] ile [3,4] arası mesafe 5 olmalı
    assert euclidean([0, 0], [3, 4]) == 5.0
