.. _minimessage-api:

API
===

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


Getting Started
^^^^^^^^^^^^^^^

MiniMessage exposes a simple API via the ``MiniMessage`` class.

.. note::

   Previously, a Markdown mode was available. This has been temporarily removed due to some issues 
   with the new 4.10.0 parser backend, but there are plans to re-add it once time permits.

A standard instance of the serializer is available through the ``miniMessage()`` method.

Additional customization of MiniMessage is possible via the Builder_.

MiniMessage allows you to both serialize components into MiniMessage strings and to parse/deserialize MiniMessage strings into components.

Custom tags
^^^^^^^^^^^

MiniMessage provides two systems for placeholders. Depending on how you count. Could be 4 too.

The easiest one is simple string replacements:
``MiniMessage.miniMessage().deserialize("<gray>Hello <name>", "name", "MiniDigger")``

As you can see, placeholders are defined like normal tags in the message, and resolve by a list of key value pairs (you can also pass a ``Map<String, String>`` here).

These placeholders are resolved before any other tags in the message. This means, replacements can contain MiniMessage tags:
 .. code:: java

    final TagResolver name = Placeholder.parsed("<rank> MiniDigger");
    final TagResolver rank = Placeholder.parsed("<red>[ADMIN]</red>");

    MiniMessage.miniMessage().deserialize("<gray>Hello <name>", name, rank)

Template
----------

A second system, the template system, allows you to choose between string and full components as replacements.
These are executed in the main parse loop, so the string replacements can not contain MiniMessage Tags!

.. code:: java

    MiniMessage.miniMessage().deserialize("<gray>Hello <name>", Placeholder.component("name", Component.text("TEST", NamedTextColor.RED)));
    MiniMessage.miniMessage().deserialize("<gray>Hello <name>", Placeholder.unparsed("name", "TEST"));
    TagResolver placeholders = TagResolver.resolver(Placeholder.parsed("name", "TEST"), Placeholder.parsed("name2", "TEST"));
    MiniMessage.miniMessage().deserialize("<gray>Hello <name> and <name2>", templates);

These are pretty powerful and allow you to take components you got from elsewhere (for example an itemstack or a placeholder api) and include them in your messages easily.

Placeholder resolver
--------------------

To make dealing with (external or internal) placeholder apis even easier, MiniMessage allows you to provide a placeholder resolver.

A placeholder resolver is just a ``Function<String, @Nullable ComponentLike>``, that allows you to handle tags without having to define them before hand.
Just return a Component when you resolved the placeholder, else you return ``null``.

You can define such a resolver using the builder api (for more info, see the Builder_ section below):

.. code:: java

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

     var parsed = serializer.deserialize("<green><bold>Hai");

     // Assertion passes
     assertEquals(Component.text("<bold>Hai", NamedTextColor.GREEN), parsed);

Bold transformation isn't enabled -> bold tag is not parsed.

Builder
-------

To make customizing MiniMessage easier, we provide a Builder. Use is pretty self explanatory:

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
