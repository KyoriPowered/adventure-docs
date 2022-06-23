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

         dependencies {
            implementation "net.kyori:|artifact|:|version|"
         }


   .. tab-item:: Gradle (Kotlin)

      .. code-block:: kotlin
        :substitutions:

         dependencies {
            implementation("net.kyori:|artifact|:|version|")
         }
