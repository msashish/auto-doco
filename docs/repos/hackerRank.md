# hackerRank

[View on GitHub](https://github.com/msashish/hackerRank)

---

##  Solving Problems

    Repo where we solve some problems from hacker rank and elsewhere...

### Repo structure

    /solutions  --> Has python modules having "problem statement" & solution code
    /tests      --> Has python test cases to verify /solutions
    /helper     --> Common utilities that can be shared

### Setting up env
    python -m venv .hacker
    source .hacker/bin/activate
    pip install -r requirements.txt
    
### basic git setup
    git init
    git add README.md
    git commit -m "......"
    git branch -M main
    git remote add origin https://github.com/msashish/hackerRank.git
    git push -u origin main
    
    
### Testing solutions automatically
    python -m unittest tests/test_plus_minus.py
    python -m unittest tests/test_diagonal_difference.py
    python -m unittest tests/test_stock_profit.py
    python -m unittest tests/test_present_absent.py
    python -m unittest tests/test_longest_subarray.py 
    
### Run all test cases
    python -m unittest discover tests
    
### Testing solutions manually
    python solutions/array_rotation.py
    python solutions/diagonal_difference.py
    python solutions/plus_minus.py