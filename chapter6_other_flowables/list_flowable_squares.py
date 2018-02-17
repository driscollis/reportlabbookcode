# list_flowable_squares.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import ListFlowable, ListItem
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def list_flowable_squares():
    doc = SimpleDocTemplate("list_flowable_squares.pdf",
                            pagesize=letter
                            )
    styles = getSampleStyleSheet()
    normal = styles['Normal']
    story = []

    flowables = [
        Paragraph('Paragraph numero uno', normal),
        ListItem(Paragraph('Paragraph #2', normal),
                 bulletColor="blue"),
        Paragraph('Paragraph #3', normal),
    ]

    flowables.append(
        ListFlowable(
            [Paragraph("I'm a sublist item", normal),
             ListItem(Paragraph("I'm another sublist item", normal),
                      bulletColor='blue'),
             ListItem(Paragraph("I'm the last sublist item", normal),
                      bulletColor='red')
             ],
            bulletType='bullet',
            start='square'
        ))

    lflow = ListFlowable(flowables, bulletType='I')
    story.append(lflow)

    doc.build(story)

if __name__ == '__main__':
    list_flowable_squares()