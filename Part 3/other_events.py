import wx

app = wx.App()
frame = wx.Frame(None)

class Panel(wx.Panel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)


panel = Panel(frame)
frame.Show()
app.MainLoop()