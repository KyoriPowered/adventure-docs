===========
MiniMessage
===========

MiniMessage is a string based format to represent Minecraft chat components in a human-readable
format that is easy to edit.

Usage
^^^^^

Adding the repository

.. tabs::

   .. group-tab:: Maven

      .. code:: xml

         <repositories>
             <!-- ... -->
             <repository> <!-- for development builds -->
               <id>sonatype-oss-snapshots</id>
               <url>https://oss.sonatype.org/content/repositories/snapshots/</url>
             </repository>
             <!-- ... -->
         </repositories>

   .. group-tab:: Gradle (Groovy)

      .. code:: groovy

         repositories {
            // for development builds
            maven {
                name = "sonatype-oss-snapshots"
                url = "https://oss.sonatype.org/content/repositories/snapshots/"
            }
            // for releases
            mavenCentral()
         }

   .. group-tab:: Gradle (Kotlin)

      .. code:: kotlin

         repositories {
            // for development builds
            maven(url = "https://oss.sonatype.org/content/repositories/snapshots/") {
                name = "sonatype-oss-snapshots"
            }
            // for releases
            mavenCentral()
         }

   Declaring the dependency:

.. tabs::

   .. group-tab:: Maven

      .. code:: xml

         <dependency>
            <groupId>net.kyori</groupId>
            <artifactId>adventure-text-minimessage</artifactId>
            <version>4.10.0-SNAPSHOT</version>
         </dependency>

   .. group-tab:: Gradle (Groovy)

      .. code:: groovy

         dependencies {
            implementation "net.kyori:adventure-text-minimessage:4.10.0-SNAPSHOT"
         }


   .. group-tab:: Gradle (Kotlin)

      .. code:: kotlin

         dependencies {
            implementation("net.kyori:adventure-text-minimessage:4.10.0-SNAPSHOT")
         }

API
^^^

MiniMessage exposes a simple API via the ``MiniMessage`` class.

.. note::

   Previously, a Markdown mode was available. This has been temporarily removed due to some issues 
   with the new 4.2.0 parser backend, but there are plans to re-add it once time permits.

A standard instance of the serializer is available through the ``miniMessage()`` method.

Additional customization of MiniMessage is possible via the Builder_.

MiniMessage allows you to both serialize components into MiniMessage strings and to parse/deserialize MiniMessage strings into components.

Format
^^^^^^

This library uses tags. Everything you do will be defined with tags. Tags have a start tag and an end tag (the ``<reset>`` tag is an exception here).
Start tags are mandatory (obviously), end tags aren't outside of ``strict`` mode.
``<yellow>Hello <blue>World<yellow>!`` and ``<yellow>Hello <blue>World</blue>!`` and even ``<yellow>Hello </yellow><blue>World</blue><yellow>!</yellow>`` all do the same.

All tag names are case-insensitive to reduce the possibility for conflict, but we recommend keeping all tag names lowercase (or at the very least, being consistent).

Some tags have inner tags. Those look like this: ``<tag:inner>stuff</tag>``. For example: ``<hover:show_text:"<red>test:TEST">TEST`` or ``<click:run_command:test>TEST``
As you can see, those sometimes contain components, sometimes just strings. Refer to the detailed docs below.

