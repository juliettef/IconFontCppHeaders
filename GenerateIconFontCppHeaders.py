# Convert Font Awesome, Fork Awesome, Google Material Design, Pictogrammers Material Design Icons, Kenney Game, 
# Fontaudio, Codicons and Lucide icon font parameters to C, C++, C#, Python, Rust and Go compatible formats.
#
#------------------------------------------------------------------------------
#
# 1 - Source material
#
#   1.1 - Font Awesome [ FA ]
#       https://fontawesome.com
#       https://github.com/FortAwesome/Font-Awesome
#
#       1.1.1 - version 4
#           https://github.com/FortAwesome/Font-Awesome/tree/4.x
#           https://github.com/FortAwesome/Font-Awesome/blob/4.x/src/icons.yml
#           https://github.com/FortAwesome/Font-Awesome/blob/4.x/fonts/fontawesome-webfont.ttf
#
#       1.1.2 - version 5 Free
#           https://github.com/FortAwesome/Font-Awesome/tree/5.x
#           https://github.com/FortAwesome/Font-Awesome/blob/5.x/metadata/icons.yml
#           https://github.com/FortAwesome/Font-Awesome/blob/5.x/webfonts/fa-brands-400.ttf [ FAB ]
#           https://github.com/FortAwesome/Font-Awesome/blob/5.x/webfonts/fa-regular-400.ttf [ FAR ]
#           https://github.com/FortAwesome/Font-Awesome/blob/5.x/webfonts/fa-solid-900.ttf [ FAS ]
#
#       1.1.3 - version 5 Pro
#           Download files from https://fontawesome.com
#           \fontawesome-pro-n.n.n-web\metadata\icons.yml
#           \fontawesome-pro-n.n.n-web\webfonts\fa-brands-400.ttf [ FAB ]
#           \fontawesome-pro-n.n.n-web\webfonts\fa-light-300.ttf [ FAL ]
#           \fontawesome-pro-n.n.n-web\webfonts\fa-regular-400.ttf [ FAR ]
#           \fontawesome-pro-n.n.n-web\webfonts\fa-solid-900.ttf [ FAS ]
#
#       1.1.4 - version 6 Free
#           https://github.com/FortAwesome/Font-Awesome/tree/6.x
#           https://github.com/FortAwesome/Font-Awesome/blob/6.x/metadata/icons.yml
#           https://github.com/FortAwesome/Font-Awesome/blob/6.x/webfonts/fa-brands-400.ttf [ FAB ]
#           https://github.com/FortAwesome/Font-Awesome/blob/6.x/webfonts/fa-regular-400.ttf [ FAR ]
#           https://github.com/FortAwesome/Font-Awesome/blob/6.x/webfonts/fa-solid-900.ttf [ FAS ]
#
#   1.2 - Fork Awesome [ FK ]
#           https://forkaweso.me/Fork-Awesome/
#           https://github.com/ForkAwesome/Fork-Awesome
#           https://github.com/ForkAwesome/Fork-Awesome/blob/master/src/icons/icons.yml
#           https://github.com/ForkAwesome/Fork-Awesome/blob/master/fonts/forkawesome-webfont.ttf
#
#   1.3 - Google Material Design Icons [ MD ] and Material Symbols [ MS ]
#           https://fonts.google.com/icons
#           https://github.com/google/material-design-icons
#
#       1.3.1 - Material Design Icons [ MD ]
#           https://fonts.google.com/icons?icon.set=Material+Icons
#           https://github.com/google/material-design-icons/blob/master/font/MaterialIcons-Regular.codepoints
#           https://github.com/google/material-design-icons/blob/master/font/MaterialIcons-Regular.ttf
#
#       1.3.2 - Material Symbols [ MS ]
#           https://fonts.google.com/icons?icon.set=Material+Symbols
#           https://github.com/google/material-design-icons/blob/master/variablefont/MaterialSymbolsOutlined%5BFILL%2CGRAD%2Copsz%2Cwght%5D.codepoints
#           https://github.com/google/material-design-icons/blob/master/variablefont/MaterialSymbolsOutlined%5BFILL,GRAD,opsz,wght%5D.ttf [ MSO ]
#           https://github.com/google/material-design-icons/blob/master/variablefont/MaterialSymbolsRounded[FILL,GRAD,opsz,wght].ttf [ MSR ]
#           https://github.com/google/material-design-icons/blob/master/variablefont/MaterialSymbolsSharp[FILL,GRAD,opsz,wght].ttf [ MSS ]
#
#   1.4 - Pictogrammers Material Design Icons [ MDI ]
#           https://pictogrammers.com/library/mdi/
#           https://github.com/Templarian/MaterialDesign-Webfont
#           https://github.com/Templarian/MaterialDesign-Webfont/blob/master/css/materialdesignicons.css
#           https://github.com/Templarian/MaterialDesign-Webfont/blob/master/fonts/materialdesignicons-webfont.ttf
#
#   1.5 - Kenney Game Icons and Expansion [ KI ]
#           http://kenney.nl/assets/game-icons http://kenney.nl/assets/game-icons-expansion
#           https://github.com/nicodinh/kenney-icon-font
#           https://github.com/nicodinh/kenney-icon-font/blob/master/css/kenney-icons.css
#           https://github.com/nicodinh/kenney-icon-font/blob/master/fonts/kenney-icon-font.ttf
#
#   1.6 - Fontaudio [ FAD ]
#           https://github.com/fefanto/fontaudio
#           https://github.com/fefanto/fontaudio/blob/master/font/fontaudio.css
#           https://github.com/fefanto/fontaudio/blob/master/font/fontaudio.ttf
#
#   1.7 - Codicons [ CI ]
#           https://microsoft.github.io/vscode-codicons/dist/codicon.html
#           https://github.com/microsoft/vscode-codicons
#           https://microsoft.github.io/vscode-codicons/dist/codicon.css
#           https://microsoft.github.io/vscode-codicons/dist/codicon.ttf
#
#   1.8 - Lucide [ LC ]
#           https://lucide.dev
#           https://github.com/lucide-icons/lucide
#           https://unpkg.com/lucide-static@latest/font/lucide.css
#           https://unpkg.com/lucide-static@latest/font/lucide.ttf
#
#
#------------------------------------------------------------------------------
#
# 2 - Data sample
#
#   Font Awesome 4 example:
#
#           - input:                music:
#                                     changes:
#                                       - '1'
#                                       - 5.0.0
#                                     label: Music
#                                     search:
#                                       terms:
#                                         - note
#                                         - sound
#                                     styles:
#                                       - solid
#                                     unicode: f001
#
#           - output C and C++:     #define ICON_FA_MUSIC "\xef\x80\x81"	// U+f001
#           - output C#:            public const string Music = "\uf001";
#           - output Python:        ICON_MUSIC = '\uf001'
#           - output Rust:          pub const ICON_MUSIC: char = '\u{f001}';
#           - output Go:            "Music":	"\xef\x80\x81", 	// U+f001
#
#   All fonts have computed min, max_16 and max unicode fonts.
#   The min excludes the ASCII characters code points.
#   The max_16 is for use with libraries that only support 16 bit code points.
#
#           - output C and C++:     #define ICON_MIN_FA 0xf000
#                                   #define ICON_MAX_16_FA 0xf2e0
#                                   #define ICON_MAX_FA 0xf2e0
#             Exception for Font Awesome brands: we use ICON_MIN_FAB, ICON_MAX_16_FAB and ICON_MAX_FAB
#             to differentiate between brand and non-brand icons so they can be used together
#             (the defines must be unique in C and C++).
#
#           - output C#:            public const int IconMin = 0xf000;
#                                   public const int IconMax16 = 0xf2e0;
#                                   public const int IconMax = 0xf2e0;
#
#           - output Python:        ICON_MIN = 0xf000
#                                   ICON_MAX_16 = 0xf2e0
#                                   ICON_MAX = 0xf2e0
#
#           - output Rust:          pub const ICON_MIN: char = '\u{f000}';
#                                   pub const ICON_MAX_16: char = '\u{f2e0}';
#                                   pub const ICON_MAX: char = '\u{f2e0}';
#
#           - output Go:            Min: 0xf000,
#                                   Max16: 0xf2e0,
#                                   Max: 0xf2e0,
#
#------------------------------------------------------------------------------
#
# 3 - Script dependencies
#
#   3.1 - Fonts source material online
#   3.2 - Python 3 - https://www.python.org/downloads/
#   3.3 - Requests - https://pypi.org/project/requests/
#   3.4 - PyYAML - https://pypi.org/project/PyYAML/
#
#------------------------------------------------------------------------------
#
# 4 - References
#
#   GitHub repository: https://github.com/juliettef/IconFontCppHeaders/
#
#------------------------------------------------------------------------------


