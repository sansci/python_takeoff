import wx

class myFrame(wx.Frame):
	def __init__(self):
		super().__init__(parent=None, title = 'Hello World', size=(600,400))
		panel = wx.Panel(self)
		mySzr = wx.BoxSizer(wx.VERTICAL)
		self.textCtrl = wx.TextCtrl(panel)
		mySzr.Add(self.textCtrl,0,wx.ALL|wx.EXPAND,5)
		myBtn = wx.Button(panel, label = 'Testing')
		myBtn.Bind(wx.EVT_BUTTON, self.on_press)
		mySzr.Add(myBtn,0,wx.ALL|wx.CENTER,5)
		panel.SetSizer(mySzr)
		
		
		self.SetSize(600,400)
		self.Center()
		self.Show()

	def on_press(self,event):
		value = self.textCtrl.GetValue()
		if not value:
			print("You did not text any value")
		else:
			print(f'Value = "{value}"')
			

def main():
	app = wx.App()
	frame = myFrame()
	app.MainLoop()
		
if __name__ == '__main__':
	main()