=================
transportMissions
=================

Defines parameters for the different possible transport missions on a map.

.. element:: transportMissions

   .. element:: mission

      Defines a specific mission type.

      :attrib name: The name of the mission type
      :attrib npcIndex: .. todo:: This attribute needs documenting.
      :attrib npcName: .. todo:: This attribute needs documenting.
      :attrib rewardScale: Scalar multiplier to apply to the base reward value.

   .. element:: pickupTrigger

      Defines a possible location for the transport mission to start at.

      :attrib index: Name/Index of the starting point for the mission.
      :attrib rewardScale: Scalar multiplier to apply to reward if mission starts at this location.
      :attrib title: Name of starting point to display in mission summary.

   .. element:: dropoffTrigger

      Defines a possible location for the mission.

      :attrib index: Name/Index of the ending point for the mission.
      :attrib rewardScale: Scalar multiplier to apply to reward if mission ends at this location.
      :attrib title: Name of ending point to display in mission summary.

   .. element:: object

      Defines the 3D object that is being transported.

      :attrib filename: Defines the filepath to the i3d file of the object's 3D model.
      :attrib max: The maximum possible number of objects to be transported.
      :attrib min: The minimum possible number of objects to be transported.
      :attrib offset: .. todo:: This file needs documenting
      :attrib size: .. todo:: This file needs documenting
      :attrib title: Name used to refer to the objects to be transported.