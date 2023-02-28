# SpotLighter
Save Windows SpotLight (lockscreen) wallpapers

## Notes
  * Batch versions will overwrite old wallpapers, since SpotLight has new wallpapers with old descriptions

## Python
* Full `.py` program, uses `os` library to run operating system commands
  * parses json files in ContentDeliveryManager's Spotlight metadata folder
  * Copies *only* SpotLight wallpapers from ContentDeliveryManager to `Spotbright\` (Landscape) and `Spotbright Portrait\` (Portrait)
    * Adds .jpg extension to files (`cbe08dfd20aa279904886c7dc465ee9f925a587bf96b948262f4f844db8f6c2f.jpg`)
    * Renames filename to description from metadata (`Lofoten Islands, Norway.jpg`)
    * Enumerates duplicate filenames (`Lofoten Islands, Norway (1).jpg`)

___
## Batch v0.2.1
* Builds and runs python commands
  * parses json files in ContentDeliveryManager's Spotlight metadata folder
  * Copies *only* SpotLight wallpapers from ContentDeliveryManager to `Spotbright\` (Landscape) and `Spotbright Portrait\` (Portrait)
    * Adds .jpg extension to files (`cbe08dfd20aa279904886c7dc465ee9f925a587bf96b948262f4f844db8f6c2f.jpg`)
    * Renames filename to description from metadata (`Lofoten Islands, Norway.jpg`)

## Batch v0.1.0
* Copies *ALL* files from ContentDeliveryManager
* Deletes the files under 150 KB (icons and logos)
* Adds .jpg extension to files (`cbe08dfd20aa279904886c7dc465ee9f925a587bf96b948262f4f844db8f6c2f.jpg`)
* Moves files to `Spotbright\` (Landscape & Portrait)
