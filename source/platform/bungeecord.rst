==========
BungeeCord 
==========

Adventure targets the latest version of BungeeCord and BungeeCord-compatible
forks, such as Waterfall.

Add the artifact to your build file:

First, add the repository:

.. tab-set::
   
   .. tab-item:: Maven
      :sync: maven

      .. code:: xml

         <repositories>
             <!-- ... -->
             <repository> <!-- for development builds -->
               <id>sonatype-oss-snapshots</id>
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
         <artifactId>adventure-platform-bungeecord</artifactId>
         <version>4.1.0</version>
         </dependency>
   
   .. tab-item:: Gradle (Groovy)
      :sync: gradle-groovy

      .. code:: groovy

         dependencies {
            implementation "net.kyori:adventure-platform-bungeecord:4.1.0"
         }


   .. tab-item:: Gradle (Kotlin)
      :sync: gradle-kotlin

      .. code:: kotlin

         dependencies {
            implementation("net.kyori:adventure-platform-bungeecord:4.1.0")
         }

Usage
-----

You should first obtain an ``BungeeAudiences`` object by using :java:`BungeeAudiences.create(plugin)`. This object is thread-safe
and can be reused from different threads if needed. This object should also be *closed* when the plugin is disabled.

Note that not all functionality is available on the proxy. Sending chat messages, action bar messages, titles, and boss bars, and tab list header and footer are supported, but all other requests will fail silently.

A simple example of how to appropriately initialize this platform follows:

.. code:: java

   public class MyPlugin extends Plugin {
     private BungeeAudiences adventure;

     public @NonNull BungeeAudiences adventure() {
       if(this.adventure == null) {
         throw new IllegalStateException("Cannot retrieve audience provider while plugin is not enabled");
       }
       return this.adventure;
     }

     @Override
     public void onEnable() {
       this.adventure = BungeeAudiences.create(this);
     }

     @Override
     public void onDisable() {
       if(this.adventure != null) {
         this.adventure.close();
         this.adventure = null;
       }
     }

   }

Component serializers
---------------------

For functionality not already supported by ``Audience``, the ``BungeeCordComponentSerializer`` allows you to convert between Adventure :doc:`Components </text>` and the native BungeeCord chat component API and back.

.. caution::

    For some areas of the proxy (notably, sending server list responses), the component serializer cannot be appropriately injected unless a ``BungeeAudiences`` instance has been initialized. Using Adventure ``Component`` instances **will not** work without a created ``BungeeAudiences`` instance.
