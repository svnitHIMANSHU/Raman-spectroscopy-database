import wx
import sqlite3
import os 

class Example(wx.Frame):
 
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(1000,800))
        self.inter_list = list() 

 
        self.InitUI()
        self.Layout()
        self.Centre()
        self.Show()
 
    def InitUI(self):
 
        p = wx.Panel(self)
       
        bs = wx.BoxSizer(wx.VERTICAL)
        self.text = wx.TextCtrl(p,size = (50,30),style = wx.TE_MULTILINE |wx.TE_CENTER)
        bs.Add(self.text, 1, wx.EXPAND)
        self.list = wx.ListCtrl(p,size = (50,30),style = wx.LC_REPORT)
        self.list.InsertColumn(0, 'MOLECULE NUMBER', width = 150) 
        self.list.InsertColumn(1, 'MOLECULE NAME', wx.LIST_FORMAT_RIGHT, 200) 
        self.list.InsertColumn(2, 'MOLECULE SYMBOL', wx.LIST_FORMAT_RIGHT, 200)
        bs.Add(self.list, 1, wx.EXPAND)
        
        gs = wx.GridSizer(10, 18, 5, 5)
        bs.Add(gs, 1, wx.EXPAND)

        self.conn = sqlite3.connect('RAMAN.db')
        for row_id in range(1,11):
           for col_id in range(1,19):
             print row_id,col_id
             cursor= self.conn.execute("SELECT * FROM ELEMENT where ROW_NO==%d AND COLUMN_NO==%d"%(row_id,col_id))
             if(cursor==None):
                gs.Add(wx.StaticText(p,-1,''))
             else:
                elements = cursor.fetchall()
                if(elements==None or len(elements)==0):
                   gs.Add(wx.StaticText(p,-1,''))
                else:
                   print elements[0]
                   btn = wx.Button(p, -1,str(elements[0][1]), (10,20))                              
                   btn.Bind(wx.EVT_BUTTON, self.OnClick, btn)
                   gs.Add(btn, -1, wx.EXPAND)
                   
        self.search_btn=wx.Button(p,-1,"Search!")
        self.search_btn.Bind(wx.EVT_BUTTON, self.OnSearch, self.search_btn)
        bs.Add(self.search_btn,0,wx.ALIGN_CENTER)
        
        self.plot_btn=wx.Button(p,-1,"Plot!")
        self.plot_btn.Bind(wx.EVT_BUTTON, self.OnPlot, self.plot_btn)
        bs.Add(self.plot_btn,0,wx.ALIGN_CENTER)
        
        self.reset_btn=wx.Button(p,-1,"Reset!")
        self.reset_btn.Bind(wx.EVT_BUTTON, self.OnReset, self.reset_btn)
        bs.Add(self.reset_btn,0,wx.ALIGN_LEFT)
        p.SetSizer(bs)
        
         
    def OnClick(self, event):                                       
        name = event.GetEventObject().GetLabelText()
        cursor= self.conn.execute("SELECT * FROM ELEMENT where SYMBOL==?", (name,))
        elements = cursor.fetchall()
        print elements
        cursor= self.conn.execute("SELECT ATOMIC_NUMBER FROM ELEMENT where SYMBOL = ?", (name,))
        numbers = cursor.fetchone()[0]
        atomicnumber = numbers
        cursor= self.conn.execute("SELECT MOL_NUMBER FROM LINK where ELEMENT_NUMBER = ?", (atomicnumber,))
        mnumbers = cursor.fetchall()
        print mnumbers
        mnum_list = []
        for i in mnumbers:
             mnum_list.append(i[0])
        print mnum_list
        self.inter_list.append(mnum_list)
        print self.inter_list
        self.molecule_list=list(set.intersection(*map(set,self.inter_list)))
        print self.molecule_list
        self.text.AppendText(str(elements[0][1]))
        self.text.AppendText("\n")
               
    def OnSearch(self, event):        
        placeholder = '?'
        placeholders = ','.join(placeholder for unused in self.molecule_list)
        query = 'SELECT * FROM MOLECULE WHERE MOL_NUMBER IN (%s)' % placeholders
        cursor = self.conn.execute(query, self.molecule_list)
        final = cursor.fetchall()
        print final         
        for j in final: 
            self.list.Append((j[0],j[1],j[2]))                            

    def OnReset(self, event):                                    
        self.list.ClearAll()
        self.text.Clear()
        
    def OnPlot(self, event):                                       
        btn=event.GetEventObject().GetLabel()
        print "my plot=",btn
    

app = wx.App()
Example(None, title = 'Raman Spectroscopy Database')
app.MainLoop()	
