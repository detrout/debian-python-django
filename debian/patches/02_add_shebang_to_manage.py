--- django/core/management.py~       2006-07-27 18:02:02.000000000 +0100
+++ django/core/management.py        2006-12-05 16:57:10.526185500 +0000
@@ -652,12 +652,19 @@
             path_old = os.path.join(d, f)
             path_new = os.path.join(top_dir, relative_dir, f.replace('%s_name' % ap
p_or_project, name))
             fp_old = open(path_old, 'r')
             fp_new = open(path_new, 'w')
-            fp_new.write(fp_old.read().replace('{{ %s_name }}' % app_or_project, na
me).replace('{{ %s_name }}' % other, other_name))
+            if f == "manage.py":
+                fp_new.write("#!/usr/bin/python%d.%d%s" % (sys.version_info[0], sys
.version_info[1], os.linesep))
+                fp_new.write(fp_old.read().replace('{{ %s_name }}' % app_or_project
, name).replace('{{ %s_name }}' % other, other_name))
+            else:
+                fp_new.write(fp_old.read().replace('{{ %s_name }}' % app_or_project
, name).replace('{{ %s_name }}' % other, other_name))
             fp_old.close()
             fp_new.close()
-            shutil.copymode(path_old, path_new)
+            if f == "manage.py":
+                os.chmod(path_new, 0755)
+            else:
+                shutil.copymode(path_old, path_new)

