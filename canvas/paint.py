import tkinter

class PaintApp(tkinter.Frame):
    def __init__(self, app):
        super().__init__(app)
        self.app = app
        # 画面全体のサイズ
        self.app.geometry("400x400")

        # キャンバスのサイズ
        self.canvas = tkinter.Canvas(self.app, width=300, height=300, bg="white")
        # キャンバスの配置位置
        self.canvas.place(x=50,y=20)

        # ラジオボタンの設定
        self.pen_on = True
        self.radio_value=tkinter.IntVar(value=1)
        # ラジオボタン1
        self.pen_button=tkinter.Radiobutton(
            self.app,text='pen',
            command=self.radio_click,
            variable=self.radio_value,
            value=1
        )
        self.pen_button.place(x=80,y=330)
        # ラジオボタン2
        self.erase_button=tkinter.Radiobutton(
            self.app,text='erase',
            command=self.radio_click,
            variable=self.radio_value,
            value=2
        )
        self.erase_button.place(x=150,y=330)

        # 左クリックしながら移動している間は描画のイベント
        self.canvas.bind('<B1-Motion>',self.paint)
        
        # マウスを離したら変数を初期化
        self.canvas.bind('<ButtonRelease-1>',self.reset)

        self.befor_x=None
        self.befor_y=None
        
    def paint(self,now):
        if self.befor_x and self.befor_y:
            # ペンか消しゴムを判定
            if self.pen_on:
                color = 'black'
                width = 5
            else:
                color = 'white'
                width = 30
            # 描画の処理
            self.canvas.create_line(
                self.befor_x,self.befor_y,
                now.x,now.y,
                width=width,
                fill=color,
                capstyle="round",
                smooth=True
            )
        self.befor_x = now.x
        self.befor_y = now.y

    def reset(self, event):
        self.befor_x, self.befor_y = None, None

    def radio_click(self):
        if self.radio_value.get() == 1:
            self.pen_on = True
        else:
            self.pen_on = False
        

app = tkinter.Tk()
app = PaintApp(app)
app.mainloop()
