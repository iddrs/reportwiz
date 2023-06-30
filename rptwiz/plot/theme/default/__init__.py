from rptwiz.plot.theme.default import colors

title = dict(
    x=0.02,
    ha='left'
)

subtitle = dict(
    loc='right', fontdict=dict(fontsize='small')
)

barh1 = dict(
    color=colors.primary,
    edgecolor=colors.edge
)

barh_labels = dict(
    horizontalalignment='left',
    verticalalignment='center',
    color=colors.black)

line_grid = dict(
    visible=True,
    which='major',
    axis='both',
    color=colors.grey,
    alpha=0.5
)