# face_demo.py

from reportlab.lib import colors
from reportlab.graphics import widgetbase
from reportlab.graphics.shapes import Drawing, String


def face_demo():
    drawing = Drawing(width=400, height=200)

    sad_face = widgetbase.Face()
    sad_face.skinColor = colors.blue
    sad_face.mood = 'sad'
    drawing.add(sad_face)

    ok_face = widgetbase.Face()
    ok_face.skinColor = colors.beige
    ok_face.mood = 'ok'
    ok_face.x = 110
    drawing.add(ok_face)

    happy_face = widgetbase.Face()
    happy_face.skinColor = colors.yellow
    happy_face.mood = 'happy'
    happy_face.x = 215
    drawing.add(happy_face)

    drawing.save(formats=['pdf'], outDir='.', fnRoot='face_demo')

if __name__ == '__main__':
    face_demo()