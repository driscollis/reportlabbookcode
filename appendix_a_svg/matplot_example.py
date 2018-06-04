import matplotlib.pyplot as pyplot

def create_matplotlib_svg(plot_path):
    """
    Create an SVG using matplotlib
    """
    pyplot.plot(list(range(5)))
    pyplot.title = 'matplotlib SVG + ReportLab'
    pyplot.ylabel = 'Increasing numbers'
    pyplot.savefig(plot_path, format='svg')

if __name__ == '__main__':
    from svg_demo import svg_demo
    svg_path = 'matplot.svg'
    create_matplotlib_svg(svg_path)
    svg_demo(svg_path, 'matplot.pdf')
