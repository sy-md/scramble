import pynecone as pc
import engine as eg


class State(pc.State):

    text_input: str = ""
    left: str = ""
    mid: str = ""
    right: str = ""
    size = 0
    mid_size = 0
    text: list = []
    lf_buf: int = 0
    rt_buf = 0
    stg = []
    seen = []
    left_act = True
    right_act = False
    complete = False
    noithin = 1


    def get_size(self, txt):
        self.size = eg.size(txt)
        self.mid_size = self.size // 2
        self.text_input = txt
        self.left = eg.get_left(self.text_input, self.mid_size)
        self.mid = eg.get_mid(self.text_input, self.mid_size)
        self.right = eg.get_right(self.text_input, self.mid_size)
        self.lf_buf = (len(self.left)-1)

    def scramble(self):
        self.text = [self.mid]

    def next_letter(self):
        """
        * might need pointer for this to work out for the placment
        1.) pop from the left and the right
        2.) and put the letters in the queue
        3.) then take the letter from the qu and display them one by one
        """

        if self.left_act:
            self.text = eg.left(self.text, self.lf_buf, self.left)
            self.seen.append(self.left[self.lf_buf])
            self.lf_buf -= 1
            self.left_act = not (self.left_act)

        if self.right_act:
            self.text = eg.right(self.text, self.rt_buf, self.right)
            self.seen.append(self.right[self.rt_buf])
            self.rt_buf += 1
            self.left_act = not self.left_act

        self.right_act = not (self.right_act)

        self.noithin += 1
        if len(self.text) == self.size:
            self.right_act, self.left_act = False, False
            self.complete = True

    def clear(self):
        self.text_input = ""
        self.left = ""
        self.mid = ""
        self.right = ""
        self.size = 0
        self.mid_size = 0
        self.text = ""
        self.text = []
        self.lf_buf = 0
        self.rt_buf = 0
        self.stg = []
        self.seen = []
        self.left_act = True
        self.right_act = False
        self.complete = False
        self.noithin = 1

def index():  # HTML
    return pc.vstack(
            pc.text(State.text),
            pc.input(
                on_blur=lambda txt: State.get_size(txt)
            ),
            pc.button(
                "submit",
                on_click=State.scramble,
            ),

            """ debugging:
                uncomment to see under the hood
            """,
           #pc.text("size: -> ",State.size),
           #pc.text("mid size: -> ",State.mid_size),
           #pc.text("left: -> ",State.left),
           #pc.text("mid: -> ",State.mid),
           #pc.text("right: -> ",State.right),
           #pc.text("result: -> ",State.text),
           #pc.text("seen: -> ",State.seen),
           #pc.text("text len: -> ",State.noithin),
           #pc.text("stg: -> ",State.seen),
           #pc.text("left len: -> ",State.lf_buf),
           #pc.text("right len: -> ",State.rt_buf),
           #pc.text("right bool: -> ",State.right_act),
           #pc.text("left bool: -> ",State.left_act),

            pc.button(
                "next letter",
                on_click=State.next_letter
            ),
            pc.divider(),
            pc.hstack(
               pc.foreach(State.text, show_letter)
            ),
            pc.cond(
                State.complete,
                pc.button(
                    "play again",
                    on_click=State.clear
                ),
            )
        )



def show_letter(text):
    return pc.button(text)








app = pc.App(state=State)
app.add_page(index)
app.compile()
