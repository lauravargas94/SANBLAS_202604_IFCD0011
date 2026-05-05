from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("demo.pdf")

canvas.drawString(72, 72, "Hello, World!")

canvas.save()