==========
BungeeCord 
==========

Adventure targets the latest version of BungeeCord and BungeeCord-compatible
forks, such as Waterfall.

Add the artifact to your build file:

First, add the repository:

.. tabs::
   
   .. group-tab:: Maven

      .. code:: xml

         <repositories>
             <!-- ... -->
             <repository> <!-- for development builds -->
               <id>sonatype-oss</id>
               <url>https://oss.sonatype.org/content/repositories/snapshots/</url>
             </repository>
             <!-- ... -->
         </repositories>
   
   .. group-tab:: Gradle (Groovy)

      .. code:: groovy

         repositories {
            // for development builds
            maven {
                name = 'sonatype-oss'
                url = 'https://oss.sonatype.org/content/repositories/snapshots/'
            }
            // for releases
            mavenCentral()
         }

   .. group-tab:: Gradle (Kotlin)

      .. code:: kotlin

         repositories {
            // for development builds
            maven(url = "https://oss.sonatype.org/content/repositories/snapshots/") {
                name = "sonatype-oss"
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
         <artifactId>adventure-platform-bungeecord</artifactId>
         <version>4.0.0-SNAPSHOT</version>
         </dependency>
   
   .. group-tab:: Gradle (Groovy)

      .. code:: groovy

         dependencies {
            implementation 'net.kyori:adventure-platform-bungeecord:4.0.0-SNAPSHOT'
         }


   .. group-tab:: Gradle (Kotlin)

      .. code:: kotlin

         dependencies {
            implementation("net.kyori:adventure-platform-bungeecord:4.0.0-SNAPSHOT")
         }

Usage
-----

You should first obtain an ``BungeeAudiences`` object by using ``BungeeAudiences.create(plugin)``. This object is thread-safe
and can be reused from different threads if needed.

Note that not all functionality is available on the proxy. Sending chat messages, action bar messages, titles and boss bars
are supported, but all other requests will fail silently.

Component serializers
---------------------

The ``BungeeCordComponentSerializer`` allows you to convert between Adventure :doc:`Components </text>` and the native BungeeCord
chat component API and back.