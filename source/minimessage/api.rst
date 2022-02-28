.. _minimessage-api:

API
===

Usage
^^^^^

Adding the repository

.. tab-set::

   .. tab-item:: Maven
      :sync: maven

      .. code:: xml

         <repositories>
             <!-- ... -->
             <repository> <!-- for development builds -->
               <id>sonatype-oss-snapshots</id>
               <url>https://oss.sonatype.org/content/repositories/snapshots/</url>
             </repository>
             <!-- ... -->
         </repositories>

   .. tab-item:: Gradle (Groovy)
      :sync: gradle-groovy

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

   .. tab-item:: Gradle (Kotlin)
      :sync: gradle-kotlin

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

.. tab-set::

   .. tab-item:: Maven
      :sync: maven

      .. code:: xml

         <dependency>
            <groupId>net.kyori</groupId>
            <artifactId>adventure-text-minimessage</artifactId>
            <version>4.10.0-SNAPSHOT</version>
         </dependency>

   .. tab-item:: Gradle (Groovy)
      :sync: gradle-groovy

      .. code:: groovy

         dependencies {
            implementation "net.kyori:adventure-text-minimessage:4.10.0-SNAPSHOT"
         }


   .. tab-item:: Gradle (Kotlin)
      :sync: gradle-kotlin

      .. code:: kotlin

         dependencies {
            implementation("net.kyori:adventure-text-minimessage:4.10.0-SNAPSHOT")
         }


Getting Started
^^^^^^^^^^^^^^^

MiniMessage exposes a simple API via the ``MiniMessage`` class.

.. note::

   Previously, a Markdown mode was available. This has been temporarily removed due to some issues 
   with the new 4.10.0 parser backend, but there are plans to re-add it once time permits.

A standard instance of the serializer is available through the :java:`miniMessage()` method. This uses the default set of tags and is not in strict mode.

Additional customization of MiniMessage is possible via the Builder_.

MiniMessage allows you to both serialize components into MiniMessage strings and to parse/deserialize MiniMessage strings into components.

Here's a short example to try things out:

.. code:: java

   Audience player = ...;
   var mm = MiniMessage.miniMessage();

   Component parsed = mm.deserialize("Hello <rainbow>world</rainbow>, isn't <underlined>MiniMessage</underlined> fun?");

   player.sendMessage(parsed);


For more advanced uses, additional tag resolvers can be registered, which when given a tag name and arguments will produce a ``Tag`` instance. These are described in more detail below.

Builder
-------

To make customizing MiniMessage easier, we provide a Builder. The specific methods on the builder are explained in the javadoc.

.. code:: java

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

Error handling
--------------

By default, MiniMessage will never throw an exception caused by user input. Instead, it will treat any invalid tags as normal text. ``MiniMessage.Builder#strict(true)`` mode will enable strict mode, 
which throws exceptions on unclosed tags, but still will allow any improperly specified tags through.

To capture information on why a parse may have failed, ``MiniMessage.Builder#debug(Consumer<String>)`` can be provided, which will accept debug logging for an input string.

Tag Resolvers
^^^^^^^^^^^^^

All tag resolution goes through tag resolvers. There is one global tag resolver, which describes the tags available through a `MiniMessage` instance, plus parse-specific resolvers which can provide additional input-specific tags.

Tag resolvers are the binding between a name and arguments, and the logic to produce a ``Component`` contained in a ``Tag`` instance. They are composable so a ``TagResolver`` can produce any number of actual ``Tag`` instances. The tag name passed to resolvers will always be lower-cased, to ensure case-insensitve searches.

MiniMessage has built-in resolver types that can be used for most use-cases, including custom tags and fixed-value placeholder-style tags. For single-tag resolvers, use the static factory methods in 
``TagResolver`` and ``Placeholder``. To combine multiple resolvers, take a look at the tag resolver builder, :java:`TagResolver.builder()`.

Tag names are only allowed to contain the characters a-z, 0-9, ``_``, and ``-``. They can also optionally start with any of the following characters: ``!?#``.

Placeholder resolvers are especially useful for simple cases:

.. code:: java

    MiniMessage.miniMessage().deserialize("<gray>Hello <name> :)", Placeholder.component("name", Component.text("TEST", NamedTextColor.RED))); // return Component.text("Hello ", NamedTextColor.GRAY).append(Component.text("TEST", NamedTextColor.RED), Component.text(" :)"))
    MiniMessage.miniMessage().deserialize("<gray>Hello <name>", Placeholder.unparsed("name", "<red>TEST :)")); // returns Component.text("Hello <red>TEST :)", NamedTextColor.GRAY);
    MiniMessage.miniMessage().deserialize("<gray>Hello <name> :)", Placeholder.parsed("name", "<red>TEST")); // returns Component.text("Hello ", NamedTextColor.GRAY).append(Component.text("TEST :)", NamedTextColor.RED));
    TagResolver placeholders = TagResolver.resolver(Placeholder.parsed("name", "TEST"), Placeholder.parsed("name2", "TEST"));
    MiniMessage.miniMessage().deserialize("<gray>Hello <name> and <name2>", placeholders);


