======
Bukkit
======

The Adventure platform implementation for Bukkit targets Paper, Spigot, and Bukkit for
Minecraft 1.7.10 through 1.16.1.

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
         <artifactId>adventure-platform-bukkit</artifactId>
         <version>4.0.0-SNAPSHOT</version>
         </dependency>
   
   .. group-tab:: Gradle (Groovy)

      .. code:: groovy

         dependencies {
            implementation 'net.kyori:adventure-platform-bukkit:4.0.0-SNAPSHOT'
         }


   .. group-tab:: Gradle (Kotlin)

      .. code:: kotlin

         dependencies {
            implementation("net.kyori:adventure-platform-bukkit:4.0.0-SNAPSHOT")
         }

Usage
-----

You should first obtain an ``BukkitAudiences`` object by using ``BukkitAudiences.create(plugin)``. This object is thread-safe
and can be reused from different threads if needed. From here, Bukkit ``CommandSender`` s and ``Player`` s may be converted into
``Audience`` s using the appropriate methods on ``BukkitAudiences`` .

Component serializers
---------------------

The Bukkit platform provides the ``MinecraftComponentSerializer`` (available on Craftbukkit-based servers), and the ``BungeeCordComponentSerializer`` (available on Spigot and Paper servers) to convert directly between Adventure :doc:`Components </text>`
