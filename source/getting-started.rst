===============
Getting Started
===============

To use Adventure in your project, you will need to add the following dependency and repository (if using Gradle):

.. tabs::

   .. group-tab:: Maven

      .. code-block:: xml
        :substitutions:

         <dependency>
            <groupId>net.kyori</groupId>
            <artifactId>adventure-api</artifactId>
            <version>|version|</version>
         </dependency>

   .. group-tab:: Gradle (Groovy)

      .. code-block:: groovy
        :substitutions:

         repositories {
           mavenCentral()
         }

         dependencies {
            implementation "net.kyori:adventure-api:|version|"
         }


   .. group-tab:: Gradle (Kotlin)

      .. code-block:: kotlin
        :substitutions:

         repositories {
           mavenCentral()
         }

         dependencies {
            implementation("net.kyori:adventure-api:|version|")
         }

Some platforms already use Adventure natively.
In this case, you will not need to add Adventure as a dependency.
To view the list of platforms that include Adventure, see :doc:`/platform/native`.

To use Adventure with other platforms, you may wish to look at the platform-specific adapters.
A list of platforms with supported adapters can be found at :doc:`/platform/index`.

Using Snapshot Builds
^^^^^^^^^^^^^^^^^^^^^

To use snapshot builds, you will need to add the following repository:

.. tabs::

   .. group-tab:: Maven

      .. code:: xml

         <repositories>
             <repository>
                <id>sonatype-oss-snapshots</id>
                <url>https://oss.sonatype.org/content/repositories/snapshots/</url>
             </repository>
         </repositories>

   .. group-tab:: Gradle (Groovy)

      .. code:: groovy

         repositories {
            maven {
                name = "sonatype-oss-snapshots"
                url = "https://oss.sonatype.org/content/repositories/snapshots/"
            }
         }

   .. group-tab:: Gradle (Kotlin)

      .. code:: kotlin

         repositories {
            maven(url = "https://oss.sonatype.org/content/repositories/snapshots/") {
                name = "sonatype-oss-snapshots"
            }
         }