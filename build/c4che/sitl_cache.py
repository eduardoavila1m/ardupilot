AP_LIBRARIES = ['AP_HAL_SITL', 'SITL', 'AP_Scripting', 'AP_Scripting/lua/src']
AP_LIBRARIES_OBJECTS_KW = {}
AR = ['/usr/bin/ar']
ARFLAGS = ['rcs']
BINDIR = '/usr/bin'
BOARD = 'sitl'
BOOTLOADER = False
BUILD_SUMMARY_HEADER = ['target', 'size_text', 'size_data', 'size_bss', 'size_total']
CC = ['/usr/bin/gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('9', '3', '0')
CFLAGS = ['-ffunction-sections', '-fdata-sections', '-fsigned-char', '-Wall', '-Wextra', '-Wformat', '-Wpointer-arith', '-Wcast-align', '-Wundef', '-Wno-missing-field-initializers', '-Wno-unused-parameter', '-Wno-redundant-decls', '-Wno-unknown-pragmas', '-Wno-trigraphs', '-Wno-format-contains-nul', '-Werror=shadow', '-Werror=return-type', '-Werror=unused-result', '-Werror=unused-variable', '-Werror=narrowing', '-Werror=attributes', '-Werror=overflow', '-Werror=parentheses', '-Werror=format-extra-args', '-Werror=ignored-qualifiers', '-MMD']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
COMPILER_CC = 'gcc'
COMPILER_CXX = 'g++'
CONFIGURE_FILES = ['/home/eduardo/anaconda3/lib/python3.7/importlib/_bootstrap.py', '/home/eduardo/anaconda3/lib/python3.7/importlib/_bootstrap_external.py', '/home/eduardo/anaconda3/lib/python3.7/encodings/__init__.py', '/home/eduardo/anaconda3/lib/python3.7/codecs.py', '/home/eduardo/anaconda3/lib/python3.7/encodings/aliases.py', '/home/eduardo/anaconda3/lib/python3.7/encodings/utf_8.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waf-light', '/home/eduardo/anaconda3/lib/python3.7/encodings/latin_1.py', '/home/eduardo/anaconda3/lib/python3.7/io.py', '/home/eduardo/anaconda3/lib/python3.7/abc.py', '/home/eduardo/anaconda3/lib/python3.7/site.py', '/home/eduardo/anaconda3/lib/python3.7/os.py', '/home/eduardo/anaconda3/lib/python3.7/stat.py', '/home/eduardo/anaconda3/lib/python3.7/posixpath.py', '/home/eduardo/anaconda3/lib/python3.7/genericpath.py', '/home/eduardo/anaconda3/lib/python3.7/_collections_abc.py', '/home/eduardo/anaconda3/lib/python3.7/_sitebuiltins.py', '/home/eduardo/anaconda3/lib/python3.7/_bootlocale.py', '/home/eduardo/anaconda3/lib/python3.7/types.py', '/home/eduardo/anaconda3/lib/python3.7/importlib/__init__.py', '/home/eduardo/anaconda3/lib/python3.7/warnings.py', '/home/eduardo/anaconda3/lib/python3.7/importlib/util.py', '/home/eduardo/anaconda3/lib/python3.7/importlib/abc.py', '/home/eduardo/anaconda3/lib/python3.7/importlib/machinery.py', '/home/eduardo/anaconda3/lib/python3.7/contextlib.py', '/home/eduardo/anaconda3/lib/python3.7/collections/__init__.py', '/home/eduardo/anaconda3/lib/python3.7/operator.py', '/home/eduardo/anaconda3/lib/python3.7/keyword.py', '/home/eduardo/anaconda3/lib/python3.7/heapq.py', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/_heapq.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/reprlib.py', '/home/eduardo/anaconda3/lib/python3.7/functools.py', '/home/eduardo/anaconda3/lib/python3.7/site-packages/sphinxcontrib/__init__.py', '/home/eduardo/anaconda3/lib/python3.7/inspect.py', '/home/eduardo/anaconda3/lib/python3.7/dis.py', '/home/eduardo/anaconda3/lib/python3.7/opcode.py', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/_opcode.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/collections/abc.py', '/home/eduardo/anaconda3/lib/python3.7/enum.py', '/home/eduardo/anaconda3/lib/python3.7/linecache.py', '/home/eduardo/anaconda3/lib/python3.7/tokenize.py', '/home/eduardo/anaconda3/lib/python3.7/re.py', '/home/eduardo/anaconda3/lib/python3.7/sre_compile.py', '/home/eduardo/anaconda3/lib/python3.7/sre_parse.py', '/home/eduardo/anaconda3/lib/python3.7/sre_constants.py', '/home/eduardo/anaconda3/lib/python3.7/copyreg.py', '/home/eduardo/anaconda3/lib/python3.7/token.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/__init__.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Scripting.py', '/home/eduardo/anaconda3/lib/python3.7/__future__.py', '/home/eduardo/anaconda3/lib/python3.7/shlex.py', '/home/eduardo/anaconda3/lib/python3.7/shutil.py', '/home/eduardo/anaconda3/lib/python3.7/fnmatch.py', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/zlib.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/bz2.py', '/home/eduardo/anaconda3/lib/python3.7/_compression.py', '/home/eduardo/anaconda3/lib/python3.7/threading.py', '/home/eduardo/anaconda3/lib/python3.7/traceback.py', '/home/eduardo/anaconda3/lib/python3.7/_weakrefset.py', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/_bz2.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/lzma.py', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/_lzma.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/grp.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Utils.py', '/home/eduardo/anaconda3/lib/python3.7/datetime.py', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/math.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/_datetime.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/platform.py', '/home/eduardo/anaconda3/lib/python3.7/subprocess.py', '/home/eduardo/anaconda3/lib/python3.7/signal.py', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/_posixsubprocess.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/select.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/selectors.py', '/home/eduardo/anaconda3/lib/python3.7/base64.py', '/home/eduardo/anaconda3/lib/python3.7/struct.py', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/_struct.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/binascii.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/pickle.py', '/home/eduardo/anaconda3/lib/python3.7/_compat_pickle.py', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/_pickle.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Errors.py', '/home/eduardo/anaconda3/lib/python3.7/hashlib.py', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/_hashlib.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/_blake2.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/_sha3.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/encodings/hex_codec.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Configure.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/ConfigSet.py', '/home/eduardo/anaconda3/lib/python3.7/copy.py', '/home/eduardo/anaconda3/lib/python3.7/weakref.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Logs.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/ansiterm.py', '/home/eduardo/anaconda3/lib/python3.7/ctypes/__init__.py', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/_ctypes.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/ctypes/_endian.py', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/fcntl.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/termios.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/logging/__init__.py', '/home/eduardo/anaconda3/lib/python3.7/string.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Options.py', '/home/eduardo/anaconda3/lib/python3.7/tempfile.py', '/home/eduardo/anaconda3/lib/python3.7/random.py', '/home/eduardo/anaconda3/lib/python3.7/bisect.py', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/_bisect.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/_random.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/optparse.py', '/home/eduardo/anaconda3/lib/python3.7/textwrap.py', '/home/eduardo/anaconda3/lib/python3.7/gettext.py', '/home/eduardo/anaconda3/lib/python3.7/locale.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Context.py', '/home/eduardo/anaconda3/lib/python3.7/imp.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Node.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Build.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Runner.py', '/home/eduardo/anaconda3/lib/python3.7/queue.py', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/_queue.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Task.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/TaskGen.py', 'Tools/ardupilotwaf/ardupilotwaf.py', 'Tools/ardupilotwaf/ap_persistent.py', 'Tools/ardupilotwaf/boards.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/__init__.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/compiler_cxx.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/ccroot.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/c_aliases.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/c_preproc.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/c_config.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/c_osx.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/c_tests.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/gxx.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/ar.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/clangxx.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/icpc.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/compiler_c.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/extras/__init__.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/extras/c_bgxlc.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/xlc.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/extras/c_emscripten.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/gcc.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/extras/c_nec.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/clang.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/icc.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/waf_unit_test.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/python.py', 'Tools/ardupilotwaf/build_summary.py', 'Tools/ardupilotwaf/ap_library.py', 'Tools/ardupilotwaf/toolchain.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/cxx.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/Tools/c.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/extras/gccdeps.py', 'Tools/ardupilotwaf/cxx_checks.py', '/home/eduardo/ROS_Projects/apm/ardupilot/modules/waf/waflib/extras/clang_compilation_database.py', '/home/eduardo/anaconda3/lib/python3.7/json/__init__.py', '/home/eduardo/anaconda3/lib/python3.7/json/decoder.py', '/home/eduardo/anaconda3/lib/python3.7/json/scanner.py', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/_json.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/json/encoder.py', '/home/eduardo/anaconda3/lib/python3.7/pipes.py', 'Tools/ardupilotwaf/mavgen.py', '/home/eduardo/anaconda3/lib/python3.7/xml/__init__.py', '/home/eduardo/anaconda3/lib/python3.7/xml/etree/__init__.py', '/home/eduardo/anaconda3/lib/python3.7/xml/etree/ElementTree.py', '/home/eduardo/anaconda3/lib/python3.7/xml/etree/ElementPath.py', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/pyexpat.cpython-37m-x86_64-linux-gnu.so', '/home/eduardo/anaconda3/lib/python3.7/lib-dynload/_elementtree.cpython-37m-x86_64-linux-gnu.so', 'Tools/ardupilotwaf/uavcangen.py', 'Tools/ardupilotwaf/git_submodule.py', 'Tools/ardupilotwaf/gtest.py', 'Tools/ardupilotwaf/static_linking.py', '/home/eduardo/ROS_Projects/apm/ardupilot/wscript']
CONFIGURE_HASH = b'\x80J\xcd\x9f\xb1O\x1f\xf7z-7%\xd2\x02G)'
CPPPATH_ST = '-I%s'
CXX = ['/usr/bin/g++']
CXXFLAGS = ['-std=gnu++11', '-fdata-sections', '-ffunction-sections', '-fno-exceptions', '-fsigned-char', '-Wall', '-Wextra', '-Wformat', '-Wpointer-arith', '-Wcast-align', '-Wundef', '-Wno-unused-parameter', '-Wno-missing-field-initializers', '-Wno-reorder', '-Wno-redundant-decls', '-Wno-unknown-pragmas', '-Wno-expansion-to-defined', '-Wno-format-contains-nul', '-Werror=attributes', '-Werror=format-security', '-Werror=format-extra-args', '-Werror=enum-compare', '-Werror=array-bounds', '-Werror=uninitialized', '-Werror=init-self', '-Werror=narrowing', '-Werror=return-type', '-Werror=switch', '-Werror=sign-compare', '-Werror=type-limits', '-Werror=unused-result', '-Werror=shadow', '-Werror=unused-variable', '-Werror=delete-non-virtual-dtor', '-Wfatal-errors', '-Wno-trigraphs', '-Werror=parentheses', '-Werror=unused-but-set-variable', '-Werror=suggest-override', '-Werror=float-equal', '-O3', '-DHAL_HAVE_AP_ROMFS_EMBEDDED_H', '-MMD']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_cxxshlib = ['-fPIC']
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o']
CXX_NAME = 'gcc'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DEBUG = False
DEFINES = ['SKETCHBOOK="/home/eduardo/ROS_Projects/apm/ardupilot"', 'AP_SCRIPTING_CHECKS=1', 'CONFIG_HAL_BOARD=HAL_BOARD_SITL', 'CONFIG_HAL_BOARD_SUBTYPE=HAL_BOARD_SUBTYPE_NONE', 'ENABLE_HEAP=1', 'ENABLE_SCRIPTING=1', 'LUA_32BITS=1']
DEFINES_ST = '-D%s'
DEFINE_COMMENTS = {'WAF_BUILD': '', '__STDC_FORMAT_MACROS': '', 'HAVE_FEENABLEEXCEPT': '', 'HAVE_CMATH_ISFINITE': '', 'HAVE_CMATH_ISINF': '', 'HAVE_CMATH_ISNAN': '', 'NEED_CMATH_ISFINITE_STD_NAMESPACE': '', 'NEED_CMATH_ISINF_STD_NAMESPACE': '', 'NEED_CMATH_ISNAN_STD_NAMESPACE': '', 'HAVE_ENDIAN_H': '', 'HAVE_BYTESWAP_H': '', 'HAVE_MEMRCHR': '', 'PYTHONDIR': '', 'PYTHONARCHDIR': '', '_GNU_SOURCE': ''}
DEST_BINFMT = 'elf'
DEST_CPU = 'x86_64'
DEST_OS = 'linux'
DSDL_COMPILER = '/home/eduardo/ROS_Projects/apm/ardupilot/modules/uavcan/libuavcan/dsdl_compiler/libuavcan_dsdlc'
DSDL_COMPILER_DIR = '/home/eduardo/ROS_Projects/apm/ardupilot/modules/uavcan/libuavcan/dsdl_compiler'
ENABLE_ASSERTS = False
ENABLE_GCCDEPS = ['c', 'cxx']
ENABLE_HEADER_CHECKS = False
GIT = ['/usr/bin/git']
GIT_SUBMODULES = ['gtest', 'mavlink']
HAS_GTEST = True
HAVE_BYTESWAP_H = 1
HAVE_CMATH_ISFINITE = 1
HAVE_CMATH_ISINF = 1
HAVE_CMATH_ISNAN = 1
HAVE_ENDIAN_H = 1
HAVE_FEENABLEEXCEPT = 1
HAVE_MEMRCHR = 1
INCLUDES = ['/home/eduardo/ROS_Projects/apm/ardupilot/libraries/', '/home/eduardo/ROS_Projects/apm/ardupilot/libraries/AP_Common/missing']
LIB = ['m']
LIBDIR = '/usr/lib'
LIBPATH_ST = '-L%s'
LIB_ST = '-l%s'
LINKFLAGS = ['-Wl,--gc-sections', '-pthread']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINKFLAGS_cxxshlib = ['-shared']
LINKFLAGS_cxxstlib = ['-Wl,-Bstatic']
LINK_CC = ['/usr/bin/gcc']
LINK_CXX = ['/usr/bin/g++']
MAVLINK_DIR = '/home/eduardo/ROS_Projects/apm/ardupilot/modules/mavlink'
NEED_CMATH_ISFINITE_STD_NAMESPACE = 1
NEED_CMATH_ISINF_STD_NAMESPACE = 1
NEED_CMATH_ISNAN_STD_NAMESPACE = 1
OPTIONS = {'colors': 'auto', 'jobs': 16, 'keep': 0, 'verbose': 0, 'zones': '', 'profile': 0, 'pdb': 0, 'whelp': 0, 'out': '', 'top': '', 'no_lock_in_run': '', 'no_lock_in_out': '', 'no_lock_in_top': '', 'prefix': '/usr', 'bindir': None, 'libdir': None, 'progress_bar': 0, 'targets': '', 'files': '', 'destdir': '', 'force': False, 'distcheck_args': None, 'check_cxx_compiler': None, 'check_c_compiler': None, 'no_tests': False, 'all_tests': False, 'clear_failed_tests': False, 'testcmd': False, 'dump_test_scripts': False, 'pyc': 1, 'pyo': 1, 'nopycache': None, 'python': None, 'pythondir': None, 'pythonarchdir': None, 'program_group': [], 'upload': None, 'upload_port': None, 'check_verbose': None, 'clean_all_sigs': None, 'summary_all': None, 'board': 'sitl', 'debug': False, 'toolchain': None, 'disable_gccdeps': False, 'enable_asserts': False, 'bootloader': False, 'autoconfig': True, 'submodule_update': True, 'enable_header_checks': False, 'default_parameters': None, 'enable_math_check_indexes': False, 'disable_scripting': False, 'scripting_checks': True, 'apstatedir': '', 'rsync_dest': '', 'enable_benchmarks': False, 'enable_lttng': False, 'disable_libiio': False, 'disable_tests': False, 'enable_sfml': False, 'enable_sfml_audio': False, 'sitl_osd': False, 'sitl_rgbled': False, 'build_dates': False, 'sitl_flash_storage': False, 'static': False}
PREFIX = '/usr'
PYC = 1
PYFLAGS = ''
PYFLAGS_OPT = '-O'
PYO = 1
PYTAG = 'cpython-37'
PYTHON = ['/home/eduardo/anaconda3/bin/python']
PYTHONARCHDIR = '/usr/lib/python3.7/site-packages'
PYTHONDIR = '/usr/lib/python3.7/site-packages'
PYTHON_VERSION = '3.7'
ROMFS_FILES = [('sandbox.lua', 'libraries/AP_Scripting/scripts/sandbox.lua')]
RPATH_ST = '-Wl,-rpath,%s'
RSYNC = ['/usr/bin/rsync']
SHLIB_MARKER = '-Wl,-Bdynamic'
SIZE = ['/usr/bin/size']
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
SUBMODULE_UPDATE = True
TOOLCHAIN = 'native'
cfg_files = ['/home/eduardo/ROS_Projects/apm/ardupilot/build/sitl/ap_config.h']
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
cxxprogram_PATTERN = '%s'
cxxshlib_PATTERN = 'lib%s.so'
cxxstlib_PATTERN = 'lib%s.a'
define_key = []
macbundle_PATTERN = '%s.bundle'
