==================
Player List (Tab List)
==================

Adventure supports changing the header (top) and footer (bottom) of the player list.

.. image:: /components/images/playerlist.png
   :alt: Image showing a player list with header and footer

.. code-block:: java

    public void sendMyFooter(final Audience server) {
        final Component footer = Component.text("Thank you for visiting kyori.net");
        server.sendPlayerListFooter(footer);
    }

Depending on your platform, sending only a header may clear the existing footer, and vice versa. This is especially
common with proxies. To prevent this, you may send both the header and footer simultaneously:

.. code-block:: java

    public void sendMyHeaderAndFooter(final Audience player) {
        final Component header = Component.text("My Cool Server", NamedTextColor.BLUE);
        final Component footer = Component.text("It is: today!");
        player.sendPlayerListHeaderAndFooter(header, footer);
    }
