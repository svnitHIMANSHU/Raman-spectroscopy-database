import wx
import sqlite3
import os

class Example(wx.Frame):                                                                          
      
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title = title,size = (800,450))
        self.InitUI()
        self.Layout()
        self.Centre()
        self.Show()
         
    def InitUI(self):

        p = wx.Panel(self)
 
        bs = wx.BoxSizer(wx.VERTICAL)
        self.t1 = wx.TextCtrl(p, size = (120,30), style = wx.TE_MULTILINE |wx.TE_CENTER)
        bs.Add(self.t1, 1, wx.EXPAND)
        self.t2 = wx.TextCtrl(p, size = (120,30), style = wx.TE_MULTILINE |wx.TE_CENTER)
        bs.Add(self.t2, 1, wx.EXPAND)

        gs = wx.GridSizer(10,18,5,5)
        bs.Add(gs, 1, wx.EXPAND)

        self.conn = sqlite3.connect('RAMAN.db')
        for row_id in range(1,11):
         for col_id in range(1,19):
          print row_id,col_id
          cursor = self.conn.execute("SELECT * FROM ELEMENT WHERE ROW_NO==%d AND COLUMN_NO==%d"%(row_id,col_id))
          if(cursor==None):
            gs.Add(StaticText(p,-1,''))
          else:
            elements = cursor.fetchall()
          if(elements==None or len(elements)==0):
             gs.Add(wx.StaticText(p,-1,''))
          else:
            print elements[0]
	    btn = wx.Button(p, -1, str(elements[0][1]), (10,20))
	    btn.Bind(wx.EVT_BUTTON, self.OnClick, btn)
	    gs.Add(btn, -1 , wx.EXPAND)

        self.btn=wx.Button(p,-1,"Search!")
        bs.Add(self.btn,0,wx.ALIGN_CENTER) 
        p.SetSizer(bs)

        

    def OnClick(self, event):
        name = event.GetEventObject().GetLabelText()
        cursor=self.conn.execute("SELECT * FROM ELEMENT WHERE SYMBOL = ?", [name])
        elements = cursor.fetchall()
        cursor=self.conn.execute("SELECT ATOMIC_NUMBER FROM ELEMENT where SYMBOL = ?", [name])
        numbers = cursor.fetchall()
        print numbers
        atomicnumber = numbers[0][0]
        cursor=self.conn.execute("SELECT MOL_NUMBER FROM LINK where ELEMENT_NUMBER = ?", [atomicnumber])
        mnumber = cursor.fetchall()
        print mnumber
        combinations = mnumber[0][0]
    def combinations_intersection(combinations):
        if not combinations:
           return set()
        result = combinations[0]
        for s in combinations[1:]:
            result &=s
        return result
        print result
        #cursor=self.conn.execute("SELECT * FROM MOLECULE where MOL_NUMBER = ?", [combinations])
        #compounds = cursor.fetchall()
        #print compounds
        self.t1.AppendText(str(elements[0][0]))
        self.t1.AppendText("\n")
        #self.conn.close()


app = wx.App()
Example(None, title = 'Raman Spectroscopy Database')
app.MainLoop()
