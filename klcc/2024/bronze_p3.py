def count_m(n):
    c = 0

    for i in n:
        if i % 11 == 0:
            c += 1

    return c

print(count_m([10, 15, 2, 15, 11, 2, 14, 18, 15, 15, 10, 2, 16, 8, 17, 11, 11, 8, 19, 17]))
print(count_m([189, 142, 113, 73, 26, 161, 100, 7, 59, 4, 140, 122, 7, 155, 130, 82, 183, 11, 28, 160, 197, 53, 29, 97, 34, 161, 36, 172, 3, 70, 57, 129, 77, 174, 155, 59, 12, 88, 25, 114, 90, 57, 43, 55, 32, 135, 93, 191, 20, 144, 34, 197, 135, 34, 17, 38, 132, 125, 62, 105, 155, 193, 14, 30, 66, 143, 190, 67, 35, 190, 197, 46, 39, 53, 68, 134, 99, 91, 87, 146, 44, 54, 123, 136, 134, 105, 152, 66, 75, 149, 126, 24, 131, 117, 74, 41, 128, 96, 132, 2, 108, 195, 41, 70, 125, 145, 187, 8, 28, 149, 51, 126, 24, 52, 34, 17, 164, 175, 40, 31, 168, 115, 171, 72, 152, 30, 168, 134, 43, 141, 140, 163, 31, 193, 171, 192, 169, 8, 136, 108, 129, 193, 122, 181, 92, 97, 187, 34, 113, 68, 94, 160, 68, 139, 36, 132, 189, 63, 25, 83, 64, 24, 74, 46, 88, 190, 59, 182, 77, 18, 189, 107, 184, 46, 178, 38, 25, 53, 4, 107, 40, 92, 188, 70, 168, 164, 140, 12, 155, 108, 48, 68, 27, 40, 195, 116, 32, 54, 58, 168]))
print(count_m([979, 2002, 519, 1017, 1335, 1117, 1636, 2010, 1531, 1023, 1288, 625, 1098, 1387, 293, 625, 1078, 204, 34, 301, 934, 1525, 1022, 1269, 467, 1119, 968, 707, 1175, 701, 715, 1005, 721, 754, 1867, 324, 735, 193, 427, 1257, 670, 1855, 1758, 1662, 1104, 1225, 242, 281, 1370, 1878, 36, 1606, 1829, 1591, 1650, 1686, 1675, 1451, 2020, 2020, 854, 1388, 422, 707, 1205, 1159, 416, 1619, 1041, 1470, 222, 1663, 1864, 1899, 1093, 1418, 595, 1430, 888, 1615, 439, 956, 1814, 283, 134, 1834, 521, 1420, 2022, 1222, 1886, 875, 1268, 1056, 764, 939, 665, 1010, 1208, 263, 1175, 95, 280, 1136, 316, 901, 365, 105, 919, 125, 1505, 372, 1702, 1474, 1927, 822, 1768, 1965, 1993, 281, 598, 1814, 509, 60, 1811, 1909, 1210, 683, 1338, 2016, 403, 550, 28, 1456, 63, 1154, 600, 1911, 374, 382, 1891, 1357, 1558, 1471, 886, 1741, 599, 318, 992, 1613, 754, 1755, 2004, 1543, 1884, 106, 1128, 142, 246, 1795, 1733, 367, 362, 1223, 1107, 728, 481, 1402, 1028, 707, 1039, 337, 636, 1983, 1389, 1222, 688, 582, 551, 959, 542, 1865, 1292, 1163, 1087, 2017, 814, 361, 763, 994, 1951, 1781, 1309, 1877, 790, 531, 521, 1403, 1280, 905, 1775, 649, 1518, 1502, 709, 814, 1449, 647, 514, 791, 875, 787, 1753, 542, 1076, 61, 641, 1110, 1389, 891, 1294, 737, 1334, 1205, 1529, 1057, 1307, 1467, 657, 1291, 1863, 904, 882, 275, 518, 1028, 519, 1767, 2011, 971, 87, 420, 746, 1105, 784, 609, 892, 909, 572, 1413, 1431, 2015, 1849, 1510, 1257, 1080, 1236, 388, 642, 643, 1125, 662, 1412, 914, 747, 1467, 1276, 467, 280, 1569, 1429, 437, 1538, 234, 1674, 874, 1067, 562, 1884, 1715, 1179, 1787, 6, 433, 1860, 1249, 587, 1669, 1318, 593, 1037, 439, 420, 1151, 179, 599, 2, 320, 1283, 1145, 1013, 1266, 938, 688, 1504, 815, 1002, 1157, 558, 709, 414, 1876, 1147, 1045, 138, 1287, 1459, 113, 1185, 1749, 1748, 918, 582, 600, 1451, 1361, 124, 1996, 1606, 218, 1212, 1974, 1579, 783, 1488, 405, 534, 83, 935, 218, 1853, 524, 682, 453, 417, 380, 610, 387, 1484, 1418, 1090, 885, 1286, 1576, 1027, 466, 2007, 1696, 457, 704, 783, 792, 155, 758, 361, 1691, 1239, 1985, 1280, 245, 1614, 69, 1812, 1622, 1142, 746, 274, 1112, 1448, 162, 1698, 1649, 1770, 1412, 400, 452, 576, 1836, 851, 680, 515, 734, 622, 1699, 625, 20, 795, 813, 1750, 354]))