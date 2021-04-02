===============
Troubleshooting/FAQ
===============


This page covers some errors and problems you might encounter while using this library.

**How do i turn a string with legacy formatting (& or §) into a component?**

Use the serializer located here: :doc:`/serializer/legacy`


**Method/Class not found on platforms with native support**

Make sure the version of adventure provided by your native platform is equal or higher than the version you are
developing in. If your code uses a method from adventure 4.5.0 while the server running the code has adventure 4.4.0
you might get errors. All code in adventure should have a @since tag in its javadoc snippet, which you can use to check
for this error.

**Players can not hear a sound/some sounds**

Make sure that the player has the correct Sound source level turned up, in addition to the master volume. When sending
a sound you have to specify a ``Sound.Source``, so remember that the sound you are sending might not behave like the
normal sound if you specify otherwise.

