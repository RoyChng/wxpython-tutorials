import wx

app = wx.App()
frame = wx.Frame(None, title="Unit Converter")
frame.SetMinSize((400,400))

class Panel(wx.Panel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        
        # -- 1. Changes Font Size for all widgets --
        font = self.GetFont()
        font.SetPointSize(11)
        self.SetFont(font)

        # -- 2. Initialise widgets --
        input_label = wx.StaticText(self, label="Input:")
        output_label = wx.StaticText(self, label="Output:")
        self.input_textctrl = wx.TextCtrl(self)
        self.output_texctrl = wx.TextCtrl(self, style=wx.TE_READONLY)
        self.selection_radio_box = wx.RadioBox(self, label="Select conversion", choices=["KM to M", "M to KM"], style=wx.HORIZONTAL)

        # -- 3. Create layout sizer --
        grid_layout = wx.GridBagSizer(vgap=10, hgap=10)

        # -- 4. Add widgets to layout --
        grid_layout.Add(1, 30, pos=(0,0))
        grid_layout.Add(input_label, pos=(1,0), flag=wx.ALL, border=10)
        grid_layout.Add(self.input_textctrl, pos=(1,1), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=10)
        grid_layout.Add(self.selection_radio_box, pos=(2,0), span=(1,2), flag=wx.ALL, border=10)
        grid_layout.Add(output_label, pos=(3,0), flag=wx.ALL, border=10)
        grid_layout.Add(self.output_texctrl, pos=(3,1), span=(1,2), flag=wx.EXPAND | wx.ALL, border=10)

        # -- 5. Configure layout & add to panel --
        grid_layout.AddGrowableCol(1)
        self.SetSizer(grid_layout)

        # -- 6. Bind widget to event listener --


panel = Panel(frame)
frame.Show()
app.MainLoop()

