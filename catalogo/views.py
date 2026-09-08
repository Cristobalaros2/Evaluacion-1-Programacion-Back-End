from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.views.decorators.http import require_POST
import json
import hashlib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USUARIOS_FILE = os.path.join(BASE_DIR, "usuarios.json")
PRODUCTOS_FILE = os.path.join(BASE_DIR, "productos.json")

PRODUCTOS_DEFAULT = [
    {"id": 1, "nombre": "Martillo de uñas 16oz", "categoria": "Herramientas manuales", "precio": 15990, "stock": 25, "imagen": "images/01-martillo.jpg"},
    {"id": 2, "nombre": "Destornillador plano 6mm", "categoria": "Herramientas manuales", "precio": 4990, "stock": 40, "imagen": "images/02-destornillador.jpg"},
    {"id": 3, "nombre": "Llave inglesa 12 pulgadas", "categoria": "Herramientas manuales", "precio": 12990, "stock": 15, "imagen": "images/03-llave-inglesa.jpg"},
    {"id": 4, "nombre": "Alicate de presión 8 pulgadas", "categoria": "Herramientas manuales", "precio": 9990, "stock": 0, "imagen": "images/04-alicate.jpg"},
    {"id": 5, "nombre": "Sierra manual 20 pulgadas", "categoria": "Herramientas manuales", "precio": 18990, "stock": 8, "imagen": "images/05-sierra-manual.jpg"},
    {"id": 6, "nombre": "Nivel de burbuja 60cm", "categoria": "Herramientas manuales", "precio": 14990, "stock": 12, "imagen": "images/06-nivel-burbuja.jpg"},
    {"id": 7, "nombre": "Cinta métrica 5 metros", "categoria": "Herramientas manuales", "precio": 3990, "stock": 50, "imagen": "images/07-cinta-metrica.jpg"},
    {"id": 8, "nombre": "Pinza de corte diagonal", "categoria": "Herramientas manuales", "precio": 7990, "stock": 0, "imagen": "images/08-alicate-corte.jpg"},
    {"id": 9, "nombre": "Llave torx set 10 piezas", "categoria": "Herramientas manuales", "precio": 8990, "stock": 20, "imagen": "images/09-llave-torx.jpg"},
    {"id": 10, "nombre": "Taladro eléctrico 650W", "categoria": "Herramientas eléctricas", "precio": 45990, "stock": 10, "imagen": "images/10-taladro.jpg"},
    {"id": 11, "nombre": "Amoladora angular 4.5 pulgadas", "categoria": "Herramientas eléctricas", "precio": 39990, "stock": 7, "imagen": "images/11-amoladora.jpg"},
    {"id": 12, "nombre": "Sierra circular 7.25 pulgadas", "categoria": "Herramientas eléctricas", "precio": 69990, "stock": 5, "imagen": "images/12-sierra-circular.jpg"},
    {"id": 13, "nombre": "Rotomartillo SDS 800W", "categoria": "Herramientas eléctricas", "precio": 59990, "stock": 0, "imagen": "images/13-set-brocas.jpg"},
    {"id": 14, "nombre": "Lijadora orbital 1/3 HP", "categoria": "Herramientas eléctricas", "precio": 29990, "stock": 9, "imagen": "images/14-lijadora-orbital.jpg"},
    {"id": 15, "nombre": "Caladora 6.5A", "categoria": "Herramientas eléctricas", "precio": 34990, "stock": 6, "imagen": "images/15-caladora.jpg"},
    {"id": 16, "nombre": "Compresor de aire 6 HP", "categoria": "Herramientas eléctricas", "precio": 189990, "stock": 3, "imagen": "images/16-compresor.jpg"},
    {"id": 17, "nombre": "Pistola de calor 1500W", "categoria": "Herramientas eléctricas", "precio": 19990, "stock": 11, "imagen": "images/17-pistola-calor.jpg"},
    {"id": 18, "nombre": "Soldador inversor 200A", "categoria": "Herramientas eléctricas", "precio": 89990, "stock": 4, "imagen": "images/18-soldador.jpg"},
    {"id": 19, "nombre": "Generator portátil 3500W", "categoria": "Herramientas eléctricas", "precio": 299990, "stock": 2, "imagen": "images/19-generator.jpg"},
    {"id": 20, "nombre": "Tornillos para madera #8 x 2\"", "categoria": "Fijaciones", "precio": 2990, "stock": 200, "imagen": "images/20-tornillos.jpg"},
    {"id": 21, "nombre": "Clavos de acero 3 pulgadas", "categoria": "Fijaciones", "precio": 1990, "stock": 300, "imagen": "images/21-clavos.jpg"},
    {"id": 22, "nombre": "Tarugos de nailon 6mm", "categoria": "Fijaciones", "precio": 3490, "stock": 150, "imagen": "images/22-tarugos.jpg"},
    {"id": 23, "nombre": "Anclajes químicos 300ml", "categoria": "Fijaciones", "precio": 12990, "stock": 25, "imagen": "images/23-anclajes.jpg"},
    {"id": 24, "nombre": "Bisagras reforzadas 3 pulgadas", "categoria": "Fijaciones", "precio": 4990, "stock": 80, "imagen": "images/24-bisagras.jpg"},
    {"id": 25, "nombre": "Candado de seguridad 60mm", "categoria": "Fijaciones", "precio": 7990, "stock": 30, "imagen": "images/25-candado.jpg"},
    {"id": 26, "nombre": "Pintura acrílica blanca 1 galón", "categoria": "Pinturas y acabados", "precio": 18990, "stock": 45, "imagen": "images/26-pintura.jpg"},
    {"id": 27, "nombre": "Pintura esmalte negro 1 galón", "categoria": "Pinturas y acabados", "precio": 21990, "stock": 0, "imagen": "images/27-pintura-esmalte.jpg"},
    {"id": 28, "nombre": "Rodillo de fieltro 9 pulgadas", "categoria": "Pinturas y acabados", "precio": 5990, "stock": 35, "imagen": "images/28-rodillo.jpg"},
    {"id": 29, "nombre": "Brocha 4 pulgadas", "categoria": "Pinturas y acabados", "precio": 3990, "stock": 60, "imagen": "images/29-brocha.jpg"},
    {"id": 30, "nombre": "Masking tape 2 pulgadas", "categoria": "Pinturas y acabados", "precio": 2990, "stock": 100, "imagen": "images/30-masking-tape.jpg"},
    {"id": 31, "nombre": "Lija grano 120 (10 hojas)", "categoria": "Pinturas y acabados", "precio": 4990, "stock": 70, "imagen": "images/31-lija.jpg"},
    {"id": 32, "nombre": "Lodo para pared 25kg", "categoria": "Pinturas y acabados", "precio": 14990, "stock": 20, "imagen": "images/32-lodo.jpg"},
    {"id": 33, "nombre": "Tubo PVC 2\" x 6m", "categoria": "Plomería", "precio": 8990, "stock": 40, "imagen": "images/33-tubo-pvc.jpg"},
    {"id": 34, "nombre": "Codo PVC 90° 1/2\"", "categoria": "Plomería", "precio": 990, "stock": 120, "imagen": "images/34-codo-pvc.jpg"},
    {"id": 35, "nombre": "Llave de paso 1/2\"", "categoria": "Plomería", "precio": 12990, "stock": 18, "imagen": "images/35-llave-paso.jpg"},
    {"id": 36, "nombre": "Silicona transparente 300ml", "categoria": "Plomería", "precio": 4990, "stock": 55, "imagen": "images/36-silicona.jpg"},
    {"id": 37, "nombre": "Cinta teflón 1/2\"", "categoria": "Plomería", "precio": 1490, "stock": 90, "imagen": "images/37-cinta-teflon.jpg"},
    {"id": 38, "nombre": "Cable THW #12 (100m)", "categoria": "Electricidad", "precio": 69990, "stock": 15, "imagen": "images/38-cable.jpg"},
    {"id": 39, "nombre": "Interruptor simple polaridad", "categoria": "Electricidad", "precio": 2990, "stock": 85, "imagen": "images/39-interruptor.jpg"},
    {"id": 40, "nombre": "Lámpara LED 15W dulce", "categoria": "Electricidad", "precio": 4990, "stock": 0, "imagen": "images/40-lampara.jpg"},
]

