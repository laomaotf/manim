import os
from tkinter import CENTER
from manimlib import *
import random



class GOBANG_1(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unit = 0.06
        self.font_size = 18*2
    def getBoard(self,N,target_color=WHITE):
        DIRS = [UP,LEFT,UR,UL]
        COLOR_SEQ = [LIGHT_BROWN]  + [target_color for _ in range(N)]
        random.shuffle(COLOR_SEQ) 
        direction = random.choice(DIRS)
        stones = []
        for color in COLOR_SEQ:
            if color != target_color:
                opacity = 0.0
            stones.append(
                Circle(color=color,fill_opacity=opacity,radius=self.unit/2,stroke_color=color)
            )
        board = Square(color=LIGHT_BROWN,side_length=self.unit*10,fill_color=LIGHT_BROWN,fill_opacity=1.0)
        
        stones = VGroup(*stones).arrange(direction,buff=self.unit).next_to(board,IN,buff=0)
        # coef = Tex(r"\times w_{}".format(N),
        #     color=DARK_BROWN, fill_opacity=1.0,font_size=self.font_size,tab_width=self.unit/2)       
        # coef.next_to(board,RIGHT,buff=self.unit)
        return VGroup(board,stones)
    def getW(self,N,postfix="+"):
        sym = Tex(r" \times w_{} {}".format(N,postfix),
            color=DARK_BROWN, fill_opacity=1.0,font_size=self.font_size,tab_width=self.unit/2)      
        return sym
    def construct(self):
        for _ in range(1):
            board4 = self.getBoard(4)
            self.play(Write(board4))
            self.play(board4.animate.move_to(UP*3))
            self.play(board4.animate.move_to(UP*3 + LEFT*6))
            
            board3 = self.getBoard(3)
            self.play(Write(board3))
            self.play(board3.animate.move_to(UP*4))
            self.play(board3.animate.move_to(UP*3 + LEFT*4))
            
            board2 = self.getBoard(2)
            self.play(Write(board2))
            self.play(board2.animate.move_to(UP*4))
            self.play(board2.animate.move_to(UP*3 + LEFT*2))
            
            board1 = self.getBoard(1)
            self.play(Write(board1))
            self.play(board1.animate.move_to(UP*4))
            self.play(board1.animate.move_to(UP*3 + LEFT*0))
            
        W4 = self.getW(4)
        W4.next_to(board4,direction=RIGHT, buff=self.unit*3)
        W3 = self.getW(3)
        W3.next_to(board3,direction=RIGHT,buff=self.unit*3)
        W2 = self.getW(2)
        W2.next_to(board2,direction=RIGHT,buff=self.unit*3)
        W1 = self.getW(1," = S")
        W1.next_to(board1,direction=RIGHT,buff=self.unit*3)
        W = VGroup(W1,W2,W3,W4)
        self.play(FadeIn(W))
        self.wait(2)
        



class GOBANG(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unit = 0.08
        self.font_size = 18*2
    def getBoard(self,N,target_color=BLACK):
        DIRS = [UP,LEFT,UR,UL]
        COLOR_SEQ = [LIGHT_BROWN]  + [target_color for _ in range(N)]
        random.shuffle(COLOR_SEQ) 
        direction = random.choice(DIRS)
        stones = []
        for color in COLOR_SEQ:
            if color != target_color:
                opacity = 0
            else:
                opacity = 1.0
            stones.append(
                Circle(color=color,fill_opacity=opacity,radius=self.unit/2,stroke_color=color,stroke_opacity=opacity)
            )
        board = Square(color=LIGHT_BROWN,side_length=self.unit*10,fill_color=LIGHT_BROWN,fill_opacity=1.0)
        
        stones = VGroup(*stones).arrange(direction,buff=self.unit).next_to(board,IN,buff=0)
        return VGroup(board,stones)
    def getW(self,N,postfix="+"):
        sym = Tex(r" \times w_{} {}".format(N,postfix),
            color=DARK_BROWN, fill_opacity=1.0,font_size=self.font_size,tab_width=self.unit/2)      
        return sym
    def construct(self):
        for _ in range(1):
            text4 = Text("Connect-4").move_to(DOWN)
            self.play(Write(text4))
            for _ in range(3):
                board4 = self.getBoard(4)
                self.play(FadeInFromPoint(board4,LEFT))
                self.play(FadeOutToPoint(board4,RIGHT))
            self.play(FadeInFromPoint(board4,LEFT))
            self.play(FadeOut(text4))
            self.play(board4.animate.move_to(UP*3))
            self.play(board4.animate.move_to(UP*3 + LEFT*6))
            
            text3 = Text("Connect-3").move_to(DOWN)
            self.play(Write(text3))
            for _ in range(2):
                board3 = self.getBoard(3)
                self.play(FadeIn(board3,shift=LEFT))
                self.play(FadeOut(board3,shift=RIGHT))
            self.play(FadeIn(board3,shift=LEFT))
            self.play(FadeOut(text3))
            self.play(board3.animate.move_to(UP*4))
            self.play(board3.animate.move_to(UP*3 + LEFT*4))
            
            text2 = Text("Connect-2").move_to(DOWN)
            self.play(Write(text2))
            for _ in range(1):
                board2 = self.getBoard(2)
                self.play(ShowIncreasingSubsets(board2))
                self.play(FadeOut(board2))
            self.play(ShowIncreasingSubsets(board2))
            self.play(FadeOut(text2))            
            self.play(board2.animate.move_to(UP*4))
            self.play(board2.animate.move_to(UP*3 + LEFT*2))
            
            text1 = Text("Connect-1").move_to(DOWN)
            self.play(Write(text1))
            board1 = self.getBoard(1)
            self.play(ShowCreation(board1))
            self.play(FadeOut(text1))
            self.play(board1.animate.move_to(UP*4))
            self.play(board1.animate.move_to(UP*3 + LEFT*0))
            
        WB4 = self.getW(4)
        WB4.next_to(board4,direction=RIGHT, buff=self.unit*3)
        WB3 = self.getW(3)
        WB3.next_to(board3,direction=RIGHT,buff=self.unit*3)
        WB2 = self.getW(2)
        WB2.next_to(board2,direction=RIGHT,buff=self.unit*3)
        WB1 = self.getW(1,"")
        WB1.next_to(board1,direction=RIGHT,buff=self.unit*3)
        ScoreS = Tex(r" = ", "S_{self}",color=DARK_BROWN, fill_opacity=1.0,font_size=self.font_size,tab_width=self.unit/2)
        ScoreS.next_to(WB1,direction=RIGHT,buff=self.unit*3)
        WB = VGroup(WB1,WB2,WB3,WB4,ScoreS)
        self.play(FadeIn(WB))
        
        
        for _ in range(1):
            board4 = self.getBoard(4,WHITE)
            self.play(Write(board4))
            self.play(board4.animate.move_to(UP*2))
            self.play(board4.animate.move_to(UP*2 + LEFT*6))
            
            board3 = self.getBoard(3,WHITE)
            self.play(Write(board3))
            self.play(board3.animate.move_to(UP*2))
            self.play(board3.animate.move_to(UP*2 + LEFT*4))
            
            board2 = self.getBoard(2,WHITE)
            self.play(Write(board2))
            self.play(board2.animate.move_to(UP*2))
            self.play(board2.animate.move_to(UP*2 + LEFT*2))
            
            board1 = self.getBoard(1,WHITE)
            self.play(Write(board1))
            self.play(board1.animate.move_to(UP*2))
            self.play(board1.animate.move_to(UP*2 + LEFT*0))
            
        WW4 = self.getW(8)
        WW4.next_to(board4,direction=RIGHT, buff=self.unit*3)
        WW3 = self.getW(7)
        WW3.next_to(board3,direction=RIGHT,buff=self.unit*3)
        WW2 = self.getW(6)
        WW2.next_to(board2,direction=RIGHT,buff=self.unit*3)
        WW1 = self.getW(5,"")
        WW1.next_to(board1,direction=RIGHT,buff=self.unit*3)
        ScoreO = Tex(r" = ", "S_{other}",color=DARK_BROWN, fill_opacity=1.0,font_size=self.font_size,tab_width=self.unit/2)
        ScoreO.next_to(WW1,direction=RIGHT,buff=self.unit*3)
        WW = VGroup(WW1,WW2,WW3,WW4,ScoreO)
        self.play(FadeIn(WW))
        
        Score = Tex(r"(1 - \alpha) \times S_{self} - \alpha \times S_{other} = S",color=DARK_BROWN, fill_opacity=1.0,font_size=self.font_size,tab_width=self.unit/2)
        self.play(TransformMatchingTex(VGroup(ScoreO,ScoreS),Score))
        self.wait(3)
        Wall = Tex(r"W_{i}",color=DARK_BROWN, fill_opacity=1.0,font_size=self.font_size,tab_width=self.unit/2)
        Indices = Tex(r"i \in 1,2,3,...,8",color=DARK_BROWN, fill_opacity=1.0,font_size=self.font_size,tab_width=self.unit/2)
        Alpha = Tex(r"\alpha",color=DARK_BROWN, fill_opacity=1.0,font_size=self.font_size,tab_width=self.unit/2)
        Wall.move_to(DOWN)
        Indices.next_to(Wall,DOWN)
        Alpha.next_to(Indices,DOWN)
        self.play(Write(Wall))
        self.play(Write(Indices))
        self.play(Write(Alpha))
        
        self.wait(2)
                
        
if __name__ == "__main__":
    os.system("manimgl {} GOBANG -c black -wm".format(__file__))    