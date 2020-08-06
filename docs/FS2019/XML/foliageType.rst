===========
foliageType
===========

Configuration information for different types of foliage on the map (bushes, grass, crops, etc.)

.. element:: foliageType

   :attrib distanceTexturePath: .. todo:: This attribute needs documenting.

   .. element:: foliageLayer

      :attrib cellSize: .. todo:: This attribute needs documenting.
      :attrib decalLayer: .. todo:: This attribute needs documenting.
      :attrib densityMapChannelOffset: .. todo:: This attribute needs documenting.
      :attrib name: The name of the foliage layer.
      :attrib numBlocksPerUnit: .. todo:: This attribute needs documenting.
      :attrib numDensityMapChannels: .. todo:: This attribute needs documenting.
      :attrib objectMask: .. todo:: This attribute needs documenting.
      :attrib shapeSource: The path to the i3d file that has the layer's 3D model.

      .. element:: foliageStateDefaults

         :attrib distanceMapLayer: .. todo:: This attribute needs documenting.
         :attrib heightVariance: .. todo:: This attribute needs documenting.
         :attrib horizontalPositionVariance: .. todo:: This attribute needs documenting.
         :attrib widthVariance: .. todo:: This attribute needs documenting.

      .. element:: foliageLoadDefaults

         :attrib atlasOffset: .. todo:: This attribute needs documenting.
         :attrib atlasSize: .. todo:: This attribute needs documenting.
         :attrib blendOutDistance: .. todo:: This attribute needs documenting.
         :attrib lod: .. todo:: This attribute needs documenting.
         :attrib texCoords: .. todo:: This attribute needs documenting.
         :attrib viewDistance: .. todo:: This attribute needs documenting.

      .. element:: foliageState

         :attrib distanceMap: .. todo:: This attribute needs documenting.
         :attrib distanceMapLyaer:
         :attrib height:
         :attrib heightVariance:
         :attrib horizontalPositionVariance:
         :attrib index:
         :attrib name: The name of the foliage state (e.g. green middle, harvest ready 2).
            Controls the way that the plant state is displayed on the map
         :attrib numBlocksPerUnit: .. todo:: This attribute needs documenting.
         :attrib width: .. todo:: This attribute needs documenting.
         :attrib widthVariance: .. todo:: This attribute needs documenting.

         .. element:: foliageShape

            .. element:: foliageLod

               Configuration for the Levels of detail for the foliage.

               :attrib atlasOffset: .. todo:: This attribute needs documenting.
               :attrib atlasSize: .. todo:: This attribute needs documenting.
               :attrib blockShape: .. todo:: This attribute needs documenting.
               :attrib lod: Which level of detail this configuration refers to.
               :attrib texCoords: .. todo:: This attribute needs documenting.
