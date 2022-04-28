import os
from os import path
import pathlib
import shutil
import time

target_folder = "/home/bali/Downloads/"
is_image = ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.psd', '.webp', '.svg', '.raw', '.arw', '.cr2', '.nrw', '.k25', '.svgz', '.ai', '.eps', '.xcf']
is_video = video_file_extensions = [
    '.264', '.3g2', '.3gp', '.3gp2', '.3gpp', '.3gpp2', '.3mm', '.3p2', '.60d', '.787', '.89', '.aaf', '.aec', '.aep', '.aepx',
    '.aet', '.aetx', '.ajp', '.ale', '.am', '.amc', '.amv', '.amx', '.anim', '.aqt', '.arcut', '.arf', '.asf', '.asx', '.avb',
    '.avc', '.avd', '.avi', '.avp', '.avs', '.avs', '.avv', '.axm', '.bdm', '.bdmv', '.bdt2', '.bdt3', '.bik', '.bin', '.bix',
    '.bmk', '.bnp', '.box', '.bs4', '.bsf', '.bvr', '.byu', '.camproj', '.camrec', '.camv', '.ced', '.cel', '.cine', '.cip',
    '.clpi', '.cmmp', '.cmmtpl', '.cmproj', '.cmrec', '.cpi', '.cst', '.cvc', '.cx3', '.d2v', '.d3v', '.dat', '.dav', '.dce',
    '.dck', '.dcr', '.dcr', '.ddat', '.dif', '.dir', '.divx', '.dlx', '.dmb', '.dmsd', '.dmsd3d', '.dmsm', '.dmsm3d', '.dmss',
    '.dmx', '.dnc', '.dpa', '.dpg', '.dream', '.dsy', '.dv', '.dv-avi', '.dv4', '.dvdmedia', '.dvr', '.dvr-ms', '.dvx', '.dxr',
    '.dzm', '.dzp', '.dzt', '.edl', '.evo', '.eye', '.ezt', '.f4p', '.f4v', '.fbr', '.fbr', '.fbz', '.fcp', '.fcproject',
    '.ffd', '.flc', '.flh', '.fli', '.flv', '.flx', '.gfp', '.gl', '.gom', '.grasp', '.gts', '.gvi', '.gvp', '.h264', '.hdmov',
    '.hkm', '.ifo', '.imovieproj', '.imovieproject', '.ircp', '.irf', '.ism', '.ismc', '.ismv', '.iva', '.ivf', '.ivr', '.ivs',
    '.izz', '.izzy', '.jss', '.jts', '.jtv', '.k3g', '.kmv', '.ktn', '.lrec', '.lsf', '.lsx', '.m15', '.m1pg', '.m1v', '.m21',
    '.m21', '.m2a', '.m2p', '.m2t', '.m2ts', '.m2v', '.m4e', '.m4u', '.m4v', '.m75', '.mani', '.meta', '.mgv', '.mj2', '.mjp',
    '.mjpg', '.mk3d', '.mkv', '.mmv', '.mnv', '.mob', '.mod', '.modd', '.moff', '.moi', '.moov', '.mov', '.movie', '.mp21',
    '.mp21', '.mp2v', '.mp4', '.mp4v', '.mpe', '.mpeg', '.mpeg1', '.mpeg4', '.mpf', '.mpg', '.mpg2', '.mpgindex', '.mpl',
    '.mpl', '.mpls', '.mpsub', '.mpv', '.mpv2', '.mqv', '.msdvd', '.mse', '.msh', '.mswmm', '.mts', '.mtv', '.mvb', '.mvc',
    '.mvd', '.mve', '.mvex', '.mvp', '.mvp', '.mvy', '.mxf', '.mxv', '.mys', '.ncor', '.nsv', '.nut', '.nuv', '.nvc', '.ogm',
    '.ogv', '.ogx', '.osp', '.otrkey', '.pac', '.par', '.pds', '.pgi', '.photoshow', '.piv', '.pjs', '.playlist', '.plproj',
    '.pmf', '.pmv', '.pns', '.ppj', '.prel', '.pro', '.prproj', '.prtl', '.psb', '.psh', '.pssd', '.pva', '.pvr', '.pxv',
    '.qt', '.qtch', '.qtindex', '.qtl', '.qtm', '.qtz', '.r3d', '.rcd', '.rcproject', '.rdb', '.rec', '.rm', '.rmd', '.rmd',
    '.rmp', '.rms', '.rmv', '.rmvb', '.roq', '.rp', '.rsx', '.rts', '.rts', '.rum', '.rv', '.rvid', '.rvl', '.sbk', '.sbt',
    '.scc', '.scm', '.scm', '.scn', '.screenflow', '.sec', '.sedprj', '.seq', '.sfd', '.sfvidcap', '.siv', '.smi', '.smi',
    '.smil', '.smk', '.sml', '.smv', '.spl', '.sqz', '.srt', '.ssf', '.ssm', '.stl', '.str', '.stx', '.svi', '.swf', '.swi',
    '.swt', '.tda3mt', '.tdx', '.thp', '.tivo', '.tix', '.tod', '.tp', '.tp0', '.tpd', '.tpr', '.trp', '.ts', '.tsp', '.ttxt',
    '.tvs', '.usf', '.usm', '.vc1', '.vcpf', '.vcr', '.vcv', '.vdo', '.vdr', '.vdx', '.veg','.vem', '.vep', '.vf', '.vft',
    '.vfw', '.vfz', '.vgz', '.vid', '.video', '.viewlet', '.viv', '.vivo', '.vlab', '.vob', '.vp3', '.vp6', '.vp7', '.vpj',
    '.vro', '.vs4', '.vse', '.vsp', '.w32', '.wcp', '.webm', '.wlmp', '.wm', '.wmd', '.wmmp', '.wmv', '.wmx', '.wot', '.wp3',
    '.wpl', '.wtv', '.wve', '.wvx', '.xej', '.xel', '.xesc', '.xfl', '.xlmv', '.xmv', '.xvid', '.y4m', '.yog', '.yuv', '.zeg',
    '.zm1', '.zm2', '.zm3', '.zmv'
]
is_document = ['.pdf', '.doc', '.docx', '.odt', '.xls', '.xlsx', '.ods', '.ppt', '.pptx', '.txt']
is_program = ['.html', '.htm', '.php', '.py', '.sh', '.sql', '.rpm', '.deb', '.appimage', '.dart', '.css', '.js', '.jsx', '.env', '.json', '.md', '.htaccess', '.log', '.conf', '.xml', '.yml', '.key']
is_compressed = ['.tar', '.gz', '.zip', '.rar', '.xz', '.7zip']
is_font = ['.jfproj', '.ttf', '.pfa', '.woff', '.fnt', '.otf', '.woff2', '.odttf']

