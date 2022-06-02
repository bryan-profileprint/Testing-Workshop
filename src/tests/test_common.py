from src.common import sum_two, mult_two


# Step 1: Use asserts to check that the function works
assert sum_two(50, 100) == 150 
assert sum_two(20, 51) == 71 
assert sum_two(-20, -51) == -71 
assert sum_two(0, 0) == 0 
assert sum_two(5, 0) == 5
assert sum_two(0, 10) == 10
assert sum_two(-10, 10) == 0
assert sum_two(-51, 20) == -31

# Step 2: Use pytest
def test_sum_two__both_positive_1():
    assert sum_two(50, 100) == 150 

def test_sum_two__both_positive_2():
    assert sum_two(20, 51) == 71 

def test_sum_two__both_negatives():
    assert sum_two(-20, -51) == -71 

def test_sum_two__both_zeroes():
    assert sum_two(0, 0) == 0 

def test_sum_two__positive_and_zero():
    assert sum_two(5, 0) == 5

def test_sum_two__positive_negative():
    assert sum_two(-10, 10) == 0

# mult-two
def test_mult_two__both_positive_1():
    assert mult_two(50, 100) == 5000 

def test_mult_two__both_positive_2():
    assert mult_two(20, 51) == 1020 

def test_mult_two__both_negatives():
    assert mult_two(-20, -51) == 1020 

def test_mult_two__both_zeroes():
    assert mult_two(0, 0) == 0 

def test_mult_two__positive_and_zero():
    assert mult_two(5, 0) == 0

def test_mult_two__positive_negative():
    assert mult_two(-10, 10) == -100


# Step 3: TestSuite
class TestSumTwo:
    def test_both_positive_1(self):
        assert sum_two(50, 100) == 150 

    def test_both_positive_2(self):
        assert sum_two(20, 51) == 71 

    def test_both_negatives(self):
        assert sum_two(-20, -51) == -71 

    def test_both_zeroes(self):
        assert sum_two(0, 0) == 0 

    def test_positive_and_zero(self):
        assert sum_two(5, 0) == 5

    def test_positive_negative(self):
        assert sum_two(-10, 10) == 0


class TestMultTwo:
    def test_both_positive_1(self):
        assert mult_two(50, 100) == 5000 

    def test_both_positive_2(self):
        assert mult_two(20, 51) == 1020 

    def test_both_negatives(self):
        assert mult_two(-20, -51) == 1020 

    def test_both_zeroes(self):
        assert mult_two(0, 0) == 0

    def test_positive_and_zero(self):
        assert mult_two(5, 0) == 0

    def test_positive_negative(self):
        assert mult_two(-10, 10) == -100
