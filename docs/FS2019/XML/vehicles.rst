========
vehicles
========



Defines the default vehicles for a map that are given to the player when starting a game.


.. todo:: This document might be able to have more information than currently
      listed. This will need verification.

.. element:: vehicles

   .. element:: vehicle

      Configuration for a single vehicle.

      :attrib defaultFarmProperty: .. todo:: This attribute needs documenting.
      :attrib farmId: The farm that the vehicle belongs to.
      :attrib filename: Path to the i3d file that contains the vehicle.
      :attrib propertyState: .. todo:: This attribute needs documenting.
      :attrib tourId: .. todo:: This attribute needs documenting.
      :attrib xPosition: .. todo:: This attribute needs documenting.
      :attrib yOffset: .. todo:: This attribute needs documenting.
      :attrib yRotation: .. todo:: This attribute needs documenting.
      :attrib zPosition: .. todo:: This attribute needs documenting.

   .. element:: fillUnit

      .. element:: unit

         Used to define if the specificed vehicle is carrying anything.

         :attrib index: .. todo:: This attribute needs documenting.
         :attrib fillType: What is being carried.
         :attrib fillLevel: How much of the item is being carried.

   .. element:: sowingMachine

      Used to specify what type of seed the sowing machine is set to sow.

      :attrib selectedSeedFruitType: The type of seed selected.


   .. element:: configuration

      .. todo:: This element needs documentation

      :attrib name: .. todo:: This attribute needs documenting.
      :attrib id: .. todo:: This attribute needs documenting.

   .. element:: boughtConfiguration

      .. todo:: This element needs documentation.

      :attrib name: .. todo:: This attribute needs documenting.
      :attrib id: .. todo:: This attribute needs documenting.
