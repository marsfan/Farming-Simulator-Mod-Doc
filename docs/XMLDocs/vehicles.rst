========
vehicles
========



Defines the default vehicles for a map that are given to the player when starting a game.


.. todo:: This document might be able to have more information than currently
      listed. This will need verification.

.. element:: vehicles

   .. element:: vehicle

      Configuration for a single vehicle.

      :param defaultFarmProperty: .. todo:: This attribute needs documenting.
      :param farmId: The farm that the vehicle belongs to.
      :param filename: Path to the i3d file that contains the vehicle.
      :param propertyState: .. todo:: This attribute needs documenting.
      :param tourId: .. todo:: This attribute needs documenting.
      :param xPosition: .. todo:: This attribute needs documenting.
      :param yOffset: .. todo:: This attribute needs documenting.
      :param yRotation: .. todo:: This attribute needs documenting.
      :param zPosition: .. todo:: This attribute needs documenting.

   .. element:: fillUnit

      .. element:: unit

         Used to define if the specificed vehicle is carrying anything.

         :param index: .. todo:: This attribute needs documenting.
         :param fillType: What is being carried.
         :param fillLevel: How much of the item is being carried.

   .. element:: sowingMachine

      Used to specify what type of seed the sowing machine is set to sow.

      :param selectedSeedFruitType: The type of seed selected.


   .. element:: configuration

      .. todo:: This element needs documentation

      :param name: .. todo:: This attribute needs documenting.
      :param id: .. todo:: This attribute needs documenting.

   .. element:: boughtConfiguration

      .. todo:: This element needs documentation.

      :param name: .. todo:: This attribute needs documenting.
      :param id: .. todo:: This attribute needs documenting.
      :attrib test: attribute test
      :attribute test: second attribute test
