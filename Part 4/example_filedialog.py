import wx

app = wx.App()
frame = wx.Frame(None)

class Panel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.button = wx.Button(self, label="Show Message", size=(100,100))

        self.Bind(event=wx.EVT_BUTTON, handler=self.click_handler, source=self.button)

    def click_handler(self, event):
      pass
    
panel = Panel(frame)
frame.Show()
app.MainLoop()