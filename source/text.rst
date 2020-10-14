======================
Text (Chat Components)
======================

Components represent Minecraft chat components

Creating components
^^^^^^^^^^^^^^^^^^^

.. code:: java

   // Creates a line of text saying "You're a Bunny! Press <key> to jump!", with some colouring and styling.
   final TextComponent textComponent = Component.text("You're a ")
     .color(TextColor.color(0x443344))
     .append(Component.text("Bunny", NamedTextColor.LIGHT_PURPLE))
     .append(Component.text("! Press "))
     .append(
       Component.keybind("key.jump")
         .color(NamedTextColor.LIGHT_PURPLE)
         .decoration(TextDecoration.BOLD, true)
     )
     .append(Component.text(" to jump!"));
   // now you can send `textComponent` to something, such as a client

You can also use a builder, which is mutable, and creates one final
component with the children.

.. code:: java

   // Creates a line of text saying "You're a Bunny! Press <key> to jump!", with some colouring and styling.
   final TextComponent textComponent2 = Component.text()
     .content("You're a ")
     .color(TextColor.color(0x443344))
     .append(Component.text().content("Bunny").color(NamedTextColor.LIGHT_PURPLE).build())
     .append(Component.text("! Press "))
     .append(
       Component.keybind().keybind("key.jump")
         .color(NamedTextColor.LIGHT_PURPLE)
         .decoration(TextDecoration.BOLD, true)
         .build()
     )
     .append(Component.text(" to jump!"))
     .build();
   // now you can send `textComponent2` to something, such as a client

Serializing and deserializing components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Serialization to JSON, legacy, and plain representations is also
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
