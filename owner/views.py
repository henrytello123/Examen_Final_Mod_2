from django.shortcuts import render, redirect
from owner.models import Owner
from django.db.models import Q

from owner.forms import OwnerForm


def owner_list(request):
   # data_context = {'nombre_owner': 'KEVIN',
   #                 'edad': 30,
   #                 'pais': 'peru',
   #                 'vigente': False,
   #                 'pokemones': [{
   #                                 'nombre_pokemon': "charizard",
   #                                 'ataques': ['atq 1 charizard','atq 2 charizard','atq 3 charizard']
   #                             },
   #                             {
   #                                 'nombre_pokemon': "new",
   #                                 'ataques': ['atq 1 new', 'atq 2 new', 'atq 3 new']
   #                             },
   #                             {
   #                                 'nombre_pokemon': "balbasour",
   #                                 'ataques': ['atq 1 balbasour', 'atq 2 balbasour', 'atq 3 balbasour']
   #                             }
   #                             ]
   #                 }

   """crear un nuevo objeto en la base de datos"""
   #p = Owner(nombre="Alex", edad=46)
   #p.save()
   #p.nombre = "Karla"
   #p.save()

   """Obtener todos los datos de una tabla en la BD"""
   #data_context = Owner.objects.all()

   #SELECT * FROM public.owner_owner

   """filtracion de datos: filter()"""
   #data_context = Owner.objects.filter(edad='37')
   #data_context = Owner.objects.filter(nombre='Karla')
   #data_context = Owner.objects.filter(nombre='Rousmery', edad='37')

   """Ordenar por cualquier atributo en la Base de Datos"""
   #data_context = Owner.objects.order_by('nombre')

   """Ordenar alfabéticamente por edad"""
   #data_context = Owner.objects.order_by('edad')

   """Ordenar de manera inversa por la edad"""
   #data_context = Owner.objects.order_by('-edad')

   """Acortar datos: Obtener un rango de registro de una tabla en la base de datos"""
   #data_context = Owner.objects.all()[0:5]

   """Eliminar el objeto con id = 31 en la BD"""
   #p = Owner.objects.get(id=11)
   #p.delete()

   """Concatenar consultas"""
   #data_context = Owner.objects.filter(nombre="Karla").order_by("edad")

   """Eliminando un conjunto de datos específico"""
   #data_context = Owner.objects.filter(pais__startswith="ale").delete()

   """Actualización de datos en la BD a un cierto un grupo de datos"""
   #data_context = Owner.objects.filter(pais__startswith="bra").update(edad=17)

   """ Consultas complejas Q """
   #query = Q(pais__startswith='pe') | Q(pais__startswith='ec')
   #print("Query: {}".format(query))
   #data_context = Owner.objects.filter(query)

   "Negar Q"
   #query = Q(pais__startswith='pe') & ~Q(edad=37)
   #print("Query: {}".format(query))
   #data_context = Owner.objects.filter(query)

   "Error de consulta Q"
   #query = Q(pais__startswith='pe') | Q(pais__startswith='br')
   #print("Query: {}".format(query))
   #query correcta
   #data_context = Owner.objects.filter(query, edad=37)
   #query invalida
   #data_context = Owner.objects.filter(edad=37, query)

   data_context = Owner.objects.all()

   #print("lista de owners: {} " .format(data_context))
   return render(request, 'owner/owners.html', context={'data': data_context})

   #return render(request, 'owner/owner_list.html', context=data_context)

def owner_details(request):

   return render(request, 'owner/owner_detail.html', {})

def owner_search(request):
   query = request.GET.get('q', '')
   #print("query: {}".format(query))
   results = (
       Q(nombre__icontains=query)
   )
   print("resuts: {}".format(results))
   data_context = Owner.objects.filter(results).distinct()

   return render(request, 'owner/owner_search.html', context={'data': data_context, "query": query})


def owner_create(request):
   #aqui se usa el forms.py
   if request.method == "POST":
       form = OwnerForm(request.POST)
       if form.is_valid():
           """Guarda todos los campos que vienen desde la plantilla"""
           try:
               form.save()
               return redirect('owner_list')
           except:
               pass
   else:
       form = OwnerForm()

   return render(request, 'owner/owner-create.html', {'form': form})
