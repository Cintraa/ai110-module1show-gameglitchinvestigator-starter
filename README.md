# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
      A Streamlit number guessing game. Pick a difficulty, guess the secret number, and use the higher/lower hints to win in as few attempts as possible.
- [x] Detail which bugs you found.
      Hint messages were backwards: a guess above the secret said "Go HIGHER".
      The secret turned into text on every other attempt, so the same guess could get opposite hints.
      New Game didn't restart after a win or loss.
      Attempts started at 1, so Normal showed 7 attempts left instead of 8, and a first-try win scored 90.
- [x] Explain what fixes you applied.
      Moved get_range_for_difficulty, parse_guess, check_guess and update_score from app.py into logic_utils.py.
      Swapped the hint messages and removed the text-comparison fallback in check_guess.
      The secret is now always passed to check_guess as a number.
      Attempts start at 0, and New Game resets attempts, score, status, history and the secret, using the difficulty's range.
      Added 5 pytest cases for the fixes (8 total, all passing).

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Choose Normal. The game shows "Attempts left: 8". The secret is 50 (visible in Developer Debug Info
2. Enter 30. The game shows "📈 Go HIGHER!"
3. Enter 60. The game shows "📉 Go LOWER!"
4. Enter 50. Balloons appear, with "You won! The secret was 50. Final score: 70".
5. Click New Game. A fresh game starts with 8 attempts, and guessing works again.

## 🧪 Test Results

```
$ python -m pytest -q
........                                                                 [100%]
8 passed in 0.03s
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
