import os
from manimlib import *
import random



class GOBANG(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lines = []
        with open("codes.py",'r') as f:
            for line in f:
                line_content = line.strip()
                if line_content == "":
                    continue
                if line_content[0] == '#':
                    continue
                print(line)
                lines.append(line.rstrip())
        self.lines = lines
        self.lineno = 0
        self.unit = 0.1
        self.font_size = 24
    def getW(self):
        sym = Text("{} {}".format(self.lineno+1,self.lines[self.lineno]), indent = 4,stroke_width=0,
            color=GREEN_E, fill_opacity=0.9,font_size=self.font_size,tab_width=self.unit)      
        self.lineno += 1
        if self.lineno >= len(self.lines):
            self.lineno = 0
        return sym
    def construct(self):
        first_line = None
        for n in range(len(self.lines)):
            line = self.getW()
            if first_line is None:
                line.move_to(UP * 3.5 + LEFT * 3)
                first_line = line
            else:
                line.move_to(UP * (3.5 - self.unit*4*n))
                line.align_to(first_line,LEFT)
            self.play(Write(line))
            self.wait(1)
        


        
if __name__ == "__main__":
    os.system("manimgl {} GOBANG -c white -wm".format(__file__))    