import pynecone as pc
import engine as eg
#import time

class State(pc.State):

    text_input: str = "" #good
    left: str = "" #good
    mid: str = "" #good
    right: str = "" #good
    size = 0 #good
    mid_size = 0 #good
    text = []


    def get_size(self, txt):
        self.size = eg.size(txt)
        self.mid_size = self.size // 2
        self.text_input = txt
        self.left = eg.get_left(self.text_input,self.mid_size)
        self.mid = eg.get_mid(self.text_input,self.mid_size)
        self.right = eg.get_right(self.text_input,self.mid_size)
        self.text = [self.left,self.mid,self.right]

   #def scramble(self):
   #    self.left = eg.get_left(self.text_input,self.mid_size)
   #    self.mid = eg.get_mid(self.text_input,self.mid_size)
   #    self.right = eg.get_right(self.text_input,self.mid_size)
   #    self.text = [self.left,self.mid,self.right]

def index():
    return pc.vstack(
            pc.text(State.text),
            pc.input(
                placeholder="type a phrase...",
                on_change= lambda txt: State.get_size(txt)
            ),
            pc.button(
                "submit",
                #on_click=State.scramble,
            ),
            pc.text("size: -> ",State.size),
            pc.text("mid size: -> ",State.mid_size),
            pc.text("left: -> ",State.left),
            pc.text("mid: -> ",State.mid),
            pc.text("right: -> ",State.right),
            pc.text("result: -> ",State.text)
        )

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
