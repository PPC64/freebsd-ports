--- common.gypi.orig	2019-09-09 16:35:03 UTC
+++ common.gypi
@@ -390,7 +390,7 @@
             'ldflags': [ '-m32' ],
           }],
           [ 'target_arch=="ppc64" and OS!="aix"', {
-            'cflags': [ '-m64', '-mminimal-toc' ],
+            'cflags': [ '-m64' ],
             'ldflags': [ '-m64' ],
           }],
           [ 'target_arch=="s390x"', {
