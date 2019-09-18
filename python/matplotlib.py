#
# This is one of my favorite styles
#
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = 14,7
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['figure.facecolor'] = 'white'


#
# Percentage formatter
#
import matplotlib.ticker as ticker
ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))


#
# Ridgeline plot
# 
# This assumes the rows are temporal, specifically "semiday" in this case,
# and there is more than one column defined by "treatment" in this case.
# The histogram data comes from df[value].
#
import seaborn as sns
def ridgeline(df, value, clip=None):
    with sns.plotting_context('notebook') as c:
        sns.set(context=c, style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

        # Initialize the FacetGrid object
        pal = sns.cubehelix_palette(60, rot=-.25, light=.7)
        g = sns.FacetGrid(df, row="semiday", col='treatment', hue="semiday",
                          aspect=15, height=.5, palette=pal,
                          margin_titles=True)

        # Draw the densities in a few steps
        g.map(sns.kdeplot, value, clip_on=False, shade=True, alpha=1, lw=1.5,
              bw=.05, clip=clip)
        g.map(sns.kdeplot, value, clip_on=False, color="w", lw=2,
              bw=.05, clip=clip)
        g.map(plt.axhline, y=0, lw=2, clip_on=False)
        g.map(plt.axvline, x=1, lw=2, clip_on=False, ls='--', color='k', alpha=0.7)


        # Define and use a simple function to label the plot in axes coordinates
        def label(x, color, label):
            ax = plt.gca()
            s = x.max().strftime('%Y-%m-%dT%H')
            ax.text(0, .2, s, fontweight="bold", color=color,
                    ha="left", va="center", transform=ax.transAxes)


        g.map(label, "semiday")

        # Set the subplots to overlap
        g.fig.subplots_adjust(hspace=-.65)

        # Remove axes details that don't play well with overlap
        g.set_titles(row_template="", template="")
        g.set(yticks=[])
        g.axes[-1,0].set_xlabel(value)
        g.axes[-1,1].set_xlabel(value)
        g.despine(bottom=True, left=True)
        return g