Single (``'``) and double (``"``) quotes can be used interchangeably, but for your own sanity, please stay consistent, choose one for all your messages. MiniMessage *should* handle mismatched quotes nicely tho.

The default tags try to represent components in a manner compatible with Vanilla, but simplifying some elements.
It might to helpful to use `the minecraft wiki <https://minecraft.gamepedia.com/Raw_JSON_text_format>`_ as a reference, especially for stuff like the actions and values of click and hover events.

The `MiniMessage Web Viewer <https://webui.adventure.kyori.net>`_ allows testing MiniMessage text locally, without having to spin up a Minecraft instance. 
It can be helpful to put examples from these docs into the viewer while learning.

The Components
--------------

Color
*****

Color the next parts

Tag
   ``<_colorname_>``
Arguments
   * | ``_colorname_``, any minecraft color constant: ``black``, ``dark_blue``, ``dark_green``, ``dark_aqua``, ``dark_red``, ``dark_purple``, ``gold``, ``gray``, ``dark_gray``, ``blue``, ``green``, ``aqua``, ``red``, ``light_purple``, ``yellow``, or ``white``.
     | 
     | ``dark_grey`` can be used in place of ``dark_gray``, and so can ``grey`` in place of ``gray``.
     | Hex colours are supported as well, with the format ``#RRGGBB``.
Examples
   * ``<yellow>Hello <blue>World</blue>!``
   * ``<red>This is a <green>test!``
   * ``<#00ff00>R G B!``

.. image:: /minimessage/images/color_1.png
   :alt: The result of parsing ``<yellow>Hello <blue>World</blue>!``, shown in-game in the Minecraft client's chat window
.. image:: /minimessage/images/color_2.png
   :alt: The result of parsing ``<red>This is a <green>test!``, shown in-game in the Minecraft client's chat window

Color (verbose)
***************

A more verbose way of defining colors

Tag
   ``<color:_colorNameOrHex_>``
Aliases
   ``colour``, ``c``
Arguments
   * ``_colorNameOrHex_``, can be any of the values from above (so named colors or hex colors)
Examples
   * ``<color:yellow>Hello <color:blue>World</color:blue>!``
   * ``<color:#FF5555>This is a <color:#55FF55>test!``

.. image:: /minimessage/images/color_verbose_1.png
   :alt: The result of parsing ``<color:yellow>Hello <color:blue>World</color:blue>!``, shown in-game in the Minecraft client's chat window

.. image:: /minimessage/images/color_verbose_2.png
   :alt: The result of parsing ``<color:#FF5555>This is a <color:#55FF55>test!``, shown in-game in the Minecraft client's chat window

Decoration
***********

Decorate the next parts

Tag
   ``<_decorationname_[:false]>``, or ``<!_decorationname_>`` as an alias to invert the decoration.
Arguments:
   ``_decorationname_``, Any decoration supported in Minecraft:
   
   =================   =======
   Decoration           Aliases
   =================   =======
   ``bold``            ``b``
   ``italic``          ``em`` or ``i``
   ``underlined``      ``u``
   ``strikethrough``   ``st``
   ``obfuscated``      ``obf``
   =================   =======

Examples:
   * ``<underlined>This is <bold>important</bold>!``

.. image:: /minimessage/images/decoration_1.png
   :alt: The result of parsing ``<underlined>This is <bold>important</bold>!``, shown in-game in the Minecraft client's chat window

Reset
*****

Close all currently open tags, resetting colour/decoration/etc. The reset tag cannot be closed.

In strict mode, reset tags are forbidden.

Tag
   ``<reset>``
Aliases
   ``r``
Arguments
   non
Examples
   * ``<yellow><bold>Hello <reset>world!``

.. image:: /minimessage/images/reset_1.png
   :alt: The result of parsing ``<yellow><bold>Hello <reset>world!``, shown in-game in the Minecraft client's chat window

Click
*****

Allows doing multiple things when clicking on the component.

Tag
   ``<click:_action_:_value_>``
Arguments
   * ``_action_``, the type of click event, one of `this list <https://jd.adventure.kyori.net/api/latest/net/kyori/adventure/text/event/ClickEvent.Action.html#enum.constant.summary>`_
   * ``_value_``, the argument for that particular event, refer to `the minecraft wiki <https://minecraft.gamepedia.com/Raw_JSON_text_format>`_
Examples
   * ``<click:run_command:/say hello>Click</click> to say hello``
   * ``Click <click:copy_to_clipboard:Haha you suck> this </click>to copy your score!``

.. image:: /minimessage/images/click_1.png
   :alt: The result of parsing ``<click:run_command:/say hello>Click</click> to say hello``, shown in-game in the Minecraft client's chat window

Hover
*****

Allows doing multiple things when hovering on the component.

Tag
   ``<hover:_action_:_value..._>``
Arguments
   * ``_action_``, the type of hover event, one of this `list <https://jd.adventure.kyori.net/api/latest/net/kyori/adventure/text/event/HoverEvent.Action.html#field.summary>`_
   * ``_value..._``, arguments specific to each event action:
     
     .. list-table:: Arguments for each action
        :header-rows: 1

        * - Action
          - Value
        * - ``show_text``
          - ``_text_`` (a MiniMessage string) 
        * - ``show_item``
          - ``_type_[:_count_[:tag]]`` (a ``Key`` for the item's type, optionally followed by count (an integer) and tag (a SNBT string))
        * -  ``show_entity``
          -  ``_type_:_uuid_[:_name_]`` (a ``Key`` ID of the entity type, the entity's UUID, and an optional custom name)

Examples
   * ``<hover:show_text:'<red>test'>TEST``

.. image:: /minimessage/images/hover_1.png
   :alt: The result of parsing ``<hover:show_text:'<red>test'>TEST``, shown in-game in the Minecraft client's chat window

Keybind
*******

Allows displaying the configured key for actions

Tag
   ``<key:_key_>``
Arguments
   * ``_key_``, the keybind identifier of the action
Examples
   * ``Press <red><key:key.jump> to jump!``

.. image:: /minimessage/images/key_1.png
   :alt: The result of parsing ``Press <red><key:key.jump> to jump!``, shown in-game in the Minecraft client's chat window

Translatable
************

Allows displaying minecraft messages using the player locale

Tag
   ``<lang:_key_:_value1_:_value2_...>``
Aliases
   ``tr``, ``translate``
Arguments
   * ``_key_``, the translation key
   * ``_valueX_``, optional values that are used for placeholders in the key (they will end up in the ``with`` tag in the json)
Examples
   * ``You should get a <lang:block.minecraft.diamond_block>!``
   * ``<lang:commands.drop.success.single:'<red>1':'<blue>Stone'>!``

.. image:: /minimessage/images/translatable_1.png
   :alt: The result of parsing ``You should get a <lang:block.minecraft.diamond_block>!``, shown in-game in the Minecraft client's chat window in English
.. image:: /minimessage/images/translatable_2.png
   :alt: The result of parsing ``<lang:commands.drop.success.single:'<red>1':'<blue>Stone'>!``, shown in-game in the Minecraft client's chat window in English

Insertion
*********

Allow insertion of text into chat via shift click

Tag
   ``<insertion:_text_>``
Arguments
   * ``_text_``, the text to insert
Examples
   * ``Shift-click <insert:test>this</insert> to insert!``

.. image:: /minimessage/images/insertion_1.png
   :alt: The result of parsing ``Shift-click <insert:test>this</insert> to insert!``, shown in-game in the Minecraft client's chat window

Rainbow
*******

Rainbow colored text?!

Tag
   ``<rainbow:[!][phase]>``
Arguments
   * phase, optional
   * ``!``, literal value which reverses the rainbow, optional
Examples
   * ``<yellow>Woo: <rainbow>||||||||||||||||||||||||</rainbow>!``
   * ``<yellow>Woo: <rainbow:!>||||||||||||||||||||||||</rainbow>!``
   * ``<yellow>Woo: <rainbow:2>||||||||||||||||||||||||</rainbow>!``
   * ``<yellow>Woo: <rainbow:!2>||||||||||||||||||||||||</rainbow>!``

.. image:: /minimessage/images/rainbow_1.png
   :alt: The result of parsing all four examples in series, shown in-game in the Minecraft client's chat window

Gradient
********

Gradient colored text

Tag
   ``<gradient:[color1]:[color...]:[phase]>``
Arguments
   a list of 1 to n colors, either hex or named colors and an optional phase param (range -1 to 1) allows you to shift the gradient around, creating animations.
Examples
   * ``<yellow>Woo: <gradient>||||||||||||||||||||||||</gradient>!``
   * ``<yellow>Woo: <gradient:#5e4fa2:#f79459>||||||||||||||||||||||||</gradient>!``
   * ``<yellow>Woo: <gradient:#5e4fa2:#f79459:red>||||||||||||||||||||||||</gradient>!``
   * ``<yellow>Woo: <gradient:green:blue>||||||||||||||||||||||||</gradient>!``

.. image:: /minimessage/images/gradient_1.png
   :alt: The result of parsing the examples for the gradint tag, shown in-game in the Minecraft client's chat window

Font
****

Allows to change the font of the text

Tag
   ``<font:key>``
Arguments
   the namespaced key of the font, defaulting to ``minecraft``
Examples
   * ``Nothing <font:uniform>Uniform <font:alt>Alt  </font> Uniform``
   * ``<font:myfont:custom_font>Uses a custom font from a resource pack</font>``

.. image:: /minimessage/images/font_1.png
   :alt: The result of parsing ``Nothing <font:uniform>Uniform <font:alt>Alt  </font> Uniform``, shown in-game in the Minecraft client's chat window

Custom tags
^^^^^^^^^^^

MiniMessage provides two systems for placeholders. Depending on how you count. Could be 4 too.

The easiest one is simple string replacements:
``MiniMessage.miniMessage().parse("<gray>Hello <name>", "name", "MiniDigger")``

As you can see, placeholders are defined like normal tags in the message, and resolve by a list of key value pairs (you can also pass a ``Map<String, String>`` here).

These placeholders are resolved before any other tags in the message. This means, replacements can contain MiniMessage tags:
 .. code:: java

    final TagResolver name = Placeholder.parsed("<rank> MiniDigger");
    final TagResolver rank = Placeholder.parsed("<red>[ADMIN]</red>");

    MiniMessage.miniMessage().parse("<gray>Hello <name>", name, rank)

Template
----------

A second system, the template system, allows you to choose between string and full components as replacements.
These are executed in the main parse loop, so the string replacements can not contain MiniMessage Tags!

.. code:: java

    MiniMessage.miniMessage().parse("<gray>Hello <name>", Template.of("name", Component.text("TEST", NamedTextColor.RED)));
    MiniMessage.miniMessage().parse("<gray>Hello <name>", Template.of("name", "TEST"));
    List<Template> templates = List.of(Template.of("name", "TEST"), Template.of("name2", "TEST"));
    MiniMessage.miniMessage().parse("<gray>Hello <name> and <name2>", templates);

These are pretty powerful and allow you to take components you got from elsewhere (for example an itemstack or a placeholder api) and include them in your messages easily.

Placeholder resolver
--------------------

To make dealing with (external or internal) placeholder apis even easier, MiniMessage allows you to provide a placeholder resolver.

A placeholder resolver is just a ``Function<String, @Nullable ComponentLike>``, that allows you to handle tags without having to define them before hand.
Just return a Component when you resolved the placeholder, else you return ``null``.

You can define such a resolver using the builder api (for more info, see the Builder_ section below):

.. code :: java

    Function<String, ComponentLike> resolver = (name) -> {
        if (name.equalsIgnoreCase("test")) {
            return Component.text("TEST").color(NamedTextColor.RED);
        }
        return null;
    };

    Component result = MiniMessage.builder().placeholderResolver(resolver).build().deserialize("<green><bold><test>");

Customization
^^^^^^^^^^^^^

MiniMessage is designed to be extended, configured and adjusted to fit your needs.

Transformations
---------------

At the core, its build around the concept of transformations. A transformation is a object, that transforms a component, by changing its style or adding events, some even delete the original component and replace it with new ones.
Explaining all possibilities would be out of scope for this documentation, if you are interested in implementing your own transformations, look at the built-in ones as a guide.

When the parser encounters a start tag, it will look it up in the transformation registry, and if it finds something, the transformation will be loaded (as in, initialized with the tag name and its parameters) and then added to a list.
When the parser then encounters a string, it will apply all transformations onto that tag.
When the parser encounters a close tag, the transformation for that tag will be removed from the list again, so that further strings will not be transformed anymore.

Transformations are registered into the transformation registry using transformation types.
A transformation type defines a predicate, to check if the given tag can be parsed by the transformation, and a transformation parser, which handles initialization of transformations.

This predicate will always receive a fully lower-case tag name, to ease comparisons.

MiniMessage allows you to pass your own transformation registry, which allows you to both disable built-in transformation types, only allowing a few transformation types or even passing your own transformation types.
MiniMessage also provides convenience methods to do that:

.. code:: java

    MiniMessage serializer = MiniMessage.builder()
     .tags(b -> b.clear().add(TransformationType.COLOR))
     .build();

     var parsed = serializer.parse("<green><bold>Hai");

     // Assertion passes
     assertEquals(Component.text("<bold>Hai", NamedTextColor.GREEN), parsed);

Bold transformation isn't enabled -> bold tag is not parsed.

Builder
-------

To make customizing MiniMessage easier, we provide a Builder. Use is pretty self explanatory:

.. code :: java

    MiniMessage minimessage = MiniMessage.builder()
        .tags(TagResolver.builder()
          .resolver(StandardTags.color())
          .resolver(StandardTags.decorations())
          .resolver(this.additionalPlaceholders)
         )
        .build();

.. tip::
   
   It's a good idea to initialize such a MiniMessage instance once, in a central location, and then use it for all your messages.
   Exception being if you want to customize MiniMessage based on permissions of a user (for example, admins should be allowed to use color and decoration in the message, normal users not)
