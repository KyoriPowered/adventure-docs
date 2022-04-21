======
Fabric
======

Adventure supports Fabric on *Minecraft: Java Edition* 1.16 and up, for both serverside and clientside use. Each major version of Minecraft will usually require a new release of the platform.

The platform supports all features, including localization and custom renderers.

----------
Dependency
----------

The Fabric platform is packaged as a mod, designed to be included in mods via jar-in-jar packaging. As with the rest of the Adventure projects, releases are distributed on Maven Central, and snapshots on Sonatype OSS.

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
            }
            // for releases
            mavenCentral()
         }

.. tab-set::
   
   .. tab-item:: Gradle (Groovy)
      :sync: gradle-groovy

      .. code:: groovy

         dependencies {
            modImplementation include("net.kyori:adventure-platform-fabric:5.2.1") // for Minecraft 1.18.2
         }


   .. tab-item:: Gradle (Kotlin)
      :sync: gradle-kotlin

      .. code:: kotlin

         dependencies {
            modImplementation(include("net.kyori:adventure-platform-fabric:5.2.1")!!) // for Minecraft 1.18.2
         }

The Fabric platform requires *fabric-api-base* in order to provide the locale change event, and can optionally use Colonel_ to allow the ``Component`` and ``Key`` argument types to be used on clients without the mod installed. There are no other dependencies.

.. attention::

   Each major Minecraft release will require different platform versions. The following platform versions are the last released version for each Minecraft release. Older releases may not receive any support.

   ================= ================= ======================================
   Minecraft Version Adventure version ``adventure-platform-fabric`` version
   ================= ================= ======================================
   1.16.2-1.16.4     4.9.3             4.0.0
   1.17.x            4.9.3             4.1.0
   1.18, 1.18.1      4.10.0            5.1.0
   1.18.2            4.10.0            5.2.1
   ================= ================= ======================================


------
Server
------

The logical-server side of the Fabric platform can be accessed any time a server is available, through a ``FabricServerAudiences`` instance. By default, translatable components will be rendered with the global translator, but a custom renderer can be passed when initializing the platform. 

All ``AudienceProvider`` interface methods are supported, except for the ``permission`` method. This will become supported as soon as Fabric gets a suitable permissions API.

To get started with Adventure, set up an audience provider like this:

.. code:: java

   public class MyMod implements ModInitializer {
     private FabricServerAudiences adventure;

     public FabricServerAudiences adventure() {
       if(this.adventure == null) {
         throw new IllegalStateException("Tried to access Adventure without a running server!");
       }
     }

     @Override
     public void onInitialize() {
       // Register with the server lifecycle callbacks
       // This will ensure any platform data is cleared between game instances
       // This is important on the integrated server, where multiple server instances
       // can exist for one mod initialization.
       ServerLifecycleEvents.SERVER_STARTING.register(server -> this.platform = FabricServerAudiences.of(server));
       ServerLifecycleEvents.SERVER_STOPPED.register(server -> this.platform = null);
     }
   }

From here, audiences can be aquired for players and any other ``CommandSource``. Specialized serializer instances are also available, to allow using game information in component serialization.

~~~~~~~~~~~~
Localization
~~~~~~~~~~~~

As part of the platform's translation support, the :java:`PlayerLocales.CHANGED_EVENT` callback will be called any time a player on the server receives an updated language from their client, and allows accessing the current locale for a player.

~~~~~~~~
Commands
~~~~~~~~

The Fabric platform provides custom argument types to specify ``Key`` and ``Component`` parameters in Brigadier commands, and has helpers to easily get an ``Audience`` from a ``CommandSourceStack`` (yarn: ``ServerCommandSource``) instance.

.. warning::

    If these custom argument types are used, Vanilla clients will not be able to join unless the Colonel_ mod is installed on the server. Like the platform, it is small and easily included in your mod jar.

As an example, here's a simple command that will echo whatever is provided as input:

.. code:: java


   // A potential method to be in the mod initializer class above
   private static final String ARG_MESSAGE = "message";

   void registerCommands(final CommandDispatcher dispatcher, final boolean isDedicated) {
     dispatcher.register(literal("echo").then(argument(ARG_MESSAGE, component()).executes(ctx -> {
       final AdventureCommandSourceStack source = this.adventure().audience(ctx.getSource());
       final Component message = component(ctx, ARG_MESSAGE);

       source.sendMessage(Component.text("You said: ").append(message));
     }));
   }

------
Client
------

Special for the Fabric platform, purely clientside operations are supported. The setup is less involved than it is for the server, since the client is a singleton, and there is only one subject that can be acted on: the client's player.

This means that for most users the ``FabricClientAudiences`` object can be treated as a singleton. The only exception is users using a custom renderer. This makes using Adventure audiences fairly simple, as this code example shows:

.. code:: java

   void doThing() {
     // Get the audience
     final Audience client = FabricClientAudiences.of().audience();

     // Do something. This will only work when the player is ingame.
     client.sendMessage(Component.text("meow", NamedTextColor.DARK_PURPLE));
   }

The full functionality of the ``Audience`` interface is available, including localization!

-------------------------
Working with native types
-------------------------

Sadly, Adventure can't provide API for every place chat components are used in the game. However, for areas not covered by the API in ``Audience``, it's possible to convert components between native and Adventure types. See the methods on ``FabricAudiences`` for an idea of what's available.


.. _Colonel: https://gitlab.com/stellardrift/colonel