import requests
import yaml
import os
import sys
import logging

if sys.version_info[0] < 3:
    raise Exception( "Python 3 or a more recent version is required." )

# Fonts

class Font:
    font_name = '[ ERROR - Missing font name ]'
    font_abbr = '[ ERROR - Mssing font abbreviation ]'
    font_minmax_abbr = ''   # optional - use if min and max defines must be differentiated. See Font Awesome Brand for example.
    font_data = '[ ERROR - Missing font data file or url ]'
    ttfs = '[ ERROR - Missing ttf ]'

    @classmethod
    def get_icons( cls, input_data ):
        # intermediate representation of the fonts data, identify the min and max
        logging.error( 'Missing implementation of class method get_icons for {!s} ]'.format( cls.font_name ))
        icons_data = {}
        icons_data.update({ 'font_min' : '[ ERROR - Missing font min ]',
                            'font_max' : '[ ERROR - Missing font max ]',
                            'icons' : '[ ERROR - Missing list of pairs [ font icon name, code ]]' })
        return icons_data

    @classmethod
    def get_intermediate_representation( cls ):
        font_ir = {}
        if 'http' in cls.font_data:  # if url, download data
            response = requests.get( cls.font_data, timeout = 2 )
            if response.status_code == 200:
                input_raw = response.text
                logging.info( 'Downloaded - ' + cls.font_name )
            else:
                raise Exception( 'Download failed - ' + cls.font_name )
        else:   # read data from file if present
            if os.path.isfile( cls.font_data ):
                with open( cls.font_data, 'r' ) as f:
                    input_raw = f.read()
                    f.close()
                    logging.info( 'File read - ' + cls.font_name )
            else:
                raise Exception( 'File ' + cls.font_name + ' missing - ' + cls.font_data )
        if input_raw:
            icons_data = cls.get_icons( input_raw )
            font_ir.update( icons_data )
            font_ir.update({ 'font_data' : cls.font_data,
                             'font_name' : cls.font_name,
                             'font_abbr' : cls.font_abbr,
                             'font_minmax_abbr' : cls.font_minmax_abbr,
                             'ttfs' : cls.ttfs, })
            logging.info( 'Generated intermediate data - ' + cls.font_name )
        return font_ir


