from tkinter import Frame,Label,CENTER
import GameLogic
import Constants as c

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        
        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>",self.key_down)
        self.commands={c.KEY_UP:GameLogic.move_up,c.KEY_DOWN:GameLogic.move_down,c.KEY_LEFT:GameLogic.move_left,c.KEY_RIGHT:GameLogic.move_right}
        
        self.grid_cells=[]
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
        
        self.mainloop()
        
    def init_grid(self):
        background=Frame(self,bg=c.BACKGROUND_COLOUR_GAME,width=c.SIZE,height=c.SIZE)
        background.grid()
        for i in range(c.GRID_LEN):
            grid_row=[]
            for j in range(c.GRID_LEN):
                cell=Frame(background,bg=c.BACKGROUND_COLOUR_EMPTY_CELL,width=c.SIZE/c.GRID_LEN,height=c.SIZE/c.GRID_LEN)
                cell.grid(row=i,column=j,padx=c.GRID_PADDING,pady=c.GRID_PADDING)
                t=Label(master=cell,text="",bg=c.BACKGROUND_COLOUR_EMPTY_CELL,justify=CENTER,font=c.FONT,width=10,height=5)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)
    
    def init_matrix(self):
        self.matrix=GameLogic.Start()
        GameLogic.add2(self.matrix)
        GameLogic.add2(self.matrix)
        
    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number=self.matrix[i][j]
                if(new_number==0):
                    self.grid_cells[i][j].configure(text="",bg=c.BACKGROUND_COLOUR_EMPTY_CELL)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number),bg=c.BACKGROUND_COLOUR_DICT[new_number],fg=c.CELL_COLOUR_DICT[new_number])
        self.update_idletasks()
        
    def key_down(self,event):
        key=repr(event.char)
        if key in self.commands:
            self.matrix,changed=self.commands[repr(event.char)](self.matrix)
            if changed:
                GameLogic.add2(self.matrix)
                self.update_grid_cells()
                changed=False
                if(GameLogic.currState(self.matrix)=='WON'):
                    self.grid_cells[1][1].configure(text="You",bg=c.BACKGROUND_COLOUR_EMPTY_CELL)
                    self.grid_cells[1][2].configure(text="Win",bg=c.BACKGROUND_COLOUR_EMPTY_CELL)
                if(GameLogic.currState(self.matrix)=='LOST'):
                    self.grid_cells[1][1].configure(text="You",bg=c.BACKGROUND_COLOUR_EMPTY_CELL)
                    self.grid_cells[1][2].configure(text="Lose",bg=c.BACKGROUND_COLOUR_EMPTY_CELL)
        
gamegrid=Game2048()