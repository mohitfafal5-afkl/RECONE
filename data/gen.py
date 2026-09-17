import json
import os

phones = [
    {
        'id': 'samsung-galaxy-s24-ultra',
        'name': 'Samsung Galaxy S24 Ultra',
        'brand': 'Samsung',
        'series': 'Galaxy S',
        'category': 'camera-mavericks',
        'categoryName': 'Camera Mavericks',
        'price': 129999,
        'priceFormatted': '₹1,29,999',
        'antutu': 2050000,
        'antutuFormatted': '2.05M',
        'processor': 'Snapdragon 8 Gen 3 for Galaxy',
        'ram': '12GB LPDDR5X',
        'storage': '256GB UFS 4.0',
        'display': {
            'size': '6.8"',
            'resolution': '3120 x 1440 (QHD+)',
            'type': 'Dynamic AMOLED 2X',
            'isFlat': True,
            'refresh': '120Hz',
            'brightness': '2600 nits',
            'protection': 'Corning Gorilla Armor'
        },
        'battery': {
            'capacity': '5000 mAh',
            'capacityNum': 5000,
            'charging': '45W Wired',
            'chargingTime': '30 min (65%)',
            'wirelessCharging': True
        },
        'camera': {
            'main': '200 MP (f/1.7)',
            'mainSensor': 'ISOCELL HP2',
            'ois': True,
            'ultrawide': '12 MP (f/2.2)',
            'telephoto': '50 MP 5x Periscope OIS + 10 MP 3x Telephoto OIS',
            'secondary': '50 MP 5x Periscope OIS + 10 MP 3x Telephoto OIS + 12 MP Ultra-Wide',
            'selfie': '12 MP (f/2.2)',
            'video': '8K@30fps, 4K@120fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'One UI 6.1',
            'version': 'Android 14',
            'bloatware': 'Moderate (Samsung Apps)',
            'updates': '7 OS / 7 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 7',
            'bluetooth': '5.3',
            'infrared': False,
            'usb': 'USB Type-C 3.2'
        },
        'build': {
            'ipRating': 'IP68',
            'weight': '232g',
            'dimensions': '162.3 x 79.0 x 8.6 mm',
            'material': 'Titanium frame, Glass back'
        },
        'biometrics': 'Ultrasonic In-display Fingerprint',
        'imageUrl': 'images/phones/samsung-galaxy-s24-ultra.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': False,
        'isCompact': False,
        'ipRating': 'IP68',
        'weight': '232g',
        'highlights': ['AnTuTu 2.05M', 'Titanium Build', '200MP Main + 5x Telephoto', 'S Pen Support'],
        'pros': ['Unmatched camera versatility', 'Gorgeous anti-reflective flat display', 'Integrated S Pen'],
        'cons': ['Heavy and bulky', 'Expensive', 'Samsung bloatware'],
        'editorialVerdict': 'The ultimate Android powerhouse offering no-compromise specs, incredible cameras, and the unmatched utility of the S Pen.',
        'releaseYear': 2024,
        'similarPhones': ['iphone-15-pro-max', 'google-pixel-8-pro']
    },
    {
        'id': 'samsung-galaxy-s24',
        'name': 'Samsung Galaxy S24',
        'brand': 'Samsung',
        'series': 'Galaxy S',
        'category': 'compact-performers',
        'categoryName': 'Compact Performers',
        'price': 74999,
        'priceFormatted': '₹74,999',
        'antutu': 2000000,
        'antutuFormatted': '2.0M',
        'processor': 'Snapdragon 8 Gen 3 for Galaxy',
        'ram': '8GB LPDDR5X',
        'storage': '256GB UFS 4.0',
        'display': {
            'size': '6.2"',
            'resolution': '2340 x 1080 (FHD+)',
            'type': 'Dynamic AMOLED 2X',
            'isFlat': True,
            'refresh': '120Hz LTPO',
            'brightness': '2600 nits',
            'protection': 'Corning Gorilla Glass Victus 2'
        },
        'battery': {
            'capacity': '4000 mAh',
            'capacityNum': 4000,
            'charging': '25W Wired',
            'chargingTime': '30 min (50%)',
            'wirelessCharging': True
        },
        'camera': {
            'main': '50 MP (f/1.8)',
            'mainSensor': 'Samsung ISOCELL GN3',
            'ois': True,
            'ultrawide': '12 MP (f/2.2)',
            'telephoto': '10 MP 3x Telephoto OIS',
            'secondary': '10 MP 3x Telephoto OIS + 12 MP Ultra-Wide',
            'selfie': '12 MP (f/2.2)',
            'video': '8K@30fps, 4K@60fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'One UI 6.1',
            'version': 'Android 14',
            'bloatware': 'Moderate (Samsung Apps)',
            'updates': '7 OS / 7 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 6E',
            'bluetooth': '5.3',
            'infrared': False,
            'usb': 'USB Type-C 3.2'
        },
        'build': {
            'ipRating': 'IP68',
            'weight': '167g',
            'dimensions': '147.0 x 70.6 x 7.6 mm',
            'material': 'Armor Aluminum frame, Glass back'
        },
        'biometrics': 'Ultrasonic In-display Fingerprint',
        'imageUrl': 'images/phones/samsung-galaxy-s24.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': False,
        'isCompact': True,
        'ipRating': 'IP68',
        'weight': '167g',
        'highlights': ['Compact Form Factor', 'LTPO Display', '7 Years OS Updates'],
        'pros': ['Perfect compact size', 'Flagship performance', 'Bright and vibrant display'],
        'cons': ['Slow 25W charging', 'Only 8GB RAM at this price', 'Samsung bloatware'],
        'editorialVerdict': 'One of the best compact Android phones available, delivering flagship performance in a pocket-friendly size.',
        'releaseYear': 2024,
        'similarPhones': ['iphone-15', 'xiaomi-14']
    },
    {
        'id': 'samsung-galaxy-s23-fe',
        'name': 'Samsung Galaxy S23 FE',
        'brand': 'Samsung',
        'series': 'Galaxy S',
        'category': 'flagship-killers',
        'categoryName': 'Flagship Killers',
        'price': 29999,
        'priceFormatted': '₹29,999',
        'antutu': 950000,
        'antutuFormatted': '950K',
        'processor': 'Exynos 2200',
        'ram': '8GB LPDDR5',
        'storage': '128GB UFS 3.1',
        'display': {
            'size': '6.4"',
            'resolution': '2340 x 1080 (FHD+)',
            'type': 'Dynamic AMOLED 2X',
            'isFlat': True,
            'refresh': '120Hz',
            'brightness': '1450 nits',
            'protection': 'Corning Gorilla Glass 5'
        },
        'battery': {
            'capacity': '4500 mAh',
            'capacityNum': 4500,
            'charging': '25W Wired',
            'chargingTime': '30 min (50%)',
            'wirelessCharging': True
        },
        'camera': {
            'main': '50 MP (f/1.8)',
            'mainSensor': 'ISOCELL GN3',
            'ois': True,
            'ultrawide': '12 MP (f/2.2)',
            'telephoto': '8 MP 3x Telephoto OIS',
            'secondary': '8 MP 3x Telephoto OIS + 12 MP Ultra-Wide',
            'selfie': '10 MP (f/2.4)',
            'video': '4K@60fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'One UI 6.0',
            'version': 'Android 14',
            'bloatware': 'Moderate',
            'updates': '4 OS / 5 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 6E',
            'bluetooth': '5.3',
            'infrared': False,
            'usb': 'USB Type-C 2.0'
        },
        'build': {
            'ipRating': 'IP68',
            'weight': '209g',
            'dimensions': '158.0 x 76.5 x 8.2 mm',
            'material': 'Aluminum frame, Glass back'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/samsung-galaxy-s23-fe.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': False,
        'isCompact': True,
        'ipRating': 'IP68',
        'weight': '209g',
        'highlights': ['Premium Glass Build', 'Versatile Triple Cameras', 'Wireless Charging'],
        'pros': ['Great camera performance for the price', 'Premium build quality with IP68', 'Wireless charging support'],
        'cons': ['Exynos 2200 runs a bit warm', 'Thick bezels', 'Heavy for its size at 209g'],
        'editorialVerdict': 'A solid entry into Samsung\'s premium ecosystem, offering great cameras and build quality if you can look past the older processor and thick bezels.',
        'releaseYear': 2023,
        'similarPhones': ['oneplus-12r', 'nothing-phone-2']
    },
    {
        'id': 'samsung-galaxy-a55',
        'name': 'Samsung Galaxy A55',
        'brand': 'Samsung',
        'series': 'Galaxy A',
        'category': 'battery-titans',
        'categoryName': 'Battery Titans',
        'price': 27999,
        'priceFormatted': '₹27,999',
        'antutu': 690000,
        'antutuFormatted': '690K',
        'processor': 'Exynos 1480',
        'ram': '8GB LPDDR4X',
        'storage': '128GB UFS 3.1',
        'display': {
            'size': '6.6"',
            'resolution': '2340 x 1080 (FHD+)',
            'type': 'Super AMOLED',
            'isFlat': True,
            'refresh': '120Hz',
            'brightness': '1000 nits',
            'protection': 'Corning Gorilla Glass Victus+'
        },
        'battery': {
            'capacity': '5000 mAh',
            'capacityNum': 5000,
            'charging': '25W Wired',
            'chargingTime': '1 hour 25 min (0-100%)',
            'wirelessCharging': False
        },
        'camera': {
            'main': '50 MP (f/1.8)',
            'mainSensor': 'Sony IMX906',
            'ois': True,
            'ultrawide': '12 MP (f/2.2)',
            'telephoto': '5 MP Macro',
            'secondary': '12 MP Ultra-Wide + 5 MP Macro',
            'selfie': '32 MP (f/2.2)',
            'video': '4K@30fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'One UI 6.1',
            'version': 'Android 14',
            'bloatware': 'Moderate',
            'updates': '4 OS / 5 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 6',
            'bluetooth': '5.3',
            'infrared': False,
            'usb': 'USB Type-C 2.0'
        },
        'build': {
            'ipRating': 'IP67',
            'weight': '213g',
            'dimensions': '161.1 x 77.4 x 8.2 mm',
            'material': 'Aluminum frame, Glass back'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/samsung-galaxy-a55.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': False,
        'isCompact': False,
        'ipRating': 'IP67',
        'weight': '213g',
        'highlights': ['Premium Metal Frame', 'IP67 Rating', 'Reliable Battery Life'],
        'pros': ['Premium aluminum and glass build', 'Excellent battery life', 'Long software support'],
        'cons': ['Slow 25W charging', 'Thick bezels', 'Average processor performance'],
        'editorialVerdict': 'A reliable mid-ranger with premium design and excellent battery life, though it trails behind competitors in raw performance and charging speed.',
        'releaseYear': 2024,
        'similarPhones': ['nothing-phone-2a-plus', 'oneplus-nord-4']
    },
    {
        'id': 'samsung-galaxy-a35',
        'name': 'Samsung Galaxy A35',
        'brand': 'Samsung',
        'series': 'Galaxy A',
        'category': 'headphone-jack-saviors',
        'categoryName': 'Headphone Jack Saviors',
        'price': 21999,
        'priceFormatted': '₹21,999',
        'antutu': 620000,
        'antutuFormatted': '620K',
        'processor': 'Exynos 1380',
        'ram': '8GB LPDDR4X',
        'storage': '128GB UFS 2.2',
        'display': {
            'size': '6.6"',
            'resolution': '2340 x 1080 (FHD+)',
            'type': 'Super AMOLED',
            'isFlat': True,
            'refresh': '120Hz',
            'brightness': '1000 nits',
            'protection': 'Corning Gorilla Glass Victus+'
        },
        'battery': {
            'capacity': '5000 mAh',
            'capacityNum': 5000,
            'charging': '25W Wired',
            'chargingTime': '1 hour 25 min (0-100%)',
            'wirelessCharging': False
        },
        'camera': {
            'main': '50 MP (f/1.8)',
            'mainSensor': 'Samsung ISOCELL GN8',
            'ois': True,
            'ultrawide': '8 MP (f/2.2)',
            'telephoto': '5 MP Macro',
            'secondary': '8 MP Ultra-Wide + 5 MP Macro',
            'selfie': '13 MP (f/2.2)',
            'video': '4K@30fps'
        },
        'audio': {
            'jack35mm': True,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'One UI 6.1',
            'version': 'Android 14',
            'bloatware': 'Moderate',
            'updates': '4 OS / 5 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 6',
            'bluetooth': '5.3',
            'infrared': False,
            'usb': 'USB Type-C 2.0'
        },
        'build': {
            'ipRating': 'IP67',
            'weight': '209g',
            'dimensions': '161.7 x 78.0 x 8.2 mm',
            'material': 'Plastic frame, Glass back'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/samsung-galaxy-a35.webp',
        'isFlat': True,
        'hasJack': True,
        'hasOIS': True,
        'isCleanOS': False,
        'isCompact': False,
        'ipRating': 'IP67',
        'weight': '209g',
        'highlights': ['IP67 Water Resistance', 'Gorilla Glass Victus+', '3.5mm Headphone Jack'],
        'pros': ['Durable build with IP67', 'Long software support', 'Includes a 3.5mm headphone jack'],
        'cons': ['Slow 25W charging', 'Dated UFS 2.2 storage', 'Performance is mediocre'],
        'editorialVerdict': 'A durable and reliable option with an IP67 rating and a rare headphone jack, making it a safe bet for casual users.',
        'releaseYear': 2024,
        'similarPhones': ['cmf-phone-1', 'poco-x6-pro']
    },
    {
        'id': 'iphone-15-pro-max',
        'name': 'Apple iPhone 15 Pro Max',
        'brand': 'Apple',
        'series': 'iPhone',
        'category': 'camera-mavericks',
        'categoryName': 'Camera Mavericks',
        'price': 159900,
        'priceFormatted': '₹1,59,900',
        'antutu': 1720000,
        'antutuFormatted': '1.72M',
        'processor': 'Apple A17 Pro (3nm)',
        'ram': '8GB LPDDR5',
        'storage': '256GB NVMe',
        'display': {
            'size': '6.7"',
            'resolution': '2796 x 1290',
            'type': 'Super Retina XDR OLED',
            'isFlat': True,
            'refresh': '120Hz ProMotion LTPO',
            'brightness': '2000 nits',
            'protection': 'Ceramic Shield glass'
        },
        'battery': {
            'capacity': '4441 mAh',
            'capacityNum': 4441,
            'charging': '27W Wired + 15W MagSafe',
            'chargingTime': '30 min (50%)',
            'wirelessCharging': True
        },
        'camera': {
            'main': '48 MP (f/1.78)',
            'mainSensor': 'Custom Sony Sensor',
            'ois': True,
            'ultrawide': '12 MP (f/2.2)',
            'telephoto': '12 MP 5x Tetraprism Telephoto OIS',
            'secondary': '12 MP 5x Telephoto OIS + 12 MP Ultra-Wide',
            'selfie': '12 MP (f/1.9) OIS',
            'video': '4K@60fps ProRes, Cinematic mode'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'iOS 17',
            'version': 'iOS 17',
            'bloatware': 'None',
            'updates': '5+ Yrs OS & Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 6E',
            'bluetooth': '5.3',
            'infrared': False,
            'usb': 'USB Type-C 3.2 Gen 2'
        },
        'build': {
            'ipRating': 'IP68',
            'weight': '221g',
            'dimensions': '159.9 x 76.7 x 8.25 mm',
            'material': 'Titanium frame, Glass back'
        },
        'biometrics': 'Face ID',
        'imageUrl': 'images/phones/iphone-15-pro-max.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': True,
        'isCompact': False,
        'ipRating': 'IP68',
        'weight': '221g',
        'highlights': ['Titanium Frame', '5x Optical Zoom', 'A17 Pro 3nm Chip', 'USB-C'],
        'pros': ['Incredible video recording capabilities', 'Lighter titanium build', 'Excellent battery life'],
        'cons': ['Very expensive', 'Slow charging speeds', 'iOS restrictions'],
        'editorialVerdict': 'The best iPhone ever made, offering unparalleled video recording, a lighter titanium body, and finally embracing USB-C.',
        'releaseYear': 2023,
        'similarPhones': ['samsung-galaxy-s24-ultra', 'google-pixel-8-pro']
    },
    {
        'id': 'iphone-15-pro',
        'name': 'Apple iPhone 15 Pro',
        'brand': 'Apple',
        'series': 'iPhone',
        'category': 'compact-performers',
        'categoryName': 'Compact Performers',
        'price': 134900,
        'priceFormatted': '₹1,34,900',
        'antutu': 1720000,
        'antutuFormatted': '1.72M',
        'processor': 'Apple A17 Pro (3nm)',
        'ram': '8GB LPDDR5',
        'storage': '128GB NVMe',
        'display': {
            'size': '6.1"',
            'resolution': '2556 x 1179',
            'type': 'Super Retina XDR OLED',
            'isFlat': True,
            'refresh': '120Hz ProMotion LTPO',
            'brightness': '2000 nits',
            'protection': 'Ceramic Shield glass'
        },
        'battery': {
            'capacity': '3274 mAh',
            'capacityNum': 3274,
            'charging': '27W Wired + 15W MagSafe',
            'chargingTime': '30 min (50%)',
            'wirelessCharging': True
        },
        'camera': {
            'main': '48 MP (f/1.78)',
            'mainSensor': 'Custom Sony Sensor',
            'ois': True,
            'ultrawide': '12 MP (f/2.2)',
            'telephoto': '12 MP 3x Telephoto OIS',
            'secondary': '12 MP 3x Telephoto OIS + 12 MP Ultra-Wide',
            'selfie': '12 MP (f/1.9) OIS',
            'video': '4K@60fps ProRes, Cinematic mode'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'iOS 17',
            'version': 'iOS 17',
            'bloatware': 'None',
            'updates': '5+ Yrs OS & Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 6E',
            'bluetooth': '5.3',
            'infrared': False,
            'usb': 'USB Type-C 3.2 Gen 2'
        },
        'build': {
            'ipRating': 'IP68',
            'weight': '187g',
            'dimensions': '146.6 x 70.6 x 8.25 mm',
            'material': 'Titanium frame, Glass back'
        },
        'biometrics': 'Face ID',
        'imageUrl': 'images/phones/iphone-15-pro.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': True,
        'isCompact': True,
        'ipRating': 'IP68',
        'weight': '187g',
        'highlights': ['Compact Titanium Build', 'A17 Pro Chip', 'Action Button'],
        'pros': ['Extremely powerful in a compact size', 'Comfortable lighter titanium build', 'Versatile Action button'],
        'cons': ['Battery life could be better', 'Expensive', 'Charging is still slow'],
        'editorialVerdict': 'A powerhouse of a compact phone that combines premium titanium materials with industry-leading performance.',
        'releaseYear': 2023,
        'similarPhones': ['samsung-galaxy-s24', 'xiaomi-14']
    },
    {
        'id': 'iphone-15',
        'name': 'Apple iPhone 15',
        'brand': 'Apple',
        'series': 'iPhone',
        'category': 'clean-software',
        'categoryName': 'Clean Software Purists',
        'price': 69900,
        'priceFormatted': '₹69,900',
        'antutu': 1350000,
        'antutuFormatted': '1.35M',
        'processor': 'Apple A16 Bionic (4nm)',
        'ram': '6GB LPDDR5',
        'storage': '128GB NVMe',
        'display': {
            'size': '6.1"',
            'resolution': '2556 x 1179',
            'type': 'Super Retina XDR OLED',
            'isFlat': True,
            'refresh': '60Hz',
            'brightness': '2000 nits',
            'protection': 'Ceramic Shield glass'
        },
        'battery': {
            'capacity': '3349 mAh',
            'capacityNum': 3349,
            'charging': '27W Wired + 15W MagSafe',
            'chargingTime': '30 min (50%)',
            'wirelessCharging': True
        },
        'camera': {
            'main': '48 MP (f/1.6)',
            'mainSensor': 'Custom Sony Sensor',
            'ois': True,
            'ultrawide': '12 MP (f/2.4)',
            'telephoto': None,
            'secondary': '12 MP Ultra-Wide',
            'selfie': '12 MP (f/1.9)',
            'video': '4K@60fps Cinematic mode'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'iOS 17',
            'version': 'iOS 17',
            'bloatware': 'None',
            'updates': '5+ Yrs OS & Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 6',
            'bluetooth': '5.3',
            'infrared': False,
            'usb': 'USB Type-C 2.0'
        },
        'build': {
            'ipRating': 'IP68',
            'weight': '171g',
            'dimensions': '147.6 x 71.6 x 7.8 mm',
            'material': 'Aluminum frame, Color-infused glass back'
        },
        'biometrics': 'Face ID',
        'imageUrl': 'images/phones/iphone-15.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': True,
        'isCompact': True,
        'ipRating': 'IP68',
        'weight': '171g',
        'highlights': ['Dynamic Island', '48MP Main Camera', 'USB-C', 'Clean iOS Experience'],
        'pros': ['Major upgrades over previous generation', 'Clean and fluid iOS experience', 'Reliable point-and-shoot camera'],
        'cons': ['Only 60Hz display in 2024', 'Slow charging speeds', 'USB-C speeds are limited to 2.0'],
        'editorialVerdict': 'The baseline iPhone finally gets meaningful upgrades like Dynamic Island and USB-C, though the 60Hz screen remains a sore point.',
        'releaseYear': 2023,
        'similarPhones': ['samsung-galaxy-s24', 'google-pixel-8a']
    },
    {
        'id': 'google-pixel-8a',
        'name': 'Google Pixel 8a',
        'brand': 'Google',
        'series': 'Pixel',
        'category': 'clean-software',
        'categoryName': 'Clean Software Purists',
        'price': 52999,
        'priceFormatted': '₹52,999',
        'antutu': 1080000,
        'antutuFormatted': '1.08M',
        'processor': 'Google Tensor G3 (4nm)',
        'ram': '8GB LPDDR5X',
        'storage': '128GB UFS 3.1',
        'display': {
            'size': '6.1"',
            'resolution': '2400 x 1080 (FHD+)',
            'type': 'Actua OLED',
            'isFlat': True,
            'refresh': '120Hz',
            'brightness': '2000 nits',
            'protection': 'Corning Gorilla Glass 3'
        },
        'battery': {
            'capacity': '4492 mAh',
            'capacityNum': 4492,
            'charging': '18W Wired + 7.5W Wireless',
            'chargingTime': '1 hour 45 min',
            'wirelessCharging': True
        },
        'camera': {
            'main': '64 MP (f/1.89)',
            'mainSensor': 'Sony IMX787',
            'ois': True,
            'ultrawide': '13 MP (f/2.2)',
            'telephoto': None,
            'secondary': '13 MP Ultra-Wide',
            'selfie': '13 MP (f/2.2)',
            'video': '4K@60fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'Pixel UI',
            'version': 'Android 14',
            'bloatware': 'None',
            'updates': '7 OS / 7 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 6E',
            'bluetooth': '5.3',
            'infrared': False,
            'usb': 'USB Type-C 3.2'
        },
        'build': {
            'ipRating': 'IP67',
            'weight': '188g',
            'dimensions': '152.1 x 72.7 x 8.9 mm',
            'material': 'Aluminum frame, Plastic back'
        },
        'biometrics': 'Optical In-display Fingerprint, Face Unlock',
        'imageUrl': 'images/phones/google-pixel-8a.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': True,
        'isCompact': True,
        'ipRating': 'IP67',
        'weight': '188g',
        'highlights': ['Pure Google Software', '7 Years Updates', 'Compact 120Hz Display'],
        'pros': ['Unbeatable clean software experience', 'Phenomenal still photography', 'Incredible 7-year update promise'],
        'cons': ['Tensor G3 runs warm under load', 'Very slow 18W charging', 'Thick display bezels'],
        'editorialVerdict': 'The Pixel 8a brings Google\'s AI smarts and legendary camera quality to a more accessible price point with an unbeatable update promise.',
        'releaseYear': 2024,
        'similarPhones': ['nothing-phone-2', 'iphone-15']
    },
    {
        'id': 'google-pixel-8-pro',
        'name': 'Google Pixel 8 Pro',
        'brand': 'Google',
        'series': 'Pixel',
        'category': 'camera-mavericks',
        'categoryName': 'Camera Mavericks',
        'price': 105999,
        'priceFormatted': '₹1,05,999',
        'antutu': 1100000,
        'antutuFormatted': '1.10M',
        'processor': 'Google Tensor G3 (4nm)',
        'ram': '12GB LPDDR5X',
        'storage': '128GB UFS 3.1',
        'display': {
            'size': '6.7"',
            'resolution': '2992 x 1344',
            'type': 'Super Actua LTPO OLED',
            'isFlat': True,
            'refresh': '120Hz',
            'brightness': '2400 nits',
            'protection': 'Corning Gorilla Glass Victus 2'
        },
        'battery': {
            'capacity': '5050 mAh',
            'capacityNum': 5050,
            'charging': '30W Wired + 23W Wireless',
            'chargingTime': '1 hour 20 min',
            'wirelessCharging': True
        },
        'camera': {
            'main': '50 MP (f/1.68)',
            'mainSensor': 'Samsung ISOCELL GNK',
            'ois': True,
            'ultrawide': '48 MP (f/1.95)',
            'telephoto': '48 MP 5x Telephoto OIS',
            'secondary': '48 MP 5x Telephoto OIS + 48 MP Ultra-Wide',
            'selfie': '10.5 MP (f/2.2)',
            'video': '4K@60fps with Video Boost'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'Pixel UI',
            'version': 'Android 14',
            'bloatware': 'None',
            'updates': '7 OS / 7 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 7',
            'bluetooth': '5.3',
            'infrared': False,
            'usb': 'USB Type-C 3.2'
        },
        'build': {
            'ipRating': 'IP68',
            'weight': '213g',
            'dimensions': '162.6 x 76.5 x 8.8 mm',
            'material': 'Aluminum frame, Glass back'
        },
        'biometrics': 'Optical In-display Fingerprint, Face Unlock',
        'imageUrl': 'images/phones/google-pixel-8-pro.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': True,
        'isCompact': False,
        'ipRating': 'IP68',
        'weight': '213g',
        'highlights': ['Super Actua Display', 'Pro Camera Controls', 'Temperature Sensor', 'Google AI'],
        'pros': ['Industry-leading still photography', 'Clean and smart software features', 'Bright and flat display'],
        'cons': ['Tensor G3 trails behind Snapdragon 8 Gen 3', 'Slow charging', 'Base model starts at 128GB'],
        'editorialVerdict': 'A photographer\'s dream phone with unmatched computational photography and the cleanest version of Android available.',
        'releaseYear': 2023,
        'similarPhones': ['samsung-galaxy-s24-ultra', 'iphone-15-pro-max']
    },
    {
        'id': 'oneplus-12',
        'name': 'OnePlus 12',
        'brand': 'OnePlus',
        'series': 'Number Series',
        'category': 'flagship-killers',
        'categoryName': 'Flagship Killers',
        'price': 64999,
        'priceFormatted': '₹64,999',
        'antutu': 2100000,
        'antutuFormatted': '2.1M',
        'processor': 'Snapdragon 8 Gen 3 (4nm)',
        'ram': '12GB LPDDR5X',
        'storage': '256GB UFS 4.0',
        'display': {
            'size': '6.82"',
            'resolution': '3168 x 1440 (2K)',
            'type': 'LTPO AMOLED',
            'isFlat': False,
            'refresh': '120Hz',
            'brightness': '4500 nits (peak)',
            'protection': 'Corning Gorilla Glass Victus 2'
        },
        'battery': {
            'capacity': '5400 mAh',
            'capacityNum': 5400,
            'charging': '100W SUPERVOOC + 50W wireless',
            'chargingTime': '26 min (0-100%)',
            'wirelessCharging': True
        },
        'camera': {
            'main': '50 MP (f/1.6)',
            'mainSensor': 'Sony LYT-808',
            'ois': True,
            'ultrawide': '48 MP (f/2.2)',
            'telephoto': '64 MP 3x Periscope OIS',
            'secondary': '64 MP 3x Periscope OIS + 48 MP Ultra-Wide',
            'selfie': '32 MP (f/2.4)',
            'video': '8K@24fps, 4K@60fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo with Dolby Atmos'
        },
        'os': {
            'name': 'OxygenOS 14',
            'version': 'Android 14',
            'bloatware': 'Minimal',
            'updates': '4 OS / 5 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 7',
            'bluetooth': '5.4',
            'infrared': True,
            'usb': 'USB Type-C 3.2'
        },
        'build': {
            'ipRating': 'IP65',
            'weight': '220g',
            'dimensions': '164.3 x 75.8 x 9.2 mm',
            'material': 'Aluminum frame, Glass back'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/oneplus-12.webp',
        'isFlat': False,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': True,
        'isCompact': False,
        'ipRating': 'IP65',
        'weight': '220g',
        'highlights': ['Hasselblad Cameras', '100W Charging', '5400mAh Battery', 'Alert Slider'],
        'pros': ['Exceptional battery life and fast charging', 'Clean OxygenOS experience', 'Great versatile camera setup'],
        'cons': ['Curved screen is prone to accidental touches', 'Only IP65 rating, no IP68', 'Quite heavy at 220g'],
        'editorialVerdict': 'The OnePlus 12 marks a return to form for the brand, offering genuine flagship specs at a much more reasonable price than competitors.',
        'releaseYear': 2024,
        'similarPhones': ['iqoo-12', 'samsung-galaxy-s24']
    },
    {
        'id': 'oneplus-12r',
        'name': 'OnePlus 12R',
        'brand': 'OnePlus',
        'series': 'Number Series',
        'category': 'flagship-killers',
        'categoryName': 'Flagship Killers',
        'price': 39999,
        'priceFormatted': '₹39,999',
        'antutu': 1550000,
        'antutuFormatted': '1.55M',
        'processor': 'Snapdragon 8 Gen 2 (4nm)',
        'ram': '8GB LPDDR5X',
        'storage': '128GB UFS 3.1',
        'display': {
            'size': '6.78"',
            'resolution': '2780 x 1264 (1.5K)',
            'type': 'LTPO 4.0 AMOLED',
            'isFlat': False,
            'refresh': '120Hz',
            'brightness': '4500 nits (peak)',
            'protection': 'Corning Gorilla Glass Victus 2'
        },
        'battery': {
            'capacity': '5500 mAh',
            'capacityNum': 5500,
            'charging': '100W SUPERVOOC',
            'chargingTime': '26 min (0-100%)',
            'wirelessCharging': False
        },
        'camera': {
            'main': '50 MP (f/1.8)',
            'mainSensor': 'Sony IMX890',
            'ois': True,
            'ultrawide': '8 MP (f/2.2)',
            'telephoto': None,
            'secondary': '8 MP Ultra-Wide + 2 MP Macro',
            'selfie': '16 MP (f/2.4)',
            'video': '4K@60fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'OxygenOS 14',
            'version': 'Android 14',
            'bloatware': 'Minimal',
            'updates': '3 OS / 4 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 7',
            'bluetooth': '5.3',
            'infrared': True,
            'usb': 'USB Type-C 2.0'
        },
        'build': {
            'ipRating': 'IP64',
            'weight': '207g',
            'dimensions': '163.3 x 75.3 x 8.8 mm',
            'material': 'Aluminum frame, Glass back'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/oneplus-12r.webp',
        'isFlat': False,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': True,
        'isCompact': False,
        'ipRating': 'IP64',
        'weight': '207g',
        'highlights': ['Snapdragon 8 Gen 2', '5500mAh Battery', '100W Fast Charging', 'Alert Slider'],
        'pros': ['Phenomenal performance for the price', 'Outstanding battery life', 'Premium curved design'],
        'cons': ['Secondary cameras are poor', 'No wireless charging', 'Curved screen might not appeal to all'],
        'editorialVerdict': 'An absolute performance monster for the price, pairing last year\'s flagship chip with incredible battery life.',
        'releaseYear': 2024,
        'similarPhones': ['iqoo-neo-9-pro', 'vivo-v30-pro']
    },
    {
        'id': 'oneplus-nord-4',
        'name': 'OnePlus Nord 4',
        'brand': 'OnePlus',
        'series': 'Nord Series',
        'category': 'battery-titans',
        'categoryName': 'Battery Titans',
        'price': 29999,
        'priceFormatted': '₹29,999',
        'antutu': 1210000,
        'antutuFormatted': '1.21M',
        'processor': 'Snapdragon 7+ Gen 3 (4nm)',
        'ram': '8GB LPDDR5X',
        'storage': '256GB UFS 4.0',
        'display': {
            'size': '6.74"',
            'resolution': '2772 x 1240 (1.5K)',
            'type': 'Fluid AMOLED',
            'isFlat': True,
            'refresh': '120Hz',
            'brightness': '2150 nits (peak)',
            'protection': 'Glass protection'
        },
        'battery': {
            'capacity': '5500 mAh',
            'capacityNum': 5500,
            'charging': '100W SUPERVOOC',
            'chargingTime': '28 min (0-100%)',
            'wirelessCharging': False
        },
        'camera': {
            'main': '50 MP (f/1.8)',
            'mainSensor': 'Sony LYT-600',
            'ois': True,
            'ultrawide': '8 MP (f/2.2)',
            'telephoto': None,
            'secondary': '8 MP Ultra-Wide',
            'selfie': '16 MP (f/2.4)',
            'video': '4K@60fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'OxygenOS 14.1',
            'version': 'Android 14',
            'bloatware': 'Minimal',
            'updates': '4 OS / 6 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 6',
            'bluetooth': '5.4',
            'infrared': True,
            'usb': 'USB Type-C 2.0'
        },
        'build': {
            'ipRating': 'IP65',
            'weight': '199g',
            'dimensions': '162.5 x 75.0 x 8.0 mm',
            'material': 'Aluminum unibody'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/oneplus-nord-4.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': True,
        'isCompact': False,
        'ipRating': 'IP65',
        'weight': '199g',
        'highlights': ['Metal Unibody Design', 'Massive 5500mAh Battery', '100W Charging', '6 Years Security Updates'],
        'pros': ['Durable and unique all-metal design', 'Stellar battery and charging speeds', 'Longest software support in this segment'],
        'cons': ['Average ultra-wide camera', 'No telephoto lens', 'No wireless charging'],
        'editorialVerdict': 'A standout mid-ranger boasting a nostalgic metal unibody design, fantastic battery life, and excellent software support.',
        'releaseYear': 2024,
        'similarPhones': ['realme-gt-6t', 'poco-f6']
    },
    {
        'id': 'xiaomi-14',
        'name': 'Xiaomi 14',
        'brand': 'Xiaomi',
        'series': 'Number Series',
        'category': 'compact-performers',
        'categoryName': 'Compact Performers',
        'price': 69999,
        'priceFormatted': '₹69,999',
        'antutu': 1980000,
        'antutuFormatted': '1.98M',
        'processor': 'Snapdragon 8 Gen 3 (4nm)',
        'ram': '12GB LPDDR5X',
        'storage': '512GB UFS 4.0',
        'display': {
            'size': '6.36"',
            'resolution': '2670 x 1200 (1.5K)',
            'type': 'LTPO OLED',
            'isFlat': True,
            'refresh': '120Hz',
            'brightness': '3000 nits (peak)',
            'protection': 'Corning Gorilla Glass Victus'
        },
        'battery': {
            'capacity': '4610 mAh',
            'capacityNum': 4610,
            'charging': '90W Wired + 50W Wireless',
            'chargingTime': '31 min (0-100%)',
            'wirelessCharging': True
        },
        'camera': {
            'main': '50 MP (f/1.6)',
            'mainSensor': 'Light Hunter 900',
            'ois': True,
            'ultrawide': '50 MP (f/2.2)',
            'telephoto': '50 MP 3.2x Telephoto OIS',
            'secondary': '50 MP 3.2x Telephoto OIS + 50 MP Ultra-Wide',
            'selfie': '32 MP (f/2.0)',
            'video': '8K@24fps, 4K@60fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'HyperOS',
            'version': 'Android 14',
            'bloatware': 'Moderate',
            'updates': '4 OS / 5 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 7',
            'bluetooth': '5.4',
            'infrared': True,
            'usb': 'USB Type-C 3.2 Gen 1'
        },
        'build': {
            'ipRating': 'IP68',
            'weight': '193g',
            'dimensions': '152.8 x 71.5 x 8.2 mm',
            'material': 'Aluminum frame, Glass back'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/xiaomi-14.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': False,
        'isCompact': True,
        'ipRating': 'IP68',
        'weight': '193g',
        'highlights': ['Compact Size', 'Leica Optics', 'Snapdragon 8 Gen 3', '90W Charging'],
        'pros': ['Incredible Leica-tuned cameras', 'Perfect one-handed size', 'Stunning flat display'],
        'cons': ['HyperOS has bloatware', 'Runs warm during heavy gaming', 'Selfie camera is only average'],
        'editorialVerdict': 'One of the very few compact Android flagships that refuses to compromise on performance or camera capabilities.',
        'releaseYear': 2024,
        'similarPhones': ['samsung-galaxy-s24', 'iphone-15-pro']
    },
    {
        'id': 'poco-f6',
        'name': 'POCO F6',
        'brand': 'POCO',
        'series': 'F Series',
        'category': 'flagship-killers',
        'categoryName': 'Flagship Killers',
        'price': 25999,
        'priceFormatted': '₹25,999',
        'antutu': 1530000,
        'antutuFormatted': '1.53M',
        'processor': 'Snapdragon 8s Gen 3 (4nm)',
        'ram': '8GB LPDDR5X',
        'storage': '256GB UFS 4.0',
        'display': {
            'size': '6.67"',
            'resolution': '2712 x 1220 (1.5K)',
            'type': 'AMOLED',
            'isFlat': True,
            'refresh': '120Hz',
            'brightness': '2400 nits',
            'protection': 'Corning Gorilla Glass Victus'
        },
        'battery': {
            'capacity': '5000 mAh',
            'capacityNum': 5000,
            'charging': '90W Turbo',
            'chargingTime': '35 min (0-100%)',
            'wirelessCharging': False
        },
        'camera': {
            'main': '50 MP (f/1.59)',
            'mainSensor': 'Sony IMX882',
            'ois': True,
            'ultrawide': '8 MP (f/2.2)',
            'telephoto': None,
            'secondary': '8 MP Ultra-Wide',
            'selfie': '20 MP (f/2.2)',
            'video': '4K@60fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'HyperOS',
            'version': 'Android 14',
            'bloatware': 'Moderate (Debloatable)',
            'updates': '3 OS / 4 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 6',
            'bluetooth': '5.4',
            'infrared': True,
            'usb': 'USB Type-C 2.0'
        },
        'build': {
            'ipRating': 'IP64',
            'weight': '179g',
            'dimensions': '160.5 x 74.4 x 7.8 mm',
            'material': 'Plastic frame, Plastic back'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/poco-f6.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': False,
        'isCompact': False,
        'ipRating': 'IP64',
        'weight': '179g',
        'highlights': ['Snapdragon 8s Gen 3', 'Flat 1.5K AMOLED', '90W Charging', 'Lightweight Design'],
        'pros': ['Insane performance for the price', 'Great flat display with high brightness', 'Lightweight and comfortable to hold'],
        'cons': ['Plastic build feels cheap', 'HyperOS bloatware', 'Average ultra-wide camera'],
        'editorialVerdict': 'The reigning champion of budget performance, delivering near-flagship speeds at a fraction of the cost.',
        'releaseYear': 2024,
        'similarPhones': ['poco-x6-pro', 'realme-gt-6t']
    },
    {
        'id': 'poco-x6-pro',
        'name': 'POCO X6 Pro',
        'brand': 'POCO',
        'series': 'X Series',
        'category': 'flagship-killers',
        'categoryName': 'Flagship Killers',
        'price': 22999,
        'priceFormatted': '₹22,999',
        'antutu': 1250000,
        'antutuFormatted': '1.25M',
        'processor': 'Dimensity 8300-Ultra (4nm)',
        'ram': '8GB LPDDR5X',
        'storage': '256GB UFS 4.0',
        'display': {
            'size': '6.67"',
            'resolution': '2712 x 1220 (1.5K)',
            'type': 'AMOLED',
            'isFlat': True,
            'refresh': '120Hz',
            'brightness': '1800 nits (peak)',
            'protection': 'Corning Gorilla Glass 5'
        },
        'battery': {
            'capacity': '5000 mAh',
            'capacityNum': 5000,
            'charging': '67W Turbo',
            'chargingTime': '45 min (0-100%)',
            'wirelessCharging': False
        },
        'camera': {
            'main': '64 MP (f/1.7)',
            'mainSensor': 'OmniVision OV64B',
            'ois': True,
            'ultrawide': '8 MP (f/2.2)',
            'telephoto': None,
            'secondary': '8 MP Ultra-Wide + 2 MP Macro',
            'selfie': '16 MP (f/2.4)',
            'video': '4K@30fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'HyperOS',
            'version': 'Android 14',
            'bloatware': 'Heavy (Debloatable)',
            'updates': '3 OS / 4 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 6',
            'bluetooth': '5.4',
            'infrared': True,
            'usb': 'USB Type-C 2.0'
        },
        'build': {
            'ipRating': 'IP53',
            'weight': '186g',
            'dimensions': '160.5 x 74.3 x 8.3 mm',
            'material': 'Plastic frame, Vegan Leather/Plastic back'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/poco-x6-pro.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': False,
        'isCompact': False,
        'ipRating': 'IP53',
        'weight': '186g',
        'highlights': ['Dimensity 8300-Ultra', '1.5K Flat Display', 'UFS 4.0 Storage'],
        'pros': ['Unbeatable gaming performance in its segment', 'Fast UFS 4.0 storage', 'Vibrant flat display'],
        'cons': ['Heavy bloatware out of the box', 'Cameras are mediocre', 'Plastic build'],
        'editorialVerdict': 'A gaming beast on a budget, sacrificing camera quality and premium materials for sheer, unadulterated power.',
        'releaseYear': 2024,
        'similarPhones': ['poco-f6', 'realme-gt-6t']
    },
    {
        'id': 'redmi-note-13-pro-plus',
        'name': 'Redmi Note 13 Pro+',
        'brand': 'Xiaomi',
        'series': 'Redmi Note',
        'category': 'camera-mavericks',
        'categoryName': 'Camera Mavericks',
        'price': 31999,
        'priceFormatted': '₹31,999',
        'antutu': 750000,
        'antutuFormatted': '750K',
        'processor': 'Dimensity 7200-Ultra (4nm)',
        'ram': '8GB LPDDR5',
        'storage': '256GB UFS 3.1',
        'display': {
            'size': '6.67"',
            'resolution': '2712 x 1220 (1.5K)',
            'type': 'Curved AMOLED',
            'isFlat': False,
            'refresh': '120Hz',
            'brightness': '1800 nits (peak)',
            'protection': 'Corning Gorilla Glass Victus'
        },
        'battery': {
            'capacity': '5000 mAh',
            'capacityNum': 5000,
            'charging': '120W HyperCharge',
            'chargingTime': '19 min (0-100%)',
            'wirelessCharging': False
        },
        'camera': {
            'main': '200 MP (f/1.65)',
            'mainSensor': 'Samsung ISOCELL HP3',
            'ois': True,
            'ultrawide': '8 MP (f/2.2)',
            'telephoto': None,
            'secondary': '8 MP Ultra-Wide + 2 MP Macro',
            'selfie': '16 MP (f/2.4)',
            'video': '4K@30fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'HyperOS',
            'version': 'Android 14',
            'bloatware': 'Moderate',
            'updates': '3 OS / 4 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 6',
            'bluetooth': '5.3',
            'infrared': True,
            'usb': 'USB Type-C 2.0'
        },
        'build': {
            'ipRating': 'IP68',
            'weight': '204.5g',
            'dimensions': '161.4 x 74.2 x 8.9 mm',
            'material': 'Aluminum frame, Glass/Vegan Leather back'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/redmi-note-13-pro-plus.webp',
        'isFlat': False,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': False,
        'isCompact': False,
        'ipRating': 'IP68',
        'weight': '204.5g',
        'highlights': ['200MP Main Camera', 'IP68 Rating', 'Curved Display', '120W Charging'],
        'pros': ['Excellent 200MP primary camera', 'Premium curved design with IP68', 'Insanely fast 120W charging'],
        'cons': ['Useless 2MP macro camera', 'HyperOS contains bloat', 'Performance is average for the price'],
        'editorialVerdict': 'It brings flagship-tier design, IP68 protection, and a massive 200MP sensor to the mid-range segment.',
        'releaseYear': 2024,
        'similarPhones': ['realme-12-pro-plus', 'vivo-v30-pro']
    },
    {
        'id': 'nothing-phone-2a-plus',
        'name': 'Nothing Phone (2a) Plus',
        'brand': 'Nothing',
        'series': 'Phone',
        'category': 'clean-software',
        'categoryName': 'Clean Software Purists',
        'price': 27999,
        'priceFormatted': '₹27,999',
        'antutu': 805000,
        'antutuFormatted': '805K',
        'processor': 'Dimensity 7350 Pro (4nm)',
        'ram': '8GB LPDDR4X',
        'storage': '256GB UFS 2.2',
        'display': {
            'size': '6.7"',
            'resolution': '2412 x 1080 (FHD+)',
            'type': 'Flexible AMOLED',
            'isFlat': True,
            'refresh': '120Hz',
            'brightness': '1300 nits (peak)',
            'protection': 'Corning Gorilla Glass 5'
        },
        'battery': {
            'capacity': '5000 mAh',
            'capacityNum': 5000,
            'charging': '50W',
            'chargingTime': '56 min (0-100%)',
            'wirelessCharging': False
        },
        'camera': {
            'main': '50 MP (f/1.88)',
            'mainSensor': 'Samsung GN9',
            'ois': True,
            'ultrawide': '50 MP (f/2.2)',
            'telephoto': None,
            'secondary': '50 MP Ultra-Wide',
            'selfie': '50 MP (f/2.2)',
            'video': '4K@30fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'Nothing OS 2.6',
            'version': 'Android 14',
            'bloatware': 'None',
            'updates': '3 OS / 4 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 6',
            'bluetooth': '5.3',
            'infrared': False,
            'usb': 'USB Type-C 2.0'
        },
        'build': {
            'ipRating': 'IP54',
            'weight': '190g',
            'dimensions': '161.7 x 76.3 x 8.5 mm',
            'material': 'Plastic frame, Transparent plastic back'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/nothing-phone-2a-plus.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': True,
        'isCompact': False,
        'ipRating': 'IP54',
        'weight': '190g',
        'highlights': ['Glyph Interface', 'Symmetrical Bezels', 'Dual 50MP Cameras', 'Clean Software'],
        'pros': ['Striking transparent design with Glyphs', 'Incredibly smooth and clean software', 'Great battery life'],
        'cons': ['Plastic build scratches easily', 'Uses slower UFS 2.2 storage', 'Charger not included in box'],
        'editorialVerdict': 'A masterclass in design and software experience, making it the most fun and unique phone in the mid-range segment.',
        'releaseYear': 2024,
        'similarPhones': ['cmf-phone-1', 'samsung-galaxy-a55']
    },
    {
        'id': 'nothing-phone-2',
        'name': 'Nothing Phone (2)',
        'brand': 'Nothing',
        'series': 'Phone',
        'category': 'clean-software',
        'categoryName': 'Clean Software Purists',
        'price': 32999,
        'priceFormatted': '₹32,999',
        'antutu': 1150000,
        'antutuFormatted': '1.15M',
        'processor': 'Snapdragon 8+ Gen 1 (4nm)',
        'ram': '8GB LPDDR5',
        'storage': '128GB UFS 3.1',
        'display': {
            'size': '6.7"',
            'resolution': '2412 x 1080 (FHD+)',
            'type': 'LTPO OLED',
            'isFlat': True,
            'refresh': '120Hz',
            'brightness': '1600 nits (peak)',
            'protection': 'Corning Gorilla Glass'
        },
        'battery': {
            'capacity': '4700 mAh',
            'capacityNum': 4700,
            'charging': '45W Wired + 15W Wireless + 5W Reverse',
            'chargingTime': '55 min (0-100%)',
            'wirelessCharging': True
        },
        'camera': {
            'main': '50 MP (f/1.88)',
            'mainSensor': 'Sony IMX890',
            'ois': True,
            'ultrawide': '50 MP (f/2.2)',
            'telephoto': None,
            'secondary': '50 MP Ultra-Wide',
            'selfie': '32 MP (f/2.45)',
            'video': '4K@60fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'Nothing OS 2.5',
            'version': 'Android 14',
            'bloatware': 'None',
            'updates': '3 OS / 4 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 6',
            'bluetooth': '5.3',
            'infrared': False,
            'usb': 'USB Type-C 2.0'
        },
        'build': {
            'ipRating': 'IP54',
            'weight': '201.2g',
            'dimensions': '162.1 x 76.4 x 8.6 mm',
            'material': 'Aluminum frame, Glass back'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/nothing-phone-2.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': True,
        'isCompact': False,
        'ipRating': 'IP54',
        'weight': '201.2g',
        'highlights': ['Advanced Glyph Interface', 'Snapdragon 8+ Gen 1', 'Premium Build', 'Wireless Charging'],
        'pros': ['Premium glass and metal build', 'Fluid software experience without bloatware', 'Wireless charging support'],
        'cons': ['Only IP54 rating', 'Older processor compared to rivals', 'Cameras can be inconsistent'],
        'editorialVerdict': 'It successfully blends a premium build, eccentric design, and buttery smooth software into a compelling package.',
        'releaseYear': 2023,
        'similarPhones': ['google-pixel-8a', 'oneplus-12r']
    },
    {
        'id': 'cmf-phone-1',
        'name': 'CMF Phone 1',
        'brand': 'Nothing',
        'series': 'CMF',
        'category': 'flagship-killers',
        'categoryName': 'Flagship Killers',
        'price': 15999,
        'priceFormatted': '₹15,999',
        'antutu': 665000,
        'antutuFormatted': '665K',
        'processor': 'Dimensity 7300 (4nm)',
        'ram': '6GB LPDDR4X',
        'storage': '128GB UFS 2.2',
        'display': {
            'size': '6.67"',
            'resolution': '2400 x 1080 (FHD+)',
            'type': 'Super AMOLED',
            'isFlat': True,
            'refresh': '120Hz',
            'brightness': '2000 nits (peak)',
            'protection': 'Glass protection'
        },
        'battery': {
            'capacity': '5000 mAh',
            'capacityNum': 5000,
            'charging': '33W',
            'chargingTime': '1 hour 20 min',
            'wirelessCharging': False
        },
        'camera': {
            'main': '50 MP (f/1.8)',
            'mainSensor': 'Sony Sensor',
            'ois': False,
            'ultrawide': None,
            'telephoto': None,
            'secondary': '2 MP Depth Sensor',
            'selfie': '16 MP (f/2.0)',
            'video': '4K@30fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': False,
            'speakerDetails': 'Single Bottom Firing'
        },
        'os': {
            'name': 'Nothing OS 2.6',
            'version': 'Android 14',
            'bloatware': 'None',
            'updates': '2 OS / 3 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': False,
            'wifi': 'Wi-Fi 6',
            'bluetooth': '5.3',
            'infrared': False,
            'usb': 'USB Type-C 2.0'
        },
        'build': {
            'ipRating': 'IP52',
            'weight': '197g',
            'dimensions': '164.0 x 77.0 x 8.0 mm',
            'material': 'Plastic frame, Interchangeable plastic back'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/cmf-phone-1.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': False,
        'isCleanOS': True,
        'isCompact': False,
        'ipRating': 'IP52',
        'weight': '197g',
        'highlights': ['Modular Back Cover', 'Clean Nothing OS', 'Dimensity 7300', 'Super AMOLED'],
        'pros': ['Unique swappable back covers', 'Bloatware-free Nothing OS', 'Good performance for the price'],
        'cons': ['No ultra-wide camera', 'Mono speaker', 'No NFC'],
        'editorialVerdict': 'An innovative budget phone that brings a fresh modular design and clean software to a segment dominated by boring plastic slabs.',
        'releaseYear': 2024,
        'similarPhones': ['poco-x6-pro', 'samsung-galaxy-a35']
    },
    {
        'id': 'vivo-v30-pro',
        'name': 'Vivo V30 Pro',
        'brand': 'Vivo',
        'series': 'V Series',
        'category': 'camera-mavericks',
        'categoryName': 'Camera Mavericks',
        'price': 39999,
        'priceFormatted': '₹39,999',
        'antutu': 960000,
        'antutuFormatted': '960K',
        'processor': 'Dimensity 8200 (4nm)',
        'ram': '8GB LPDDR5',
        'storage': '256GB UFS 3.1',
        'display': {
            'size': '6.78"',
            'resolution': '2800 x 1260 (1.5K)',
            'type': 'Curved AMOLED',
            'isFlat': False,
            'refresh': '120Hz',
            'brightness': '2800 nits (peak)',
            'protection': 'Schott Alpha Glass'
        },
        'battery': {
            'capacity': '5000 mAh',
            'capacityNum': 5000,
            'charging': '80W FlashCharge',
            'chargingTime': '43 min (0-100%)',
            'wirelessCharging': False
        },
        'camera': {
            'main': '50 MP (f/1.88)',
            'mainSensor': 'Sony IMX920',
            'ois': True,
            'ultrawide': '50 MP (f/2.0)',
            'telephoto': '50 MP 2x Telephoto OIS',
            'secondary': '50 MP 2x Telephoto OIS + 50 MP Ultra-Wide',
            'selfie': '50 MP (f/2.0)',
            'video': '4K@60fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': False,
            'speakerDetails': 'Single Speaker'
        },
        'os': {
            'name': 'Funtouch OS 14',
            'version': 'Android 14',
            'bloatware': 'Moderate',
            'updates': '2 OS / 3 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 6',
            'bluetooth': '5.3',
            'infrared': False,
            'usb': 'USB Type-C 2.0'
        },
        'build': {
            'ipRating': 'IP54',
            'weight': '187g',
            'dimensions': '164.4 x 75.1 x 7.5 mm',
            'material': 'Plastic frame, Glass back'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/vivo-v30-pro.webp',
        'isFlat': False,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': False,
        'isCompact': False,
        'ipRating': 'IP54',
        'weight': '187g',
        'highlights': ['Zeiss Optics', 'Quad 50MP Cameras', 'Aura Light', 'Slim Design'],
        'pros': ['Exceptional portrait photography with Zeiss effects', 'Very slim and lightweight', 'Great battery life despite thin design'],
        'cons': ['Mono speaker is unacceptable at this price', 'Plastic frame', 'Funtouch OS bloatware'],
        'editorialVerdict': 'A portrait photography marvel that punches above its weight in camera performance, but cuts corners on build and audio.',
        'releaseYear': 2024,
        'similarPhones': ['redmi-note-13-pro-plus', 'oneplus-12r']
    },
    {
        'id': 'iqoo-neo-9-pro',
        'name': 'iQOO Neo 9 Pro',
        'brand': 'iQOO',
        'series': 'Neo Series',
        'category': 'flagship-killers',
        'categoryName': 'Flagship Killers',
        'price': 36999,
        'priceFormatted': '₹36,999',
        'antutu': 1680000,
        'antutuFormatted': '1.68M',
        'processor': 'Snapdragon 8 Gen 2 (4nm)',
        'ram': '8GB LPDDR5X',
        'storage': '256GB UFS 4.0',
        'display': {
            'size': '6.78"',
            'resolution': '2800 x 1260 (1.5K)',
            'type': 'LTPO AMOLED',
            'isFlat': True,
            'refresh': '144Hz',
            'brightness': '3000 nits (peak)',
            'protection': 'Glass protection'
        },
        'battery': {
            'capacity': '5160 mAh',
            'capacityNum': 5160,
            'charging': '120W FlashCharge',
            'chargingTime': '27 min (0-100%)',
            'wirelessCharging': False
        },
        'camera': {
            'main': '50 MP (f/1.88)',
            'mainSensor': 'Sony IMX920',
            'ois': True,
            'ultrawide': '8 MP (f/2.2)',
            'telephoto': None,
            'secondary': '8 MP Ultra-Wide',
            'selfie': '16 MP (f/2.45)',
            'video': '8K@30fps, 4K@60fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'Funtouch OS 14',
            'version': 'Android 14',
            'bloatware': 'Moderate',
            'updates': '3 OS / 4 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 7',
            'bluetooth': '5.3',
            'infrared': True,
            'usb': 'USB Type-C 2.0'
        },
        'build': {
            'ipRating': 'IP54',
            'weight': '190g',
            'dimensions': '163.5 x 75.7 x 8.0 mm',
            'material': 'Plastic frame, Glass or Vegan Leather back'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/iqoo-neo-9-pro.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': False,
        'isCompact': False,
        'ipRating': 'IP54',
        'weight': '190g',
        'highlights': ['Snapdragon 8 Gen 2', '144Hz Flat Display', '120W Charging', 'Dual-Tone Leather'],
        'pros': ['Phenomenal gaming performance', 'Flat 144Hz LTPO display is great', 'Super fast 120W charging'],
        'cons': ['Funtouch OS has bloatware', 'Average ultra-wide camera', 'Plastic frame'],
        'editorialVerdict': 'An absolute performance beast targeted at gamers, offering blazing fast charging and a great flat display.',
        'releaseYear': 2024,
        'similarPhones': ['oneplus-12r', 'poco-f6']
    },
    {
        'id': 'iqoo-12',
        'name': 'iQOO 12',
        'brand': 'iQOO',
        'series': 'Flagship Series',
        'category': 'flagship-killers',
        'categoryName': 'Flagship Killers',
        'price': 52999,
        'priceFormatted': '₹52,999',
        'antutu': 2150000,
        'antutuFormatted': '2.15M',
        'processor': 'Snapdragon 8 Gen 3 (4nm)',
        'ram': '12GB LPDDR5X',
        'storage': '256GB UFS 4.0',
        'display': {
            'size': '6.78"',
            'resolution': '2800 x 1260 (1.5K)',
            'type': 'LTPO AMOLED',
            'isFlat': True,
            'refresh': '144Hz',
            'brightness': '3000 nits (peak)',
            'protection': 'Glass protection'
        },
        'battery': {
            'capacity': '5000 mAh',
            'capacityNum': 5000,
            'charging': '120W FlashCharge',
            'chargingTime': '26 min (0-100%)',
            'wirelessCharging': False
        },
        'camera': {
            'main': '50 MP (f/1.68)',
            'mainSensor': 'Sony IMX920',
            'ois': True,
            'ultrawide': '50 MP (f/2.0)',
            'telephoto': '64 MP 3x Periscope OIS',
            'secondary': '64 MP 3x Periscope OIS + 50 MP Ultra-Wide',
            'selfie': '16 MP (f/2.45)',
            'video': '8K@30fps, 4K@60fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'Funtouch OS 14',
            'version': 'Android 14',
            'bloatware': 'Moderate',
            'updates': '3 OS / 4 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 7',
            'bluetooth': '5.4',
            'infrared': True,
            'usb': 'USB Type-C 2.0'
        },
        'build': {
            'ipRating': 'IP64',
            'weight': '205.6g',
            'dimensions': '163.2 x 75.9 x 8.1 mm',
            'material': 'Aluminum frame, Glass back'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/iqoo-12.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': False,
        'isCompact': False,
        'ipRating': 'IP64',
        'weight': '205.6g',
        'highlights': ['Snapdragon 8 Gen 3', '64MP Periscope Camera', '144Hz Display', '120W Charging'],
        'pros': ['Unbelievable value for Snapdragon 8 Gen 3', 'Surprisingly versatile camera setup', 'Great gaming performance'],
        'cons': ['Funtouch OS needs refinement', 'Only IP64 rating', 'No wireless charging'],
        'editorialVerdict': 'It sets a new benchmark for flagship killers, bringing top-tier gaming performance and genuinely great cameras to an accessible price.',
        'releaseYear': 2023,
        'similarPhones': ['oneplus-12', 'xiaomi-14']
    },
    {
        'id': 'realme-gt-6t',
        'name': 'Realme GT 6T',
        'brand': 'Realme',
        'series': 'GT Series',
        'category': 'flagship-killers',
        'categoryName': 'Flagship Killers',
        'price': 21999,
        'priceFormatted': '₹21,999',
        'antutu': 1210000,
        'antutuFormatted': '1.21M',
        'processor': 'Snapdragon 7+ Gen 3 (4nm)',
        'ram': '8GB LPDDR5X',
        'storage': '128GB UFS 3.1',
        'display': {
            'size': '6.78"',
            'resolution': '2780 x 1264 (1.5K)',
            'type': 'LTPO AMOLED',
            'isFlat': True,
            'refresh': '120Hz',
            'brightness': '6000 nits (peak)',
            'protection': 'Corning Gorilla Glass Victus 2'
        },
        'battery': {
            'capacity': '5500 mAh',
            'capacityNum': 5500,
            'charging': '120W SUPERVOOC',
            'chargingTime': '26 min (0-100%)',
            'wirelessCharging': False
        },
        'camera': {
            'main': '50 MP (f/1.88)',
            'mainSensor': 'Sony LYT-600',
            'ois': True,
            'ultrawide': '8 MP (f/2.2)',
            'telephoto': None,
            'secondary': '8 MP Ultra-Wide',
            'selfie': '32 MP (f/2.45)',
            'video': '4K@60fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'Realme UI 5.0',
            'version': 'Android 14',
            'bloatware': 'Moderate',
            'updates': '3 OS / 4 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': True,
            'wifi': 'Wi-Fi 6',
            'bluetooth': '5.4',
            'infrared': True,
            'usb': 'USB Type-C 2.0'
        },
        'build': {
            'ipRating': 'IP65',
            'weight': '191g',
            'dimensions': '162.0 x 75.1 x 8.6 mm',
            'material': 'Plastic frame, Plastic back'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/realme-gt-6t.webp',
        'isFlat': True,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': False,
        'isCompact': False,
        'ipRating': 'IP65',
        'weight': '191g',
        'highlights': ['Snapdragon 7+ Gen 3', '6000 Nits Display', '5500mAh Battery', '120W Charging'],
        'pros': ['Blazing fast performance for the price', 'Ultra-bright display', 'Huge battery with fast charging'],
        'cons': ['Average camera performance', 'Plastic build', 'Realme UI has bloatware'],
        'editorialVerdict': 'An aggressive budget flagship that dominates in raw performance, battery, and charging speed.',
        'releaseYear': 2024,
        'similarPhones': ['poco-f6', 'oneplus-nord-4']
    },
    {
        'id': 'realme-12-pro-plus',
        'name': 'Realme 12 Pro+',
        'brand': 'Realme',
        'series': 'Number Series',
        'category': 'camera-mavericks',
        'categoryName': 'Camera Mavericks',
        'price': 29999,
        'priceFormatted': '₹29,999',
        'antutu': 720000,
        'antutuFormatted': '720K',
        'processor': 'Snapdragon 7s Gen 2 (4nm)',
        'ram': '8GB LPDDR4X',
        'storage': '128GB UFS 3.1',
        'display': {
            'size': '6.7"',
            'resolution': '2412 x 1080 (FHD+)',
            'type': 'Curved AMOLED',
            'isFlat': False,
            'refresh': '120Hz',
            'brightness': '950 nits (peak)',
            'protection': 'Double-reinforced glass'
        },
        'battery': {
            'capacity': '5000 mAh',
            'capacityNum': 5000,
            'charging': '67W SUPERVOOC',
            'chargingTime': '48 min (0-100%)',
            'wirelessCharging': False
        },
        'camera': {
            'main': '50 MP (f/1.8)',
            'mainSensor': 'Sony IMX890',
            'ois': True,
            'ultrawide': '8 MP (f/2.2)',
            'telephoto': '64 MP 3x Periscope OIS',
            'secondary': '64 MP 3x Periscope OIS + 8 MP Ultra-Wide',
            'selfie': '32 MP (f/2.4)',
            'video': '4K@30fps'
        },
        'audio': {
            'jack35mm': False,
            'stereo': True,
            'speakerDetails': 'Dual Stereo'
        },
        'os': {
            'name': 'Realme UI 5.0',
            'version': 'Android 14',
            'bloatware': 'Moderate',
            'updates': '2 OS / 3 Yrs Security'
        },
        'connectivity': {
            'fiveG': True,
            'nfc': False,
            'wifi': 'Wi-Fi 6',
            'bluetooth': '5.2',
            'infrared': False,
            'usb': 'USB Type-C 2.0'
        },
        'build': {
            'ipRating': 'IP65',
            'weight': '190g',
            'dimensions': '161.5 x 74.0 x 8.7 mm',
            'material': 'Plastic frame, Vegan Leather back'
        },
        'biometrics': 'Optical In-display Fingerprint',
        'imageUrl': 'images/phones/realme-12-pro-plus.webp',
        'isFlat': False,
        'hasJack': False,
        'hasOIS': True,
        'isCleanOS': False,
        'isCompact': False,
        'ipRating': 'IP65',
        'weight': '190g',
        'highlights': ['64MP Periscope Camera', 'Luxury Watch Design', 'Curved Display', 'Vegan Leather'],
        'pros': ['Segment-first 64MP periscope telephoto lens', 'Unique and premium vegan leather design', 'Great portrait photography'],
        'cons': ['Performance is weak for the price', 'Bloatware in Realme UI', 'Screen brightness is a bit low'],
        'editorialVerdict': 'It democratizes periscope zoom cameras, offering flagship-tier portraits wrapped in a striking luxury watch-inspired design.',
        'releaseYear': 2024,
        'similarPhones': ['redmi-note-13-pro-plus', 'vivo-v30-pro']
    }
]

os.makedirs(r"c:\Users\FORAM\Videos\RECONE\data", exist_ok=True)
with open(r"c:\Users\FORAM\Videos\RECONE\data\phones.json", "w", encoding="utf-8") as f:
    json.dump(phones, f, indent=2, ensure_ascii=False)
print("File successfully written with valid JSON and NO trailing commas.")
