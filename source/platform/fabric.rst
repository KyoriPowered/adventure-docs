======
Fabric
======

Adventure supports Fabric on *Minecraft: Java Edition* 1.16 and up, for both server-side and client-side use. Each major version of Minecraft will usually require a new release of the platform.

The platform supports all features, including localization and custom renderers.

When using at least version 5.3.0, this platform provides a *near-native* experience by directly implementing Adventure interfaces on Minecraft classes where possible.

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
            modImplementation include("net.kyori:adventure-platform-fabric:|fabric_version|") // for Minecraft 1.20.2
         }


   .. tab-item:: Gradle (Kotlin)
      :sync: gradle-kotlin

      .. code-block:: kotlin
        :substitutions:

         dependencies {
            modImplementation(include("net.kyori:adventure-platform-fabric:|fabric_version|")!!) // for Minecraft 1.20.2
         }

The Fabric platform requires *fabric-api-base* in order to provide the locale change event, and can optionally use Colonel_ to allow the ``Component`` and ``Key`` argument types to be used on clients without the mod installed. There are no other dependencies.

.. attention::

   Each major Minecraft release will require different platform versions. For older Minecraft versions, consult the table below.

   .. dropdown:: Historic Versions

      ================= ================= ======================================
      Minecraft Version Adventure version ``adventure-platform-fabric`` version
      ================= ================= ======================================
      1.16.2-1.16.4     4.9.3             4.0.0
      1.17.x            4.9.3             4.1.0
      1.18, 1.18.1      4.10.0            5.1.0
      1.18.2            4.11.0            5.3.1
      1.19              4.11.0            5.4.0
      1.19.1-1.19.2     4.12.0            5.5.2
      1.19.3            4.13.0            5.7.0
      1.19.4            4.13.0            5.8.0
      1.20-1.20.1       4.14.0            5.9.0
      ================= ================= ======================================

---------
Basic use
---------

The easiest way to get started with this platform is to work with the Minecraft game objects that directly implement Adventure interfaces (requires Loom 0.11 or newer).

This covers almost all cases where the default renderer is used.

The following Adventure interfaces are directly implemented:

``Audience``
    :java:`net.minecraft.commands.CommandSourceStack`, :java:`net.minecraft.server.MinecraftServer`, :java:`net.minecraft.server.rcon.RconConsoleSource`,
    :java:`net.minecraft.server.level.ServerPlayer`, :java:`net.minecraft.client.player.LocalPlayer`

``Sound.Emitter``
    :java:`net.minecraft.world.entity.Entity`

``Sound.Type``
    :java:`net.minecraft.sounds.SoundEvent`

``Identified``
    :java:`net.minecraft.world.entity.player.Player`

``ComponentLike``
    :java:`net.minecraft.network.chat.Component`

``Key``
    :java:`net.minecraft.resources.ResourceLocation`

``Keyed``
    :java:`net.minecraft.resources.ResourceKey`

``HoverEventSource``
    :java:`net.minecraft.world.entity.Entity`,
    :java:`net.minecraft.world.item.ItemStack`

``SignedMessage``
    :java:`net.minecraft.network.chat.PlayerChatMessage`

``SignedMessage.Signature``
    :java:`net.minecraft.network.chat.MessageSignature`

Additionally, all :java:`Key`\ s created will be :java:`ResourceLocation` instances (on Loader 0.14.0+)

Using these injections, getting started is as simple as:


.. code:: java

   void greet(final ServerPlayer player) {
     player.sendMessage(Component.text().content("Hello ").append(player.get(Identity.DISPLAY_NAME).get().color(NamedTextColor.RED)));
   }

For more complex use cases, :java:`FabricServerAudiences` or :java:`FabricClientAudiences` provide additional API.

------
Server
------

The logical-server side of the Fabric platform can be accessed any time a server is available, through a ``FabricServerAudiences`` instance. By default, translatable components will be rendered with the global translator, but a custom renderer can be passed when initializing the platform.

All ``AudienceProvider`` interface methods are supported, except for the ``permission`` method. This will become supported as soon as Fabric gets a suitable permissions API.

To get started with Adventure, set up an audience provider like this:

.. code:: java

   public class MyMod implements ModInitializer {
     private volatile FabricServerAudiences adventure;

     public FabricServerAudiences adventure() {
       FabricServerAudiences ret = this.adventure;
       if(ret == null) {
         throw new IllegalStateException("Tried to access Adventure without a running server!");
       }
       return ret;
     }

     @Override
     public void onInitialize() {
       // Register with the server lifecycle callbacks
       // This will ensure any platform data is cleared between game instances
       // This is important on the integrated server, where multiple server instances
       // can exist for one mod initialization.
       ServerLifecycleEvents.SERVER_STARTING.register(server -> this.adventure = FabricServerAudiences.of(server));
       ServerLifecycleEvents.SERVER_STOPPED.register(server -> this.adventure = null);
     }
   }

From here, audiences can be acquired for players and any other ``CommandSource``. Specialized serializer instances are also available, to allow using game information in component serialization.

~~~~~~~~~~~~
Localization
~~~~~~~~~~~~

As part of the platform's translation support, the :java:`PlayerLocales.CHANGED_EVENT` callback will be called any time a player on the server receives an updated language from their client, and allows accessing the current locale for a player.

~~~~~~~~
Commands
~~~~~~~~

The Fabric platform provides custom argument types to specify ``Key`` and ``Component`` parameters in Brigadier commands, and has helpers to easily get an ``Audience`` from a ``CommandSourceStack`` (yarn: ``ServerCommandSource``) instance.

.. warning::

    If these custom argument types are used (pre-1.19), Vanilla clients will not be able to join unless the Colonel_ mod is installed on the server. Like the platform, it is small and easily included in your mod jar.

As an example, here's a simple command that will echo whatever is provided as input:

.. code:: java


   // A potential method to be in the mod initializer class above
   private static final String ARG_MESSAGE = "message";

   void registerCommands(final CommandDispatcher dispatcher, final boolean isDedicated) {
     dispatcher.register(literal("echo").then(argument(ARG_MESSAGE, component()).executes(ctx -> {
       final Component message = component(ctx, ARG_MESSAGE);

       ctx.getSource().sendMessage(Component.text("You said: ").append(message));
     }));
   }

------
Client
------

Special for the Fabric platform, purely client-side operations are supported. The setup is less involved than it is for the server, since the client is a singleton, and there is only one subject that can be acted on: the client's player.

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

Sadly, Adventure can't provide API for every place chat components are used in the game. However, for areas not covered by the API in ``Audience``, it's possible to convert components between native and Adventure types. See certain native types which implement
Adventure interfaces, and the methods on ``FabricAudiences`` for other available conversions.


.. _Colonel: https://gitlab.com/stellardrift/colonel
