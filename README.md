# IconFontCHeaders
C++ 11 headers for icon fonts

A set of header files for using icon fonts in C++, along with the python generator used to create the files.

Each header contains defines for one font, with each icon code point defined as ICON_*, along with the min and max code points for font loading purposes (for example ICON_MIN_FA and ICON_MAX_FA).

## Usage

Using [ImGui](https://github.com/ocornut/imgui) as an example UI library:

    #include "IconsFontAwesome.h"
    
    ImGuiIO& io = ImGui::GetIO();
     io.Fonts->AddFontDefault();
     
     // merge in icons from Font Awesome
    static const ImWchar icons_ranges[] = { ICON_MIN_FA, ICON_MAX_FA, 0 };
    ImFontConfig icons_config; icons_config.MergeMode = true; icons_config.PixelSnapH = true;
    io.Fonts->AddFontFromFileTTF( fontFile.c_str(), 16.0f, &icons_config, icons_ranges);
    
    // in an imgui window somewhere...
    ImGui::Text( ICON_FA_FILE "  File" ); // use string literal concatenation, ouputs a file icon and File as a string.