class FontFA4( Font ):              # legacy Font Awesome version 4
    font_name = 'Font Awesome 4'
    font_abbr = 'FA'
    font_data = 'https://github.com/FortAwesome/Font-Awesome/raw/4.x/src/icons.yml'
    ttfs = [[ font_abbr, 'fontawesome-webfont.ttf', 'https://github.com/FortAwesome/Font-Awesome/blob/4.x/fonts/fontawesome-webfont.ttf' ]]

    @classmethod
    def get_icons( cls, input_data ):
        icons_data = { }
        data = yaml.safe_load( input_data )
        font_min = '0x10ffff'
        font_min_int = int( font_min, 16 )
        font_max_16 = '0x0'   # 16 bit max 
        font_max_16_int = int( font_max_16, 16 )
        font_max = '0x0'
        font_max_int = int( font_max, 16 )
        icons = []
        for item in data[ 'icons' ]:
            item_unicode = item[ 'unicode' ].zfill( 4 )
            item_int = int( item_unicode, 16 )
            if item_int < font_min_int and item_int > 0x0127 :  # exclude ASCII characters code points
                font_min = item_unicode
                font_min_int = item_int
            if item_int > font_max_16_int and item_int <= 0xffff:   # exclude code points > 16 bits
                font_max_16 = item_unicode
                font_max_16_int = item_int
            if item_int > font_max_int:
                font_max = item_unicode
                font_max_int = item_int
            icons.append([ item[ 'id' ], item_unicode ])
        icons_data.update({ 'font_min' : font_min,
                            'font_max_16' : font_max_16,
                            'font_max' : font_max,
                            'icons' : icons })
        return icons_data


class FontFK( FontFA4 ):            # Fork Awesome, based on Font Awesome 4
    font_name = 'Fork Awesome'
    font_abbr = 'FK'
    font_data = 'https://github.com/ForkAwesome/Fork-Awesome/raw/master/src/icons/icons.yml'
    ttfs = [[ font_abbr, 'forkawesome-webfont.ttf', 'https://github.com/ForkAwesome/Fork-Awesome/blob/master/fonts/forkawesome-webfont.ttf' ]]


class FontFA5( Font ):              # Font Awesome version 5 - Regular and Solid styles
    font_name = 'Font Awesome 5'
    font_abbr = 'FA'
    font_data = 'https://github.com/FortAwesome/Font-Awesome/raw/5.x/metadata/icons.yml'
    ttfs = [[ 'FAR', 'fa-regular-400.ttf', 'https://github.com/FortAwesome/Font-Awesome/blob/5.x/webfonts/fa-regular-400.ttf' ],
            [ 'FAS', 'fa-solid-900.ttf', 'https://github.com/FortAwesome/Font-Awesome/blob/5.x/webfonts/fa-solid-900.ttf' ]]
    font_fa_style = [ 'regular', 'solid' ]

    @classmethod
    def get_icons( cls, input_data ):
        icons_data = { }
        data = yaml.safe_load( input_data )
        if data:
            font_min = '0x10ffff'
            font_min_int = int( font_min, 16 )
            font_max_16 = '0x0'   # 16 bit max 
            font_max_16_int = int( font_max_16, 16 )
            font_max = '0x0'
            font_max_int = int( font_max, 16 )
            icons = []
            for key in data:
                item = data[ key ]
                for style in item[ 'styles' ]:
                    if style in cls.font_fa_style:
                        item_unicode = item[ 'unicode' ].zfill( 4 )
                        if [ key, item_unicode ] not in icons:
                            item_int = int( item_unicode, 16 )
                            if item_int < font_min_int and item_int > 0x0127 :  # exclude ASCII characters code points
                                font_min = item_unicode
                                font_min_int = item_int
                            if item_int > font_max_16_int and item_int <= 0xffff:   # exclude code points > 16 bits
                                font_max_16 = item_unicode
                                font_max_16_int = item_int
                            if item_int > font_max_int:
                                font_max = item_unicode
                                font_max_int = item_int
                            icons.append([ key, item_unicode ])
            icons_data.update({ 'font_min':font_min, 
                                'font_max_16' : font_max_16,
                                'font_max':font_max, 
                                'icons':icons })
        return icons_data


class FontFA5Brands( FontFA5 ):     # Font Awesome version 5 - Brand style
    font_name = 'Font Awesome 5 Brands'
    font_minmax_abbr = 'FAB'
    ttfs = [[ 'FAB', 'fa-brands-400.ttf', 'https://github.com/FortAwesome/Font-Awesome/blob/5.x/webfonts/fa-brands-400.ttf' ]]
    font_fa_style = [ 'brands' ]


class FontFA5Pro( FontFA5 ):        # Font Awesome version 5 Pro - Light, Regular and Solid styles
    font_name = 'Font Awesome 5 Pro'
    font_data = 'icons.yml'
    ttfs = [[ 'FAL', 'fa-light-300.ttf', 'fa-light-300.ttf' ],
            [ 'FAR', 'fa-regular-400.ttf', 'fa-regular-400.ttf' ],
            [ 'FAS', 'fa-solid-900.ttf', 'fa-solid-900.ttf' ]]
    font_fa_style = [ 'light', 'regular', 'solid' ]


class FontFA5ProBrands( FontFA5Brands ):  # Font Awesome version 5 Pro - Brand style
    font_name = 'Font Awesome 5 Pro Brands'
    font_data = 'icons.yml'
    ttfs = [[ 'FAB', 'fa-brands-400.ttf', 'fa-brands-400.ttf' ]]


class FontFA6( FontFA5 ):           # Font Awesome version 6 - Regular and Solid styles
    font_name = 'Font Awesome 6'
    font_data = 'https://github.com/FortAwesome/Font-Awesome/raw/6.x/metadata/icons.yml'
    ttfs = [[ 'FAR', 'fa-regular-400.ttf', 'https://github.com/FortAwesome/Font-Awesome/blob/6.x/webfonts/fa-regular-400.ttf' ],
            [ 'FAS', 'fa-solid-900.ttf', 'https://github.com/FortAwesome/Font-Awesome/blob/6.x/webfonts/fa-solid-900.ttf' ]]


