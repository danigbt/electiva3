import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context


def index(request):
    template = 'index.html'

    if request.method == 'POST' and request.is_ajax():
        nombre = request.POST.get('name')
        email = request.POST.get('email')
        mensaje = request.POST.get('message')

        response_data = {}
        response_data['respuesta'] = 'Todo OK en el servidor'

        template_email = get_template('contact_template.txt')
        context = Context({
            'contact_name': nombre,
            'contact_email': email,
            'form_content': mensaje,
        })
        content = template_email.render(context)

        email = EmailMessage(
            "Nuevo contacto desde la web",
            content,
            "Tu sitio" +'<danigbt@gmail.com>',
            ['danigbt@gmail.com'],
            headers = {'Reply-To': email }
        )
        email.send()
        # return redirect('contact')

        return JsonResponse(response_data)
    

    return render(request, template, locals())
