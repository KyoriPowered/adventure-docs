.. _platforms:

=========
Platforms
=========

Adventure integrates with many of the Minecraft platforms out there. Some platforms support
Adventure natively, but other legacy platforms have their own types and need an adapter to handle Adventure types. To enable you to use Adventure with these platforms, Adventure provides a number of platform-specific adapters to
allow you to obtain ``Audience`` instances from native user types.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   native
   bukkit
   bungeecord
   spongeapi
   fabric
   viaversion


.. _sending-messages:
.. note::
  **Why is adventure-platform not sending any messages or not working correctly?**

  Firstly, please ensure you are on the latest stable version. This can be found on `Maven Central <https://search.maven.org/search?q=g:net.kyori%20AND%20a:adventure-platform*>`_.

  Next, make sure that the feature you are using exists on the client version that is receiving the action. For example, hex color codes won't work on clients older than 1.16, so hex colors will be down-sampled.

  If it's still not working, it is useful to enable debug mode by setting the system property ``net.kyori.adventure.debug`` to ``true`` and pasting (to a paste site such as https://paste.gg/) the output
  in the appropriate ``#platform-`` channel on our Discord.
  This will show what facets are being selected which will help point towards why it is not working for you.
