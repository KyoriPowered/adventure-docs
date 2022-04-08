==================
Action Bar
==================

Send messages to the action bar, located above the health bar of a player.

.. code-block:: java

    public void sendMyActionBar(final Audience server) {
        final Component actionBar = Component.text("You smell funny");
        server.sendActionBar(actionBar);
    }

It is not possible to control fade-in/out. For similar functionality, see :ref:`title`.
