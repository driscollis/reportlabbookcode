from reportlab.lib.styles import ParagraphStyle

class TestStyle(ParagraphStyle):

    def __init__(self, name):
        self.name = name

        self.__dict__.update(self.defaults)
        self.leading = 14

if __name__ == '__main__':
    p = TestStyle('test')
    print(p.name)
    print(p.leading)
    print(p.fontSize)