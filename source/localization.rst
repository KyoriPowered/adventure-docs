.. _localization:

Localization
============

Adventure provides a way to utilize Minecraft's built-in localization system for client-side translations as well as an additional Adventure-specific system for translating text.

Using Minecraft's localization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To send text to a player that will be translated in the language they have selected in their client settings, use a translatable component.
For example, :java:`Component.translatable("block.minecraft.diamond_block")` will render as "Block of Diamond" (or translated to another language) when viewed by the client.
Some translation keys have arguments which are inserted into the translated content.
For example, :java:`Component.translatable("block.minecraft.player_head.named", Component.text("Kezz101"))` will render as "Kezz101's Head".
Translatable components can have styling, hover/click events and children components just like any other component type.

Resource pack language files
----------------------------

You can provide translation files in a resource pack in order to change existing translations or add new ones.
For a guide on how to do that, see the `Minecraft Wiki <https://minecraft.wiki/w/Resource_pack#Language>`_.

Using Adventure's localization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adventure also provides a way to handle localization in Adventure itself.
This can be useful in environments where you do not have access to resource packs, or wish to do translations yourself, without relying on Minecraft's translation system.

Any component that is sent to a client is ran through the ``GlobalTranslator`` using the locale of the client.
This means that if you wish to have automatic translation of components using your own translation data, you can add a ``Translator`` to the ``GlobalTranslator``.
You can either provide your own implementation of ``Translator`` or use one of the implementations that Adventure provides.

Once you have a ``Translator`` instance, you can register it to the ``GlobalTranslator`` using :java:`GlobalTranslator.translator().addSource(myTranslator)`.
This will then make it available for automatic translation across the platform.

.. warning::

  Some implementations may not use the ``GlobalTranslator`` in every area, or at all.
  For example, Paper does not use it for items, and Minestom does not use it unless specifically enabled.
  Please consult the documentation for your platform for any limitations.

Using a custom ``Translator``
-----------------------------

A ``Translator`` is a simple interface that provides two ways of translating content.

The first ``translate`` method provides the translation key and locale as an argument and expects a nullable ``MessageFormat`` in return.
This system is comparable to Minecraft's built-in localization system, using the standard Java `message format <https://docs.oracle.com/javase/8/docs/api/java/text/MessageFormat.html>`_ for arguments.

If the first ``translate`` method returns ``null`, the second method which provides the translatable component and locale as an argument can be used.
This method allows for much richer customization of the translation process as you can return an entire component.
This means you can, for example, customize the colour and styling of the translated component, rather than relying solely on strings for the message format system.

.. warning::

  If you are overriding the component ``translate`` method, you should be careful not to unintentionally lose the children of the translatable component.
  See the Javadocs for the translate method for a code example of how to avoid this common error.

Below is an example of how one might implement a custom ``Translator``.

.. code:: java

  public class MyTranslator implements Translator {

    @Override
    public @NotNull Key name() {
      // Every translator has a name which is used to identify this specific translator instance.
      return Key.key("mynamespace:mykey");
    }

    @Override
    public @Nullable MessageFormat translate(final @NotNull String key, final @NotNull Locale locale) {
      // You could retrieve a string from a properties file, a config file, or some other system.
      // An an example, we will hard-code a check for a specific key here.
      if (key.equals("mytranslation.key") && locale == Locale.US) {
        return new MessageFormat("Hello %s!", locale);
      } else {
        // If you only want to use component translation, you can override this method and always return `null`.
        return null;
      }
    }

    @Override
    public @Nullable Component translate(@NotNull TranslatableComponent component, @NotNull Locale locale) {
      // As above, we will hardcode a check here, but you should be reading this from elsewhere.
      if (key.equals("mytranslation.colorful") && locale == Locale.US) {
        return Component.text("Hello, ", NamedTextColor.GREEN)
          .append(component.arguments().get(0).color(NamedTextColor.RED))
          .append(component.children()); // Always make sure to copy the children over!
      } else {
        return null;
      }
    }
  }

Using a ``TranslationRegistry``
-------------------------------

A ``TranslationRegistry`` is a collection of ``Translator`` instances.
It can provide a simpler way creating a ``Translator`` without having to implement the logic for determining translations yourself.
You can create a translation registry and then add or remove translations at will.
This allows you to retain the same functionality as a ``Translator`` without the overhead of writing your own logic for determining the translations.

There are also methods on ``TranslationRegistry`` to bulk register from `resource bundles <https://docs.oracle.com/javase/8/docs/api/java/util/ResourceBundle.html>`_.
You may also want to use Adventure's ``UTF8ResourceBundleControl`` utility class to create your bundle.

.. code:: java

  // As above, every translator needs an identifying key!
  final TranslationRegistry myRegistry = TranslationRegistry.create(Key.key("mynamespace:mykey"));

  // You can add translations one-by-one, or in bulk. Consult the Javadocs for a full list of methods.
  myRegistry.register("mytranslation.key", Locale.US, new MessageFormat("Hello %s!", Locale.US));

  // You can then register this to the global translator so the translations are available there!
  GlobalTranslator.translator().addSource(myRegistry);

Using ``MiniMessageTranslator``
-------------------------------

Adventure also provides a translator that can use MiniMessage strings, with automatic support for placeholders and arguments.
For more information, see :ref:`minimessage-translator`.
