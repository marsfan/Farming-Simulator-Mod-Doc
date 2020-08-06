=====
wheel
=====

Defines properties for a wheel object.


Main Elements
=============

.. element:: wheel

   .. element:: default

      .. element:: physics

         Defines the physics properties  of the wheel.


         :param frictionScale: Decimal value to multiply base friction by for the wheel.
         :param mass: The mass of the wheel.
         :param maxLatStiffness: Maximum possible wheel stiffness on lateral axis.
         :param maxLatStiffnessLoad: .. todo:: Needs adding
         :param maxLongStiff: Maximum possible wheel stiffness on longitudinal axis.
         :param radius: The wheel radius
         :param tireType: The type of tire that the wheel has. The standard tire types in the game are: *mud*, *street*, *offRoad*,and *crawler*.
         :param width: The width of the wheel.


      .. element:: tire

         Configuration options for the tire. See :data:`tire` for details

      .. element:: outerRim

         Configuration for the outer rim of the wheel. See :data:`outerRim` for details

      .. element:: innerRim

         Configuration for the inner rim of the wheel. See :data:`innerRim` for details.

   .. element:: configuration

      Define additional possible configurations for the wheel

      .. element:: configuration

         :param id: Name/Identifier for the configuration.


         .. element:: tire

            Configuration options for the tire. See :data:`tire` for details

         .. element:: outerRim

            Configuration for the outer rim of the wheel. See :data:`outerRim` for details

         .. element:: innerRim

            Configuration for the inner rim of the wheel. See :data:`innerRim` for details.

         .. element:: additional

            Defines additional parts of the wheel. Commonly used to add wheel weights.

            :param filename: Path to i3d file for additional parts.
            :param mass: Mass of additional parts.
            :param nodeLeft: i3d node for left mounting
            :param nodeRight: i3d node for right mounting
            :param offset: Offset value for the model.
            :param scale: Scale for the model. Three values (x y z) seperated by spaces.



Elements Used Multiple Times in File
======================================

.. element:: tire

    :param filename: Path to the tire i3d file.
    :param isCareWheel: .. todo:: Needs adding
    :param maxDeformation: Maximum deformation the tire can have.
    :param nodeLeft: i3d node for mounting the wheel on the left.
    :param nodeRight: i3d node for mouting wheel on the right.
    :param tireTrackAtlasIndex: .. todo:: Needs adding

.. element:: outerRim

    :param filename: Path to the outer rim i3d file
    :param node: i3d node to use for alignment.
    :param scale: Scale factor to apply to the model
    :param widthAndDiam: Width and diameter of the outer rim. Seperated by spaces.

.. element:: innerRim

    :param filename: Path to the inner rim i3d file
    :param nodeLeft: Left side i3d node to use for alignment.
    :param nodeRight: Right side node to use for alignment
    :param offset: offset to apply to the model
    :param scale: Scale factor to apply to the model
    :param widthAndDiam: Width and diameter of the outer rim. Seperated by spaces.


