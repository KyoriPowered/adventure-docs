==================
PlayerList/Tablist
==================

Adventure does currently only support changing the header and footer of the tablist through
``Audience#sendPlayerListHeader``, ``Audience#sendPlayerListFooter`` and ``Audience#sendPlayerListHeaderAndFooter``.

Sending only a header might also display an existing footer. Likewise, sending only a footer might also display
an existing header. This can vary depending on the platform you are running on.