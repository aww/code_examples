# Use a Pandas option context to temporarily allow an unlimited number of rows and columns
# to be displayed in a notebook
with pd.option_context('display.max_rows', 999, 'display.max_columns', 99,
                       'large_repr', 'info'):
  display(df)


# You can format the display of DataFrames in many ways
# Here we make a colormap from a matrix of values
import seaborn as sns
cm = sns.light_palette("blue", as_cmap=True)
mtx = df.grouby(['a', 'b']).size().unstack().fillna(0)  # Count rows by categories 'a' and 'b'
mtx = mtx.style.background_gradient(cmap=cm)
display(mtx)