def move_file(destination_path, file_name, file_ext, file_name_plain):
    if not path.exists(destination_path):
        os.mkdir(destination_path)
    for files in os.listdir(destination_path):
        file_path = os.path.join(target_folder, files)
        if os.path.exists(destination_path+file_name):
            file_name_new = file_name_plain+"copy("+ str(round(time.time())) +")"+file_ext 
    else:
        file_name_new = file_name 
    
    if(os.path.exists(target_folder+file_name)):
        shutil.move(target_folder+file_name, destination_path+file_name_new)

for files in os.listdir(target_folder):
    file_path = os.path.join(target_folder, files)
    if os.path.isfile(file_path):
        file_extension = pathlib.Path(file_path).suffix
        file_name_plain = pathlib.Path(file_path).stem
        if file_extension.lower() in is_image:
            move_file(target_folder + "Images/", files, file_extension, file_name_plain)
        if file_extension.lower() in is_video:
            move_file(target_folder + "Videos/", files, file_extension, file_name_plain)
        if file_extension.lower() in is_document:
            move_file(target_folder + "Documents/", files, file_extension, file_name_plain)
        if file_extension.lower() in is_program:
            move_file(target_folder + "Programs/", files, file_extension, file_name_plain)
        if file_extension.lower() in is_compressed:
            move_file(target_folder + "Compressed/", files, file_extension, file_name_plain)
        if file_extension.lower() in is_font:
            move_file(target_folder + "Fonts/", files, file_extension, file_name_plain)
        else :
            move_file(target_folder + "Miscs/", files, file_extension, file_name_plain)
