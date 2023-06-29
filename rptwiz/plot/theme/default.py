"""Tema inspirado em https://flatuicolors.com/palette/defo."""

colors = dict(
    primary='#2980b9',
    secondary='#8e44ad',
    positive='#16a085',
    negative='#c0392b',
    alternative='#f39c12',
    black='#2c3e50',
    white='#ecf0f1',
    grey='#bdc3c7',
    edge=None,
    face='#ecf0f1',
)

title = dict(
    x=0.02,
    ha='left'
)

subtitle = dict(
    loc='right', fontdict=dict(fontsize='small')
)

barh1 = dict(
    color=colors['primary'],
    edgecolor=colors['edge']
)

barh_labels = dict(
    horizontalalignment='left',
    verticalalignment='center',
    color=colors['black'])

line_grid = dict(
    visible=True,
    which='major',
    axis='both',
    color=colors['grey'],
    alpha=0.5
)