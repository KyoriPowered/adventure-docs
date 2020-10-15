=====
Books
=====

Books in adventure is not necessarily connected to an interactable book item in the client.
As of the current release such a connection needs to be implemented outside of adventure.



Creating a Book
---------------

Any component that surpass the game limit for text per page will be truncated client side, the same applies
to the amount of components(pages). Further reading about these limits can be done at the `minecraft wiki <https://minecraft.gamepedia.com/Book_and_Quill#Writing>`_

.. code:: java

    //Create and open a book about cats for the target audience
    public void openMyBook(final @NonNull Audience target){
        Component bookTitle = TextComponent.text("Encyclopedia of cats");
        Component bookAuthor = TextComponent.text("catlovr2000");
        Collection<Component> bookPages = Cats.getCatKnowledge();

        Book myBook = Book.book(bookTitle, bookAuthor, bookAuthor);
        target.openBook(myBook);
    }
