===============
Getting Started
===============

To use Adventure in your project, you will need to add the following dependency and repository (if using Gradle):

.. tab-set::

   .. tab-item:: Maven
      :sync: maven

      .. code-block:: xml
        :substitutions:

         <dependency>
            <groupId>net.kyori</groupId>
            <artifactId>adventure-api</artifactId>
            <version>|version|</version>
         </dependency>

   .. tab-item:: Gradle (Groovy)
      :sync: gradle-groovy

      .. code-block:: groovy
        :substitutions:

         repositories {
           mavenCentral()
         }

         dependencies {
            implementation "net.kyori:adventure-api:|version|"
         }


   .. tab-item:: Gradle (Kotlin)
      :sync: gradle-kotlin

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

.. tab-set::

   .. tab-item:: Maven
      :sync: maven

      .. code:: xml

         <repositories>
             <repository>
                <id>sonatype-oss-snapshots</id>
                <url>https://oss.sonatype.org/content/repositories/snapshots/</url>
             </repository>
         </repositories>

   .. tab-item:: Gradle (Groovy)
      :sync: gradle-groovy

      .. code:: groovy

         repositories {
            maven {
                name = "sonatype-oss-snapshots"
                url = "https://oss.sonatype.org/content/repositories/snapshots/"
            }
         }

   .. tab-item:: Gradle (Kotlin)
      :sync: gradle-kotlin

      .. code:: kotlin

         repositories {
            maven(url = "https://oss.sonatype.org/content/repositories/snapshots/") {
                name = "sonatype-oss-snapshots"
            }
         }
