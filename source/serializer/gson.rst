====
Gson
====

The Gson text serializer converts chat components to their JSON representation
and back using the Gson library. If you are interested in sending a chat component
for display in a Minecraft client, or want to support advanced chat component features,
you should use the Gson text serializer.

An average user of this text serializer will typically want to only deserialize a
component from an external source - serialization is done automatically by the
:doc:`/platform/index` when the component is sent to the user.

**Importing this serializer into your project**

.. tabs::

   .. group-tab:: Maven

      .. code:: xml

         <dependency>
            <groupId>net.kyori</groupId>
            <artifactId>adventure-text-serializer-gson</artifactId>
            <version>4.7.0</version>
         </dependency>

   .. group-tab:: Gradle (Groovy)

      .. code:: groovy

         dependencies {
            implementation "net.kyori:adventure-text-serializer-gson:4.7.0"
         }


   .. group-tab:: Gradle (Kotlin)

      .. code:: kotlin

         dependencies {
            implementation("net.kyori:adventure-text-serializer-gson:4.7.0")
         }


Usage
-----

The Gson serializer is accessed using the ``GsonComponentSerializer``.

In Minecraft 1.16, Mojang made several major changes to the JSON chat format, adding
RGB chat colors and changing how hover events are serialized. Components generated for
older versions of Minecraft will still be able to be displayed in a 1.16 client,
however components serialized for a 1.16 client will not be able to be displayed in
a Minecraft 1.15.2 client or lower. 

To get a serializer that works with 1.16 clients and above, use
``GsonComponentSerializer.gson()``. To get a serializer that works with all versions
of Minecraft that support text components, use ``GsonComponentSerializer.colorDownsamplingGson()``.
This serializer downsamples RGB colors to the closest Mojang legacy color and serializes
hover events in a way that is backwards compatible with older clients.

Which serializer should I use?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If all you're doing is loading and saving components to a configuration file or a database,
you probably want to use the default 1.16 serializer.

If you're looking to send a component to a client, first consider whether you can one of the
provided platforms. If you can't use a platform, generally you should prefer the default
serializer for deserializing components (as it is backwards-compatible), and make a decision
on whether to use the default or the color downsampling serializer based on the version the
client is on.