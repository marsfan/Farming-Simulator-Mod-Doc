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


         :attrib frictionScale: Decimal value to multiply base friction by for the wheel.
         :attrib mass: The mass of the wheel.
         :attrib maxLatStiffness: Maximum possible wheel stiffness on lateral axis.
         :attrib maxLatStiffnessLoad: .. todo:: Needs adding
         :attrib maxLongStiff: Maximum possible wheel stiffness on longitudinal axis.
         :attrib radius: The wheel radius
         :attrib tireType: The type of tire that the wheel has. The standard tire types in the game are: *mud*, *street*, *offRoad*,and *crawler*.
         :attrib width: The width of the wheel.


      .. element:: tire

         Configuration options for the tire. See :data:`tire` for details

      .. element:: outerRim

         Configuration for the outer rim of the wheel. See :data:`outerRim` for details

      .. element:: innerRim

         Configuration for the inner rim of the wheel. See :data:`innerRim` for details.

   .. element:: configuration

      Define additional possible configurations for the wheel

      .. element:: configuration

         :attrib id: Name/Identifier for the configuration.


         .. element:: tire

            Configuration options for the tire. See :data:`tire` for details

         .. element:: outerRim

            Configuration for the outer rim of the wheel. See :data:`outerRim` for details

         .. element:: innerRim

            Configuration for the inner rim of the wheel. See :data:`innerRim` for details.

         .. element:: additional

            Defines additional parts of the wheel. Commonly used to add wheel weights.

            :attrib filename: Path to i3d file for additional parts.
            :attrib mass: Mass of additional parts.
            :attrib nodeLeft: i3d node for left mounting
            :attrib nodeRight: i3d node for right mounting
            :attrib offset: Offset value for the model.
            :attrib scale: Scale for the model. Three values (x y z) seperated by spaces.



Elements Used Multiple Times in File
======================================

.. element:: tire

    :attrib filename: Path to the tire i3d file.
    :attrib isCareWheel: .. todo:: Needs adding
    :attrib maxDeformation: Maximum deformation the tire can have.
    :attrib nodeLeft: i3d node for mounting the wheel on the left.
    :attrib nodeRight: i3d node for mouting wheel on the right.
    :attrib tireTrackAtlasIndex: .. todo:: Needs adding

.. element:: outerRim

    :attrib filename: Path to the outer rim i3d file
    :attrib node: i3d node to use for alignment.
    :attrib scale: Scale factor to apply to the model
    :attrib widthAndDiam: Width and diameter of the outer rim. Seperated by spaces.

.. element:: innerRim

    :attrib filename: Path to the inner rim i3d file
    :attrib nodeLeft: Left side i3d node to use for alignment.
    :attrib nodeRight: Right side node to use for alignment
    :attrib offset: offset to apply to the model
    :attrib scale: Scale factor to apply to the model
    :attrib widthAndDiam: Width and diameter of the outer rim. Seperated by spaces.


