##
# CSV Tiled Plugin
# Copyrigpyt 2014, Thorbjørn Lindeijer <thorbjorn@lindeijer.nl>
#
# This file is part of Tiled.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see .
##

from layer import Layer
from mapformat import WritableMapFormat
from PyQt5.QtCore import (
    QByteArray,
    QFile,
    QDir, 
    QFileInfo, 
    QIODevice,
    QSaveFile
)

class CsvPlugin(WritableMapFormat):
    def __init__(self):
        super().__init__()
        
        self.mError = ''

    # MapWriterInterface
    def write(self, map, fileName):       
        # Get file paths for each layer
        layerPaths = self.outputFiles(map, fileName)

        # Traverse all tile layers
        currentLayer = 0
        for layer in map.layers():
            if layer.layerType() != Layer.TileLayerType:
                continue
            
            tileLayer = layer

            file = QSaveFile(layerPaths[currentLayer])

            if (not file.open(QIODevice.WriteOnly | QIODevice.Text)):
                self.mError = self.tr("Could not open file for writing.")
                return False
            
            # Write out tiles either by ID or their name, if given. -1 is "empty"
            for y in range(0, tileLayer.height()):
                for x in range(0, tileLayer.width()):
                    if (x > 0):
                        file.write(",")
                    cell = tileLayer.cellAt(x, y)
                    tile = cell.tile
                    if (tile and tile.hasProperty("name")) :
                        file.write(tile.property("name").encode())
                    else:
                        if tile:
                            id = tile.id()
                        else:
                            id = -1
                        file.write(QByteArray.number(id))

                file.write("\n")
            
            if (file.error() != QFile.NoError) :
                self.mError = file.errorString()
                return False
            
            if (not file.commit()) :
                self.mError = file.errorString()
                return False

        return True
    
    def nameFilter(self):
        return self.tr("CSV files (*.csv)")
    
    def errorString(self):
        return self.mError

    def outputFiles(self, map, fileName):
        result = []

        # Extract file name without extension and path
        fileInfo = QFileInfo(fileName)
        base = fileInfo.completeBaseName() + "_"
        path = fileInfo.path()

        # Loop layers to calculate the path for the exported file
        for layer in map.layers():
            if layer.layerType() != Layer.TileLayerType:
                continue

            # Get the output file name for this layer
            layerName = layer.name()
            layerFileName = base + layerName + ".csv"
            layerFilePath = QDir(path).filePath(layerFileName)

            result.append(layerFilePath)

        # If there was only one tile layer, there's no need to change the name
        # (also keeps behavior backwards compatible)
        if len(result) == 1:
            result[0] = fileName

        return result
