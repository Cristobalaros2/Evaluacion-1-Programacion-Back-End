# Documento de uso de IA — ES1 Ferretería El Martillo

## Parte 1: Registro de consultas

### Consulta 1
**Prompt:** Genera una lista de 40 productos de ferretería en formato JSON con los campos: id, nombre, categoría, precio y stock. Incluye categorías como herramientas manuales, herramientas eléctricas, fijaciones, pinturas y acabados, plomería y electricidad. Algunos productos deben tener stock 0 para simular agotados.

**Resumen de respuesta:** Me entregó una lista completa de 40 productos con valores realistas de precios chilenos y stock variado. Distribuyó los productos en 6 categorías y aseguró que 7 productos tuvieran stock 0.

**Adaptación:** Copié la lista directamente al archivo views.py como una lista de diccionarios de Python. Ajusté algunos precios para que fueran más coherentes con el mercado local.

### Consulta 2
**Prompt:** Crea un template base.html para una ferretería llamada "Ferretería El Martillo" con header, nav, main y footer. Usa colores azules profesionales y CSS inline o en el template. Incluye herencia de templates con {% block %}.

**Resumen de respuesta:** Me dio un template completo con estructura HTML5, CSS con gradientes azules, y bloques para herencia. Incluyó un diseño responsive con grid.

**Adaptación:** Usé la estructura base y agregué el nombre del negocio. Modifiqué los colores para un tono más oscuro y profesional.

### Consulta 3
**Prompt:** Diseña una vista de catálogo en Django que muestre productos en tarjetas (cards) con CSS grid. Cada tarjeta debe mostrar nombre, categoría, precio y estado del stock. Los productos sin stock deben verse diferentes (más opacos o con borde rojo).

**Resumen de respuesta:** Me creó un template lista.html con grid de tarjetas, condicionales para stock, badges de color y efectos hover. Incluyó un resumen estadístico arriba.

**Adaptación:** Integré el template con la vista existente, asegurándome de que los campos del JSON coincidieran con los usados en el template.

### Consulta 4
**Prompt:** Crea una vista de detalle en Django para mostrar un producto individual con todos sus campos. Maneja el caso de que el producto no exista devolviendo un 404.

**Resumen de respuesta:** Me proporcionó una vista con get_object_or_404 o búsqueda manual en la lista, y un template de detalle con los mismos estilos del catálogo.

**Adaptación:** Usé la búsqueda manual en la lista (ya que no hay base de datos) y lancé Http404 directamente. Creé el template detalle.html con herencia de base.html.

### Consulta 5
**Prompt:** Agrega un resumen calculado en la vista de Django que muestre el total de productos, cuántos están disponibles y cuántos agotados. Muestra estos números en el template.

**Resumen de respuesta:** Me sugirió calcular las estadísticas en la vista usando len() y sum() con comprensiones, y pasarlas al contexto.

**Adaptación:** Implementé las estadísticas directamente en la función lista_productos y las mostré en un div de resumen en lista.html.

### Consulta 6
**Prompt:** Hazme una landing page que envuelva al catálogo. La landing debe tener un hero con imagen de fondo, sección de productos destacados, categorías con imágenes y un call to action.

**Resumen de respuesta:** Me creó una landing page completa con hero, sección de 4 productos destacados (los más caros), 6 tarjetas de categorías con imágenes de Pexels, sección de beneficios y call to action. Usó CSS con gradientes, sombras y animaciones hover.

**Adaptación:** Adapté la landing al proyecto existente, usando los productos del catálogo para los destacados. Descargué 6 imágenes de Pexels para las categorías. Conecté la landing en la ruta raíz "/" y moví el catálogo a "/catalogo/".

### Consulta 7
**Prompt:** Necesito un sistema de autenticación con usuarios guardados en un archivo JSON, no en la base de datos. Haz login, registro y logout. Las contraseñas deben estar hasheadas. Crea un usuario admin automáticamente.

**Resumen de respuesta:** Me proporcionó un sistema completo de autenticación con hash SHA-256 para contraseñas, archivo usuarios.json para persistencia, login con sesión de Django, registro con validaciones y creación automática del usuario admin.

