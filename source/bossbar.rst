=========
Boss Bars
=========

Constructing a Boss Bar
^^^^^^^^^^^^^^^^^^^^^^^^

Boss Bars are composed of:
* A component which represents the text shown
* A percentage, how full the bar should be from 0 (empty) to 1 (full)
* A color, the main color of the boss bar
* A style/overlay graphic that allows you to select the amount notches on the boss bar

.. code:: java

  // Let's create some example Boss Bars
  final Component name = Component.text("Foo Bar");
  final BossBar emptyBar = BossBar.bossBar(name, 0, BossBar.Color.RED, BossBar.Overlay.PROGRESS);
  final BossBar halfBar = BossBar.bossBar(name, 0.5f, BossBar.Color.GREEN, BossBar.Overlay.NOTCHED_10);
  final BossBar fullBar = BossBar.bossBar(name, 1, BossBar.Color.BLUE, BossBar.Overlay.NOTCHED_20);
  // You can now send these Boss Bars to an audience
