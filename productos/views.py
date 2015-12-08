import datetime
from django.shortcuts import render
from models import Producto, Categoria, Marca, Compra
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.db.models import Q
from forms import CompraForm, ProductoForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail
from django.contrib.humanize.templatetags.humanize import intcomma
from django.core.urlresolvers import reverse


def productos_index(request):
    template = 'productos/index.html'

    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()

    return render(request, template, locals())


def ajax_user_search( request ):
    if request.is_ajax():
        q = request.GET.get( 'q' )
        print "q= %s" % (q)
        if q is not None:
            results = Producto.objects.filter( 
                Q( nombre__icontains = q ) |
                Q( categoria__nombre__icontains = q )|
                Q( marca__nombre__icontains = q )).order_by( 'nombre' )
            print "resultados %s" % results

            return render_to_response( 'productos/results.html', { 'results': results, }, 
                context_instance = RequestContext( request ) )


def ajax_categoria_filter( request ):
    if request.is_ajax():
        id_cat = request.GET.get( 'id_cat' )
        print "id_cat %s" % id_cat
        if id_cat is not None:
            results = Producto.objects.filter(categoria=id_cat)
            # results = Producto.objects.filter( 
            #     Q( categoria__id = id_cat )).order_by( 'nombre' )
            print "resultados %s" % results

            return render_to_response( 'productos/results.html', { 'results': results, }, 
                context_instance = RequestContext( request ) )


def ajax_marca_filter( request ):
    if request.is_ajax():
        id_mar = request.GET.get( 'id_mar' )
        print "id_mar %s" % id_mar
        if id_mar is not None:
            results = Producto.objects.filter(marca=id_mar)
            # results = Producto.objects.filter( 
            #     Q( categoria__id = id_mar )).order_by( 'nombre' )
            print "resultados %s" % results

            return render_to_response( 'productos/results.html', { 'results': results, }, 
                context_instance = RequestContext( request ) )


def comprar(request, producto_pk):
    template = 'productos/comprar.html'
    producto_seleccionado = Producto.objects.get(pk=producto_pk)
    

    if Compra.objects.filter(comfirmada=False).exists():
        compra = Compra.objects.get(comfirmada=False)
        compra.producto.add(producto_seleccionado)
        compra.save()
    else:
        compra = Compra()
        compra.save()
        compra.producto.add(producto_seleccionado)
        compra.save()

    lista_productos = compra.producto.all()
    total = 0
    for i in lista_productos:
        total = total + i.precio

    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)

        if form.is_valid():
            compra.total = total
            compra.comfirmada = True
            compra.save()
            form.save()
            #se envia el email al usuario y se redirige a la pagina de exito de compra
            template_email = get_template('productos/compra_template.txt')
            mensaje = "<strong>" + compra.usuario + "</strong> - email: " + compra.email
            mensaje = mensaje + " <br> Usted realizo la compra de:<ul> "
            for producto in compra.producto.all():
                mensaje = mensaje + "<li>" + producto.nombre + " - &#8370; " + str(intcomma(producto.precio)) + "</li>"
            mensaje = mensaje +"</ul>"
            mensaje = mensaje + "Total: &#8370; " + str(intcomma(compra.total)) 

            send_mail('Compra desde la web de Gonzalez Gimenez % s' % (datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')),
                'Notificacion de compra:',
                'danigbt@gmail.com', [compra.email], fail_silently=False, html_message=mensaje)
            
            return HttpResponseRedirect('/productos/compra_exitosa/')
    else:
        form = CompraForm(instance=compra)

    return render(request, template, locals())


def compra_exitosa(request):
    template = 'productos/compra_exitosa.html'
    ultima_compra = Compra.objects.latest('fecha')

    return render(request, template, locals())


def ver_carro(request):
    template = 'productos/carro.html'

    if Compra.objects.filter(comfirmada=False).exists():
        compra = Compra.objects.get(comfirmada=False)
        lista_productos = compra.producto.all()

        total = 0
        for i in lista_productos:
            total = total + i.precio

    else:
        return HttpResponseRedirect('/productos/carro_vacio/')

    

    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)

        if form.is_valid():
            compra.total = total
            compra.comfirmada = True
            compra.save()
            form.save()
            #se envia el email al usuario y se redirige a la pagina de exito de compra
            template_email = get_template('productos/compra_template.txt')
            mensaje = "<strong>" + compra.usuario + "</strong> - email: " + compra.email
            mensaje = mensaje + " <br> Usted realizo la compra de:<ul> "
            for producto in compra.producto.all():
                mensaje = mensaje + "<li>" + producto.nombre + " - &#8370; " + str(intcomma(producto.precio)) + "</li>"
            mensaje = mensaje +"</ul>"
            mensaje = mensaje + "Total: &#8370; " + str(intcomma(compra.total)) 

            send_mail('Compra desde la web de Gonzalez Gimenez % s' % (datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')),
                'Notificacion de compra:',
                'danigbt@gmail.com', [compra.email], fail_silently=False, html_message=mensaje)
            
            return HttpResponseRedirect('/productos/compra_exitosa/')
    else:
        form = CompraForm(instance=compra)

    return render(request, template, locals())


def remover_carro(request, producto_pk):
    compra = Compra.objects.get(comfirmada=False)

    lista_productos = compra.producto.all()
    
    #se remueve el producto del carro de compra
    compra.producto.remove(Producto.objects.get(pk=producto_pk))


    return HttpResponseRedirect(reverse('carro'))


def carro_vacio(request):
    template = 'productos/carro_vacio.html'

    return render(request, template, locals())


def cargar_producto(request):
    template = 'productos/cargar_producto.html'

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)

        if form.is_valid():
            
            form.save()
            return HttpResponseRedirect('/productos/#productos')
    else:
        form = ProductoForm()

    return render(request, template, locals())