class FontFA6Brands( FontFA5Brands ):     # Font Awesome version 6 - Brand style
    font_name = 'Font Awesome 6 Brands'
    font_data = 'https://github.com/FortAwesome/Font-Awesome/raw/6.x/metadata/icons.yml'
    ttfs = [[ 'FAB', 'fa-brands-400.ttf', 'https://github.com/FortAwesome/Font-Awesome/blob/6.x/webfonts/fa-brands-400.ttf' ]]


class FontMD( Font ):               # Google Material Design
    font_name = 'Material Design'
    font_abbr = 'MD'
    font_data = 'https://github.com/google/material-design-icons/raw/master/font/MaterialIcons-Regular.codepoints'
    ttfs = [[ font_abbr, 'MaterialIcons-Regular.ttf', 'https://github.com/google/material-design-icons/blob/master/font/MaterialIcons-Regular.ttf' ]]

    @classmethod
    def get_icons( cls, input_data ):
        icons_data = {}
        lines = str.split( input_data, '\n' )
        if lines:
            font_min = '0x10ffff'
            font_min_int = int( font_min, 16 )
            font_max_16 = '0x0'   # 16 bit max 
            font_max_16_int = int( font_max_16, 16 )
            font_max = '0x0'
            font_max_int = int( font_max, 16 )
            icons = []
            for line in lines :
                if line == 'flourescent ec31': # Issue #27 workaround: exclude duplicate Material Design 'flourescent ec31'. https://github.com/juliettef/IconFontCppHeaders/issues/27
                    logging.warning( "Issue #27 workaround: exclude duplicate Material Design 'flourescent ec31'. https://github.com/juliettef/IconFontCppHeaders/issues/27" )
                else:
                    words = str.split(line)
                    if words and len( words ) >= 2:
                        word_unicode = words[ 1 ].zfill( 4 )
                        word_int = int( word_unicode, 16 )
                        if word_int < font_min_int and word_int > 0x0127 :  # exclude ASCII characters code points
                            font_min = word_unicode
                            font_min_int = word_int
                        if word_int > font_max_16_int and word_int <= 0xffff:   # exclude code points > 16 bits
                            font_max_16 = word_unicode
                            font_max_16_int = word_int
                        if word_int > font_max_int:
                            font_max = word_unicode
                            font_max_int = word_int
                        icons.append( words )
            icons_data.update({ 'font_min' : font_min,
                                'font_max_16' : font_max_16,
                                'font_max' : font_max,
                                'icons' : icons })
        return icons_data


class FontMS( Font ):               # Google Material Symbols
    font_name = 'Material Symbols'
    font_abbr = 'MS'
    font_data = 'https://github.com/google/material-design-icons/raw/master/variablefont/MaterialSymbolsOutlined%5BFILL%2CGRAD%2Copsz%2Cwght%5D.codepoints'
    ttfs = [[ 'MSO', 'MaterialSymbolsOutlined[FILL,GRAD,opsz,wght].ttf', 'https://github.com/google/material-design-icons/raw/master/variablefont/MaterialSymbolsOutlined%5BFILL,GRAD,opsz,wght%5D.ttf' ],
            [ 'MSR', 'MaterialSymbolsRounded[FILL,GRAD,opsz,wght].ttf', 'https://github.com/google/material-design-icons/raw/master/variablefont/MaterialSymbolsRounded%5BFILL,GRAD,opsz,wght%5D.ttf' ],
            [ 'MSS', 'MaterialSymbolsSharp[FILL,GRAD,opsz,wght].ttf', 'https://github.com/google/material-design-icons/raw/master/variablefont/MaterialSymbolsSharp%5BFILL,GRAD,opsz,wght%5D.ttf' ]]

    @classmethod
    def get_icons( cls, input_data ):
        icons_data = {}
        lines = str.split( input_data, '\n' )
        if lines:
            font_min = '0x10ffff'
            font_min_int = int( font_min, 16 )
            font_max_16 = '0x0'   # 16 bit max 
            font_max_16_int = int( font_max_16, 16 )
            font_max = '0x0'
            font_max_int = int( font_max, 16 )
            icons = []
            for line in lines :
                words = str.split(line)
                if words and len( words ) >= 2:
                    word_unicode = words[ 1 ].zfill( 4 )
                    word_int = int( word_unicode, 16 )
                    if word_int < font_min_int and word_int > 0x0127 :  # exclude ASCII characters code points
                        font_min = word_unicode
                        font_min_int = word_int
                    if word_int > font_max_16_int and word_int <= 0xffff:   # exclude code points > 16 bits
                        font_max_16 = word_unicode
                        font_max_16_int = word_int
                    if word_int > font_max_int:
                        font_max = word_unicode
                        font_max_int = word_int
                    icons.append( words )
            icons_data.update({ 'font_min' : font_min,
                                'font_max_16' : font_max_16,
                                'font_max' : font_max,
                                'icons' : icons })
        return icons_data


