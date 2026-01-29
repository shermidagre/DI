Tutorial Básico de reStructuredText
===================================

Sphinx utiliza reStructuredText (reST) como su lenguaje de marcado. Aquí tienes algunos ejemplos básicos.

Títulos
-------

Los títulos se crean subrayando el texto con caracteres de puntuación. La longitud del subrayado debe ser igual a la del texto.

- Nivel 1: ``==========``
- Nivel 2: ``----------``
- Nivel 3: ``~~~~~~~~~~``

Estilos de Texto
----------------

- **Texto en negrita**: ``**Texto en negrita**``
- *Texto en cursiva*: ``*Texto en cursiva*``
- ``Código monoespaciado``: ````Código monoespaciado````

Listas
------

Listas no ordenadas:

* Un elemento
* Otro elemento
  * Un sub-elemento

Listas ordenadas:

1. Primer elemento
2. Segundo elemento

Bloques de Código
-----------------

Puedes incluir bloques de código de diferentes lenguajes.

.. code-block:: python

   def hola_mundo():
       print("¡Hola, Sphinx!")

Enlaces
-------

Puedes enlazar a otras páginas o a sitios externos.

- Enlace interno: :doc:`api_reference`
- Enlace externo: `Sitio oficial de Sphinx <https://www.sphinx-doc.org/>`_
