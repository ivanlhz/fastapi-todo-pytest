# Ejemplo de un TODOLIST usando arquitectura modular
Este ejemplo es un ejemplo de API simple de un gestor de tareas para ejemplificar como usar una arquitectura modular con FastApi. Tambien se han inlcluido test de los distintos endpoints.

## Beneficios de una Arquitectura Modular
1. **Mejor mantenimiento:** Cada componente, routers, controllers, services y repositories, tiene su responsabilidad única, reduciendo el riesgo de efectos no esperados cuando se hacen cambios.
2. **Mejora de testeabilidad:** Con capas diferenciadas, las pruebas unitarias se vuelven más sencillas. Podemos probar cada componente de forma aislada, garantizando la robustez y fiabilidad en toda nuestra aplicación..
3. **Escabilidad y flexibilidad:** El diseño modular facilita una escalabilidad más sencilla. Se pueden agregar nuevas características o modificar las existentes sin tener que rehacer gran parte del código. Esta flexibilidad también permite cambiar bases de datos o actualizar la lógica de negocio sin complicaciones.

## Getting Started
Para usar la aplicación sigue los siguientes pasos:
1. Clona el repositorio 
2. Crear un entorno virtual usando `python -m venv .venv` o `python3 -m venv .venv` en Mac y Linux
3. Activa tu entorno virutal `env\Scripts\activate` o `source env/bin/activate` en Mac y Linux
4. Instala las dependencias del proyecto `pip install -r requirements.txt` o `pip3 install -r requirements.txt` en Mac y Linux
5. Instala las dependencias para los tests `pip install -r test-requirements.txt` o `pip3 install -r test-requirements.txt` en Mac y Linux

## Ejecutar el servicio
Para lanzar la aplicacion `python app.py` o `python3 app.py`

Una vez hemos lanzado la aplicacion podemos pobrarla desde postman haciendo las peticiones que necesitemos a `http://localhost:8000/api/todos`
También podemos ver el swagger en `http://localhost:8000/docs`

## Lanzar los tests
1. Generamos el coverage `coverage run -m pytest` 
2. Generamos el report en formato html `coverage html`
3. Abrimos el coverage generado en el navegador 
    ```
    open htmlcov/index.html  # En macOS
    xdg-open htmlcov/index.html  # En Linux
    start htmlcov/index.html  # En Windows
    ```
