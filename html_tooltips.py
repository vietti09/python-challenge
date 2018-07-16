import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use('tkinter')
import numpy as np
import pandas as pd
import mpld3
from mpld3 import plugins
import tkinter
from iex import stock

# # Define some CSS to control our custom labels
# css = """
# table
# {
#   border-collapse: collapse;
# }
# th
# {
#   color: #ffffff;
#   background-color: #000000;
# }
# td
# {
#   background-color: #cccccc;
# }
# table, th, td
# {
#   font-family:Arial, Helvetica, sans-serif;
#   border: 1px solid black;
#   text-align: right;
# }
# """
#
# fig, ax = plt.subplots()
# ax.grid(True, alpha=0.3)
#
# N = 50
# df = pd.DataFrame(index=range(N))
# df['x'] = np.random.randn(N)
# df['y'] = np.random.randn(N)
# df['z'] = np.random.randn(N)
#
# labels = []
# for i in range(N):
#     label = df.ix[[i], :].T
#     label.columns = ['Row {0}'.format(i)]
#     # .to_html() is unicode; so make leading 'u' go away with str()
#     labels.append(str(label.to_html()))
#
# points = ax.plot(df.x, df.y, 'o', color='b',
#                  mec='k', ms=15, mew=1, alpha=.6)
#
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_title('HTML tooltips', size=20)
#
# tooltip = plugins.PointHTMLTooltip(points[0], labels,
#                                    voffset=10, hoffset=10, css=css)
# plugins.connect(fig, tooltip)
#
# mpld3.show()
#
#
# np.random.seed(9615)

# generate df

df1 = stock("AAPL").chart_table(range='1m')
df2 = stock("AAPL").chart_table(range='1y')
df3 = stock("AAPL").chart_table(range='2y')
df4 = stock("AAPL").chart_table(range='5y')
df1 = df1.to_list()
df = pd.Series(df1).to_json(orient='values')

# plot line + confidence interval
fig, ax = plt.subplots()
ax.grid(True, alpha=0.3)

for key, val in df.iteritems():
    l, = ax.plot(val.index, val.values, label=key)
    ax.fill_between(val.index,
                    1, 3,
                    color=l.get_color(), alpha=.4)

# define interactive legend

handles, labels = ax.get_legend_handles_labels() # return lines and labels
interactive_legend = plugins.InteractiveLegendPlugin(zip(handles,
                                                         ax.collections),
                                                     labels,
                                                     alpha_unsel=0.5,
                                                     alpha_over=1.5,
                                                     start_visible=True)
plugins.connect(fig, interactive_legend)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Interactive legend', size=20)

mpld3.show()
