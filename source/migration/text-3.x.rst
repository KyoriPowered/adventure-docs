=======================
Migrating from text 3.x
=======================

Adventure is an evolution of the text 3.x API. If you've worked with
the text API before, the switch to Adventure should be quick and relatively
painless. For the most part, you'll just need to depend on the Adventure API
and the relevant :doc:`/platform/index` you support and replace references
to classes in ``net.kyori.text`` to ``next.kyori.adventure.text``.

However, before you continue, it is strongly recommended you read about
:doc:`/audiences`. Unlike text, Adventure defines a standard interface for
sending content (including chat messages) to viewers. In addition, Adventure
defines interfaces for other gameplay mechanics that can be arbitrarily sent
to players.