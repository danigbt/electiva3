from django.shortcuts import render
from models import Producto, Categoria, Marca
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Q


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