**Adaptación:** Implementé todo en views.py con funciones auxiliares (_cargar_usuarios, _guardar_usuarios, _hashear_password, _autenticar, _es_admin). El admin se crea automáticamente al cargar la página si no existe. Agregué templates login.html y registro.html con estilos consistentes.

### Consulta 8
**Prompt:** Haz un panel de administración donde el admin pueda agregar, editar y eliminar productos. Los cambios deben guardarse en un archivo JSON para que persistan.

**Resumen de respuesta:** Me creó vistas CRUD completas (admin_lista, admin_agregar, admin_editar, admin_eliminar) con templates para cada operación. Los productos se guardan en productos.json y se recargan desde ahí.

**Adaptación:** Conecté las vistas con el sistema de autenticación existente, verificando que el usuario sea admin antes de permitir acceso. Creé templates admin_productos.html (tabla con opciones), admin_agregar.html (formulario) y admin_editar.html (formulario prellenado).

### Consulta 9
**Prompt:** Crea un carrito de compras que persista cuando el usuario cierra sesión. Que se guarde en un archivo JSON por usuario y que el usuario pueda agregar, quitar productos y modificar cantidades.

**Resumen de respuesta:** Me proporcionó un sistema de carrito persistente con archivo carrito_{username}.json por cada usuario. Incluye agregar producto, incrementar/decrementar cantidad, eliminar producto y vaciar carrito. La información persiste entre sesiones.

**Adaptación:** Implementé en views.py las funciones _cargar_carrito, _guardar_carrito y las vistas agregar_al_carrito, ver_carrito, modificar_carrito, eliminar_del_carrito y vaciar_carrito. Creé el template carrito.html con controles +/- para cantidades y botón de compra.

### Consulta 10
**Prompt:** Agrega un botón de "Comprar" en el carrito que descuente el stock de los productos y muestre una confirmación. Si no hay stock suficiente, muestre un error.

**Resumen de respuesta:** Me creó una vista de compra que valida el stock de cada producto en el carrito, descuenta las cantidades correspondientes, guarda los productos actualizados en productos.json y redirige a una página de confirmación.

**Adaptación:** Implementé la vista comprar que carga productos.json, verifica stock suficiente para cada item, descuenta y guarda. Creé template compra_exitosa.html con resumen de la compra. Agregué botón de compra verde en carrito.html con estilo distintivo.

### Consulta 11
**Prompt:** Ponle imágenes reales a los productos. Necesito 40 imágenes de productos de ferretería. Búscalas en Pexels y descárgalas.

**Resumen de respuesta:** Me proporcionó URLs de imágenes de Pexels para cada producto, con el formato de descarga directa. Me dio 40 imágenes organizadas por categoría.

**Adaptación:** Descargué las 40 imágenes una por una usando curl con las URLs de Pexels. Guardé todas en catalogo/static/images/ con nombres descriptivos (01-martillo.jpg, 02-destornillador.jpg, etc.). Corregí imágenes que no coincidían con su producto (tornillos, pintura esmalte, silicona, cinta teflón, lámpara LED).

### Consulta 12
**Prompt:** Extrae todo el CSS de los templates a un archivo externo style.css. No quiero ningún tag style en los HTML.

**Resumen de respuesta:** Me identificó todos los bloques style de base.html, lista.html y detalle.html, y los consolidó en un único archivo catalogo/static/css/style.css organizado por secciones.

**Adaptación:** Separé el CSS en secciones claras: variables, reset, header/nav, footer, cards, responsive, admin, carrito, landing, auth, alerts. Actualicé los 3 templates para usar {% static 'css/style.css' %} en lugar de CSS inline.

### Consulta 13
**Prompt:** El footer no se queda abajo, se pega al contenido. Haz que el footer siempre esté al fondo de la página sin importar cuánto contenido haya.

**Resumen de respuesta:** Me explicó el problema del sticky footer y me dio la solución con flexbox: min-height: 100vh en body, flex: 1 en main, y display: flex flex-direction: column en body.

**Adaptación:** Agregué las propiedades al CSS: body con min-height: 100vh, display: flex, flex-direction: column. Main con flex: 1. Esto empuja el footer al fondo sin importar la cantidad de contenido.

