=========
SpongeAPI 
=========

Adventure provides a platform for SpongeAPI 7 for *Minecraft: Java Edition* 1.12. For SpongeAPI 8 and up (targeting *Minecraft: Java Edition* 1.16.4), Adventure is the native text library, so no platform is needed.

.. kyori-dep:: adventure-platform-spongeapi platform

Usage
~~~~~

The SpongeAPI platform can either be created through Guice dependency injection, or created directly. We recommend using injection, since less boilerplate is requred.

An example plugin is fairly straightforward:

.. code:: java

   @Plugin(/* [...] */)
   public class MyPlugin {
     private final SpongeAudiences adventure;

     @Inject
     MyPlugin(final SpongeAudiences adventure) {
       this.adventure = adventure;
     }

     public @NonNull SpongeAudiences adventure() {
       return this.adventure;
     }
   }


This sets up a ``SpongeAudiences`` instance that can provide audiences for players, or any ``MessageReceiver``.
