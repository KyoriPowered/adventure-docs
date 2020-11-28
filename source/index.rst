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
         <dependencyManagement>
             <dependencies>
                 <dependency>
                     <groupId>net.kyori</groupId>
                     <artifactId>adventure-bom</artifactId>
                     <version>4.2.0</version>
                     <type>pom</type>
                     <scope>import</scope>
                 </dependency>
             </dependencies>
         </dependencyManagement>
         <dependency>
            <groupId>net.kyori</groupId>
            <artifactId>adventure-api</artifactId>
         </dependency>
   
   .. group-tab:: Gradle (Groovy)

      .. code:: groovy

         dependencies {
            implementation platform('net.kyori:adventure-bom:4.2.0')
             // Use dependency defined in BOM.
             // Version is not needed, because the version
             // defined in the BOM is a dependency constraint
             // that is used.
            implementation 'net.kyori:adventure-api'
         }


   .. group-tab:: Gradle (Kotlin)

      .. code:: kotlin

         dependencies {
            implementation(platform("net.kyori:adventure-bom:4.2.0"))
            implementation("net.kyori:adventure-api")
         }

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
