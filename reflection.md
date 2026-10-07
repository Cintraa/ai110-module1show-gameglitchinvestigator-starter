# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The first time I ran the game it looked normal, it opened on my browser and i could navigate between the difficulties, click buttons etc.  The first bug was on the hints pointed the wrong way, it told me to go lower when I was already below the secret, and the same guess could get opposite hints on back-to-back turns. After I won, the New Game button didn't even work. Last bug was when game said I had 7 attempts left before I had guessed at all, and the sidebar says 8 were allowed.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location |
| ----- | ----------------- | --------------- | ---------------------- | ----------------------- |
| Secret 50, guess 60 | Hint "📉 Go LOWER!" because 60 is above the secret | Hint "📈 Go HIGHER!" | none | app.py, `check_guess()`: the `guess > secret` branch returns the "Go HIGHER" message, so the hint messages are swapped |
| Secret 50, submit 9 twice in a row | Same hint both times (go higher) | 1st: "📈 Go HIGHER!", 2nd: "📉 Go LOWER!" | none | app.py, submit block: `if st.session_state.attempts % 2 == 0: secret = str(st.session_state.secret)` turns the secret into a string on even attempts, so `check_guess()` falls into `except TypeError` and compares text ("9" > "50" is True) |
| Win a game, then click "New Game 🔁" | Fresh game: new secret in the difficulty's range; score, attempts and history reset; guessing allowed | "You already won. Start a new game to play again." stays and guesses are blocked | none | app.py, `if new_game:` block: resets only `attempts` (to 0) and `secret` (always `random.randint(1, 100)`); `status`, `score` and `history` are never reset, so `st.stop()` still runs |
| Start a fresh game on Normal (8 attempts allowed) | "Attempts left: 8"; a first-guess win worth 100 points | "Attempts left: 7"; a first-guess win worth 90 points | none | app.py, session-state setup: `st.session_state.attempts = 1` should be 0, so `update_score()` sees attempt 2 on the first guess |

**Pre-fix play trace (Normal difficulty)**

```
Sidebar: Range 1 to 100, Attempts allowed: 8
Start:   info bar shows "Attempts left: 7"        <- should be 8
Debug:   Secret = 50
Guess 9  -> "📈 Go HIGHER!"
Guess 9  -> "📉 Go LOWER!"                        <- same guess, opposite hint
Guess 60 -> "📈 Go HIGHER!"                       <- secret is lower
Guess 50 -> balloons, "You won! The secret was 50. Final score: 45"
Click New Game -> debug panel shows a new secret, but
                  "You already won. Start a new game to play again." stays
                  and new guesses are blocked
```

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude, Gemini
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

I put "hint shows the secret" as a bug and Claude said it wasn't a real bug because the secret only appears in the Developer Debug Info expander, not in the hint from check_guess(). I verified it and it was correct

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

Claude wrote a play trace using secret 50, but my real secret was 40, so I rejected it as fake evidence. I replayed the game and rewrote the trace with what my screen actually showed.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided the bug was fixed only when its pytest case passed and replaying my Phase 1 inputs no longer reproduced it.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

test_numeric_not_text_comparison checks that a guess of 9 against a secret of 50 returns "Too Low"; the old string comparison ("9" > "50") would fail it, and it passes now.

- Did AI help you design or understand any tests? How?

Claude Code wrote the new tests from my bug table, and I updated the starter tests to unpack check_guess's (outcome, message) tuple.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