class FontMDI( Font ):               # Pictogrammers Material Design Icons
    font_name = 'Material Design Icons'
    font_abbr = 'MDI'
    font_data_prefix = '.mdi-'
    font_data = 'https://github.com/Templarian/MaterialDesign-Webfont/raw/master/css/materialdesignicons.css'
    ttfs = [[ font_abbr, 'materialdesignicons-webfont.ttf', 'https://github.com/Templarian/MaterialDesign-Webfont/raw/master/fonts/materialdesignicons-webfont.ttf' ]]

    @classmethod
    def get_icons( cls, input_data ):
        icons_data = {}
        lines = str.split( input_data, '}\n' )
        if lines:
            font_min = '0x10ffff'
            font_min_int = int( font_min, 16 )
            font_max_16 = '0x0'   # 16 bit max 
            font_max_16_int = int( font_max_16, 16 )
            font_max = '0x0'
            font_max_int = int( font_max, 16 )
            icons = []
            for line in lines :
                if cls.font_data_prefix in line and '::before' in line:
                    font_id = line.partition( cls.font_data_prefix )[ 2 ].partition( '::before' )[ 0 ]
                    font_code = line.partition( '"\\' )[ 2 ].partition( '"' )[ 0 ].zfill( 4 )
                    font_code_int = int( font_code, 16 )
                    if font_code_int < font_min_int and font_code_int > 0x0127 :  # exclude ASCII characters code points
                        font_min = font_code
                        font_min_int = font_code_int
                    if font_code_int > font_max_16_int and font_code_int <= 0xffff:   # exclude code points > 16 bits
                        font_max_16 = font_code
                        font_max_16_int = font_code_int
                    if font_code_int > font_max_int:
                        font_max = font_code
                        font_max_int = font_code_int
                    icons.append([ font_id, font_code ])
            icons_data.update({ 'font_min' : font_min,
                                'font_max_16' : font_max_16,
                                'font_max' : font_max,
                                'icons' : icons  })
        return icons_data


class FontKI( Font ):               # Kenney Game icons
    font_name = 'Kenney'
    font_abbr = 'KI'
    font_data_prefix = '.ki-'
    font_data = 'https://github.com/nicodinh/kenney-icon-font/raw/master/css/kenney-icons.css'
    ttfs = [[ font_abbr, 'kenney-icon-font.ttf', 'https://github.com/nicodinh/kenney-icon-font/blob/master/fonts/kenney-icon-font.ttf' ]]

    @classmethod
    def get_icons( cls, input_data ):
        icons_data = {}
        lines = str.split( input_data, '}\n' )
        if lines:
            font_min = '0x10ffff'
            font_min_int = int( font_min, 16 )
            font_max_16 = '0x0'   # 16 bit max 
            font_max_16_int = int( font_max_16, 16 )
            font_max = '0x0'
            font_max_int = int( font_max, 16 )
            icons = []
            for line in lines :
                if cls.font_data_prefix in line and ':before' in line:
                    font_id = line.partition( cls.font_data_prefix )[ 2 ].partition( ':before' )[ 0 ]
                    font_code = line.partition( '"\\' )[ 2 ].partition( '"' )[ 0 ].zfill( 4 )
                    font_code_int = int( font_code, 16 )
                    if font_code_int < font_min_int and font_code_int > 0x0127 :  # exclude ASCII characters code points
                        font_min = font_code
                        font_min_int = font_code_int
                    if font_code_int > font_max_16_int and font_code_int <= 0xffff:   # exclude code points > 16 bits
                        font_max_16 = font_code
                        font_max_16_int = font_code_int
                    if font_code_int > font_max_int:
                        font_max = font_code
                        font_max_int = font_code_int
                    icons.append([ font_id, font_code ])
            icons_data.update({ 'font_min' : font_min,
                                'font_max_16' : font_max_16,
                                'font_max' : font_max,
                                'icons' : icons  })
        return icons_data


class FontFAD( FontKI ):               # Fontaudio
    font_name = 'Fontaudio'
    font_abbr = 'FAD'
    font_data_prefix = '.icon-fad-'
    font_data = 'https://github.com/fefanto/fontaudio/raw/master/font/fontaudio.css'
    ttfs = [[ font_abbr, 'fontaudio.ttf', 'https://github.com/fefanto/fontaudio/blob/master/font/fontaudio.ttf' ]]


class FontCI( FontKI ):               # Codicons
    font_name = 'Codicons'
    font_abbr = 'CI'
    font_data_prefix = '.codicon-'
    font_data = 'https://microsoft.github.io/vscode-codicons/dist/codicon.css'
    ttfs = [[ font_abbr, 'codicon.ttf', 'https://microsoft.github.io/vscode-codicons/dist/codicon.ttf' ]]


class FontLC( FontKI ):               # Lucide
    font_name = 'Lucide'
    font_abbr = 'LC'
    font_data_prefix = '.icon-'
    font_data = 'https://unpkg.com/lucide-static@latest/font/lucide.css'    # alt 'https://cdn.jsdelivr.net/npm/lucide-static@latest/font/lucide.css'
    ttfs = [[ font_abbr, 'lucide.ttf', 'https://unpkg.com/lucide-static@latest/font/lucide.ttf' ]]  # alt 'https://cdn.jsdelivr.net/npm/lucide-static@latest/font/lucide.ttf'


# Languages


class Language:
    language_name = '[ ERROR - Missing language name ]'
    file_name = '[ ERROR - Missing file name ]'
    intermediate = {}

    def __init__( self, intermediate ):
        self.intermediate = intermediate

    @classmethod
    def prelude( cls ):
        logging.error( 'Missing implementation of class method prelude for {!s}'.format( cls.language_name ))
        return ''

    @classmethod
    def line_icon( cls, icon ):
        logging.error( 'Missing implementation of class method line_icon for {!s}'.format( cls.language_name ))
        return ''

    @classmethod
    def epilogue( cls ):
        return ''

    @classmethod
    def convert( cls ):
        result = cls.prelude()
        for icon in cls.intermediate.get( 'icons' ):
            line_icon = cls.line_icon( icon )
            result += line_icon
        result += cls.epilogue()
        logging.info( 'Converted - {!s} for {!s}'.format( cls.intermediate.get( 'font_name' ), cls.language_name ))
        return result

    @classmethod
    def save_to_file( cls ):
        filename = cls.file_name.format( name = str( cls.intermediate.get( 'font_name' )).replace( ' ', '' ))
        converted = cls.convert()
        with open( filename, 'w' ) as f:
            f.write( converted )
            f.close()
        logging.info( 'Saved - {!s}'.format( filename ))


