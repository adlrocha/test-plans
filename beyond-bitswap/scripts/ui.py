import ipywidgets as widgets

class Layout:
    def __init__(self):
        self.testcase = widgets.Text(description="Testcase")
        self.input_data = widgets.Text(description="Input Data Type")
        self.file_size = widgets.Text(description="File Size")
        self.files_directory = widgets.Text(description="Files Directory")
        self.run_count = widgets.IntSlider(description="Run Count", min=1, max=300)

        self.n_nodes = widgets.IntSlider(description="# nodes", min=2, max=300)
        self.n_leechers = widgets.IntSlider(description="# leechers", min=1, max=300)
        self.n_passive = widgets.IntSlider(description="# passive ", min=0, max=300)
        self.max_connection_rate = widgets.IntSlider(description="Max connections (%)", value=100, min=0, max=100)
        self.churn_rate = widgets.IntSlider(description="Churn Rate (%)", min=0, max=100)

        self.grid = widgets.GridspecLayout(5, 2, height='300px')


    def show(self):
        self.grid[0, 0] = self.testcase
        self.grid[1, 0] = self.input_data
        self.grid[2, 0] = self.file_size
        self.grid[3, 0] = self.files_directory
        self.grid[4, 0] = self.run_count
        self.grid[0, 1] = self.n_nodes
        self.grid[1, 1] = self.n_leechers
        self.grid[2, 1] = self.n_passive
        self.grid[3, 1] = self.churn_rate
        return self.grid


        