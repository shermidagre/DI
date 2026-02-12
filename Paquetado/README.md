
```markdown
# 📦 Guía de Comandos para Empaquetado Python

Este documento resume los comandos necesarios para construir, instalar y distribuir el paquete.

---

## 2. Generar los Archivos de Distribución (Build)

Este es el paso para crear la carpeta `dist/` con el **`.tar.gz`** y el **`.whl`**.

> **¡Importante!**: Ejecutar esto en la raíz del proyecto (donde está `pyproject.toml`).

```bash
pip install build

python -m build

```

**Resultado:**

* Se crea la carpeta `dist/`.
* Dentro verás: `paquete-x.x.x.tar.gz` (Source) y `paquete-x.x.x.whl` (Wheel).

---

## 3. Instalar el Paquete en Local (Para probarlo)

Si quieres instalar tu propia librería en tu ordenador para probar que funciona:

**Opción A: Instalación normal**
(Instala la versión actual, si cambias el código tienes que reinstalar)

```bash
pip install .

```

**Opción B: Instalación en modo editable (Recomendado para desarrollo)**
(Cualquier cambio en el código se refleja al instante sin reinstalar)

```bash
pip install -e .

```

---

## 4. Verificar el Paquete (Opcional)

Comprueba que los archivos generados no tienen errores antes de subirlos:

```bash
twine check dist/*

```

---

## 5. Limpieza (Resetear)

Si necesitas borrar todo para volver a generar el paquete desde cero, elimina estas carpetas:

* `dist/`
* `build/`
* `*.egg-info/`

En PowerShell puedes hacerlo rápido con:

```powershell
Remove-Item -Recurse -Force dist, build, *.egg-info

```


## 6. Instalación en Modo Desarrollo
Para no tener que reinstalar el paquete cada vez que edites un archivo `.py`, usa el flag `-e` (editable):

```powershell
pip install -e .

```

¿Qué hace esto? Crea un enlace simbólico en tu entorno virtual hacia tu carpeta de trabajo. Si cambias un print o una lógica en MatOperacion.py, el comando lanzador usará el código nuevo al instante.

## 2. El Comando lanzador

El comando lanzador está configurado en el archivo pyproject.toml y funciona como un acceso directo a la lógica principal de tu aplicación.

Requisitos para que funcione:
Estructura en pyproject.toml: Debe apuntar a la ruta completa: fontes.paquete_exemplo_Samuel.main:main.

Función main: El archivo main.py debe tener una función definida como def main():.

Cómo ejecutarlo:
Simplemente escribe en cualquier parte de tu terminal (con el entorno virtual activado):

```powershell
lanzador

```