class LanguageC( Language ):
    language_name = 'C and C++'
    file_name = 'Icons{name}.h'

    @classmethod
    def prelude( cls ):
        tmpl_prelude = '// Generated by https://github.com/juliettef/IconFontCppHeaders script GenerateIconFontCppHeaders.py\n' + \
            '// for {lang}\n' + \
            '// from codepoints {font_data}\n' + \
            '// for use with font {ttf_files}\n\n' + \
            '#pragma once\n\n'
        ttf_files = []
        for ttf in cls.intermediate.get( 'ttfs' ):
            ttf_files.append( ttf[ 2 ])
        result = tmpl_prelude.format( lang = cls.language_name,
                                      font_data = cls.intermediate.get( 'font_data' ),
                                      ttf_files = ', '.join( ttf_files ))
        tmpl_prelude_define_file_name = '#define FONT_ICON_FILE_NAME_{font_abbr} "{file_name_ttf}"\n'
        for ttf in cls.intermediate.get( 'ttfs' ):
            result += tmpl_prelude_define_file_name.format( font_abbr = ttf[ 0 ], file_name_ttf = ttf[ 1 ])
        result += '\n'
        # min/max
        tmpl_line_minmax = '#define ICON_{minmax}_{abbr} 0x{val}\n'
        abbreviation = cls.intermediate.get( 'font_minmax_abbr' ) if cls.intermediate.get( 'font_minmax_abbr' ) else cls.intermediate.get('font_abbr')
        result += tmpl_line_minmax.format( minmax = 'MIN',
                                           abbr = abbreviation,
                                           val = cls.intermediate.get( 'font_min' )) + \
                  tmpl_line_minmax.format( minmax = 'MAX_16',
                                           abbr = abbreviation,
                                           val = cls.intermediate.get( 'font_max_16' )) + \
                  tmpl_line_minmax.format( minmax = 'MAX',
                                           abbr = abbreviation,
                                           val = cls.intermediate.get( 'font_max' )) + '\n'
        return result

    @classmethod
    def line_icon( cls, icon ):
        tmpl_line_icon = '#define ICON_{abbr}_{icon} "{code}"\t// U+{unicode}\n'
        icon_name = str.upper( icon[ 0 ]).replace( '-', '_' )
        icon_code = repr( chr( int( icon[ 1 ], 16 )).encode( 'utf-8' ))[ 2:-1 ]
        result = tmpl_line_icon.format( abbr = cls.intermediate.get( 'font_abbr' ),
                                        icon = icon_name,
                                        code = icon_code,
                                        unicode =icon[ 1 ] )
        return result

    @classmethod
    def convert_ttf_to_header( cls ):
        for ttf in cls.intermediate.get( 'ttfs' ):
            # retrieve and read ttf file
            if 'http' in ttf[ 2 ]:
                # download and read (if file is on GitHub, add '?raw=true')
                response = requests.get( ttf[ 2 ] + '?raw=true' if 'github.com' in ttf[ 2 ] else ttf[ 2 ], timeout = 2 )
                if response.status_code == 200:
                    ttf_data = response.content
                    logging.info( 'ttf file downloaded - ' + ttf[ 1 ] )
                else:
                    raise Exception( 'ttf file missing - ' + ttf[ 2 ])
            else:
                # open from disk and read
                if os.path.isfile( ttf[ 2 ] ):
                    with open( ttf[ 2 ], 'rb' ) as f:
                        ttf_data = f.read()
                        f.close()
                        logging.info( 'ttf file read - ' + ttf[ 1 ])
                else:
                    raise Exception( 'ttf file missing - ' + ttf[ 2 ])
            # convert to header and save to disk
            if ttf_data:
                # convert ttf to header
                tmpl_prelude_ttf = '// Generated by https://github.com/juliettef/IconFontCppHeaders script GenerateIconFontCppHeaders.py\n' + \
                                   '// for {lang}\n' + \
                                   '// from font {ttf_file}\n' + \
                                   '// Requires #include <stdint.h>\n\n' + \
                                   '#pragma once\n\n' + \
                                   'static const uint8_t s_{name}_ttf[{size}] = \n{{'
                result = tmpl_prelude_ttf.format( lang = cls.language_name,
                                                  ttf_file = ttf[ 2 ],
                                                  name = str( ttf[ 1 ][ :-len('.ttf') ].replace( '-', '_' ).replace( ' ', '' )),
                                                  size = str( len( ttf_data )))
                n = 0
                for byte in ttf_data:
                    if (n % 16) == 0:
                        result += '\n\t'
                    result += "0x" + str( hex( int( byte / 16 ))[ 2: ]) + str( hex( byte % 16 )[ 2: ]) + ", "
                    n += 1
                result += '\n};\n\n'
                # save to disk
                ttf_header_file_name = cls.file_name.format( name = str( cls.intermediate.get( 'font_name' )).replace( ' ', '' )) + '_' + ttf[ 1 ] + '.h'
                with open( ttf_header_file_name, 'w' ) as f:
                    f.write( result )
                    f.close()
                logging.info( 'ttf File Saved - {!s}'.format( ttf_header_file_name ))
            else:
                raise Exception( 'Failed ttf to header conversion' + ttf[ 1 ] )


