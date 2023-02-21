=======================
Migrating from text 3.x
=======================

Adventure is an evolution of the text 3.x API. If you've worked with
the text API before, the switch to Adventure should be relatively quick.
For the most part, you'll just need to depend on the Adventure API
and the relevant :doc:`/platform/index` you support and replace references
to classes in ``net.kyori.text`` to ``net.kyori.adventure.text``, though see
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
In text 3.x, components could be constructed using the :java:`<type>Component.of()` methods.
In Adventure, we've changed to using :java:`Component.<type>(/*...*/)` style methods to allow
for easier static imports.

Similarly, :java:`Style.of(/*...*/)` is changed to :java:`Style.style(/*...*/)`.

``.builder()``
^^^^^^^^^^^^^^
Builders are now created by calling the aforementioned factory methods with no parameters.
For example, :java:`TextComponent.builder()` becomes :java:`Component.text()`.

Note that the equivalent of :java:`TextComponent.builder("hello")` is :java:`Component.text().content("hello")`.

``.append()`` with a String argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Component builders in 3.x had a shorthand for appending a new text component: :java:`builder.append("wow")`.
In Adventure you have to write it in full, :java:`builder.append(Component.text("wow"))` in this case.

``LegacyComponentSerializer``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In text 3.x, you would deserialize a component that used a color code prefix that
differed from the section symbol normally used by using :java:`LegacyComponentSerializer.legacy().deserialize(string, altChar)`.
In Adventure, the API to use is :java:`LegacyComponentSerializer.legacy(altChar).deserialize(string)`.

To make a linking serializer you have to use the builder.
Change :java:`LegacyComponentSerializer.legacyLinking(style)`
to :java:`LegacyComponentSerializer.builder().extractUrl(style).build()`.

``TextColor`` renamed to ``NamedTextColor``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to accommodate the new RGB colors introduced in 1.16, all the named text colors
were moved to the ``NamedTextColor`` class. References to the old ``TextColor`` class
should be updated to refer to ``NamedTextColor``.

Serializer
----------

If you have a need to interoperate with clients using the old text 3.x API, you
can use the ``adventure-text-serializer-legacy-text3`` artifact, which includes a
``LegacyText3ComponentSerializer`` that can convert from Adventure to text 3.x
components and back. Note that RGB colors will be downsampled.
