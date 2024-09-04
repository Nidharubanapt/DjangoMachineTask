from django.shortcuts import render, get_object_or_404, redirect
from .models import PDFDocument
from .forms import PDFDocumentForm

# View to list all PDFs
def admin_dashboard(request):
    pdfs = PDFDocument.objects.all()
    return render(request, 'admin_panel/admin_dashboard.html', {'pdfs': pdfs})

# View to handle PDF upload
def upload_pdf(request):
    if request.method == 'POST':
        form = PDFDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PDFDocumentForm()
    return render(request, 'admin_panel/upload_pdf.html', {'form': form})

# View to handle PDF update
def update_pdf(request, pk):
    pdf = get_object_or_404(PDFDocument, pk=pk)
    if request.method == 'POST':
        form = PDFDocumentForm(request.POST, request.FILES, instance=pdf)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PDFDocumentForm(instance=pdf)
    return render(request, 'admin_panel/update_pdf.html', {'form': form})

# View to handle PDF deletion
def delete_pdf(request, pk):
    pdf = get_object_or_404(PDFDocument, pk=pk)
    pdf.delete()
    return redirect('admin_dashboard')