class LanguageCSharp( Language ):
    language_name = "C#"
    file_name = 'Icons{name}.cs'

    @classmethod
    def prelude( cls ):
        tmpl_prelude = \
            '// <auto-generated>\n' + \
            '// Generated by https://github.com/juliettef/IconFontCppHeaders script GenerateIconFontCppHeaders.py\n' + \
            '// for {lang}\n' + \
            '// from codepoints {font_data}\n' + \
            '// for use with font {ttf_files}\n' + \
            '// </auto-generated>\n\n' + \
            'namespace IconFonts\n' + \
            '{{\n' + \
            '    public class {font_name}\n' + \
            '    {{\n'
        ttf_files = []
        for ttf in cls.intermediate.get( 'ttfs' ):
            ttf_files.append( ttf[ 2])
        result = tmpl_prelude.format( lang = cls.language_name,
                                      font_data = cls.intermediate.get( 'font_data' ),
                                      ttf_files = ', '.join( ttf_files ),
                                      font_name = cls.intermediate.get( 'font_name' ).replace( ' ', '' ))
        tmpl_prelude_define_file_name = '        public const string FontIconFileName{font_abbr} = "{file_name_ttf}";\n'
        for ttf in cls.intermediate.get( 'ttfs' ):
            result += tmpl_prelude_define_file_name.format( font_abbr = ttf[ 0 ], file_name_ttf = ttf[ 1 ])
        result += '\n'
        # min/max
        tmpl_line_minmax = '        public const int Icon{minmax} = 0x{val};\n'
        result += tmpl_line_minmax.format( minmax = 'Min',
                                           val = cls.intermediate.get( 'font_min' )) + \
                  tmpl_line_minmax.format( minmax = 'Max16',
                                           val = cls.intermediate.get( 'font_max_16' )) + \
                  tmpl_line_minmax.format( minmax = 'Max',
                                          val = cls.intermediate.get( 'font_max' )) + '\n'
        return result

    @classmethod
    def epilogue( cls ):
        return '    }\n' + \
            '}\n'

    @classmethod
    def line_icon( cls, icon ):
        tmpl_line_icon = '        public const string {icon} = {literal};\n'
        icon_name = cls.to_camelcase( icon[ 0 ])
        icon_code = icon[ 1 ]
        if icon_name[ 0 ].isdigit():
            # Variable may not start with a digit
            icon_name = 'Num' + icon_name
        if icon_name == cls.intermediate.get( 'font_name' ).replace( ' ', '' ):
            # Member may not have same name as enclosing class
            icon_name += 'Icon'

        # "\u1234"
        if len( icon_code ) <= 4:
            literal = '"\\u{code}"'.format( code = icon_code.rjust( 4, '0' ))
        # "\U12345678"
        else:
            literal = '"\\U{code}"'.format( code = icon_code.rjust( 8, '0' ))
        result = tmpl_line_icon.format( icon = icon_name, literal = literal )
        return result

    @classmethod
    def to_camelcase( cls, text ):
        parts = text.split( '-' )
        for i in range( len( parts ) ):
            p = parts[i]
            parts[ i ] = p[ 0 ].upper() + p[ 1: ].lower()
        return ''.join( parts )


class LanguagePython( Language ):
    language_name = "Python"
    file_name = 'Icons{name}.py'

    @classmethod
    def prelude( cls ):
        tmpl_prelude = '# Generated by https://github.com/juliettef/IconFontCppHeaders script GenerateIconFontCppHeaders.py\n' + \
            '# for {lang}\n' + \
            '# from codepoints {font_data}\n' + \
            '# for use with font {ttf_files}\n\n' + \
            'class Icons{font_name}:\n\n'
        ttf_files = []
        for ttf in cls.intermediate.get( 'ttfs' ):
            ttf_files.append( ttf[ 2] )
        result = tmpl_prelude.format( lang = cls.language_name,
                                      font_data = cls.intermediate.get( 'font_data' ),
                                      ttf_files = ', '.join( ttf_files ),
                                      font_name = cls.intermediate.get( 'font_name' ).replace( ' ', '' ))
        tmpl_prelude_define_file_name = "    FONT_ICON_FILE_NAME_{font_abbr} = '{file_name_ttf}'\n"
        for ttf in cls.intermediate.get( 'ttfs' ):
            result += tmpl_prelude_define_file_name.format(font_abbr = ttf[ 0 ], file_name_ttf = ttf[ 1 ])
        result += '\n'
        # min/max
        tmpl_line_minmax = '    ICON_{minmax} = 0x{val}\n'
        result += tmpl_line_minmax.format( minmax = 'MIN',
                                           val = cls.intermediate.get( 'font_min' )) + \
                  tmpl_line_minmax.format( minmax = 'MAX_16',
                                           val = cls.intermediate.get( 'font_max_16' )) + \
                  tmpl_line_minmax.format( minmax = 'MAX',
                                           val = cls.intermediate.get( 'font_max' )) + '\n'
        return result

    @classmethod
    def line_icon( cls, icon ):
        tmpl_line_icon = "    ICON_{icon} = '\\u{code}'\n"
        icon_name = str.upper( icon[ 0 ]).replace( '-', '_' )
        icon_code = icon[ 1 ]
        result = tmpl_line_icon.format( icon = icon_name, code = icon_code )
        return result


