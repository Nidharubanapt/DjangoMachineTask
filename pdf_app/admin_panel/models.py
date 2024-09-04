from django.db import models

class PDFDocument(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')
    points = models.IntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

