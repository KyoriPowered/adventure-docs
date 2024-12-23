=======================================
Modded (Fabric and NeoForge shared API)
=======================================

Starting with *Minecraft: Java Edition* 1.21.2, Adventure is implemented using mostly shared code between NeoForge and Fabric.
Each major version of Minecraft will usually require a new release of the platform.

The platform supports all features, including localization and custom renderers.

----------
Dependency
----------

When building multi-loader mods, we often want to move as much code as possible into a loader-agnostic part of our projects.

Adventure facilities this through the :code:`net.kyori:adventure-platform-mod-shared` artifact.

A second variant, :code:`net.kyori:adventure-platform-mod-shared-fabric-repack`, is also published. This variant should be used
when your common code is managed by :code:`fabric-loom`.

If you are building a Fabric-only or NeoForge-only mod, or do not care to use the platform API in shared code,
then you don't need to use this artifact explicitly. This is because both platforms depend on it transitively.

As with the rest of the Adventure projects, releases are distributed on Maven Central, and snapshots on Sonatype OSS.

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
            // Loom project
            modCompileOnly("net.kyori:adventure-platform-mod-shared-fabric-repack:|mod_version|") // for Minecraft 1.21.2-1.21.4

            // NeoGradle/ModDevGradle/VanillaGradle project
            compileOnly("net.kyori:adventure-platform-mod-shared:|mod_version|") // for Minecraft 1.21.2-1.21.4
         }


   .. tab-item:: Gradle (Kotlin)
      :sync: gradle-kotlin

      .. code-block:: kotlin
        :substitutions:

         dependencies {
            // Loom project
            modCompileOnly("net.kyori:adventure-platform-mod-shared-fabric-repack:|mod_version|") // for Minecraft 1.21.2-1.21.4

            // NeoGradle/ModDevGradle/VanillaGradle project
            compileOnly("net.kyori:adventure-platform-mod-shared:|mod_version|") // for Minecraft 1.21.2-1.21.4
         }


.. attention::

   Each major Minecraft release will require different platform versions. For older Minecraft versions, consult the table below.

   .. dropdown:: Historic Versions

      ================= ================= ===========================================================
      Minecraft Version Adventure version ``adventure-platform-(mod-shared|fabric|neoforge)`` version
      ================= ================= ===========================================================
      1.21-1.21.1       4.17.0            6.0.0
      ================= ================= ===========================================================

---------
Basic use
---------

The easiest way to get started with this platform is to work with the Minecraft game objects that directly implement Adventure interfaces.

This covers almost all cases where the default renderer is used.

On Fabric, interface injection is used so that you can directly call interface methods on Minecraft objects (with loom 0.11+).

On NeoForge, you must manually cast or use the helpers provided in :java:`MinecraftAudiences`.

The following Adventure interfaces are directly implemented:

``Audience``
    :java:`net.minecraft.commands.CommandSourceStack`, :java:`net.minecraft.server.MinecraftServer`, :java:`net.minecraft.server.rcon.RconConsoleSource`,
    :java:`net.minecraft.server.level.ServerPlayer`, :java:`net.minecraft.client.player.LocalPlayer`

``AdventureCommandSourceStack``
    :java:`net.minecraft.commands.CommandSourceStack`

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

``SignedMessage.Signature``
    :java:`net.minecraft.network.chat.MessageSignature`


Using these injections, getting started is as simple as:


.. code:: java

   void greet(final ServerPlayer player) {
     ((Audience) player).sendMessage(Component.text().content("Hello ").append(player.get(Identity.DISPLAY_NAME).get().color(NamedTextColor.RED)));
   }

For more complex use cases, :java:`MinecraftServerAudiences` or :java:`MinecraftClientAudiences` provide additional API.

~~~~~~~~
Commands
~~~~~~~~

The platform provides custom argument types to specify ``Key`` and ``Component`` parameters in Brigadier commands.

.. warning::

    See the platform-specific documentation for details on registration and syncing of these argument types.

As an example, here's a simple command that will echo whatever is provided as input:

.. code:: java


   // A potential method to be in the mod initializer class above
   private static final String ARG_MESSAGE = "message";

   void registerCommands(final CommandDispatcher dispatcher, final boolean isDedicated) {
     dispatcher.register(literal("echo").then(argument(ARG_MESSAGE, component()).executes(ctx -> {
       final Component message = component(ctx, ARG_MESSAGE);

       ((Audience) ctx.getSource()).sendMessage(Component.text("You said: ").append(message));
     }));
   }

-------------------------
Working with native types
-------------------------

Sadly, Adventure can't provide API for every place chat components are used in the game. However, for areas not covered by the API in ``Audience``, it's possible to convert components between native and Adventure types. See certain native types which implement
Adventure interfaces, and the methods on ``MinecraftAudiences`` for other available conversions.


.. _Colonel: https://gitlab.com/stellardrift/colonel
