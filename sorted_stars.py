data = [
('Alpha Centauri A',    4.3,  0.26,      1.56),
('Alpha Centauri B',    4.3,  0.077,     0.45),
('Alpha Centauri C',    4.2,  0.00001,   0.00006),
("Barnard's Star",      6.0,  0.00004,   0.0005),
('Wolf 359',            7.7,  0.000001,  0.00002),
('BD +36 degrees 2147', 8.2,  0.0003,    0.006),
('Luyten 726-8 A',      8.4,  0.000003,  0.00006),
('Luyten 726-8 B',      8.4,  0.000002,  0.00004),
('Sirius A',            8.6,  1.00,      23.6),
('Sirius B',            8.6,  0.001,     0.003),
('Ross 154',            9.4,  0.00002,   0.0005),
]



distance_sorted_data = sorted(data, key=lambda star: star[1])
brightness_sorted_data = sorted(data, key=lambda star: star[2])
luminosity_sorted_data = sorted(data, key=lambda star: star[3])

distance_list = []
brightness_list = []
luminosity_list = []


for item in distance_sorted_data:
    item_list = list(item)
    distance_list.append([item_list[0],item_list[1]])

for item in brightness_sorted_data:
    item_list = list(item)
    brightness_list.append([item_list[0],item_list[2]])

for item in luminosity_sorted_data:
    item_list = list(item)
    luminosity_list.append([item_list[0],item_list[3]])




print(distance_list)
print(brightness_list)
print(luminosity_list)
