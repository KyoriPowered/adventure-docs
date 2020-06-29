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
   final TextComponent textComponent = TextComponent.of("Hello ")
     .color(TextColor.GOLD)
     .append(
       TextComponent.of("world")
         .color(TextColor.AQUA).
         decoration(TextDecoration.BOLD, true)
     )
     .append(TextComponent.of("!").color(TextColor.RED));

   // Converts textComponent to the JSON form used for serialization by Minecraft.
   String json = GsonComponentSerializer.gson().serialize(textComponent);

   // Converts textComponent to a legacy string - "&6Hello &b&lworld&c!"
   String legacy = LegacyComponentSerializer.legacy().serialize(textComponent, '&');

   // Converts textComponent to a plain string - "Hello world!"
   String plain = PlainComponentSerializer.INSTANCE.serialize(textComponent);

The same is of course also possible in reverse for deserialization.

.. code:: java

   // Converts JSON in the form used for serialization by Minecraft to a Component
   Component component = GsonComponentSerializer.gson().deserialize(json);

   // Converts a legacy string (using formatting codes) to a TextComponent
   TextComponent component = LegacyComponentSerializer.legacy().deserialize("&6Hello &b&lworld&c!", '&');

   // Converts a plain string to a TextComponent
   TextComponent component = PlainComponentSerializer.INSTANCE.deserialize("Hello world!");
