class Version:
   def compareVersion(self, version1, version2):
      versions1 = [int(v) for v in version1.split(".")]
      versions2 = [int(v) for v in version2.split(".")]
      for i in range(max(len(versions1),len(versions2))):
         v1 = versions1[i] if i < len(versions1) else 0
         v2 = versions2[i] if i < len(versions2) else 0
         if v1 > v2:
            return 1
         elif v1 <v2:
            return -1
      return 0

'''
Testcases
ordering: 0.1 < 1.1 < 1.2 < 1.2.9.9.9.9 < 1.3 < 1.3.4 < 1.10

'''
class_obj = Version()
assert class_obj.compareVersion('0.1', '1.1'), -1
assert class_obj.compareVersion('1.1', '1.2'), -1
assert class_obj.compareVersion('1.2', '1.2.9.9.9.9.9.9'), -1
assert class_obj.compareVersion('1.2.9.9.9.9.9.9', '1.3'), -1
assert class_obj.compareVersion('1.3', '1.3.4'), -1
assert class_obj.compareVersion('1.3.4', '1.10'), -1


assert class_obj.compareVersion('1.1', '0.1'), 1
assert class_obj.compareVersion('1.2', '1.1'), 1
assert class_obj.compareVersion('1.2.9.9.9.9.9.9', '1.2'), 1
assert class_obj.compareVersion('1.3', '1.2.9.9.9.9.9.9'), 1
assert class_obj.compareVersion('1.3.4', '1.3'), 1
assert class_obj.compareVersion('1.10', '1.3.4'), 1





