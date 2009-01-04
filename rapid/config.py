### Copyright (C) 2007-09 Damon Lynch <damonlynch@gmail.com>

### This program is free software; you can redistribute it and/or modify
### it under the terms of the GNU General Public License as published by
### the Free Software Foundation; either version 2 of the License, or
### (at your option) any later version.

### This program is distributed in the hope that it will be useful,
### but WITHOUT ANY WARRANTY; without even the implied warranty of
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
### GNU General Public License for more details.

### You should have received a copy of the GNU General Public License
### along with this program; if not, write to the Free Software
### Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


GCONF_KEY="/apps/rapid-photo-downloader"
GLADE_FILE = "glade3/rapid.glade"

MEDIA_LOCATION = "/media"

SKIP_DOWNLOAD = "skip download"
ADD_UNIQUE_IDENTIFIER = "add unique identifier"

REPORT_WARNING = "warning"
REPORT_ERROR = "error"
IGNORE = "ignore"

DEFAULT_PHOTO_LOCATION = "Photos"

MAX_NO_READERS = 20

RAW_FILE_EXTENSIONS = ['arw', 'dcr', 'cr2', 'crw',  'dng', 'mef', 'mos', 'mrw', 
                        'nef', 'orf', 'pef', 'raf', 'raw', 'sr2']

NON_RAW_IMAGE_FILE_EXTENSIONS = ['jpg', 'jpe', 'jpeg', 'tif', 'tiff']

CRITICAL_ERROR = 1
SERIOUS_ERROR = 2
WARNING = 3



#logging - to be implemented
#LOGFILE_DIRECTORY = '.rapidPhotoDownloader' # relative to home directory
#MAX_LOGFILE_SIZE = 100 * 1024       # bytes
#MAX_LOGFILES  = 5
