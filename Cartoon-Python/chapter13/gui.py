import wx

# windows运行命令安装wx: pip install wxPython

# 自定义窗口类
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='第一个界面', size=(300, 350))
        panel = wx.Panel(parent=self)
        # 静态文本
        self.statictext = wx.StaticText(parent=panel, label='表单')
        # 按钮
        b1 = wx.Button(parent=panel, id=10, label='Button1')
        b2 = wx.Button(parent=panel, id=11, label='Button2')
        # 输入控件
        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        userid = wx.StaticText(panel, label='用户ID：')
        pwd = wx.StaticText(panel, label='密码：')
        content = wx.StaticText(panel, label='多行文本：')

        # 创建水平方向的盒子布局管理器 hbox 对象
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        # 添加 b1, b2 到 hbox
        hbox.Add(b1, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hbox.Add(b2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # 创建垂直方向盒子布局对象 vbox
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.statictext, proportion=1,
                 flag=wx.CENTER | wx.FIXED_MINSIZE | wx.TOP, border=10)
        vbox.Add(userid, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(tc1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(pwd, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(tc2, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(content, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(tc3, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(hbox, proportion=1, flag=wx.CENTER)

        # 设置面板 panel 采用 vbox 布局
        panel.SetSizer(vbox)

        # 设置tc1初始值
        tc1.SetValue('tony')
        print('读取用户ID：{}'.format(tc1.GetValue()))

        # 绑定事件，绑定 id 为 id~id2 的按钮
        self.Bind(wx.EVT_BUTTON, self.on_click, id=10, id2=20)

    def on_click(self, event):
        event_id = event.GetId()
        print(event_id)
        if event_id == 10:
            self.statictext.SetLabelText('Button1点击!')
        else:
            self.statictext.SetLabelText('Button2点击!')


# 创建应用长须对象
app = wx.App()

frm = MyFrame()
frm.Show()

# 进入主事件循环
app.MainLoop()
