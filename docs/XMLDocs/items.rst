=====
items
=====

Defines the position of interactive objects
(selling points, silos, gas station, etc.) on a map.

.. element:: items

   .. element: item

      Define the information for a specific item/object.

      :param className: The type of object (workshop, siloPlaceable, etc)
      :param defaultFarmProperty: Whether or not the object is part of the player's farm at game start if the player
         chooses to start out with some structures.
      :param farmId: Which farm the object belongs to at game start.
      :param filename: filepath to the i3d file that contains the item's 3D model.
      :param mapBoundID:  The name used to refer to the object in the map. .. todo:: Double check this.
      :param position: Coordinates for where the object exists on the map.
      :param rotation: Coordinates for the rotation of the object on the map.
