=========
Adventure
=========

.. only:: draft

   .. warning:: This documentation is for an **unreleased** version of 
      Adventure. Some information may not be up to date, and API is subject to change.

.. toctree::
   :maxdepth: 2

   audiences
   text
   serializer/index

   bossbar
   sound
   title
   book
   minimessage

   platform/index

   nbt

   migration/index


Adventure is a library for server-controllable user interface elements in *Minecraft: Java Edition*.


Importing Adventure into your project
-------------------------------------

First, add the repository:

.. tabs::
   
   .. group-tab:: Maven

      .. code:: xml

         <repositories>
             <!-- ... -->
             <repository> <!-- for development builds -->
                <id>sonatype-oss-snapshots</id>
                <url>https://oss.sonatype.org/content/repositories/snapshots/</url>
             </repository>
             <!-- ... -->
         </repositories>
   
   .. group-tab:: Gradle (Groovy)

      .. code:: groovy

         repositories {
            // for development builds
            maven {
                name = "sonatype-oss-snapshots"
                url = "https://oss.sonatype.org/content/repositories/snapshots/"
            }
            // for releases
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
            <version>4.3.0</version>
         </dependency>
   
   .. group-tab:: Gradle (Groovy)

      .. code:: groovy

         dependencies {
            implementation "net.kyori:adventure-api:4.3.0"
         }


   .. group-tab:: Gradle (Kotlin)

      .. code:: kotlin

         dependencies {
            implementation("net.kyori:adventure-api:4.3.0")
         }

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