class LanguageRust( Language ):
    language_name = "Rust"
    file_name = 'Icons{name}.rs'

    @classmethod
    def prelude( cls ):
        tmpl_prelude = '//! Generated by https://github.com/juliettef/IconFontCppHeaders script GenerateIconFontCppHeaders.py\n' + \
            '//! for {lang}\n' + \
            '//! from codepoints {font_data}\n' + \
            '//! for use with font {ttf_files}\n\n'
        ttf_files = []
        for ttf in cls.intermediate.get( 'ttfs' ):
            ttf_files.append( ttf[ 2] )
        result = tmpl_prelude.format( lang = cls.language_name,
                                      font_data = cls.intermediate.get( 'font_data' ),
                                      ttf_files = ', '.join( ttf_files ),
                                      font_name = cls.intermediate.get( 'font_name' ).replace( ' ', '' ))
        tmpl_prelude_define_file_name = "pub const FONT_ICON_FILE_NAME_{font_abbr}: &str = \"{file_name_ttf}\";\n"
        for ttf in cls.intermediate.get( 'ttfs' ):
            result += tmpl_prelude_define_file_name.format(font_abbr = ttf[ 0 ], file_name_ttf = ttf[ 1 ])
        result += '\n'
        # min/max
        tmpl_line_minmax = "pub const ICON_{minmax}: char = '\\u{{{val}}}';\n"
        result += tmpl_line_minmax.format( minmax = 'MIN',
                                           val = cls.intermediate.get( 'font_min' )) + \
                  tmpl_line_minmax.format( minmax = 'MAX_16',
                                           val = cls.intermediate.get( 'font_max_16' )) + \
                  tmpl_line_minmax.format( minmax = 'MAX',
                                           val = cls.intermediate.get( 'font_max' )) + '\n'
        return result

    @classmethod
    def line_icon( cls, icon ):
        tmpl_line_icon = "pub const ICON_{icon}: char = '\\u{{{code}}}';\n"
        icon_name = str.upper( icon[ 0 ]).replace( '-', '_' )
        icon_code = icon[ 1 ]
        result = tmpl_line_icon.format( icon = icon_name, code = icon_code )
        return result


class LanguageGo( Language ):
    language_name = 'Go'
    file_name = 'Icons{name}.go'

    @classmethod
    def prelude( cls ):
        tmpl_prelude = '// Generated by https://github.com/juliettef/IconFontCppHeaders script GenerateIconFontCppHeaders.py\n' + \
            '// for {lang}\n' + \
            '// from codepoints {font_data}\n' + \
            '// for use with font {ttf_files}\n\n' + \
            'package IconFontCppHeaders\n\n'
        ttf_files = []
        for ttf in cls.intermediate.get( 'ttfs' ):
            ttf_files.append( ttf[ 2 ])
        result = tmpl_prelude.format( lang = cls.language_name,
                                      font_data = cls.intermediate.get( 'font_data' ),
                                      ttf_files = ', '.join( ttf_files ),
                                      package_name = str( cls.intermediate.get( 'font_name' )).replace( ' ', '' ) )
        result += 'var Icons{name} = Font'.format( name = str( cls.intermediate.get( 'font_name' )).replace( ' ', '' ) )
        result += '{\n'
        result += '\tFilenames: [][2]string{\n'
        for ttf in cls.intermediate.get( 'ttfs' ): 
            entry = '"{font_abbr}", "{file_name_ttf}"'
            result += '\t\t{' + entry.format( font_abbr = ttf[ 0 ], file_name_ttf = ttf[ 1 ]) + '},\n'
        result += '\t},\n'
        # min/max
        tmpl_line_minmax = '\t{minmax}: 0x{val},\n'
        abbreviation = cls.intermediate.get( 'font_minmax_abbr' ) if cls.intermediate.get( 'font_minmax_abbr' ) else cls.intermediate.get('font_abbr')
        result += tmpl_line_minmax.format( minmax = 'Min',
                                          abbr = abbreviation,
                                          val = cls.intermediate.get( 'font_min' )) + \
                 tmpl_line_minmax.format( minmax = 'Max16',
                                          abbr = abbreviation,
                                          val = cls.intermediate.get( 'font_max_16' )) + \
                 tmpl_line_minmax.format( minmax = 'Max',
                                          abbr = abbreviation,
                                          val = cls.intermediate.get( 'font_max' ))

        result += '\tIcons: map[string]string{\n'
        return result

    @classmethod
    def line_icon( cls, icon ):
        icon_name = cls.to_camelcase( icon[ 0 ])
        tmpl_line_icon = '\t\t"{icon}":\t"{code}", \t// U+{unicode}\n'
        icon_code = repr( chr( int( icon[ 1 ], 16 )).encode( 'utf-8' ))[ 2:-1 ]
        result = tmpl_line_icon.format( abbr = cls.intermediate.get( 'font_abbr' ),
                                        icon = icon_name,
                                        code = icon_code,
                                        unicode =icon[ 1 ])
        return result

    @classmethod
    def epilogue( cls ):
        return '\t},\n}\n'

    @classmethod
    def to_camelcase( cls, text ):
        parts = text.split( '-' )
        for i in range( len( parts )):
            p = parts[i]
            parts[ i ] = p[ 0 ].upper() + p[ 1: ].lower()
        return ''.join( parts )


# Main


fonts = [ FontFA4, FontFA5, FontFA5Brands, FontFA5Pro, FontFA5ProBrands, FontFA6, FontFA6Brands, FontFK, FontMD, FontMS, FontMDI, FontKI, FontFAD, FontCI, FontLC ]
languages = [ LanguageC, LanguageCSharp, LanguagePython, LanguageRust, LanguageGo ]
ttf2headerC = False # convert ttf files to C and C++ headers

logging.basicConfig( format='%(levelname)s : %(message)s', level = logging.WARNING )

intermediates = []
for font in fonts:
    try:
        font_intermediate = font.get_intermediate_representation()
        if font_intermediate:
            intermediates.append( font_intermediate )
    except Exception as e:
        logging.error( e )
if intermediates:
    for interm in intermediates:
        Language.intermediate = interm
        for lang in languages:
            if lang:
                lang.save_to_file()
                if ttf2headerC and lang == LanguageC:
                    try:
                        lang.convert_ttf_to_header()
                    except Exception as e:
                        logging.error( e )
