# EMAIL

from django.core.mail import send_mail

# pdf

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

# Vista para la lista

from django.shortcuts import render
from .models import Asignatura

def tabla_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'lista.html', {'asignaturas': asignaturas})


# función para el renderizado en pdf 

def generar_pdf(request):
    template_path = 'lista.html'
    asignaturas = Asignatura.objects.all()
    context = {'asignaturas': asignaturas}
    template = get_template(template_path)
    html = template.render(context)

    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')

    return HttpResponse('Error al generar el PDF: {}'.format(pdf.err), status=500)

def send_email(request):
    asunto = 'Laboratios EPIS'
    mensaje_obligatorio = 'Buen día'
    correo = 'jccahuanala@unsa.edu.pe'

    send_mail(
        asunto,
        mensaje_obligatorio,
        correo,
        ['joshep.antony.ccl7427@gmail.com',],
        fail_silently=False)
    
    return render(request, 'email.html')