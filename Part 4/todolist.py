import wx

app = wx.App()
frame = wx.Frame(None)

class Panel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.list = wx.ListBox(self)
        self.add_item = wx.Button(self, label="Add Todo")
        self.save_list = wx.Button(self, label="Save Todos")

        grid_layout = wx.GridBagSizer(vgap=10, hgap=10)

        grid_layout.Add(self.list,  pos=(0,0), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=10)
        grid_layout.Add(self.add_item, pos=(1,0), flag= wx.ALL | wx.ALIGN_CENTER, border=10)
        grid_layout.Add(self.save_list, pos=(1,1), flag= wx.ALL | wx.ALIGN_CENTER, border=10)
        grid_layout.Add(1, 10, pos=(2,0))

        grid_layout.AddGrowableRow(0)
        grid_layout.AddGrowableCol(0)
        grid_layout.AddGrowableCol(1)

        self.SetSizer(grid_layout)

        self.Bind(event=wx.EVT_BUTTON, handler=self.add_handler, source=self.add_item)
        self.Bind(event=wx.EVT_BUTTON, handler=self.save_handler, source=self.save_list)

    def add_handler(self, event):
        pass

    def save_handler(self, event):
        pass

panel = Panel(frame)
frame.Show()
app.MainLoop()