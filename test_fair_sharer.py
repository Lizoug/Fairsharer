import fair_sharer

def test_fair_sharer():
    assert fair_sharer.fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]
    assert fair_sharer.fair_sharer([0, 0, 0, 1000], 2) == [180, 0, 180, 640]