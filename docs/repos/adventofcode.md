# adventofcode

[View on GitHub](https://github.com/msashish/adventofcode)

---

Solve problems from https://adventofcode.com/2019/ and some problems elsewhere

    Day wise solutions in python
    Automatic test runs on Travis-ci at https://travis-ci.org/dashboard/builds

Steps: For problem, invoke as:

    If you are using unittest, then methods should start with test_ else unittest wont run    
    source venv/bin/activate
    python -m unittest run tests/test_solutions.py
    python -m unittest run tests/test_staircase.py
    python -m unittest run tests/test_array_addition.py
    
Steps: For exploring click - hello.py, jello.py

    python hello.py
    python hello.py --count=5 --name='Nature'
    python jello.py jello
    python jello.py hello
    python jello.py hello --count=3 --name='Abcd'
    
Steps: For exploring forking - fork_me.py, fork_new.py
    
    python fork_me.py
    python sample.py --name="who"
    python fork_new.py trigger -- python sample.py --name="who"
    -- after creating setup.py
        pip install --editable .
        fork_new -- python sample.py --name="who"

    