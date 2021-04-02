===========
Quickstart
===========

Welcome to the quickstart section! This page will quickly go through how to make some messages that can be
sent to someone.


For platforms without native support
------------------------------------

After importing the library into your project as specified on the starting page, find your appropriate
platform implementation of adventure. All supported platforms are listed on the :doc:`platform/index` page, where you
also find a short guide on how to create your ``AudienceProvider``.

Using your ``AudienceProvider``, create an ``Audience`` using any of the methods on your provider.

.. code:: java

   Audience audience = audienceProvider.all();


Create some messages, optionally with some styling:

.. code:: java

   //TextColor.color() takes three integers representing a RGB value, which will be downsampeled
   //for clients <1.16. Adventure also provides the NamedTextColor class which holds values for
   //the old minecraft colors
   final Component cats = Component.text("I love cats!", TextColor.of(239, 78, 108), TextDecoration.BOLD);
   final Component secret = Component.text("Secret text!", TextDecoration.ITALIC);

   //Since all Components are immutable, any modifications will return a **new** component
   final Component catsWithSecrets = cats.hoverEvent(HoverEvent.showText(secret));


The messages can be sent to your audience through different mediums:

.. code:: java

   audience.sendMessage(catsWithSecrets);

   final Title title = Title.title(cats, Component.empty());
   audience.showTitle(title);



For platforms with native support
---------------------------------

Create some messages to send to your players:

.. code:: java

   //TextColor.color() takes three integers representing a RGB value, which will be downsampeled
   //for clients <1.16. Adventure also provides the NamedTextColor class which holds values for
   //the old minecraft colors
   final Component cats = Component.text("I love cats!", TextColor.of(239, 78, 108), TextDecoration.BOLD);
   final Component secret = Component.text("Secret text!", NamedTextColor.RED, TextDecoration.ITALIC);

   //Since all Components are immutable, any modifications will return a **new** component
   final Component catsWithSecrets = cats.hoverEvent(HoverEvent.showText(secret));

The messages can be sent to your players through different mediums:

.. code:: java

   player.sendMessage(catsWithSecrets);

   final Title title = Title.title(cats, Component.empty());
   player.showTitle(title);