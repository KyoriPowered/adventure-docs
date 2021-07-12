================
Text Serializers
================

The lowest-level way to convert between Adventure's data and other formats 
are serializers. Some serializers convert to standard formats, while others 
convert to Adventure's own formats.

.. toctree::
    :maxdepth: 1
    :caption: Serializers

    gson
    legacy
    plain

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

   // Converts textComponent to a legacy string - "&6Hello &b&lworld&c!"
   final String legacy = LegacyComponentSerializer.legacyAmpersand().serialize(textComponent);

   // Converts textComponent to a plain string - "Hello world!"
   final String plain = PlainTextComponentSerializer.plain().serialize(textComponent);

The same is of course also possible in reverse for deserialization.

.. code:: java

   // Converts JSON in the form used for serialization by Minecraft to a Component
   final Component component = GsonComponentSerializer.gson().deserialize(json);

   // Converts a legacy string (using formatting codes) to a TextComponent
   final Component component = LegacyComponentSerializer.legacyAmpersand().deserialize("&6Hello &b&lworld&c!");

   // Converts a plain string to a TextComponent
   final Component component = PlainTextComponentSerializer.plain().deserialize("Hello world!");
