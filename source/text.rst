======================
Text (Chat Components)
======================

Components represent Minecraft chat components

Creating components
^^^^^^^^^^^^^^^^^^^

.. code:: java

   // Creates a line of text saying "You're a Bunny! Press <key> to jump!", with some colouring and styling.
   final TextComponent textComponent = TextComponent.of("You're a ")
     .color(TextColor.GRAY)
     .append(TextComponent.of("Bunny").color(TextColor.LIGHT_PURPLE))
     .append(TextComponent.of("! Press "))
     .append(
       KeybindComponent.of("key.jump")
         .color(TextColor.LIGHT_PURPLE)
         .decoration(TextDecoration.BOLD, true)
     )
     .append(TextComponent.of(" to jump!"));
   // now you can send `textComponent` to something, such as a client

You can also use a builder, which is mutable, and creates one final
component with the children.

.. code:: java

   // Creates a line of text saying "You're a Bunny! Press <key> to jump!", with some colouring and styling.
   final TextComponent textComponent2 = TextComponent.builder().content("You're a ")
     .color(TextColor.GRAY)
     .append(TextComponent.builder("Bunny").color(TextColor.LIGHT_PURPLE).build())
     .append(TextComponent.of("! Press "))
     .append(
       KeybindComponent.builder("key.jump")
         .color(TextColor.LIGHT_PURPLE)
         .decoration(TextDecoration.BOLD, true)
         .build()
     )
     .append(TextComponent.of(" to jump!"))
     .build();
   // now you can send `textComponent2` to something, such as a client

Serializing and deserializing components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Serialization to JSON, legacy and plain representations is also
supported.

Components can be serialized with :doc:`/serializer/index`.

Using components within your application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The way you use components within your application will of course vary
depending on what you’re aiming to achieve.

However, the most common task is likely to be sending a component to
some sort of Minecraft client. The method for doing this will depend on
the platform your program is running on, however it is likely to involve
serializing the component to Minecraft’s JSON format, and then sending
the JSON through another method provided by the platform.

The text library is platform agnostic and therefore doesn’t provide any
way to send components to clients. However, some platform adapters
(which make this easy!) can be found in the
`adventure-platform <https://github.com/KyoriPowered/adventure-platform>`__
project.