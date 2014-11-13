import urllib
import json
import time

replace = [".avi", "1.4", "5.1", "Dual-Audio", "Hindi-English", "[DDR]", "DvDrip-LW", "DVDRip", "BRRip", "XviD-Sam", "XviD", "1CDRip", "aXXo", "[", "]", "(", ")", "{", "}",
           "{{", "}}", "Blu-Ray", "anoxmous", "SilverRG", "SaMple-"
           "x264", "720p", "StyLishSaLH (StyLish Release)", "Free", "DvDScr", "MP3", "HDRip", "WebRip", "NLT-Release",
           "ETRG", "YIFY", "StyLishSaLH", "StyLish Release", "TrippleAudio", "EngHindiIndonesian",
           "385MB", "CooL GuY", "a2zRG", "x264", "Hindi", "AAC", "AC3", "MP3", " R6", "HDRip", "H264", "ESub", "AQOS",
           "ALLiANCE", "UNRATED", "ExtraTorrentRG", "BrRip", "mkv", "mpg", "DiAMOND", "UsaBitcom", "AMIABLE", "WEB-DL",
           "BRRIP", "XVID", "AbSurdiTy", "DVDRiP", "TASTE", "BluRay", "HR", "COCAIN", "_", ".", "BestDivX", "MAXSPEED",
           "Eng", "500MB", "FXG", "Ac3", "Feel", "Subs", "S4A", "BDRip", "FTW", "Xvid", "Noir", "1337x", "ReVoTT",
           "GlowGaze", "mp4", "Unrated", "hdrip", "ARCHiViST", "TheWretched", "www", "torrentfive", "com",
           "1080p", "1080", "SecretMyth", "Kingdom", "Release", "RISES", "DvDrip", "ViP3R", "RISES", "BiDA", "READNFO",
           "HELLRAZ0R", "tots", "BeStDivX", "UsaBit", "FASM", "NeroZ", "576p", "LiMiTED", "Series", "ExtraTorrent",
           "DVDRIP", "~",
           "BRRiP", "699MB", "700MB", "greenbud", "B89", "480p", "AMX", "007", "DVDrip", "h264", "phrax", "TODE",
           "LiNE",
           "XVid", "sC0rp", "PTpower", "OSCARS", "DXVA", "MXMG", "3LT0N", "TiTAN", "4PlayHD", "HQ", "HDRiP", "MoH",
           "MP4", "BadMeetsEvil",
           "XViD", "3Li", "PTpOWeR", "3D", "HSBS", "RiPS", "WEBRip", "R5", "PSiG", "'GokU61", "GB", "GokU61",
           "NL", "Rel", "NL",
           "PSEUDO", "DVD", "Rip", "NeRoZ", "EXTENDED", "DVDScr", "xvid", "WarrLord", "SCREAM", "MERRY", "XMAS", "iMB",
           "7o9",
           "Exclusive", "171", "DiDee", "v2", "Hon3y", "DvD", "Nydic", "RARBG", "Mafiaking", "DVDR", "SHUMANOV", "-", "!"

]

retry = ["ahl07Sample.mp4", "moviesnhacks", "mastitorrents", "cd2Push", "bokutox", "fasamoo", "lkrg", "cam", "imagine", "CharmeLeon", "sub", "dual", "audio", "+", "by", "team", "exd", "lish", "uncut", "harshad", "mastitorrents", "rmvb", "mpeg", "classified", "br", "cd1", "cd2", "cd3", "files", "m4v", "ddr", "kamera", "ahl07", "hin+", "ashish7", "vyto", "current", "hd", "jap", "bugz", "E-Sub_xRG", "pre", "CC", "ENG", "chamee",
]

def finder(name, delay=2):
    origname = name
    print "MovieLookUp", name
    year = 0
    name = name.lower()
    for y in range(1900, 2015):
        if str(y) in name:
            name = name.replace(str(y), " ")
            year = y
            break
    for value in replace:
        name = name.replace(value.lower(), " ")

    name = name.replace("&", "and")

    name = name.lstrip()
    name = name.rstrip()
    print name
    if year != 0:
        url = "http://www.omdbapi.com/?t=" + name + "&y=" + str(year)
        print url
        try:
            response = urllib.urlopen(url).read()
            jsonvalues = json.loads(response)
        except:
            if delay < 10:
                time.sleep(delay)
                return finder(name, delay+1)
            jsonvalues = "{\"Response\": \"False\", \"Error\":\"Network Error\"}"
            return jsonvalues
        if jsonvalues["Response"] == "False":
            for val in retry:
                if val.lower() in origname.lower():
                    name = name.replace(val.lower(), " ")
                    return finder(name)
        print "returning"
        return response
    else:
        url = "http://www.omdbapi.com/?t=" + name
        print url
        try:
            response = urllib.urlopen(url).read()
            jsonvalues = json.loads(response)
        except:
            if delay < 10:
                time.sleep(delay)
                return finder(name, delay+1)
            jsonvalues = "{\"Response\": \"False\", \"Error\":\"Network Error\"}"
            return jsonvalues
        if jsonvalues["Response"] == "False":
            for val in retry:
                if val.lower() in origname.lower():
                    name = name.replace(val.lower(), " ")
                    return finder(name)
        print "returning"
        return response