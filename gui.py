import wx
import sqlite3
class Example(wx.Frame):
 
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(800,600))
 
        self.InitUI()
        self.Layout()
        self.Centre()
        self.Show()
 
    def InitUI(self):
 
        p = wx.Panel(self)
       
        bs = wx.BoxSizer(wx.VERTICAL)
        self.t1 = wx.TextCtrl(p,size = (120,30),style = wx.TE_MULTILINE |wx.TE_CENTER 
)
        bs.Add(self.t1, 1, wx.EXPAND)
           
        gs = wx.GridSizer(10, 13, 5, 5)
        bs.Add(gs, 1, wx.EXPAND)

conn = sqlite3.connect('RAMAN.db')
cursor = conn.execute("SELECT SYMBOL FROM ELEMENT")
elements = cursor.fetchall()
   
i = 0
while i < 10: 
   print elements[i]
   i = i + 1       
   
i = 10
while i <20:
   print elements[i] 
   i = i +1 
  
i = 0
while i < 10: 
   print elements[i]
   i = i + 1       
   
i = 10
while i <20:
   print elements[i] 
   i = i +1 

i = 20
while i < 30: 
   print elements[i]
   i = i + 1       
   
i = 30
while i <40:
   print elements[i] 
   i = i +1 
  
i = 40
while i < 50: 
   print elements[i]
   i = i + 1       
   
i = 50
while i <60:
   print elements[i] 
   i = i +1  
   
i = 60
while i < 70: 
   print elements[i]
   i = i + 1       
   
i = 80
while i <90:
   print elements[i] 
   i = i +1 
  
i = 90
while i < 100: 
   print elements[i]
   i = i + 1       
   
i = 100
while i <110:
   print elements[i] 
   i = i +1 

i = 110
while i < 118: 
   print elements[i]
   i = i + 1        
   
for elements in cursor:       
    btn = wx.Button(p, -1, elements, (10,20))                              #buttons are added
    btn.myname = elements
    btn.Bind(wx.EVT_BUTTON, self.OnClick, btn)
    gs.Add(btn, 0, wx.EXPAND)   
        
    p.SetSizer(bs)
         
    def OnClick(self, event):                                       #When the button is clicked
        name = event.GetEventObject().myname
        self.t1.AppendText(name)
        self.t1.AppendText("\n")
   

conn.close()
app = wx.App()
Example(None, title = 'Grid demo')
app.MainLoop()
	            
	
