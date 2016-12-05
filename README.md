# NASA_wallpaper_collector
Script for crawling (about 4000) NASA images (could also be wallpaper) from [hubbleSpaceTelescope](https://www.spacetelescope.org/images/).

### USAGE:
Make sure you have at least 2GB space in your disk.

    ~ scrapy runspider allImagesIterator.py -o downloadAll.json

by default, downloaded images will be stored in

    NASA_wallpaper_collector/spiders/NASAWallPaper/full

You may want to delete those small images manually:

    ~ find full/ -name "*.jpg" -size -256k -delete

[![Screen Shot 2016-12-05 at 15.47.46.png](https://s17.postimg.org/3ozc4u48f/Screen_Shot_2016_12_05_at_15_47_46.png)](https://postimg.org/image/4ei4h74rv/)

[![Screen Shot 2016-12-05 at 16.38.53.png](https://s11.postimg.org/xbobtnpib/Screen_Shot_2016_12_05_at_16_38_53.png)](https://postimg.org/image/c20pit97j/)
