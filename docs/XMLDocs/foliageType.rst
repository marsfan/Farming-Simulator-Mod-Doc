===========
foliageType
===========

Configuration information for different types of foliage on the map (bushes, grass, crops, etc.)

.. element:: foliageType

   :param distanceTexturePath: .. todo:: This attribute needs documenting.

   .. element:: foliageLayer

      :param cellSize: .. todo:: This attribute needs documenting.
      :param decalLayer: .. todo:: This attribute needs documenting.
      :param densityMapChannelOffset: .. todo:: This attribute needs documenting.
      :param name: The name of the foliage layer.
      :param numBlocksPerUnit: .. todo:: This attribute needs documenting.
      :param numDensityMapChannels: .. todo:: This attribute needs documenting.
      :param objectMask: .. todo:: This attribute needs documenting.
      :param shapeSource: The path to the i3d file that has the layer's 3D model.

      .. element:: foliageStateDefaults

         :param distanceMapLayer: .. todo:: This attribute needs documenting.
         :param heightVariance: .. todo:: This attribute needs documenting.
         :param horizontalPositionVariance: .. todo:: This attribute needs documenting.
         :param widthVariance: .. todo:: This attribute needs documenting.

      .. element:: foliageLoadDefaults

         :param atlasOffset: .. todo:: This attribute needs documenting.
         :param atlasSize: .. todo:: This attribute needs documenting.
         :param blendOutDistance: .. todo:: This attribute needs documenting.
         :param lod: .. todo:: This attribute needs documenting.
         :param texCoords: .. todo:: This attribute needs documenting.
         :param viewDistance: .. todo:: This attribute needs documenting.

      .. element:: foliageState

         :param distanceMap: .. todo:: This attribute needs documenting.
         :param distanceMapLyaer:
         :param height:
         :param heightVariance:
         :param horizontalPositionVariance:
         :param index:
         :param name: The name of the foliage state (e.g. green middle, harvest ready 2).
            Controls the way that the plant state is displayed on the map
         :param numBlocksPerUnit: .. todo:: This attribute needs documenting.
         :param width: .. todo:: This attribute needs documenting.
         :param widthVariance: .. todo:: This attribute needs documenting.

         .. element:: foliageShape

            .. element:: foliageLod

               Configuration for the Levels of detail for the foliage.

               :param atlasOffset: .. todo:: This attribute needs documenting.
               :param atlasSize: .. todo:: This attribute needs documenting.
               :param blockShape: .. todo:: This attribute needs documenting.
               :param lod: Which level of detail this configuration refers to.
               :param texCoords: .. todo:: This attribute needs documenting.
