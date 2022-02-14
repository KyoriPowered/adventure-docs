=========
SpongeAPI 
=========

Adventure provides a platform for SpongeAPI 7 for *Minecraft: Java Edition* 1.12. For SpongeAPI 8 and up (targeting *Minecraft: Java Edition* 1.16.4), Adventure is the native text library, so no platform is needed.

To get started using this platform, add the artifact to your build file:

First, add the repository:

.. tab-set::
   
   .. tab-item:: Maven
      :sync: maven

      .. code:: xml

         <repositories>
             <!-- ... -->
             <repository> <!-- for development builds -->
               <id>sonatype-oss</id>
               <url>https://oss.sonatype.org/content/repositories/snapshots/</url>
             </repository>
             <!-- ... -->
         </repositories>
   
   .. tab-item:: Gradle (Groovy)
      :sync: gradle-groovy

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

   .. tab-item:: Gradle (Kotlin)
      :sync: gradle-kotlin

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

.. tab-set::
   
   .. tab-item:: Maven
      :sync: maven

      .. code:: xml

         <dependency>
         <groupId>net.kyori</groupId>
         <artifactId>adventure-platform-spongeapi</artifactId>
         <version>4.0.1</version>
         </dependency>
   
   .. tab-item:: Gradle (Groovy)
      :sync: gradle-groovy

      .. code:: groovy

         dependencies {
            implementation "net.kyori:adventure-platform-spongeapi:4.0.1"
         }


   .. tab-item:: Gradle (Kotlin)
      :sync: gradle-kotlin

      .. code:: kotlin

         dependencies {
            implementation("net.kyori:adventure-platform-spongeapi:4.0.1")
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
