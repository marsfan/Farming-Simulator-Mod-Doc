=====
light
=====

Defines information for light objects (such as headlights, tail lights, and turn signals)

.. element:: light

   .. element:: filename

      Path to the i3d file with the light's 3D model.

   .. element:: rootnode

      :attrib node: The i3d reference to the object's root node.

   .. element:: brakeLight

      Definition of brake light parameters.

      :attrib intensity: Brightness of the light source.
      :attrib node: i3d node reference to the light source.

   .. element:: defaultLight

      Definition of headlight parameters.

      :attrib intensity: Brightness of the light source
      :attrib node: i3d node reference to the light source.
      :attrib lightTypes: .. todo:: This attribute needs documenting.

   .. element:: reverseLight

      Definition of reverse light parameters.

      :attrib intensity: Brightness of the light source
      :attrib node: i3d node reference to the light source.
      :attrib lightTypes: .. todo:: This attribute needs documenting.

   .. element:: turnLightLeft

      Definition of left turn signal paramters.

      :attrib intensity: Brightness of the light source
      :attrib node: i3d node reference to the light source.

   .. element:: turnLightRight

      Defintion of right turn signal parameters.

      :attrib intensity: Brightness of the light source
      :attrib node: i3d node reference to the light source.

   .. element:: rotationNode1

      i3d node reference to the lights rotation node.

      .. todo:: This element needs documenting.
