=========
Adventure
=========

.. only:: draft

   .. warning:: This documentation is for an **unreleased** version of 
      Adventure. Some information may not be up to date, and API is subject to change.


Adventure is a library for server-controllable user interface elements in *Minecraft: Java Edition*. The different
elements covered by this library can be found in the index on the left, or on the bottom of this page.

Check out the :doc:`quickstart` section for a little introduction to the most basic functionality in adventure

If you are here to troubleshoot an error commonly addressed errors can be found with answers over at the :doc:`troubleshooting`
page.


Importing Adventure into your project
-------------------------------------

First, add the repository(if necessary):

.. tabs::
   
   .. group-tab:: Maven

      .. code:: xml

         <repositories>
             <!-- ... -->
             <repository> <!-- only necessary for development builds -->
                <id>sonatype-oss-snapshots</id>
                <url>https://oss.sonatype.org/content/repositories/snapshots/</url>
             </repository>
             <!-- ... -->
         </repositories>
   
   .. group-tab:: Gradle (Groovy)

      .. code:: groovy

         repositories {
            // necessary for development builds
            maven {
                name = "sonatype-oss-snapshots"
                url = "https://oss.sonatype.org/content/repositories/snapshots/"
            }
            // necessary for releases
            mavenCentral()
         }

   .. group-tab:: Gradle (Kotlin)

      .. code:: kotlin

         repositories {
            // for development builds
            maven(url = "https://oss.sonatype.org/content/repositories/snapshots/") {
                name = "sonatype-oss-snapshots"
            }
            // for releases
            mavenCentral()
         }

   Declaring the dependency:

.. tabs::
   
   .. group-tab:: Maven

      .. code:: xml

         <dependency>
            <groupId>net.kyori</groupId>
            <artifactId>adventure-api</artifactId>
            <version>4.7.0</version>
         </dependency>
   
   .. group-tab:: Gradle (Groovy)

      .. code:: groovy

         dependencies {
            implementation "net.kyori:adventure-api:4.7.0"
         }


   .. group-tab:: Gradle (Kotlin)

      .. code:: kotlin

         dependencies {
            implementation("net.kyori:adventure-api:4.7.0")
         }

.. toctree::
   :maxdepth: 2

   quickstart
   troubleshooting

   audiences
   text
   serializer/index

   bossbar
   sound
   title
   book
   tablist
   minimessage

   platform/index

   migration/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
