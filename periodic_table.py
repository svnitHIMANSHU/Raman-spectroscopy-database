import wx
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
           
        gs = wx.GridSizer(11, 18, 5, 5)
        bs.Add(gs, 1, wx.EXPAND)
 
        A = [ "H"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "He", "Li", "Be"," "," "," "," "," "," "," "," "," "," ", "B" , "C", "N", "O", "F" , "Ne", "Na", "Mg"," "," "," "," "," "," "," "," "," "," ", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca","Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru","Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "" , "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "", "Rf", "Db", "Sg", "Bh", "Hs","Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", " ", " "," ", " ", " ", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm","Yb", "Lu"," ", " ", " ","Ac", "Th" , "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk","Cf", "Es", "Fm", "Md" , "No", "Lr"," "," "," "," "," "," "," "," "," " ,"Go"," "," "," "," "," "," "," ","" ]
       
        for i in A:
            btn = wx.Button(p, -1, i, (10,20)) #buttons are added
            btn.myname = i
            btn.Bind(wx.EVT_BUTTON, self.OnClick, btn)
            gs.Add(btn, 0, wx.EXPAND)
           
        
        p.SetSizer(bs)
 
    def OnClick(self, event):  #When the button is clicked
        name = event.GetEventObject().myname
        self.t1.AppendText(name)
        self.t1.AppendText("\n")
 
app = wx.App()
Example(None, title = 'Grid demo')
app.MainLoop()

	
