# SpinorRep

A small Python utility for constructing binary matrix representations of spinors subject to a set of combinatorial constraints. Given the matrix dimensions, per-column sum limits, allowed per-row sums, and a maximum allowed overlap between any two rows, `SpinorRep` searches for a valid configuration by random column permutation with rejection sampling.

## Authors

Niren Bhoja & Harry Wells

## Requirements

- Python 3.8+
- NumPy

### Constructor parameters

| Parameter         | Type      | Description                                                                 |
|-------------------|-----------|-----------------------------------------------------------------------------|
| `num_rows`        | `int`     | Number of rows `N` in the table.                                            |
| `num_cols`        | `int`     | Number of columns `M` in the table.                                         |
| `col_sum_limit`   | `list[int]` of length `M` | Maximum number of `1`s allowed in each column.              |
| `row_sum_list`    | `list[int]` | Allowed values for the per-row sum. A solution row's sum must lie in this list. |
| `row_match_limit` | `int`     | Maximum number of matching positions allowed between any two rows.          |

### Methods

- **`permute_columns()`** — Randomly permutes the entries within each column of the working table.
- **`is_valid_rows()`** — Returns `True` if every row sum is in `row_sum_list`.
- **`is_matching_rows()`** — Returns `True` if no pair of rows shares more than `row_match_limit` matching entries.
- **`compute_solution()`** — Repeatedly permutes until a valid configuration is found, then assembles and prints the final table.

## Working example

```python
problem = SpinorRep(
    num_rows=6,
    num_cols=8,
    col_sum_limit=[5, 3, 3, 3, 3, 3, 3, 3],
    row_sum_list=[4, 2, 0],
    row_match_limit=6,
)
problem.compute_solution()
```

Output is a `numpy` array of shape `(num_rows, num_cols)` printed to stdout, along with the iteration counter showing how many permutation attempts were tried before convergence.

## Applications
While developed for a problem in pure mathematics, the underlying constraint structure is domain-agnostic. Below is an example framed as combinatorial software testing
```python
# -------------------------------------------------------
# Application Example: Combinatorial Feature-Flag Testing
# -------------------------------------------------------
#
# Scenario: You are testing a system with 5 binary feature
# flags (A, B, C, D, E). You want to design a minimal set
# of test cases such that:
#
#   - One baseline test has all 5 flags enabled           [all-ones row, always included]
#   - Each flag is active in at most 3 non-baseline tests  [col_sum_limit]
#   - Each non-baseline test activates exactly 2 or 3 flags [row_sum_list]
#   - No two tests agree on more than 3 flag settings,
#     ensuring sufficient coverage diversity              [row_match_limit]
#
# The output matrix H has shape (num_rows x num_cols):
#   - H[i][j] = 1  →  flag j is ON  in test case i
#   - H[i][j] = 0  →  flag j is OFF in test case i
#   - Row 0 is always the all-on baseline test case

problem = SpinorRep(
    num_rows=5,         # 4 non-baseline tests + 1 all-on baseline
    num_cols=5,         # 5 feature flags
    col_sum_limit=[3, 3, 3, 3, 3],  # each flag on in ≤3 non-baseline tests
    row_sum_list=[2, 3],            # each test activates 2 or 3 flags
    row_match_limit=4,              # any two tests agree on ≤3 settings
                                    # (i.e. differ in at least 2 positions)
)
problem.compute_solution()

# Example output:
#
#        A  B  C  D  E
# Test 0: [1, 1, 1, 1, 1]  <- baseline: all flags on
# Test 1: [1, 0, 1, 0, 1]
# Test 2: [0, 1, 0, 1, 1]
# Test 3: [1, 1, 0, 0, 0]
# Test 4: [0, 0, 1, 1, 0]
```
