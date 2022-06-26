Declaring the dependency:

.. tab-set::

   .. tab-item:: Maven

      .. code-block:: xml
        :substitutions:

         <dependency>
            <groupId>net.kyori</groupId>
            <artifactId>|artifact|</artifactId>
            <version>|version|</version>
         </dependency>

   .. tab-item:: Gradle (Groovy)

      .. code-block:: groovy
        :substitutions:

         repositories {
            mavenCentral()
         }

         dependencies {
            implementation "net.kyori:|artifact|:|version|"
         }


   .. tab-item:: Gradle (Kotlin)

      .. code-block:: kotlin
        :substitutions:

         repositories {
            mavenCentral()
         }

         dependencies {
            implementation("net.kyori:|artifact|:|version|")
         }

Need development/snapshot builds? :ref:`snapshot-reference`