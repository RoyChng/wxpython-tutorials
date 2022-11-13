import wx

app = wx.App()
frame = wx.Frame(None, title="Input Form")

class FormPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        # -- 1. Create a vertical layout for widgets --
        vertical_layout = wx.BoxSizer(wx.VERTICAL)

        # -- 2. Initalise widgets --

        # -- 3. Add widgets to vertical layout --
        vertical_layout.Add(self.radio_box, flag=wx.EXPAND | wx.ALL, border=10)
        vertical_layout.Add(self.combo_box, flag=wx.EXPAND | wx.ALL, border=10)
        vertical_layout.Add(self.submit_btn, flag=wx.ALL, border=10)

        self.SetSizer(vertical_layout)

        # -- 4. Bind events

panel = FormPanel(frame)
frame.Show()
app.MainLoop()
