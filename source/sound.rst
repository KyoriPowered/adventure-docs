=====
Sound
=====

Adventure contains an API to play any built-in or resource pack-provided sound. Note that
not all platforms implement playing sound.

Sending a Sound
---------------

Sounds are referred to using Minecraft's Keys (also known as ``Identifier`` or ``ResourceLocation``). Any custom sounds from resource packs can be used. If a client does not know about sounds, it will ignore the sound (though a warning will be printed to the client log).

.. code:: java

  public void playMySound(final @NonNull Audience target) {
    // Play a built-in sound at the target's location with standard volume and pitch
    target.playSound(Key.of("music_disc.13"), Sound.Source.MUSIC, 1f, 1f);
    // Play a sound from our resource pack, with a higher pitch
    target.playSound(Key.of("adventure", "rawr"), Sound.Source.AMBIENT, 1f, 1.1f);
  }

.. sidebar:: Limitations

  The client can play multiple sounds at once, but as of version 1.16 is limited to 8 sounds playing at once.

Stopping Sounds
---------------

A sound stop will stop the chosen sounds -- ranging from every sound the client is playing, to specific named sounds.


Creating a custom sound
-----------------------

Use the ``sounds.json`` to define sounds in a resource pack.

