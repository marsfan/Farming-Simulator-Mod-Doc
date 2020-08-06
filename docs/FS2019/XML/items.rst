=====
items
=====

Defines the position of interactive objects
(selling points, silos, gas station, etc.) on a map.

.. element:: items

   .. element:: item

      Define the information for a specific item/object.

      :attrib className: The type of object (workshop, siloPlaceable, etc)
      :attrib defaultFarmProperty: Whether or not the object is part of the player's farm at game start if the player chooses to start out with some structures.
      :attrib farmId: Which farm the object belongs to at game start.
      :attrib filename: filepath to the i3d file that contains the item's 3D model.
      :attrib mapBoundID:  The name used to refer to the object in the map. .. todo:: Double check this.
      :attrib position: Coordinates for where the object exists on the map.
      :attrib rotation: Coordinates for the rotation of the object on the map.