### Consulta 14
**Prompt:** Haz que el footer se vea sin tener que hacer scroll en el login.

**Resumen de respuesta:** Me sugirió reducir el padding y márgenes del header, main y footer para que todo quepa en el viewport sin scroll.

**Adaptación:** Reduje el padding del header de 1.5rem a 1rem, el margin de main de 2rem a 1.5rem, y el padding del footer de 1.2rem a 0.8rem con margin-top de 3rem a 1rem. También reduje tamaños de fuente del header.

### Consulta 15
**Prompt:** El resumen del catálogo dice "40 productos, 33 disponibles" pero no muestra los agotados. Haz que muestre "7 agotados".

**Resumen de respuesta:** Me explicó que el filtro |add de Django no hace resta correctamente con cadenas. Sugerí calcular el valor directamente en la vista y pasarlo al contexto.

**Adaptación:** Agregué la variable agotados = total - disponibles en la vista lista_productos y la pasé al contexto. Actualicé el template para usar {{ agotados }} directamente. Agregué clase CSS agotados con color rojo para distinguir visualmente.

### Consulta 16
**Prompt:** Quita el admin de Django de las URLs. No lo necesito porque tengo mi propio panel de administración.

**Resumen de respuesta:** Me sugirió eliminar la línea path('admin/', admin.site.urls) de config/urls.py y quitar django.contrib.admin de INSTALLED_APPS si no se usa.

**Adaptacióneliminé la línea de config/urls.py. django.contrib.admin sigue en INSTALLED_APPS porque es útil tenerlo disponible internamente, pero no tiene URL asociada.

### Consulta 17
**Prompt:** Reescribe el uso_ia.md con un tono personal de estudiante, no como informe técnico.

**Resumen de respuesta:** Me reescribió todo el documento en primera persona, con un tono informal pero claro, explicando qué hice y qué aprendí en cada paso.

**Adaptación:** Reescribí el archivo completo en uso_ia.md con el tono solicitado, manteniendo la estructura de las 5 consultas iniciales pero en estilo personal.

---

## Parte 2: Explicación del proceso

### Qué hice con IA

Usé la IA como asistente principal durante todo el desarrollo de la ferretería. Al principio me ayudó a generar la lista de 40 productos con precios realistas, lo que me ahorró crear cada registro manualmente. Después me dio las bases de los templates HTML y CSS que personalicé con los colores azules del negocio.

A medida que el proyecto fue creciendo, fui haciendo consultas más específicas: el sistema de autenticación con JSON, el panel de administración CRUD, el carrito de compras persistente, y la lógica de compra con descuento de stock. En cada caso, la IA me daba una estructura funcional que yo adaptaba a mi proyecto.

Las imágenes de Pexels fueron un desafío: la IA me daba las URLs pero tuve que descargarlas una por una con curl y verificar que cada imagen correspondiera al producto correcto. Algunas no coincidían y tuve que buscar las correctas.

### Qué aprendí

Aprendí a trabajar sin base de datos usando archivos JSON para persistir usuarios, productos y carritos. Esto me enseñó a manejar la serialización y deserialización de datos en Python.

También aprendí sobre herencia de templates en Django, cómo separar el CSS en archivos estáticos, y cómo usar flexbox para resolver problemas de layout como el sticky footer.

El sistema de autenticación me enseñó sobre hashing de contraseñas (SHA-256), sesiones de Django, y cómo manejar permisos de usuario (admin vs usuario regular).

Lo más importante fue aprender a adaptar el código de la IA a mis necesidades específicas. La IA me daba soluciones genéricas y yo tenía que modificarlas para que funcionaran con mi estructura de archivos JSON y sin modelos de Django.

### Qué haría diferente

Si volviera a empezar, usaría modelos de Django en lugar de archivos JSON. Aunque el enfoque con JSON funciona, es más difícil de mantener y escalar. También organizaría mejor las funciones auxiliares desde el principio, ya que al final views.py quedó bastante largo.

Las imágenes las descargaría todas de una en lugar de una por una, y verificaría que cada una coincida con su producto antes de guardarla.
