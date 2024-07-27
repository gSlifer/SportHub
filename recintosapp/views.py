from django.shortcuts import render
from .models import User, Recinto, Comment
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import RecintoForm
from django.db.models import Q
from .forms import CommentForm
from django.http import JsonResponse

@csrf_exempt # Deshabilitar la protección CSRF para esta vista
def index(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/recintos/')

@csrf_exempt # Deshabilitar la protección CSRF para esta vista
def register_user(request):
    """
    Vista para el registro de usuarios.
    
    Args: request: La solicitud HTTP.
        
    Returns:
        La plantilla 'register_user.html' en caso de GET.
        En caso de POST, registra al usuario y lo redirige a la página principal si el registro es exitoso.
        Si hay errores, vuelve a la plantilla 'register_user.html' con el mensaje de error.
    """
    if request.method == 'GET':
        # Mostrar página de registro
        return render(request, 'recintosapp/register_user.html')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            return render(request, 'recintosapp/register_user.html', {'error': 'Las contraseñas no coinciden'})

        # Verificar si ya existeel usuario.
        if User.objects.filter(username=username).exists():
            return render(request, 'recintosapp/register_user.html', {'error': 'El usuario ya existe'})

        # Crear nuevo usuario con los datos
        user = User.objects.create_user(username=username, password=password, email=email)
        user = authenticate(username=username, password=password)
        login(request, user)  # Autenticar al usuario después de registrar
        return HttpResponseRedirect('/')


@csrf_exempt
def login_user(request):
    """
    Vista para el inicio de sesión de usuarios.
    
    Args: request: La solicitud HTTP.
        
    Returns:
        La plantilla 'login_user.html' en caso de GET.
        En caso de POST, autentica al usuario y lo redirige a la página principal si las credenciales son correctas.
        Si las credenciales son incorrectas, vuelve a la plantilla 'login_user.html' con el mensaje de error.
    """
    if request.method == 'GET':

        # Renderiza plantilla login_user.html
        return render(request, 'recintosapp/login_user.html')
    
    # Maneja solicitud POST
    if request.method == 'POST':

        # Obtener username y password
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar
        user = authenticate(username=username, password=password)

        # El usuario existe
        if user is not None:

            # Inicia sesión.
            login(request, user)
            return HttpResponseRedirect('/', {'user': request.user})
        else:
            return render(request, 'recintosapp/login_user.html', {'error': 'Usuario o Contraseña incorrecta.'})
        
@csrf_exempt # Deshabilitar la protección CSRF para esta vista
def logout_user(request):
    """
    Vista para cerrar sesión de usuarios.
    
    Args: request: La solicitud HTTP.
        
    Returns: Redirige a la página de inicio de sesión.
    """
    logout(request)
    # Redireccionar a la página de inicio de sesión
    return HttpResponseRedirect('/login/')

@csrf_exempt # Deshabilitar la protección CSRF para esta vista
def recintos(request):
    """
    Vista para mostrar y agregar recintos deportivos.
    
    Args: request: La solicitud HTTP.
        
    Returns:
        La plantilla 'recintos.html' con la lista de recintos en caso de GET.
        En caso de POST, si el usuario es administrador, guarda el nuevo recinto y vuelve a la plantilla con la lista actualizada.
        Si el usuario no tiene permisos, vuelve a la plantilla con un mensaje de error.
    """
    # Deshabilitar la protección CSRF para esta vista
    
    # Inicializa la variable recintos
    recintos = Recinto.objects.all()
        
    # Maneja la solicitud GET
    if request.method == "GET":

        # Aplicar filtros si están presentes
        valoracion = request.GET.get('rating')
        deporte = request.GET.get('deporte')
        nombre = request.GET.get('nombre')
        if valoracion:
            recintos = recintos.filter(rating__gte=valoracion)
        if deporte:
            recintos = recintos.filter(Q(sport=deporte.lower()))
        if nombre:
            recintos = recintos.filter(name__icontains=nombre)

        # Renderiza la plantilla recintos.html y pasa el contexto con la lista de recintos
        return render(request, "recintosapp/index.html", {"recintos": recintos, "sports": ['Futbol', 'Baloncesto', 'Tenis', 'Padel', 'Voleibol', 'Otro']})
    
    # Maneja la solicitud POST
    if request.method == "POST":

        # Comprueba si el usuario es un administrador
        if not request.user.is_authenticated or not request.user.is_admin:
            return render(request, "recintosapp/recintos.html", {"recintos": recintos, "error": "No tienes permiso para realizar esta acción"})
        
        # Comprueba si se ha enviado el formulario de añadir recinto
        form_recinto= RecintoForm(request.POST)
        if form_recinto.is_valid():
            form_recinto.save()
        return render(request, "recintosapp/recintos.html", {"recintos": recintos, "form_recinto": form_recinto})
        
@csrf_exempt
def agregar_recinto(request):
    """
    Vista para agregar un nuevo recinto deportivo.
    
    Args: request: La solicitud HTTP.
        
    Returns:
        La plantilla 'agregar_recinto.html' con el formulario para agregar un nuevo recinto.
        En caso de POST, guarda el nuevo recinto y redirige a la página principal.
    """
    recintos = Recinto.objects.all()
    if request.method == 'POST':
        form = RecintoForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/', {'user': request.user, 'recintos': recintos})
    else:
        form = RecintoForm()
    return render(request, 'recintosapp/agregar_recinto.html',{'recintos':recintos,'form':form} )

def recintos_details(request, id):
    """
    Vista para mostrar y agregar recintos deportivos.
    
    Args: request: La solicitud HTTP.
        
    Returns:
        La plantilla 'recintos_details.html' con la lista de recintos en caso de GET.
        En caso de POST, si el usuario es administrador, guarda el nuevo recinto y vuelve a la plantilla con la lista actualizada.
        Si el usuario no tiene permisos, vuelve a la plantilla con un mensaje de error.
    """
    recinto = Recinto.objects.get(id=id)
    comments = recinto.comments.all()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.recinto = recinto
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        comment_form = CommentForm()
    
    return render(request, 'recintosapp/recintos_details.html', {'recinto': recinto, 'comments': comments, 'comment_form': comment_form})
    

@csrf_exempt
def rating(request, id):
    """
    Vista para calificar un recinto.
    
    Args: request: La solicitud HTTP.
        
    Returns: Redirige a la página principal.
    """
    if request.method == 'POST':
        recinto_id = id
        rating = request.POST.get('rating')
        recinto = Recinto.objects.get(id=recinto_id)
        recinto.rating = (recinto.rating * recinto.rating_counter + float(rating)) / (recinto.rating_counter + 1)
        recinto.rating_counter += 1
        recinto.save()
        return HttpResponseRedirect('/')

    if request.method == "GET":
        # Renderiza la plantilla recintos.html y pasa el contexto con la lista de recintos
        recinto = Recinto.objects.get(id=id)
        return render(request, "recintosapp/rating.html", {"recinto": recinto})
        

def recintos_api(request):
    """
    Request para obtener las direcciones de los recintos.
    
    Args:
        request: La solicitud HTTP.
        
    Returns: una respuesta Json con la información de las direcciones de los recintos.
    """
    recintos = Recinto.objects.all()
    data = [
        {
            'name': recinto.name,
            'address': recinto.adress,
        }
        for recinto in recintos
    ]
    return JsonResponse(data, safe=False)

