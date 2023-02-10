from fair_sharer import fair_sharer

# import could not worked as i wished to

def test_fair_sharer():
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]
    assert fair_sharer([0, 0, 0, 1000], 2) == [180, 0, 180, 640]
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]
    assert fair_sharer([0, 100, 200, 300], 3) == [54, 125, 204, 217]
    assert fair_sharer([0, 1000, 1000, 0], 1) == [100, 800, 1100, 0]
    assert fair_sharer([0, 1000, 1000, 1000], 2) == [100, 910, 880, 1110]
    
    result = fair_sharer([0, 1000, 800, 0], 1)
    assert max(result) == 900

test_fair_sharer()
