import wx

app = wx.App()
frame = wx.Frame(None)
panel = wx.Panel(frame)

button_1 = wx.Button(panel, label="Button 1")
button_2 = wx.Button(panel, label="Button 2")
button_3 = wx.Button(panel, label="Button 3")

frame.Show()
app.MainLoop()