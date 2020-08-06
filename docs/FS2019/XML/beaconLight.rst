===========
beaconLight
===========

This is used to define the parameters for a Beacon Light (aka Strobe, or revolving light).

.. element:: beaconLight

    .. element:: fileName

    A string that specifies where to find the relavent i3d file for the beaconLight

    .. element:: rootNode

        :attrib node: The root node of the beaconLight in the i3d file structure.

    .. element:: rotator


        :attrib node: The node that the rotating element of the beacon can be found attribute
        :attrib speed: The speed that the beacon rotates attribute

    .. element:: light

        :attrib shaderNode: The node that contains the model of the light inside of the beacon
        :attrib intensity: The intensity (brightness) of the light

    .. element:: realLight

        :attrib node: The node that contains the actual light source object in the model.
