======
Fabric
======

Adventure supports Fabric on *Minecraft: Java Edition* 1.16 and up, for both serverside and clientside use.

The platform supports all features, including localization and custom renderers.

----------
Dependency
----------

The fabric platform is packaged as a mod, designed to be included in mods via jar-in-jar packaging. As with the rest of the adventure projects, releases are distributed on Maven Central, and snapshots on Sonatype OSS.

.. tabs::
   
   .. group-tab:: Gradle (Groovy)

      .. code:: groovy

         dependencies {
            modImplementation include("net.kyori:adventure-platform-fabric:4.0.0-SNAPSHOT")
         }


   .. group-tab:: Gradle (Kotlin)

      .. code:: kotlin

         dependencies {
            modImplementation(include("net.kyori:adventure-platform-fabric:4.0.0-SNAPSHOT")!!)
         }

The fabric platform requires *fabric-api-base* in order to provide the locale change event, and can optionally use Colonel_ to allow the ``Component`` and ``Key`` argument types to be used on clients without the mod installed. There are no other dependencies.

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

As part of the platform's translation support, the ``PlayerLocales.CHANGED_EVENT`` callback will be called any time a player on the server receives an updated language from their client, and allows accessing the current locale for a player.

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
