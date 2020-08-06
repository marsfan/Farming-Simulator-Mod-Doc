=================
transportMissions
=================

Defines parameters for the different possible transport missions on a map.

.. element:: transportMissions

   .. element:: mission

      Defines a specific mission type.

      :param name: The name of the mission type
      :param npcIndex: .. todo:: This attribute needs documenting.
      :param npcName: .. todo:: This attribute needs documenting.
      :param rewardScale: Scalar multiplier to apply to the base reward value.

   .. element:: pickupTrigger

      Defines a possible location for the transport mission to start at.

      :param index: Name/Index of the starting point for the mission.
      :param rewardScale: Scalar multiplier to apply to reward if mission starts at this location.
      :param title: Name of starting point to display in mission summary.

   .. element:: dropoffTrigger

      Defines a possible location for the mission.

      :param index: Name/Index of the ending point for the mission.
      :param rewardScale: Scalar multiplier to apply to reward if mission ends at this location.
      :param title: Name of ending point to display in mission summary.

   .. element:: object

      Defines the 3D object that is being transported.

      :param filename: Defines the filepath to the i3d file of the object's 3D model.
      :param max: The maximum possible number of objects to be transported.
      :param min: The minimum possible number of objects to be transported.
      :param offset: .. todo:: This file needs documenting
      :param size: .. todo:: This file needs documenting
      :param title: Name used to refer to the objects to be transported.