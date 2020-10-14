======
Titles
======

Constructing a Title
^^^^^^^^^^^^^^^^^^^^

.. code:: java

  // Titles are composed of 2 components, a main title and a subtitle
  final Component mainTitle = Component.text("This is the main title", NamedTextColor.WHITE);
  final Component subtitle = Component.text("This is the subtitle", NamedTextColor.GRAY);
  final Title title = Title.title(mainTitle, subtitle);
  // You can now send `title` to an audience using `Audience#sendTitle`

Additionally, you can clear any title that is currently being shown to an audience using `Audience#clearTitle`

Title Animations
^^^^^^^^^^^^^^^^

By default, titles fade-in, stay on screen for a period of time and then fade-out.

.. code:: java

  // You can control the duration (in game ticks) of those animations by supplying a Times object
  // In this example: The fade-in will take 15 ticks which correspond to 750ms
  // After that, the title will remain for 3000ms and the finally fade-out within 20 ticks (1000ms)
  final Title.Times times = Title.Times.of(Ticks.duration(15), Duration.ofMillis(3000), Ticks.duration(20));
  final Title title2 = Title.title(Component.text("Hello!"), Component.empty(), times);
