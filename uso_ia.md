# Documento de uso de IA — ES1 Ferretería

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

## Parte 2: Explicación del proceso

Usé la IA principalmente para generar contenido y estructura visual. Para los productos, le pedí una lista completa de ferretería con precios realistas y me ahorró crear 40 registros manualmente. Para los templates, la IA me dio las bases de HTML y CSS que después personalicé con los colores y nombre del negocio.

Lo que más me sirvió fue la estructura de templates con herencia y los condicionales para el stock. Tuve que corregir algunos precios que no tenían sentido y adaptar las vistas para que funcionaran sin base de datos, ya que la IA asumía que usaba modelos de Django.

Aprendí a separar la lógica en la vista (calcular estadísticas, buscar por ID) y mostrarla en el template con Django template language. También entendí mejor cómo funciona la herencia de templates y los bloques {% block %}.
