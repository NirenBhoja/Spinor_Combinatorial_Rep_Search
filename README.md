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
