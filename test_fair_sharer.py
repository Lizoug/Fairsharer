import fair_sharer

# import could not worked as i wished to

def test_fair_sharer():
    assert fair_sharer.fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]
    assert fair_sharer.fair_sharer([0, 0, 0, 1000], 2) == [180, 0, 180, 640]
    assert fair_sharer.fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]
    assert fair_sharer.fair_sharer([0, 0, 0, 1000], 2) == [190, 0, 190, 720]
    assert fair_sharer.fair_sharer([0, 100, 200, 300], 3) == [50, 200, 300, 250]
    assert fair_sharer.fair_sharer([0, 1000, 1000, 0], 1) == [100, 900, 900, 100]
    assert fair_sharer.fair_sharer([0, 1000, 1000, 1000], 2) == [200, 800, 1000, 800]
    
    # Additional test cases
    input_data = [1, 2, 3, 4]
    expected_output = [1, 2, 3, 4]
    num_iterations = 0
    assert fair_sharer(input_data, num_iterations) == expected_output

test_fair_sharer()