Where possible, these built-in resolvers should be used, as MiniMessage can flatten combinations of these resolvers into a more efficient format.

The builder for ``MiniMessage`` allows providing a custom tag resolver rather than the default (:java:`StandardTags.all()`), allowing 

MiniMessage also provides convenience methods to do that:

.. code:: java

    MiniMessage serializer = MiniMessage.builder()
     .tags(TagResolver.builder()
       .resolver(StandardTags.color())
       .build()
     )
     .build();

     var parsed = serializer.deserialize("<green><bold>Hai");

     // Assertion passes
     assertEquals(Component.text("<bold>Hai", NamedTextColor.GREEN), parsed);

Because the :mm:`<bold>` tag is not enabled on this builder, the bold tag is interpreted as literal text.

Handling Arguments
------------------

Tag resolvers have an :java:`ArgumentQueue` paremeter, which provides any tag arguments that are present in the input. Helper methods on :java:`Tag.Argument` can assist with conversions of the tag.

Exceptions thrown by the :java:`popOr()` methods will interrupt execution, but are not currently exposed to users outside of debug output. We plan to add an auto-completion function that can 
reveal some of this information to the user, so please do try to write useful error messaces in custom tag resolvers.

Tags
^^^^

Once a tag resolver has handled arguments, it returns a :java:`Tag` object. These objects implement the logic of producing or modifying a component tree. There are three main kinds of :java:`Tag` -- all custom implementations must implement one of these interfaces.

Pre-process
-----------

These tags implement the ``PreProcess`` interface, and have a value of a raw MiniMessage string that is replaced into the user input before parsing continues.

Due to limitations in the current parser implementation, note that pre-process tags will adjust offsets in error messages, and may inhibit tab completion. However, they are currently the only way to integrate markup fragments into a message.

Inserting
---------

These tags are fairly straightforward: they represent a literal :java:`Component`. The vast majority of Tag implementations will want 
to be :java:`Inserting` tags. :java:`Inserting` tags may also optionally be self-closing -- by default, this is only true for tags created by :java:`Placeholder.unparsed(String)` and :java:`Placeholder.component(Component)`,
so that placeholders are self-contained.

Most :doc:`standard tags <./format>` are :java:`Inserting`. These tags will either directly insert a component, or use the helper :java:`Tag.styling(StyleBuilderApplicable...)` to apply style to components.

This helper can be used to efficiently apply a collection of styles with one tag. For example, to create a :mm:`<a:[href]>Title</a>` tag, that makes the ``Title`` text into a link that opens a URL with traditional link styling, this could be used:

.. code:: java

  Component aTagExample() {
    final String input = "Hello, <a:https://kyori.net>click me!</a> but not me!";
    final MiniMessage extendedInstance = MiniMessage.builder()
      .tags(b -> b.resolver(TagResolver.resolver("a", MiniMessageTest::createA)))
      .build();

    return extendedInstance.deserialize(input);
  }

  static Tag createA(final ArgumentQueue args, final Context ctx) {
    final String link = args.popOr("The <a> tag requires exactly one argument, the link to open").value();

    return Tag.styling(
      NamedTextColor.BLUE,
      TextDecoration.UNDERLINED,
      ClickEvent.openUrl(link),
      HoverEvent.showText(Component.text("Open " + link))
    );
  }

This allows producing rich styling relatively quickly.


Modifying
---------

Modifying tags are the most complex, and most specialized of the tag types available. These tags receive the node tree and have an opportunity to analyze it before 
components are constructed, and then receive every produced child component and can modify those children. This is used for the built-in :mm:`<rainbow>` and :mm:`<gradient>` tags, 
but can be applied for similar complex transformations.

Modifying tags are first given an opportunity to visit every node of the tree in a depth-first traversal. If a ``Modifying`` instance stores any state during this traversal, its resolver should return a new instance every time to prevent state corruption.

.. note::

   The :java:`Node` API in 4.10.0 is currently not very well developed -- most aspects are still internal. Additional information can be exposed as needed by tag developers.

Once the whole parse tree has been visited, the :java:`postVisit()` method is called. This method can optionally be overridden if any additional calculations must be performed.

Next, the ``Modifying`` instance enters the application phase, where the component tree is presented to the tag for transformation. This allows the tag to *modify* the contents of these components, giving it its name.

Parser Directives
-----------------

Parser directives are a special kind of tag, as they are instructions for the parser, and therefore cannot be implemented by end users.

There is currently only one, but more may be added at any time.

``RESET``
  This indicates to the parser that this tag should close all currently open tags.


This can be used to provide the functionality of a :mm:`<reset>` tag under a different name. For example:

.. code:: java

   final var clearTag = TagResolver.resolver("clear", ParserDirective.RESET);

   final var parser = MiniMessage.builder()
     .editTags(t -> t.resolver(clearTag))
     .build();

   final Component parsed = parser.deserialize("<red>hello <bold>world<clear>, how are you?");

would add a :mm:`<clear>` tag, behaving identically to the :mm:`<reset>` tag available by default -- ", how are you?" would not be bold or colored red.
