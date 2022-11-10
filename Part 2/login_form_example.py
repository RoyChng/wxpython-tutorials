import wx 

app = wx.App()
frame = wx.Frame(None)
panel = wx.Panel(frame)

email_label = wx.StaticText(panel, label="Email:")
password_label = wx.StaticText(panel, label="Password:")
email_input = wx.TextCtrl(panel)
password_input = wx.TextCtrl(panel)
submit_btn = wx.Button(panel, label="Submit", size=(1, 30))

frame.Show()
app.MainLoop()