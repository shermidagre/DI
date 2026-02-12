Aquí tienes una plantilla de `README.md` (o un archivo `COMMANDS.md`) diseñada como "chuleta" para que no se te olviden los pasos.

Puedes copiar y pegar este código en un archivo nuevo en tu proyecto:

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

