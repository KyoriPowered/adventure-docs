====
Ansi
====

The Ansi text serializer is an encoder that converts components to text containing
`ANSI escape codes <https://en.wikipedia.org/wiki/ANSI_escape_code>`_, which allows
for styled text in a terminal. This can then be used to, for example, output server
logs containing components while preserving their color and style.

Note that since it's an encoder, it can only serialize components, and can't
deserialize text back into components.

.. kyori-dep:: adventure-text-serializer-ansi api

Usage
-----

The Ansi text serializer is accessed using the ``AnsiComponentSerializer``.

Different kind of ANSI escape codes exist, allowing for different levels of color
precision, however, not all terminals support newer kinds of ANSI escape sequences.
By default, ``AnsiComponentSerializer`` will attempt to guess the supported kinds of
escape sequences based on the system's environment variables.

This can be overridden individually for a single serializer instance using the
``colorLevel`` method of the builder.

It can also be overriden globally using system properties, using the property
``net.kyori.ansi.colorLevel``, which can be set when launching the JVM using the
command-line option ``-Dnet.kyori.ansi.colorLevel=value``. 4 different values can
be set:

* ``none``: Prevent any ANSI escape sequences from being emitted at all.
* ``indexed16``: The original set of 16 colors.
* ``indexed256``: Slightly newer set of 256 colors.
* ``truecolor``: Full 24-bit spectrum of colors.

ANSI escape sequences can also be disabled using the ``terminal.ansi`` system property,
by setting it to ``false``.
