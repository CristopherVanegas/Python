from bokeh.plotting import figure, output_file, show

plot = figure(plot_width=300, plot_height=300)
plot.diamond_dot(x=[1, 2, 3], y=[1, 2, 3], size=20,
                 color="#386CB0", fill_color=None)

show(plot)

