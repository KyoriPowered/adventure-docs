====
Gson
====

The Gson text serializer converts chat components to their JSON representation
and back. If you are interested in sending a chat component for display in a
Minecraft client, or want to support advanced chat component features, you should
use the Gson text serializer.

As explained in the name, the Gson serializer uses the Gson library to serialize the
chat components to JSON.

Usage
-----

The Gson serializer is accessed using the ``GsonComponentSerializer`` class. You can
use ``GsonComponentSerializer.gson()`` for a default instance that supports RGB components
(only Minecraft 1.16 and above will be able to deserialize these components) or use
``GsonComponentSerializer.colorDownsamplingGson()`` which downsamples colors to the
closest Mojang legacy color and serializes hover events in a way that is backwards
compatible with older clients.