CATEGORIAS = [
    "Herramientas manuales",
    "Herramientas eléctricas",
    "Fijaciones",
    "Pinturas y acabados",
    "Plomería",
    "Electricidad",
]


def _hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# === USUARIOS ===

def _cargar_usuarios():
    if not os.path.exists(USUARIOS_FILE):
        admin = {
            "username": "admin",
            "email": "admin@ferreteria.cl",
            "password": _hash_password("admin123"),
            "rol": "admin",
        }
        _guardar_usuarios([admin])
        return [admin]
    with open(USUARIOS_FILE, "r", encoding="utf-8") as f:
        usuarios = json.load(f)
    admin_existe = any(u["username"] == "admin" for u in usuarios)
    if not admin_existe:
        admin = {
            "username": "admin",
            "email": "admin@ferreteria.cl",
            "password": _hash_password("admin123"),
            "rol": "admin",
        }
        usuarios.append(admin)
        _guardar_usuarios(usuarios)
    return usuarios


def _guardar_usuarios(usuarios):
    with open(USUARIOS_FILE, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=2, ensure_ascii=False)


def _autenticar(username, password):
    usuarios = _cargar_usuarios()
    hash_pw = _hash_password(password)
    for u in usuarios:
        if u["username"] == username and u["password"] == hash_pw:
            return u
    return None


