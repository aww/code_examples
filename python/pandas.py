# Use a Pandas option context to temporarily allow an unlimited number of rows and columns
# to be displayed in a notebook
with pd.option_context('display.max_rows', 999, 'display.max_columns', 99,
                       'large_repr', 'info'):
  display(df)
