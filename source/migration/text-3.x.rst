=======================
Migrating from text 3.x
=======================

Adventure is an evolution of the text 3.x API. If you've worked with
the text API before, the switch to Adventure should be relatively quick. 
For the most part, you'll just need to depend on the Adventure API
and the relevant :doc:`/platform/index` you support and replace references
to classes in ``net.kyori.text`` to ``next.kyori.adventure.text``, though see
below for major breaking changes.

A word of caution
-----------------

However, before you continue, it is strongly recommended you read about
:doc:`/audiences`. Unlike text, Adventure defines a standard interface for
sending content (including chat messages) to viewers. In addition, Adventure
defines interfaces for other gameplay mechanics that can be arbitrarily sent
to players.

Breaking changes from text 3.x
------------------------------

Factory methods renamed
^^^^^^^^^^^^^^^^^^^^^^^
In text 3.x, components could be constructed using the ``<type>Component.of()`` methods. 
In Adventure, we've changed to using ``Component.<type>(/*.../*)`` style methods to allow 
for easier static imports.

``LegacyComponentSerializer``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In text 3.x, you would deserialize a component that used a color code prefix that
differed from the section symbol normally used by using ``LegacyComponentSerializer.legacy().deserialize(string, altChar)``.
In Adventure, the API to use is ``LegacyComponentSerializer.legacy(altChar).deserialize(string)``.

``TextColor`` renamed to ``NamedTextColor``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to accomodate the new RGB colors introduced in 1.16, all the named text colors
were moved to the ``NamedTextColor`` class. References to the old ``TextColor`` class
should be updated to refer to ``NamedTextColor``.

Serializer
----------

If you have a need to interoperate with clients using the old text 3.x API, you
can use the ``adventure-text-serializer-legacy-text3`` artifact, which includes a
``LegacyText3ComponentSerializer`` that can convert from Adventure to text 3.x
components and back. Note that RGB colors will be downsampled.
