from enum import Enum


class Console(Enum):
    three_do = "3DO"
    amiga_cd_thirty_two = "Amiga CD32"
    atari_two_six_zero_zero = "Atari 2600"
    atari_five_two_zero_zero = "Atari 5200"
    atari_seven_eight_zero_zero = "Atari 7800"
    atari_jaguar = "Atari Jaguar"
    atari_xe = "Atari XE"
    colecovision = "Colecovision"
    dreamcast = "Dreamcast"
    famicom_disk_system = "Famicom Disk System"
    gamecube = "GameCube"
    genesis = "Genesis"
    intellivision = "Intellivision"
    jaguar_cd = "Jaguar CD"
    neo_geo_cd = "Neo Geo CD"
    nes = "NES"
    nintendo_sixty_four = "Nintendo 64"
    nintendo_switch = "Nintendo Switch"
    nintendo_wii = "Nintendo Wii"
    nintendo_wii_u = "Nintendo Wii U"
    odyssey_two = "Odyssey 2"
    pc_fx = "PC-FX"
    philips_cdi = "Philips CDI"
    playstation_one = "Playstation 1"
    playstation_two = "Playstation 2"
    playstation_three = "Playstation 3"
    playstation_four = "Playstation 4"
    playstation_five = "Playstation 5"
    sega_thirty_two_x = "Sega 32X"
    sega_cd = "Sega CD"
    sega_master_system = "Sega Master System"
    sega_saturn = "Sega Saturn"
    super_nintendo = "Super Nintendo"
    turbografx_sixteen = "TurboGrafx 16"
    xbox = "Xbox"
    xbox_three_six_zero = "Xbox 360"
    xbox_one = "Xbox One"
    xbox_series_x = "Xbox Series X"


class Handheld(Enum):
    three_ds = "3DS"
    atari_lynx = "Atari Lynx"
    game_gear = "Game Gear"
    gameboy = "Gameboy"
    gameboy_advance = "Gameboy Advance"
    gameboy_advance_video = "Gameboy Advance Video"
    gameboy_color = "Gameboy Color"
    neo_geo_pocket = "Neo Geo Pocket"
    neo_geo_pocket_color = "Neo Geo Pocket Color"
    nintendo_ds = "Nintendo DS"
    playstation_portable = "Playstation Portable"
    playstation_portable_video = "Playstation Portable Video"
    playstation_vita = "Playstation Vita"
    virtual_boy = "Virtual Boy"
    wonderswan = "Wonderswan"
    wonderswan_color = "Wonderswan Color"


class Computer(Enum):
    amiga = "Amiga"
    linux = "Linux"
    mac = "Mac"
    ms_dos = "MS-DOS"
    windows = "Windows"


class PageCategory(Enum):
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    E = "e"
    F = "f"
    G = "g"
    H = "h"
    I = "i"
    J = "j"
    K = "k"
    L = "l"
    M = "m"
    N = "n"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    S = "s"
    T = "t"
    U = "u"
    V = "v"
    W = "w"
    X = "x"
    Y = "y"
    Z = "z"
    NUM = "9"


class Region(Enum):
    us = "United States"
    eu = "Europe"
    jp = "Japan"


Platform = Console | Handheld | Computer
