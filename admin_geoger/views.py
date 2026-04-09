from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import DireccionSerializer
from django.http import JsonResponse
from .models import Empleado, Direccion
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

# 🔥 API REST (CRUD automático)
class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

# 🔐 LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/home')
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})

    return render(request, 'login.html')

# 🏠 HOME (MAPA)
@login_required
def home(request):
    return render(request, 'index.html')


# 👨‍💼 VISTA EMPLEADOS (HTML)
@login_required
def empleados_view(request):
    return render(request, 'empleados.html')


# 📊 API EMPLEADOS (CON RELACIÓN A UBICACIONES)
def empleados_api(request):
    empleados = []

    for emp in Empleado.objects.all():
        direcciones = []

        # 🔥 relación correcta
        for d in emp.direccion_set.all():
            direcciones.append({
                "latitud": float(d.latitud),
                "longitud": float(d.longitud),
                "direccion": d.direccion_completa,
                "fecha": d.fecha_registro.strftime("%Y-%m-%d %H:%M")
            })

        empleados.append({
            "id": emp.id,
            "nombre": emp.nombre_completo,  # ⚠️ IMPORTANTE
            "puesto": emp.puesto,
            "ubicaciones": direcciones
        })

    return JsonResponse(empleados, safe=False)

# 📍 API UBICACIONES (PARA MAPA)
def ubicaciones_api(request):
    ubicaciones = []

    for u in Direccion.objects.select_related('empleado'):
        ubicaciones.append({
            "empleado": u.empleado.nombre_completo,  # ⚠️ IMPORTANTE
            "latitud": float(u.latitud),
            "longitud": float(u.longitud),
            "fecha": u.fecha_registro.strftime("%Y-%m-%d %H:%M")
        })

    return JsonResponse(ubicaciones, safe=False)

# CREAR EMPLEADO + UBICACION
@csrf_exempt
@login_required
def crear_empleado(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # 🔥 crear empleado
        empleado = Empleado.objects.create(
            user=request.user,
            nombre_completo=data['nombre'],
            puesto=data['puesto']
        )

        # 🔥 crear UNA sola ubicación
        Direccion.objects.create(
            empleado=empleado,
            latitud=data['latitud'],
            longitud=data['longitud']
        )

        return JsonResponse({"status": "ok"})
    
# EDITAR EMPLEADO
@csrf_exempt
@login_required
def editar_empleado(request, id):
    if request.method == "POST":
        data = json.loads(request.body)

        emp = Empleado.objects.get(id=id)

        # actualizar datos
        emp.nombre_completo = data.get('nombre')
        emp.puesto = data.get('puesto')
        emp.save()

        # 🔥 BORRAR TODAS LAS UBICACIONES ANTERIORES
        Direccion.objects.filter(empleado=emp).delete()

        # 🔥 CREAR NUEVA UBICACIÓN
        Direccion.objects.create(
            empleado=emp,
            latitud=data.get('latitud'),
            longitud=data.get('longitud')
        )

        return JsonResponse({"status": "updated"})
    
    # ELIMINAR
@csrf_exempt
def eliminar_empleado(request, id):
    if request.method == "DELETE":
        emp = Empleado.objects.get(id=id)
        emp.delete()

        return JsonResponse({"status": "deleted"})
    
