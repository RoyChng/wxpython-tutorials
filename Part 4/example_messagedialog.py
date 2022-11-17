import wx

app = wx.App()
frame = wx.Frame(None)

class Panel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.button = wx.Button(self, label="Show Message", size=(100,100))

panel = Panel(frame)
frame.Show()
app.MainLoop()