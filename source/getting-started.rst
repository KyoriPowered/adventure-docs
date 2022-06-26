===============
Getting Started
===============

To use Adventure in your project, you will need to add the following dependency and repository (if using Gradle):

.. kyori-dep:: adventure-api api

Some platforms already use Adventure natively.
In this case, you will not need to add Adventure as a dependency.
To view the list of platforms that include Adventure, see :doc:`/platform/native`.

To use Adventure with other platforms, you may wish to look at the platform-specific adapters.
A list of platforms with supported adapters can be found at :doc:`/platform/index`.

.. _snapshot-reference:

Using Snapshot Builds
^^^^^^^^^^^^^^^^^^^^^

To use snapshot builds, you will need to add the following repository:

.. tab-set::

   .. tab-item:: Maven
      :sync: maven

      .. code:: xml

         <repositories>
             <repository>
                <id>sonatype-oss-snapshots1</id>
                <url>https://s01.oss.sonatype.org/content/repositories/snapshots/</url>
             </repository>
         </repositories>

   .. tab-item:: Gradle (Groovy)
      :sync: gradle-groovy

      .. code:: groovy

         repositories {
            maven {
                name = "sonatype-oss-snapshots1"
                url = "https://s01.oss.sonatype.org/content/repositories/snapshots/"
            }
         }

   .. tab-item:: Gradle (Kotlin)
      :sync: gradle-kotlin

      .. code:: kotlin

         repositories {
            maven(url = "https://s01.oss.sonatype.org/content/repositories/snapshots/") {
                name = "sonatype-oss-snapshots"
            }
         }
