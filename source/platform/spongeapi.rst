=========
SpongeAPI 
=========

Adventure provides a platform for SpongeAPI 7 for *Minecraft: Java Edition* 1.12. For SpongeAPI 8 and up (targeting *Minecraft: Java Edition* 1.16.4), Adventure is the native text library, so no platform is needed.

To get started using this platform, add the artifact to your build file:

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
         <artifactId>adventure-platform-spongeapi</artifactId>
         <version>4.0.0-SNAPSHOT</version>
         </dependency>
   
   .. group-tab:: Gradle (Groovy)

      .. code:: groovy

         dependencies {
            implementation "net.kyori:adventure-platform-spongeapi:4.0.0-SNAPSHOT"
         }


   .. group-tab:: Gradle (Kotlin)

      .. code:: kotlin

         dependencies {
            implementation("net.kyori:adventure-platform-spongeapi:4.0.0-SNAPSHOT")
         }


Usage
~~~~~

The SpongeAPI platform can either be created through Guice dependency injection, or created directly. We recommend using injection, since less boilerplate is requred.

An example plugin is fairly straightforward:

.. code:: java

   @Plugin(/* [...] */)
   public class MyPlugin {
     private final SpongeAudiences adventure;

     @Inject
     MyPlugin(final SpongeAudiences adventure) {
       this.adventure = adventure;
     }

     public @NonNull SpongeAudiences adventure() {
       return this.adventure;
     }
   }


This sets up a ``SpongeAudiences`` instance that can provide audiences for players, or any ``MessageReceiver``.
