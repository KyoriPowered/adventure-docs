============================================
MiniMessage (Textual format for components)
============================================

String based format to represent components easily, focusing on the ability to be easily editable.

Usage
^^^^^^^^^^^^^^^^^^^

Adding the repository

.. tabs::
   
   .. group-tab:: Maven

      .. code:: xml

         <repositories>
             <!-- ... -->
             <repository> <!-- for development builds -->
               <id>sonatype-oss</id>
               <url>https://oss.sonatype.org/content/repositories/snapshots/</url>
             </repository>
             <!-- ... -->
         </repositories>
   
   .. group-tab:: Gradle (Groovy)

      .. code:: groovy

         repositories {
            // for development builds
            maven {
                name = 'sonatype-oss'
                url = 'https://oss.sonatype.org/content/repositories/snapshots/'
            }
            // for releases
            mavenCentral()
         }

   .. group-tab:: Gradle (Kotlin)

      .. code:: kotlin

         repositories {
            // for development builds
            maven(url = "https://oss.sonatype.org/content/repositories/snapshots/") {
                name = "sonatype-oss"
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
            <version>3.0.0-SNAPSHOT</version>
         </dependency>
   
   .. group-tab:: Gradle (Groovy)

      .. code:: groovy

         dependencies {
            implementation 'net.kyori:adventure-text-minimessage:.0.0-SNAPSHOT'
         }


   .. group-tab:: Gradle (Kotlin)

      .. code:: kotlin

         dependencies {
            implementation("net.kyori:adventure-text-minimessage:3.0.0-SNAPSHOT")
         }

API
^^^^^^^^^^^^^^^^^^^

MiniMessage exposes a simple API via the, suprise, ``MiniMessage`` class.

There are two different instances of that interface, ``instance()`` and ``withMarkDown()``, the latter one provides simple markdown support, ontop of the MiniMessage format. More about that in the Markdown_ section.

MiniMessage allows you to both serialize components into MiniMessage strings and to parse/deserialize MiniMessage strings into components.

Placeholder
^^^^^^^^^^^^^^^^^^^

TODO write about placeholders and templates

Template
----------

Format
^^^^^^^^^^^^^^^^^^^


This library uses tags. Everything you do will be defined with tags. Tags have a start tag and an end tag (the ``<reset>`` tag is an exception here).
Start tags are mandatory (obviously), end tags aren't.
``<yellow>Hello <blue>World<yellow>!`` and ``<yellow>Hello <blue>World</blue>!`` and even ``<yellow>Hello </yellow><blue>World</blue><yellow>!</yellow>`` all do the same.

Some tags have inner tags. Those look like this: ``<tag:inner>stuff</tag>``. For example: ``<hover:show_text:"<red>test:TEST">TEST`` or ``<click:run_command:test>TEST``  
As you can see, those sometimes contain components, sometimes just strings. Refer to the detailed docs below.

Single (``'``) and double (``"``) quotes can be used interchangeably, but please stay consistent. 

The components try to represent vanilla as closely as possible. 
It might to helpful to use `the minecraft wiki <https://minecraft.gamepedia.com/Raw_JSON_text_format>`_ as a reference, especially for stuff like the actions and values of click and hover events. 

A note on inner components
---------------------------


Some components (like hover and translate) support nested/inner components. This feature is a total mess. It's best to assume that it only works because of luck.  
Following things are known to be broken in inner components and should not be used:
* Colons (``:``)
* Quotation marks (both single ``'`` and double ``"``), altho you may have luck with escaping them like this ``\"``

Please don't open issues about such cases, I don't think that I'll able to fix them. PRs are welcome tho!
There are two ``@Ignore``'d unit cases that are disabled due to these limitations.

The Components
----------------

Color
******

Color the next parts

Tag
   ``<_colorname_>``  
Arguments
   * ``_colorname_``, all minecraft color constants (check `here <https://github.com/KyoriPowered/adventure/blob/master/api/src/main/java/net/kyori/adventure/text/format/NamedTextColor.java>`_)  
Examples
   * ``<yellow>Hello <blue>World</blue>!``
   * ``<red>This is a <green>test!``

.. image:: https://i.imgur.com/wB32YpZ.png
.. image:: https://i.imgur.com/vsN3OHa.png

Color (2, hex/rgb)
******************

A different, more flexible way (supports hex colors!) for colors looks like this

Tag:
   ``<color:_colorNameOrHex_>``  
Arguments: 
   * ``_colorNameOrHex_``, can be all the values from above, or hex colors (in 1.16)  
Examples
   * ``<color:yellow>Hello <color:blue>World</color:blue>!``
   * ``<color:#FF5555>This is a <color:#55FF55>test!``

.. image:: https://i.imgur.com/wB32YpZ.png
.. image:: https://i.imgur.com/vsN3OHa.png

Decoration
************

Decorate the next parts

Tag
   ``<_decorationname_>``  
Arguments: 
   * ``_decorationname_`` , all minecraft decorations (`check here <https://github.com/KyoriPowered/adventure/blob/master/api/src/main/java/net/kyori/adventure/text/format/TextDecoration.java>`_)  
Examples:
   * ``<underlined>This is <bold>important</bold>!``

.. image:: https://i.imgur.com/hREGXQy.png

Reset
************

Reset all colors, decorations, hovers etc. Doesn't have a close tag

Tag
   ``<reset>``  
Arguments
   non  
Examples
   * ``<yellow><bold>Hello <reset>world!``

.. image:: https://i.imgur.com/bjInUhj.png

Click
************

Allows doing multiple things when clicking on the component.

Tag
   ``<click:_action_:_value_>``
Arguments
   * ``_action_``, the type of click event, one of `this list <https://github.com/KyoriPowered/adventure/blob/master/api/src/main/java/net/kyori/adventure/text/event/ClickEvent.java>`_
   * ``_value_``, the argument for that particular event, refer to `the minecraft wiki <https://minecraft.gamepedia.com/Raw_JSON_text_format>`_
Examples
   * ``<click:run_command:/say hello>Click</click> to say hello``
   * ``Click <click:copy_to_clipboard:Haha you suck> this </click>to copy your score!``

.. image:: https://i.imgur.com/J82qOHn.png

Hover
************

Allows doing multiple things when hovering on the component.

Tag
   ``<hover:_action_:_value_``
Arguments
   * ``_action_``, the type of hover event, one of this `list <https://github.com/KyoriPowered/adventure/blob/master/api/src/main/java/net/kyori/adventure/text/event/HoverEvent.java>`_
   * ``_value_``, the argument for that particular event, refer to `the minecraft wiki <https://minecraft.gamepedia.com/Raw_JSON_text_format>`_
Examples
   * ``<hover:show_text:'<red>test'>TEST``

.. image:: https://i.imgur.com/VsHDPTI.png

Keybind
************

Allows displaying the configured key for actions

Tag
   ``<key:_key_>``  
Arguments
   * ``_key_``, the minecraft key of the action  
Examples
   * ``Press <red><key:key.jump> to jump!``

.. image:: https://i.imgur.com/iQmNDF6.png

Translatable
************

Allows displaying minecraft messages using the player locale

Tag
   ``<lang:_key_:_value1_:_value2_>``  
Arguments 
   * ``_key_``, the translation key  
   * ``_valueX_``, optional values that are used for placeholders in the key (they will end up in the ``with`` tag in the json)
Examples
   * ``You should get a <lang:block.minecraft.diamond_block>!``
   * ``<lang:commands.drop.success.single:'<red>1':'<blue>Stone'>!``

.. image:: https://i.imgur.com/mpdDMF6.png
.. image:: https://i.imgur.com/esWpnxm.png

Insertion
************

Allow insertion of text into chat via shift click

Tag
   ``<insertion:_text_>``  
Arguments 
   * ``_text_``, the text to insert
Examples
   * ``Click <insert:test>this</insert> to insert!``

.. image:: https://i.imgur.com/Imhom84.png

Pre
************

Tags within this tag will not be parsed, useful for player input for example

Tag
   ``<pre>``  
Arguments
   non  
Examples
   * ``<gray><<yellow><player><gray>> <reset><pre><message></pre>``

.. image:: https://i.imgur.com/pQqaJnD.png

Rainbow
************

Rainbow colored text?!

Tag
   ``<rainbow>``  
Arguments
   phase, optional  
Examples    
   * ``<yellow>Woo: <rainbow>||||||||||||||||||||||||</rainbow>!`` 
   * ``<yellow>Woo: <rainbow:2>||||||||||||||||||||||||</rainbow>!``

.. image:: https://i.imgur.com/uNbyoYk.png

Gradient
************

Gradient colored text

Tag
   ``<gradient:[color1]:[color2]>``  
Arguments
   color1 and 2, either hex or named colors  
Examples  
   * ``<yellow>Woo: <gradient>||||||||||||||||||||||||</gradient>!``
   * ``<yellow>Woo: <gradient:#5e4fa2:#f79459>||||||||||||||||||||||||</gradient>!``
   * ``<yellow>Woo: <gradient:green:blue>||||||||||||||||||||||||</gradient>!``

.. image:: https://i.imgur.com/8qYHCWk.png

Markdown
^^^^^^^^^^^^^^^^^^^

MiniMessage also comes with a very simple markdown addon. You can enable it by calling ``MiniMessage.withMarkDown()``.

Note: Markdown will not be escaped when you call ``escapeTokens``, ``stripTokens`` however will work.

The markdown parser supports the following markup:

* Bold:
   ``**bold**`` will be transformed into ``<bold>bold</bold>``

   ``__bold__`` will be transformed into ``<bold>bold</bold>`` too
* Italic:
   ``*italic*`` will be transformed into ``<italic>italic</italic>``

   ``_italic_`` will be transformed into ``<italic>italic</italic>`` too
* Underline:
   ``~~underline~~`` will be transformed into ``<underlined>underline</underlined>``

New Ideas for additional markup? Open an issue!