def _usuario_existe(username):
    usuarios = _cargar_usuarios()
    return any(u["username"] == username for u in usuarios)


def _es_admin(username):
    usuarios = _cargar_usuarios()
    for u in usuarios:
        if u["username"] == username:
            return u.get("rol") == "admin"
    return False


# === PRODUCTOS ===

def _cargar_productos():
    if not os.path.exists(PRODUCTOS_FILE):
        _guardar_productos(PRODUCTOS_DEFAULT)
        return PRODUCTOS_DEFAULT[:]
    with open(PRODUCTOS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _guardar_productos(productos):
    with open(PRODUCTOS_FILE, "w", encoding="utf-8") as f:
        json.dump(productos, f, indent=2, ensure_ascii=False)


def _siguiente_id(productos):
    if not productos:
        return 1
    return max(p["id"] for p in productos) + 1


# === CARRITO ===

def _carrito_file(username):
    return os.path.join(BASE_DIR, f"carrito_{username}.json")


def _cargar_carrito(username):
    path = _carrito_file(username)
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _guardar_carrito(username, carrito):
    path = _carrito_file(username)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(carrito, f, indent=2, ensure_ascii=False)


# === VISTAS PÚBLICAS ===

def landing_page(request):
    username = request.session.get("username")
    es_admin = _es_admin(username) if username else False
    cart_count = len(_cargar_carrito(username)) if username else 0
    return render(request, "catalogo/landing.html", {
        "username": username,
        "es_admin": es_admin,
        "cart_count": cart_count,
    })


def lista_productos(request):
    productos = _cargar_productos()
    total = len(productos)
    disponibles = sum(1 for p in productos if p["stock"] > 0)
    agotados = total - disponibles
    username = request.session.get("username")
    es_admin = _es_admin(username) if username else False
    cart_count = len(_cargar_carrito(username)) if username else 0
    context = {
        "productos": productos,
        "total": total,
        "disponibles": disponibles,
        "agotados": agotados,
        "username": username,
        "es_admin": es_admin,
        "cart_count": cart_count,
    }
    return render(request, "catalogo/lista.html", context)


def detalle_producto(request, producto_id):
    productos = _cargar_productos()
    producto = None
    for p in productos:
        if p["id"] == producto_id:
            producto = p
            break
    if producto is None:
        raise Http404("Producto no encontrado")
    username = request.session.get("username")
    es_admin = _es_admin(username) if username else False
    cart_count = len(_cargar_carrito(username)) if username else 0
    return render(request, "catalogo/detalle.html", {
        "producto": producto,
        "username": username,
        "es_admin": es_admin,
        "cart_count": cart_count,
    })


# === AUTH ===

def vista_login(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = _autenticar(username, password)
        if user is not None:
            request.session["username"] = user["username"]
            messages.success(request, f"Bienvenido, {username}!")
            return redirect("catalogo:lista")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
            return render(request, "catalogo/login.html", {"error": True})
    return render(request, "catalogo/login.html")


def vista_registro(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        errores = []
        if not username:
            errores.append("El usuario es obligatorio.")
        if len(username) < 3:
            errores.append("El usuario debe tener al menos 3 caracteres.")
        if username == "admin":
            errores.append("Ese nombre de usuario no está disponible.")
        if _usuario_existe(username):
            errores.append("Ese usuario ya existe.")
        if password1 != password2:
            errores.append("Las contraseñas no coinciden.")
        if len(password1) < 8:
            errores.append("La contraseña debe tener al menos 8 caracteres.")

        if errores:
            return render(request, "catalogo/registro.html", {"errores": errores, "username": username, "email": email})

        usuarios = _cargar_usuarios()
        nuevo_usuario = {
            "username": username,
            "email": email,
            "password": _hash_password(password1),
            "rol": "usuario",
        }
        usuarios.append(nuevo_usuario)
        _guardar_usuarios(usuarios)

        request.session["username"] = username
        messages.success(request, "Cuenta creada exitosamente.")
        return redirect("catalogo:lista")

    return render(request, "catalogo/registro.html")


def vista_logout(request):
    request.session.flush()
    messages.info(request, "Sesión cerrada.")
    return redirect("catalogo:lista")


# === ADMIN: CRUD PRODUCTOS ===

def admin_productos(request):
    username = request.session.get("username")
    if not username or not _es_admin(username):
        messages.error(request, "No tienes acceso a esta sección.")
        return redirect("catalogo:lista")
    productos = _cargar_productos()
    return render(request, "catalogo/admin_productos.html", {
        "productos": productos,
        "username": username,
        "es_admin": True,
    })


def admin_agregar(request):
    username = request.session.get("username")
    if not username or not _es_admin(username):
        messages.error(request, "No tienes acceso a esta sección.")
        return redirect("catalogo:lista")

    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        categoria = request.POST.get("categoria", "").strip()
        precio = request.POST.get("precio", "0")
        stock = request.POST.get("stock", "0")
        imagen = request.POST.get("imagen", "").strip()

        errores = []
        if not nombre:
            errores.append("El nombre es obligatorio.")
        if not categoria:
            errores.append("La categoría es obligatoria.")
        try:
            precio = int(precio)
        except ValueError:
            errores.append("El precio debe ser un número entero.")
        try:
            stock = int(stock)
        except ValueError:
            errores.append("El stock debe ser un número entero.")

        if errores:
            return render(request, "catalogo/admin_agregar.html", {
                "errores": errores,
                "form": request.POST,
                "categorias": CATEGORIAS,
                "username": username,
                "es_admin": True,
            })

        productos = _cargar_productos()
        nuevo = {
            "id": _siguiente_id(productos),
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "stock": stock,
            "imagen": imagen if imagen else "images/01-martillo.jpg",
        }
        productos.append(nuevo)
        _guardar_productos(productos)
        messages.success(request, f"Producto '{nombre}' agregado.")
        return redirect("catalogo:admin_productos")

    return render(request, "catalogo/admin_agregar.html", {
        "categorias": CATEGORIAS,
        "username": username,
        "es_admin": True,
    })


def admin_editar(request, producto_id):
    username = request.session.get("username")
    if not username or not _es_admin(username):
        messages.error(request, "No tienes acceso a esta sección.")
        return redirect("catalogo:lista")

    productos = _cargar_productos()
    producto = None
    for p in productos:
        if p["id"] == producto_id:
            producto = p
            break
    if producto is None:
        raise Http404("Producto no encontrado")

    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        categoria = request.POST.get("categoria", "").strip()
        precio = request.POST.get("precio", "0")
        stock = request.POST.get("stock", "0")
        imagen = request.POST.get("imagen", "").strip()

        errores = []
        if not nombre:
            errores.append("El nombre es obligatorio.")
        if not categoria:
            errores.append("La categoría es obligatoria.")
        try:
            precio = int(precio)
        except ValueError:
            errores.append("El precio debe ser un número entero.")
        try:
            stock = int(stock)
        except ValueError:
            errores.append("El stock debe ser un número entero.")

        if errores:
            return render(request, "catalogo/admin_editar.html", {
                "errores": errores,
                "producto": {"id": producto_id, "nombre": nombre, "categoria": categoria, "precio": precio, "stock": stock, "imagen": imagen},
                "categorias": CATEGORIAS,
                "username": username,
                "es_admin": True,
            })

        for p in productos:
            if p["id"] == producto_id:
                p["nombre"] = nombre
                p["categoria"] = categoria
                p["precio"] = precio
                p["stock"] = stock
                p["imagen"] = imagen
                break
        _guardar_productos(productos)
        messages.success(request, f"Producto '{nombre}' actualizado.")
        return redirect("catalogo:admin_productos")

    return render(request, "catalogo/admin_editar.html", {
        "producto": producto,
        "categorias": CATEGORIAS,
        "username": username,
        "es_admin": True,
    })


@require_POST
def admin_eliminar(request, producto_id):
    username = request.session.get("username")
    if not username or not _es_admin(username):
        messages.error(request, "No tienes acceso a esta sección.")
        return redirect("catalogo:lista")

    productos = _cargar_productos()
    eliminado = False
    for i, p in enumerate(productos):
        if p["id"] == producto_id:
            nombre = p["nombre"]
            productos.pop(i)
            eliminado = True
            break
    if eliminado:
        _guardar_productos(productos)
        messages.success(request, f"Producto '{nombre}' eliminado.")
    else:
        messages.error(request, "Producto no encontrado.")
    return redirect("catalogo:admin_productos")


# === CARRITO ===

@require_POST
def agregar_al_carrito(request, producto_id):
    username = request.session.get("username")
    if not username:
        messages.error(request, "Inicia sesión para agregar al carrito.")
        return redirect("catalogo:login")

    productos = _cargar_productos()
    producto = None
    for p in productos:
        if p["id"] == producto_id:
            producto = p
            break
    if producto is None:
        raise Http404("Producto no encontrado")

    carrito = _cargar_carrito(username)
    for item in carrito:
        if item["id"] == producto_id:
            item["cantidad"] += 1
            _guardar_carrito(username, carrito)
            messages.success(request, f"'{producto['nombre']}' agregado al carrito.")
            return redirect("catalogo:lista")

    carrito.append({
        "id": producto["id"],
        "nombre": producto["nombre"],
        "precio": producto["precio"],
        "imagen": producto["imagen"],
        "cantidad": 1,
    })
    _guardar_carrito(username, carrito)
    messages.success(request, f"'{producto['nombre']}' agregado al carrito.")
    return redirect("catalogo:lista")


def ver_carrito(request):
    username = request.session.get("username")
    if not username:
        messages.error(request, "Inicia sesión para ver tu carrito.")
        return redirect("catalogo:login")

    carrito = _cargar_carrito(username)
    total = sum(item["precio"] * item["cantidad"] for item in carrito)
    cart_count = len(carrito)
    return render(request, "catalogo/carrito.html", {
        "carrito": carrito,
        "total": total,
        "username": username,
        "es_admin": _es_admin(username),
        "cart_count": cart_count,
    })


@require_POST
def actualizar_carrito(request, producto_id):
    username = request.session.get("username")
    if not username:
        return redirect("catalogo:login")

    accion = request.POST.get("accion")
    carrito = _cargar_carrito(username)

    for item in carrito:
        if item["id"] == producto_id:
            if accion == "sumar":
                item["cantidad"] += 1
            elif accion == "restar":
                item["cantidad"] -= 1
                if item["cantidad"] <= 0:
                    carrito.remove(item)
            elif accion == "eliminar":
                carrito.remove(item)
            break

    _guardar_carrito(username, carrito)
    return redirect("catalogo:carrito")


@require_POST
def vaciar_carrito(request):
    username = request.session.get("username")
    if not username:
        return redirect("catalogo:login")
    _guardar_carrito(username, [])
    messages.info(request, "Carrito vaciado.")
    return redirect("catalogo:carrito")


@require_POST
def realizar_compra(request):
    username = request.session.get("username")
    if not username:
        messages.error(request, "Inicia sesión para comprar.")
        return redirect("catalogo:login")

    carrito = _cargar_carrito(username)
    if not carrito:
        messages.error(request, "Tu carrito está vacío.")
        return redirect("catalogo:carrito")

    productos = _cargar_productos()

    # Verificar stock de cada item
    sin_stock = []
    for item in carrito:
        for p in productos:
            if p["id"] == item["id"]:
                if p["stock"] < item["cantidad"]:
                    sin_stock.append(p["nombre"])
                break

    if sin_stock:
        nombres = ", ".join(sin_stock)
        messages.error(request, f"Stock insuficiente para: {nombres}. Reduce la cantidad o elimina estos productos.")
        return redirect("catalogo:carrito")

    # Descontar stock
    for item in carrito:
        for p in productos:
            if p["id"] == item["id"]:
                p["stock"] -= item["cantidad"]
                break

    _guardar_productos(productos)

    # Calcular total y subtotales
    total = 0
    items_comprados = []
    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        total += subtotal
        items_comprados.append({
            "id": item["id"],
            "nombre": item["nombre"],
            "precio": item["precio"],
            "imagen": item["imagen"],
            "cantidad": item["cantidad"],
            "subtotal": subtotal,
        })

    # Vaciar carrito
    _guardar_carrito(username, [])

    messages.success(request, "¡Compra realizada exitosamente!")
    return render(request, "catalogo/compra_exitosa.html", {
        "items": items_comprados,
        "total": total,
        "username": username,
        "es_admin": _es_admin(username),
        "cart_count": 0,
    })
