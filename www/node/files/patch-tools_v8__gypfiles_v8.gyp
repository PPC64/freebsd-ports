--- tools/v8_gypfiles/v8.gyp.orig	2019-09-09 16:33:56 UTC
+++ tools/v8_gypfiles/v8.gyp
@@ -858,7 +858,7 @@
         }],
         # Platforms that don't have Compare-And-Swap (CAS) support need to link atomic library
         # to implement atomic memory access
-        ['v8_current_cpu in ["mips", "mipsel", "mips64", "mips64el", "ppc", "ppc64", "s390x"]', {
+        ['v8_current_cpu in ["mips", "mipsel", "mips64", "mips64el", "ppc", "s390x"]', {
           'link_settings': {
             'libraries': ['-latomic', ],
           },
