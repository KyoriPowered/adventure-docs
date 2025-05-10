========
NeoForge
========

Adventure supports NeoForge on *Minecraft: Java Edition* 1.21 and up, for both server-side and client-side use. Each major version of Minecraft will usually require a new release of the platform.

The platform supports all features, including localization and custom renderers.

----------
Dependency
----------

The NeoForge platform is packaged as a mod, designed to be included in mods via jar-in-jar packaging. As with the rest of the Adventure projects, releases are distributed on Maven Central, and snapshots on Sonatype OSS.

Add the artifact to your build file:

First, add the repository:

.. tab-set::

   .. tab-item:: Gradle (Groovy)
      :sync: gradle-groovy

      .. code:: groovy

         repositories {
            // for development builds
            maven {
                name = "sonatype-oss-snapshots1"
                url = "https://s01.oss.sonatype.org/content/repositories/snapshots/"
                mavenContent { snapshotsOnly() }
            }
            // for releases
            mavenCentral()
         }

   .. tab-item:: Gradle (Kotlin)
      :sync: gradle-kotlin

      .. code:: kotlin

         repositories {
            // for development builds
            maven(url = "https://s01.oss.sonatype.org/content/repositories/snapshots/") {
                name = "sonatype-oss-snapshots1"
                mavenContent { snapshotsOnly() }
            }
            // for releases
            mavenCentral()
         }

.. tab-set::

   .. tab-item:: Gradle (Groovy)
      :sync: gradle-groovy

      .. code-block:: groovy
        :substitutions:

         dependencies {
            implementation jarJar("net.kyori:adventure-platform-neoforge:|mod_version|") // for Minecraft 1.21.5
         }


   .. tab-item:: Gradle (Kotlin)
      :sync: gradle-kotlin

      .. code-block:: kotlin
        :substitutions:

         dependencies {
            implementation(jarJar("net.kyori:adventure-platform-neoforge:|mod_version|")!!) // for Minecraft 1.21.5
         }


.. attention::

   Each major Minecraft release will require different platform versions. For older Minecraft versions, consult the table at :doc:`/platform/modded`

---------
Basic Use
---------

See :doc:`/platform/modded` for usage details common between NeoForge and Fabric.

------
Server
------

The logical-server side of the modded platform can be accessed any time a server is available, through a ``MinecraftServerAudiences`` instance. By default, translatable components will be rendered with the global translator, but a custom renderer can be passed when initializing the platform.

All ``AudienceProvider`` interface methods are supported.

To get started with Adventure, set up an audience provider like this:

.. code:: java

   @Mod("my_mod")
   public class MyMod {
     private volatile MinecraftServerAudiences adventure;

     public MinecraftServerAudiences adventure() {
       MinecraftServerAudiences ret = this.adventure;
       if(ret == null) {
         throw new IllegalStateException("Tried to access Adventure without a running server!");
       }
       return ret;
     }

     public MyMod() {
       // Register with the server lifecycle callbacks
       // This will ensure any platform data is cleared between game instances
       // This is important on the integrated server, where multiple server instances
       // can exist for one mod initialization.
       NeoForge.EVENT_BUS.addListener((ServerStartingEvent e) -> this.platform = MinecraftServerAudiences.of(e.getServer()));
       NeoForge.EVENT_BUS.addListener((ServerStoppedEvent e) -> this.platform = null);
     }
   }

From here, audiences can be acquired for players and any other ``CommandSource``. Specialized serializer instances are also available, to allow using game information in component serialization.

--------
Commands
--------

The NeoForge platform includes a method to register the :java:`KeyArgumentType` and :java:`ComponentArgumentType`:
    :java:`AdventureArgumentTypes.register();`

This should be called from the constructor of your :java:`@Mod`-annotated class.
Registering the argument types on the server will require all clients that join to have the argument types
registered as well.

------
Client
------

Special for the modded platform, purely client-side operations are supported. The setup is less involved than it is for the server, since the client is a singleton, and there is only one subject that can be acted on: the client's player.

This means that for most users the ``MinecraftClientAudiences`` object can be treated as a singleton. The only exception is users using a custom renderer. This makes using Adventure audiences fairly simple, as this code example shows:

.. code:: java

   void doThing() {
     // Get the audience
     final Audience client = MinecraftClientAudiences.of().audience();

     // Do something. This will only work when the player is ingame.
     client.sendMessage(Component.text("meow", NamedTextColor.DARK_PURPLE));
   }

The full functionality of the ``Audience`` interface is available, including localization!
