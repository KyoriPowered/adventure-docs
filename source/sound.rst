=====
Sound
=====

Adventure contains an API to play any built-in or resource pack-provided sound. Note that
not all platforms implement playing sound.

Constructing a Sound
^^^^^^^^^^^^^^^^^^^^

Sounds are composed of:
  * A Key (also known as ``Identifier`` or ``ResourceLocation``) that decides which sound to play. Any custom sounds from resource packs can be used. If a client does not know about sounds, it will ignore the sound (though a warning will be printed to the client log).
  * A Sound source, used to tell the client what type of sound its hearing. The clients sound settings are also attributed to a source.
  * A number, determining the radius where the sound can be heard
  * A number from 0 to 2 determining the pitch the sound will be played at

**Examples:**

.. code:: java

  public void playMySound(final @NonNull Audience target) {
    // Play a built-in sound at the target's location with standard volume and pitch
    target.playSound(Sound.sound(Key.key("music_disc.13"), Sound.Source.MUSIC, 1f, 1f));
    // Play a sound from our resource pack, with a higher pitch
    target.playSound(Sound.sound(Key.key("adventure", "rawr"), Sound.Source.AMBIENT, 1f, 1.1f));
  }

.. sidebar:: Limitations

  The client can play multiple sounds at once, but as of version 1.16 is limited to 8 sounds playing at once.

Stopping Sounds
^^^^^^^^^^^^^^^

A sound stop will stop the chosen sounds -- ranging from every sound the client is playing, to specific named sounds.

.. code:: java

   public void stopMySound(final @NonNull Audience target) {
    // Stop a sound for the target
    target.stopSound(SoundStop.named(Key.key("music_disc.13"));
    // Stop all weather sounds for the target
    target.stopSound(SoundStop.source(Sound.Source.WEATHER));
    // Stop all sounds for the target
    target.stopSound(SoundStop.all());
  }

Creating a custom sound
^^^^^^^^^^^^^^^^^^^^^^^^

Use the ``sounds.json`` to define sounds in a resource pack. Further reading about this limits can be done at the `Minecraft Wiki <https://minecraft.gamepedia.com/Sounds.json>`_

