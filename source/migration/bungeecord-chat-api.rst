======================================
Migrating from the BungeeCord Chat API
======================================

Adventure's text API and the BungeeCord Chat API are designed along very different
lines. This page goes over some notable differences.

Differences in ``ComponentBuilder``
-----------------------------------

The BungeeCord ``ComponentBuilder`` treats each component independently and allows you
to manually carry over styles from a prior component. In Adventure, there are multiple
``ComponentBuilder`` s. The closest equivalent for a BungeeCord ``ComponentBuilder`` is
to append components to a top-level empty component using ``TextComponent.builder("")``
as a base. To replicate the behavior of ``ComponentBuilder``, consider the following:

  * Use the ``Style`` class to store common styles and the ``mergeStyle`` method for
    applying formatting manually.

As an example, this BungeeCord component:

.. code:: java

  new ComponentBuilder("hello")
    .color(ChatColor.GOLD)
    .append(" world", FormatRetention.NONE)
    .build()

becomes this Adventure equivalent:

.. code:: java

  TextComponent.builder("")
    .append(TextComponent.of("hello", NamedTextColor.GOLD)
    .append(TextComponent.of(" world"))
    .build()


Immutability
------------

In the BungeeCord Chat API, all components are mutable. Adventure text components,
however, are immutable - any attempt to change a component results in a new component
being created that is a copy of the original component with the change you requested.

Decoration and Styling
----------------------

The BungeeCord Chat API stores all decorations in the ``BaseComponent``.

Serializers
-----------

The BungeeCord Chat API includes three serializers. All three have equivalents in Adventure:

  * The ``TextComponent.fromLegacyText()`` deserialization method is equivalent to the
    ``deserialize`` method of the :doc:`/serializer/legacy` text serializer. Likewise, the
    ``BaseComponent.toLegacyText()`` serialization method is equivalent to the ``serialize``
    method on the legacy text serializer.
  * The ``TextComponent.toPlainText()`` serialization method is equivalent to the
    ``serialize`` method of the :doc:`/serializer/plain` text serializer. A component can be
    created from a plain-text string using ``TextComponent.of(string)``.
  * The Adventure equivalent of ``ComponentSerializer`` is the :doc:`/serializer/gson` text
    serializer.