from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_message_says_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_message_says_higher():
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_single_digit_guess_is_too_low():
    # 9 > 50 as strings, so a text comparison would wrongly say "Too High"
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low"

def test_guess_100_is_too_high():
    outcome, _ = check_guess(100, 50)
    assert outcome == "Too High"

def test_update_score_first_try_win():
    assert update_score(0, "Win", 1) == 100
