import wx

app = wx.App()

icon = wx.Icon("application_icon.ico")

# Making/Customizing Window
frame = wx.Frame(None, title="My Application")
frame.SetIcon(icon)
frame.SetBackgroundColour("#87b3ff")
frame.SetSize((400,400))
panel = wx.Panel(frame)

# Modifying Font
current_font = panel.GetFont()
current_font.SetPointSize(16)
current_font.SetUnderlined(True)
current_font.SetWeight(wx.FONTWEIGHT_BOLD)
panel.SetFont(current_font)

# Text Widget
text = wx.StaticText(panel, label="Hello World", size=(100,100), pos=(100,100))
text.SetBackgroundColour("#404258")
text.SetForegroundColour("#ffffff")

# Bitmap Widget
application_bitmap = wx.Bitmap("application_icon.png")
image = wx.StaticBitmap(panel, bitmap=application_bitmap, pos=(150,0))

frame.Center()
frame.Show()
app.MainLoop()