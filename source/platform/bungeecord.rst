==========
BungeeCord 
==========

Adventure targets the latest version of BungeeCord and BungeeCord-compatible
forks, such as Waterfall.

.. warning:: 

  The BungeeCord platform is intended for legacy environments only. 
  Most developers will want to write plugins for `Velocity <https://velocitypowered.com/>`_, which natively implements the Adventure API. No adapters required!

.. kyori-dep:: adventure-platform-bungeecord platform

Usage
-----

You should first obtain a ``BungeeAudiences`` object by using :java:`BungeeAudiences.create(plugin)`. This object is thread-safe
and can be reused from different threads if needed. This object should also be *closed* when the plugin is disabled.

Note that not all functionality is available on the proxy. Sending chat messages, action bar messages, titles, and boss bars, and tab list header and footer are supported, but all other requests will fail silently.

A simple example of how to appropriately initialize this platform follows:

.. code:: java

   public class MyPlugin extends Plugin {
     private BungeeAudiences adventure;

     public @NonNull BungeeAudiences adventure() {
       if(this.adventure == null) {
         throw new IllegalStateException("Cannot retrieve audience provider while plugin is not enabled");
       }
       return this.adventure;
     }

     @Override
     public void onEnable() {
       this.adventure = BungeeAudiences.create(this);
     }

     @Override
     public void onDisable() {
       if(this.adventure != null) {
         this.adventure.close();
         this.adventure = null;
       }
     }

   }

Component serializers
---------------------

For functionality not already supported by ``Audience``, the ``BungeeComponentSerializer`` allows you to convert between Adventure :doc:`Components </text>` and the native BungeeCord chat component API and back.

.. caution::

    For some areas of the proxy (notably, sending server list responses), the component serializer cannot be appropriately injected unless a ``BungeeAudiences`` instance has been initialized. Using Adventure ``Component`` instances **will not** work without a created ``BungeeAudiences`` instance.
