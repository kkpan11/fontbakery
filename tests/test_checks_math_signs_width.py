from fontbakery.status import WARN
from fontbakery.codetesting import (
    assert_PASS,
    assert_results_contain,
    CheckTester,
    TEST_FILE,
)


def test_check_math_signs_width():
    """Check font math signs have the same width."""
    check = CheckTester("math_signs_width")

    # The STIXTwo family was the reference font project
    # that we used to come up with the initial list of math glyphs
    # that should ideally have the same width.
    font = TEST_FILE("stixtwomath/STIXTwoMath-Regular.ttf")
    assert_PASS(check(font))

    # In our reference Montserrat Regular, the logicalnot
    # (also known as negation sign) '¬' has a width of 555 while
    # all other 12 math glyphs have width = 494.
    font = TEST_FILE("montserrat/Montserrat-Regular.ttf")
    assert_results_contain(check(font), WARN, "width-outliers")