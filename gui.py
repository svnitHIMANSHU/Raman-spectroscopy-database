import wx
import wx.grid
import sqlite3
import os

def connect():
     conn = sqlite3.connect('RAMAN.db')
     return conn
        
class Example(wx.Frame):
 
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(800,600))
 
        self.InitUI()
        self.Layout()
        self.Centre()
        self.Show()       
 
    def InitUI(self):
        self.grid_1 = wx.grid.Grid(self, -1, size=(11, 18))
        p = wx.Panel(self)
       
        bs = wx.BoxSizer(wx.VERTICAL)
        self.t1 = wx.TextCtrl(p,size = (120,30),style = wx.TE_MULTILINE |wx.TE_CENTER) 

        bs.Add(self.t1, 1, wx.EXPAND)
          
        bs.Add(grid_1, 1, wx.EXPAND)
        
        for e in range(0,11):
            for f in range(0,4):
                self.grid_1.SetCellValue(e,f,"")
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT SYMBOL FROM ELEMENT WHERE ROW=i AND COLUMN=j")
        conn.commit()
        for i in range(11):
            for j in range(0,18):
                cell=rows[i]
                self.grid_1.SetCellValue(i,j,str(cell[j]))
        btn = wx.Button(p, -1, SYMBOL, (10,20))                                   #buttons are added
        btn.myname = SYMBOL
        btn.Bind(wx.EVT_BUTTON, self.OnClick, btn)
        gs.Add(btn, 0, wx.EXPAND)        
        conn.close()
        event.Skip()
  
        
app = wx.App()
Example(None, title = 'Grid demo')
app.MainLoop()             
	
