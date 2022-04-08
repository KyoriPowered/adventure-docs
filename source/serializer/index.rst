================
Text Serializers
================

The lowest-level way to convert between Adventure's data and other formats 
are text serializers. Some serializers convert to standard formats, while others
convert to Adventure's own formats.

Components can be converted using any of these serializers:

.. code:: java

   // Creates a text component
   final TextComponent textComponent = Component.text("Hello ")
     .color(NamedTextColor.GOLD)
     .append(
       Component.text("world")
         .color(NamedTextColor.AQUA).
         decoration(TextDecoration.BOLD, true)
     )
     .append(Component.text("!").color(NamedTextColor.RED))
     .build();

   // Converts textComponent to the JSON form used for serialization by Minecraft.
   final String json = GsonComponentSerializer.gson().serialize(textComponent);

   // Converts textComponent to a legacy string of "&6Hello &b&lworld&c!".
   final String legacy = LegacyComponentSerializer.legacyAmpersand().serialize(textComponent);

   // Converts textComponent to a plain string of "Hello world!".
   final String plain = PlainTextComponentSerializer.plainText().serialize(textComponent);

The same is of course also possible in reverse for deserialization.

.. code:: java

   // Converts JSON in the form used for serialization by Minecraft to a Component.
   final Component component = GsonComponentSerializer.gson().deserialize(json);

   // Converts a legacy string (using formatting codes) to a TextComponent.
   final Component component = LegacyComponentSerializer.legacyAmpersand().deserialize("&6Hello &b&lworld&c!");

   // Converts a plain string to a TextComponent.
   final Component component = PlainTextComponentSerializer.plainText().deserialize("Hello world!");

.. toctree::
    :maxdepth: 1
    :caption: Contents:

    gson
    legacy
    plain
