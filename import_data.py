import pandas as pd
import matplotlib.cm as cm
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import plotly.graph_objects as go
from sklearn.preprocessing import  MinMaxScaler

df = pd.read_excel('cleaned_seifa.xlsx')

print(df['Index of Relative Socio-economic Disadvantage'].values)
df = df.replace('-', np.NaN, regex=True)
# s = [s**(1/2) for s in df['Usual Resident Population']]
# s = [float(i)/sum(df['Usual Resident Population']) for i in df['Usual Resident Population']]
s = df['Usual Resident Population']
min_max_scaler = MinMaxScaler()
min_max_scaler.fit([s])
s = min_max_scaler.transform([s])
c = df['Index of Education and Occupation']
minima_c = min(c)
maxima_c = max(c)

norm = matplotlib.colors.Normalize(vmin=minima_c, vmax=maxima_c, clip=True)
mapper = cm.ScalarMappable(norm=norm, cmap=cm.summer)

# Data for a three-dimensional line
xdata = df['Index of Relative Socio-economic Disadvantage']
ydata = df['Index of Economic Resources']
zdata = df['Index of Education and Occupation']

# df.plot.scatter(x='Index of Relative Socio-economic Disadvantage', y='Index of Relative Socio-economic Advantage and Disadvantage')
# scatter = df.plot.scatter(x='Index of Relative Socio-economic Disadvantage', y='Index of Economic Resources', c=mapper.to_rgba(c), s=s)

# handles, labels = scatter.legend_elements(prop="sizes")
# legnd = scatter.legend(handles, labels, loc="upper right", title="Sizes")
# red_patch = mpatches.Patch(color='red', label='The red data')
# print(handles)
# print(labels)
# plt.legend([scatter], ['Index of Relative Socio-economic Disadvantage'], title="Comparison of SEIFA Indices")

def twodim_plot():
    fig, ax = plt.subplots()

    scatter1 = plt.scatter(x=df['Index of Relative Socio-economic Disadvantage'], y=df['Index of Economic Resources'],
                           c=mapper.to_rgba(c), s=s)
    plt.xlabel('Index of Relative Socio-economic Disadvantage')
    plt.ylabel('Index of Economic Resources')
    plt.scatter(x=df['Index of Relative Socio-economic Disadvantage'], y=df['Index of Economic Resources'], c=mapper.to_rgba(c), s=s)
    lgnd = ax.legend(['High Population', 'Low population'], loc="upper left", title="Legend")
    print(lgnd.legendHandles[0])
    lgnd.legendHandles[0]._sizes = [200]
    lgnd.legendHandles[1]._sizes = [10]
    clb = plt.colorbar()
    clb.ax.tick_params(labelsize=8)
    clb.ax.set_title('Index of Education and Occupation', fontsize=8)
    plt.show()


def threedim_pyplot():
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.scatter(xdata, ydata, zdata, c=mapper.to_rgba(c), s=s)

    plt.show()


def threedim_plotly_eg():
    my_data = np.random.rand(6500, 3)  # toy 3D points
    marker_data = go.Scatter3d(
        x=my_data[:, 0],
        y=my_data[:, 1],
        z=my_data[:, 2],
        marker=go.scatter3d.Marker(size=3),
        opacity=0.8,
        mode='markers'
    )
    fig = go.Figure(data=marker_data)
    fig.show()


def threedim_plotly():
    # Data for a three-dimensional line
    marker_data = go.Scatter3d(
        x=xdata,
        y=ydata,
        z=zdata,
        marker=go.scatter3d.Marker(size=s, color=c, line=dict(width=0)),
        opacity=0.8,
        mode='markers'
    )
    fig = go.Figure(data=marker_data)
    fig.show()


if __name__ == "__main__":
    #twodim_plot()
    threedim_plotly()
