# Dust

A lightweight data analysis DSL for Python, built on NumPy.

## What is Dust?

Dust lets you analyze CSV data using a clean pipeline syntax instead of verbose pandas code.

## Example

```python
import dust as dst

df = dst.DDF('sales.csv')

# Total revenue
total = df['Revenue'] >> dst.Sum()

# Filter and sum
alice_total = dst.Filter(df, df['Salesman'] == 'Alice')['Premium'] >> dst.Sum()
```

## Operations
- `Sum`, `Avg`, `Min`, `Max`, `Count`
- `Filter` with boolean conditions (`==`, `>`, `<`, `>=`, `<=`, `!=`)
- Auto type inference and NaN handling
