=====================
Resource Pack Request
=====================

Adventure contains an API to request an Audience to download a resource pack.

Constructing a Resource Pack Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Resource Pack Requests are composed of:
  * A URI to the resource pack ZIP file
  * A string, containing the SHA-1 hash of the resource pack ZIP file
  * A boolean, determining whether the resource pack is required to continue playing on the server or not
  * An optional component used for the prompt


**Examples:**

.. code:: java

  public void sendResourcePack(final @NonNull Audience target) {
    // Build a required resource pack request
    final ResourcePackRequest serverPackRequest = ResourcePackRequest.resourcePackRequest()
        .uri(URI.create("https://example.com/resourcepack.zip"))
        .hash("2849ace6aa689a8c610907a41c03537310949294")
        .required(true)
        .prompt(Component.text("Please download the resource pack!"))
        .build();

    // Send the resource pack request to the target audience
    target.sendResourcePack(serverPackRequest);
  }

  public void sendOptionalResourcePack(final @NonNull Audience target) {
    // Build an optional resource pack request
    final ResourcePackRequest optionalPackRequest = ResourcePackRequest.resourcePackRequest()
        .uri(URI.create("https://download.example.com/optionalresourcepack.zip"))
        .hash("74041e5b4b3fb4d30c48787b1e5d087b4dd1e57e")
        .required(false)
        .prompt(Component.text("You can download this resource pack if you want!"))
        .build();

    // Send the resource pack request to the target audience
    target.sendResourcePack(optionalPackRequest);
  }
