.. _minimessage-format:

Format
======

The MiniMessage language uses tags. Everything you do will be defined with tags. Tags have a start tag and an end tag (the :mm:`<reset>` tag is an exception here).
Start tags are mandatory (obviously), but end tags aren't outside of ``strict`` mode.
:mm:`<yellow>Hello <blue>World<yellow>!` and :mm:`<yellow>Hello <blue>World</blue>!` and even :mm:`<yellow>Hello </yellow><blue>World</blue><yellow>!</yellow>` are all
visually identical. For tags with no content, tags can be auto-closed by using the format :mm:`<tag/>`. With this format, even in strict mode no separate closing tag should be provided.

All tag names are case-insensitive to reduce the possibility for conflict, but we recommend keeping all tag names lowercase (or at the very least, being consistent).

Some tags have argument. Those look like this: :mm:`<tag:argument>stuff</tag>`. For example: :mm:`<hover:show_text:"<red>test:TEST">TEST` or :mm:`<click:run_command:test>TEST`
As you can see, those sometimes contain components, sometimes just numbers, strings, or other types. Refer to the detailed docs below.

Single (``'``) and double (``"``) quotes can be used interchangeably. We recommend staying consistent, though in order to minimize escaping it might make more sense to switch quote types for some arguments.

Any meaningful token can be escaped in the locations where they have influence. In plain text, tag open characters (``<``) can be escaped with a leading backslash (``\``). Within quoted strings,
the opening quote character can be escaped (``'`` or ``"``). In either place, the escape character can be escaped in places where it would otherwise be relevant. Unquoted tag arguments cannot have escapes, for simplicity.
In locations where escaping is not supported, the literal escape character will be passed through. In locations where escaping *is* supported but a literal escape character is desired, the escape character can itself be escaped to produce a ``\``.

The default tags try to represent components in a manner compatible with Vanilla, but simplifying some elements. It might be helpful to
use `the minecraft wiki <https://minecraft.wiki/w/Raw_JSON_text_format>`_ as a reference for the Vanilla component system, especially
for things like the actions and values of click and hover events.

The `MiniMessage Web Viewer <https://webui.advntr.dev>`_ allows testing MiniMessage text locally, without having to spin up a Minecraft instance.
It can be helpful to put examples from these docs into the viewer while learning.

Strict mode
-----------

By default, MiniMessage is extremely lenient, and any invalid tags will just be ignored. Any tags left unclosed at the end of an input string will be automatically closed.

Applications can optionally enable *strict mode*, which prohibits using :mm:`<reset>`, and requires all tags to be closed in reverse order of opening. Any application
using MiniMessage should make it clear to end users which language variant is being used.

Standard tags
-------------

These are the tags included and enabled by default in MiniMessage. Specific parses of MiniMessage may add custom tags to this list, or restrict the available tags to a subset of this list. Consult application documentation for details.

Color
*****

Color the next parts

Tag
   :mm:`<_colorname_>`
Arguments
   * | ``_colorname_``, any minecraft color constant: ``black``, ``dark_blue``, ``dark_green``, ``dark_aqua``, ``dark_red``, ``dark_purple``, ``gold``, ``gray``, ``dark_gray``, ``blue``, ``green``, ``aqua``, ``red``, ``light_purple``, ``yellow``, or ``white``.
     |
     | ``dark_grey`` can be used in place of ``dark_gray``, and so can ``grey`` in place of ``gray``.
     | Hex colors are supported as well, with the format ``#RRGGBB``.
Examples
   * :mm:`<yellow>Hello <blue>World</blue>!`
   * :mm:`<red>This is a <green>test!`
   * :mm:`<#00ff00>R G B!`

.. image:: /minimessage/images/color_1.png
   :alt: The result of parsing ``<yellow>Hello <blue>World</blue>!``, shown in-game in the Minecraft client's chat window
.. image:: /minimessage/images/color_2.png
   :alt: The result of parsing ``<red>This is a <green>test!``, shown in-game in the Minecraft client's chat window

Color (verbose)
***************

A more verbose way of defining colors

Tag
   :mm:`<color:_colorNameOrHex_>`
Aliases
   ``colour``, ``c``
Arguments
   * ``_colorNameOrHex_``, can be any of the values from above (so named colors or hex colors)
Examples
   * :mm:`<color:yellow>Hello <color:blue>World</color:blue>!`
   * :mm:`<color:#FF5555>This is a <color:#55FF55>test!`

.. image:: /minimessage/images/color_verbose_1.png
   :alt: The result of parsing ``<color:yellow>Hello <color:blue>World</color:blue>!``, shown in-game in the Minecraft client's chat window

.. image:: /minimessage/images/color_verbose_2.png
   :alt: The result of parsing ``<color:#FF5555>This is a <color:#55FF55>test!``, shown in-game in the Minecraft client's chat window

Decoration
***********

Decorate the next parts

Tag
   :mm:`<_decorationname_[:false]>`, or :mm:`<!_decorationname_>` as an alias to invert the decoration.
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
   * :mm:`<underlined>This is <bold>important</bold>!`

.. image:: /minimessage/images/decoration_1.png
   :alt: The result of parsing ``<underlined>This is <bold>important</bold>!``, shown in-game in the Minecraft client's chat window

Reset
*****

Close all currently open tags, resetting color/decoration/etc. The reset tag cannot be closed.

In strict mode, reset tags are forbidden.

Tag
   :mm:`<reset>`
Arguments
   none
Examples
   * :mm:`<yellow><bold>Hello <reset>world!`

.. image:: /minimessage/images/reset_1.png
   :alt: The result of parsing ``<yellow><bold>Hello <reset>world!``, shown in-game in the Minecraft client's chat window

Click
*****

Allows doing multiple things when clicking on the component.

Tag
   :mm:`<click:_action_:_value_>`
Arguments
   * ``_action_``, the type of click event, one of `this list <https://jd.advntr.dev/api/latest/net/kyori/adventure/text/event/ClickEvent.Action.html#enum.constant.summary>`_
   * ``_value_``, the argument for that particular event, refer to `the minecraft wiki <https://minecraft.wiki/w/Raw_JSON_text_format>`_
Examples
   * :mm:`<click:run_command:/seed>Click</click> to show the world seed!`
   * :mm:`Click <click:copy_to_clipboard:Haha you suck> this </click>to copy your score!`

.. image:: /minimessage/images/click_1.png
   :alt: The result of parsing ``<click:run_command:/seed>Click</click> to show the world seed!``, shown in-game in the Minecraft client's chat window

.. warning::
   Since the introduction of chat signatures in 1.19.1, the client no longer executes commands that require signed arguments
   like the ``/say`` or ``/tell`` command to prevent the server from sending signed messages on the clients behalf.

Hover
*****

Allows doing multiple things when hovering on the component.

Tag
   :mm:`<hover:_action_:_value..._>`
Arguments
   * ``_action_``, the type of hover event, one of this `list <https://jd.advntr.dev/api/latest/net/kyori/adventure/text/event/HoverEvent.Action.html#field.summary>`_
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
   * :mm:`<hover:show_text:'<red>test'>TEST`

.. image:: /minimessage/images/hover_1.png
   :alt: The result of parsing ``<hover:show_text:'<red>test'>TEST``, shown in-game in the Minecraft client's chat window

Keybind
*******

Allows displaying the configured key for actions

Tag
   :mm:`<key:_key_>`
Arguments
   * ``_key_``, the keybind identifier of the action
Examples
   * :mm:`Press <red><key:key.jump> to jump!`

.. image:: /minimessage/images/key_1.png
   :alt: The result of parsing ``Press <red><key:key.jump> to jump!``, shown in-game in the Minecraft client's chat window

Translatable
************

Allows displaying minecraft messages using the player locale

Tag
   :mm:`<lang:_key_:_value1_:_value2_...>`
Aliases
   ``tr``, ``translate``
Arguments
   * ``_key_``, the translation key
   * ``_valueX_``, optional values that are used for placeholders in the key (they will end up in the ``with`` tag in the JSON)
Examples
   * :mm:`You should get a <lang:block.minecraft.diamond_block>!`
   * :mm:`<lang:commands.drop.success.single:'<red>1':'<blue>Stone'>!`

.. image:: /minimessage/images/translatable_1.png
   :alt: The result of parsing ``You should get a <lang:block.minecraft.diamond_block>!``, shown in-game in the Minecraft client's chat window in English
.. image:: /minimessage/images/translatable_2.png
   :alt: The result of parsing ``<lang:commands.drop.success.single:'<red>1':'<blue>Stone'>!``, shown in-game in the Minecraft client's chat window in English

Insertion
*********

Allow insertion of text into chat via shift click

Tag
   :mm:`<insertion:_text_>`
Arguments
   * ``_text_``, the text to insert
Examples
   * :mm:`Shift-click <insert:test>this</insert> to insert!`

.. image:: /minimessage/images/insertion_1.png
   :alt: The result of parsing ``Shift-click <insert:test>this</insert> to insert!``, shown in-game in the Minecraft client's chat window

Rainbow
*******

Rainbow-colored text?!

Tag
   :mm:`<rainbow:[!][phase]>`
Arguments
   * phase, optional
   * ``!``, literal value which reverses the rainbow, optional
Examples
   * :mm:`<yellow>Woo: <rainbow>||||||||||||||||||||||||</rainbow>!`
   * :mm:`<yellow>Woo: <rainbow:!>||||||||||||||||||||||||</rainbow>!`
   * :mm:`<yellow>Woo: <rainbow:2>||||||||||||||||||||||||</rainbow>!`
   * :mm:`<yellow>Woo: <rainbow:!2>||||||||||||||||||||||||</rainbow>!`

.. image:: /minimessage/images/rainbow_1.png
   :alt: The result of parsing all four examples in series, shown in-game in the Minecraft client's chat window

Gradient
********

Gradient colored text

Tag
   :mm:`<gradient:[color1]:[color...]:[phase]>`
Arguments
   a list of 1 to n colors, either hex or named colors and an optional phase parameter (range -1 to 1) allows you to shift the gradient around, creating animations.
Examples
   * :mm:`<yellow>Woo: <gradient>||||||||||||||||||||||||</gradient>!`
   * :mm:`<yellow>Woo: <gradient:#5e4fa2:#f79459>||||||||||||||||||||||||</gradient>!`
   * :mm:`<yellow>Woo: <gradient:#5e4fa2:#f79459:red>||||||||||||||||||||||||</gradient>!`
   * :mm:`<yellow>Woo: <gradient:green:blue>||||||||||||||||||||||||</gradient>!`

.. image:: /minimessage/images/gradient_1.png
   :alt: The result of parsing the examples for the gradient tag, shown in-game in the Minecraft client's chat window


Transition
**********

Transitions between colors.
Similar to a gradient, but everything is the same color and the phase chooses that color

Tag
   :mm:`<transition:[color1]:[color...]:[phase]>`
Arguments
   a list of 1 to n colors, either hex or named colors and an optional phase parameter (range -1 to 1) allows you to shift the transition around, creating animations.
Examples
   * :mm:`<transition:#00ff00:#ff0000:0>|||||||||</transition>`
   * :mm:`<transition:white:black:red:[phase]>Hello world [phase]</transition>`

.. image:: /minimessage/images/transition_1.png
   :alt: The result of parsing ``<transition:white:black:red:[phase]>Hello World [phase]</transition>``, shown in-game in the Minecraft client's chat window


Font
****

Allows to change the font of the text

Tag
   :mm:`<font:key>`
Arguments
   the namespaced key of the font, defaulting to ``minecraft``
Examples
   * :mm:`Nothing <font:uniform>Uniform <font:alt>Alt  </font> Uniform`
   * :mm:`<font:myfont:custom_font>Uses a custom font from a resource pack</font>`

.. image:: /minimessage/images/font_1.png
   :alt: The result of parsing ``Nothing <font:uniform>Uniform <font:alt>Alt  </font> Uniform``, shown in-game in the Minecraft client's chat window

Newline
*******

Insert a newline character.

Tag
   :mm:`<newline>`
Aliases
   ``br``
Arguments
   none
Examples
   * :mm:`Let me insert a <newline>line break here.`
   * :mm:`<hover:show_text:'<red>Hover with a<newline><green>line break'>Text with<newline>line break</hover>`

.. image:: /minimessage/images/newline_1.png
   :alt: The result of parsing ``<hover:show_text:'<red>Hover with a<newline><green>line break'>Text with<newline>line break</hover>``, shown in-game in the Minecraft client's chat window

Selector
********

*(since v4.11.0)* Insert a selector component

Tag
   :mm:`<selector:_sel_[:_separator_]>`
Aliases
   ``sel``
Arguments
   * ``_sel_``, the selector pattern to insert
   * ``_separator_`` (optional), the separator to insert between values the selector matches
Examples
   * :mm:`Hello <selector:@e[limit=5]>, I'm <selector:@s>!`

.. image:: /minimessage/images/selector_1.png
   :alt: The result of parsing ``Hello <selector:@e[limit=5]>, I'm <selector:@s>!``, show in-game in the Minecraft client's chat window

Score
*****

*(since v4.13.0)* Insert a score component.

.. note::

   The score component requires *rendering* on the server to be seen by clients. This is a platform-specific operation.

Tag
   :mm:`<score:_name_:_objective_>`
Arguments:
   * ``_name_``, the name of the score holder on the server scoreboard, or a selector resolved with receiver context
   * ``_objective_``, the name of the objective to get ``name``'s score in
Examples
   * :mm:`You have won <score:rymiel:gamesWon/> games!`

NBT
*****

*(since v4.13.0)* Insert a NBT component. The syntax of this tag is intended to be familiar to users of vanilla Minecraft's ``/data`` command.

.. note::

   The produced NBT component requires *rendering* on the server to be seen by clients. This is a platform-specific operation.

Tag
   :mm:`<nbt:block|entity|storage:id:path[:_separator_][:interpret]>`
Aliases
    ``data``
Arguments:
   * ``block|entity|storage`` the type of data source to read from -- a ``block`` entity, an ``entity`` selector, or the persistent command ``storage`` container
   * ``_id_``, the position for a block NBT component, a selector for an entity NBT component, or a key (resource location) for a storage NBT component
   * ``_path_``, the NBT path to resolve from within the data source
   * ``_separator_``, the separator between multiple values, if (primarily for entity NBT) the data source returns more than one
   * ``interpret``, the literal text ``interpret`` if the result should be parsed as component JSON
Examples
   * :mm:`Your health is <nbt:entity:'@s':Health/>`
