====
ANSI
====

The ANSI text serializer is an encoder that converts components to text containing
`ANSI escape codes <https://en.wikipedia.org/wiki/ANSI_escape_code>`_, which allows
for styled text in a terminal. This can then be used to, for example, output server
logs containing components while preserving their color and style.

Note that since it's an encoder, it can only serialize components, and can't
deserialize text back into components.

.. kyori-dep:: adventure-text-serializer-ansi api

.. _ANSI Usage:

Usage
-----

The ANSI text serializer is accessed using the ``ANSIComponentSerializer``.

Different kind of ANSI escape codes exist, allowing for different levels of color
precision, however, not all terminals support newer kinds of ANSI escape sequences.
By default, ``ANSIComponentSerializer`` will attempt to guess the supported kinds of
escape sequences based on the system's environment variables.

This can be overridden individually for a single serializer instance using the
``colorLevel`` method of the builder.

It can also be overridden globally using system properties, using the property
``net.kyori.ansi.colorLevel``, which can be set when launching the JVM using the
command-line option ``-Dnet.kyori.ansi.colorLevel=value``. 4 different values can
be set:

* ``none``: Prevent any ANSI escape sequences from being emitted at all.
* ``indexed16``: The original set of 16 colors.
* ``indexed256``: Slightly newer set of 256 colors.
* ``truecolor``: Full 24-bit spectrum of colors.

ANSI escape sequences can also be disabled using the ``terminal.ansi`` system property,
by setting it to ``false``.

ANSI library
------------

.. note::
  This section talks about the component-agnostic library. If you are only interested in
  the Adventure component-specific implementation, you do not need to read this section.

The ``AnsiComponentSerializer`` is built upon a separate ANSI library, which deals with
the lower-level ANSI escape sequence logic, and also allows for creating an ANSI
converter for any kind of component, not just those by Adventure.

.. kyori-dep:: ansi ansi

Implementation usage
^^^^^^^^^^^^^^^^^^^^

To begin with, you need to create a class that implements ``StyleOps<S>``, where ``S`` is
the "style" type for your component type. This adapter class allows for the ANSI logic to
access properties about the style.

To actually begin conversion, create an instance of a ``ANSIComponentRenderer``, by using
one of the static methods, the simplest of which is ``ANSIComponentRenderer.toString()``,
passing it an instance of your ``StyleOps`` adapter described above.

Then, you will need to traverse the structure of your component's tree, using the
``pushStyle()``, ``text()`` and ``popStyle()`` methods of the renderer instance.

Finally, call ``complete()`` after traversing the tree has finished. The renderer's job
is now concluded. In the case of the ``ToString`` renderer, you can access the result
using the ``asString()`` method.

As described in the :ref:`ANSI Usage` section, the library will, by default, try to guess the
supported colors of the current environment. This may be overridden by passing a custom
``ColorLevel`` when creating the renderer, or by using the system properties as previously
described.
