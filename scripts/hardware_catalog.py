"""
hardware_catalog.py
Hardware entity dictionary for HackerGear.
Categories:
- keyboard (键盘)
- mouse (鼠标/轨迹球)
- monitor (显示器)
- chair (人体工学椅)
- laptop (笔记本)
"""

CATALOG = [
    # ==========================================
    # KEYBOARDS
    # ==========================================
    {
        "id": "kinesis-advantage",
        "image": "/images/hardware/kinesis-advantage.jpg",
        "name": "Kinesis Advantage 360 / 2",
        "brand": "Kinesis",
        "category": "input",
        "price_tier": "$$$$",
        "tags": ["Split Concave", "Ortholinear", "Endgame Ergonomics", "RSI Relief"],
        "specs": "Contoured concave keywells, orthogonal layout, thumb clusters, mechanical switches, wireless split (360)",
        "patterns": [
            r"\bkinesis\s+advantage\b",
            r"\badvantage\s*360\b",
            r"\badvantage\s*2\b",
            r"\bkinesis\s*360\b"
        ],
        "primary_keyword": "Kinesis Advantage"
    },
    {
        "id": "zsa-moonlander",
        "image": "/images/hardware/zsa-moonlander.webp",
        "name": "ZSA Moonlander",
        "brand": "ZSA",
        "category": "input",
        "price_tier": "$$$$",
        "tags": ["Split Ergonomic", "Columnar", "Hot-swappable", "Open Source Firmware"],
        "specs": "Split columnar layout, thumb clusters, customizable tenting, RGB backlight, Oryx web configurator",
        "patterns": [
            r"\bmoonlander\b",
            r"\bzsa\s+moonlander\b"
        ],
        "primary_keyword": "Moonlander"
    },
    {
        "id": "zsa-voyager",
        "image": "/images/hardware/zsa-voyager.webp",
        "name": "ZSA Voyager",
        "brand": "ZSA",
        "category": "input",
        "price_tier": "$$$$",
        "tags": ["Ultra-thin Split", "Low Profile", "Travel Friendly", "Choc Switches"],
        "specs": "Low-profile mechanical split keyboard, magnetic tripod mounting, Kailh Choc switches, compact 52 keys",
        "patterns": [
            r"\bzsa\s+voyager\b",
            r"\bvoyager\s+keyboard\b"
        ],
        "primary_keyword": "ZSA Voyager"
    },
    {
        "id": "hhkb-professional",
        "image": "/images/hardware/hhkb-professional.jpg",
        "name": "HHKB Professional (Classic / Hybrid)",
        "brand": "Happy Hacking",
        "category": "input",
        "price_tier": "$$$",
        "tags": ["Topre Electrostatic", "60% Minimalist", "Unix Control Key", "Cult Classic"],
        "specs": "Topre capacitive switches (45g), customized UNIX layout with Control next to 'A', Bluetooth & USB-C",
        "patterns": [
            r"\bhhkb\b",
            r"\bhappy\s+hacking\s+keyboard\b",
            r"\bhhkb\s+hybrid\b",
            r"\bhhkb\s+pro\b"
        ],
        "primary_keyword": "HHKB"
    },
    {
        "id": "keychron-q-series",
        "image": "/images/hardware/keychron-q-series.webp",
        "name": "Keychron Q / V Series (Q1/Q2/Q3/V1)",
        "brand": "Keychron",
        "category": "input",
        "price_tier": "$$",
        "tags": ["Custom Mechanical", "Gasket Mount", "QMK/VIA", "High Value"],
        "specs": "CNC aluminum chassis (Q) or ABS (V), double-gasket mount, hot-swappable, full Mac/Windows support",
        "patterns": [
            r"\bkeychron\s+[qv]\d+\b",
            r"\bkeychron\s+q-series\b",
            r"\bkeychron\s+q\b",
            r"\bkeychron\s+k\d+\b",
            r"\bkeychron\b"
        ],
        "primary_keyword": "Keychron"
    },
    {
        "id": "ergodox-ez",
        "image": "/images/hardware/ergodox-ez.webp",
        "name": "Ergodox EZ",
        "brand": "ZSA",
        "category": "input",
        "price_tier": "$$$$",
        "tags": ["Split Ergonomic", "Columnar", "Tenting Kit", "Wrist Rests"],
        "specs": "Split mechanical layout, adjustable metal tenting legs, sculpted keycaps, QMK firmware",
        "patterns": [
            r"\bergodox\b",
            r"\bergodox\s+ez\b"
        ],
        "primary_keyword": "Ergodox"
    },
    {
        "id": "glove80",
        "image": "/images/hardware/glove80.webp",
        "name": "MoErgo Glove80",
        "brand": "MoErgo",
        "category": "input",
        "price_tier": "$$$$",
        "tags": ["Curved Keywells", "Wireless Split", "Low Profile Choc", "RSI Savior"],
        "specs": "Ultra-ergonomic 80-key contoured keywell layout, low-profile switches, thumb cluster, Bluetooth BLE",
        "patterns": [
            r"\bglove80\b",
            r"\bmoergo\s+glove80\b"
        ],
        "primary_keyword": "Glove80"
    },
    {
        "id": "corne-split",
        "image": "/images/hardware/corne-split.jpg",
        "name": "Corne / CRKBD (Custom Split)",
        "brand": "Open Source",
        "category": "input",
        "price_tier": "$$",
        "tags": ["40% Minimalist", "DIY Open Source", "OLED Screen", "Ultra Compact"],
        "specs": "42-key or 36-key split columnar keyboard, designed by foostan, OLED displays, ultra-portable",
        "patterns": [
            r"\bcorne\s+keyboard\b",
            r"\bcrkbd\b",
            r"\bcorne\b"
        ],
        "primary_keyword": "Corne keyboard"
    },

    # ==========================================
    # MICE & POINTING DEVICES
    # ==========================================
    {
        "id": "logitech-mx-master-3s",
        "image": "/images/hardware/logitech-mx-master-3s.jpg",
        "name": "Logitech MX Master 3S / 3",
        "brand": "Logitech",
        "category": "input",
        "price_tier": "$$",
        "tags": ["MagSpeed Wheel", "Ergonomic Contour", "Thumb Wheel", "Multi-Device Flow"],
        "specs": "Quiet Click electromagnetic wheel (1,000 lines/sec), 8K DPI sensor, horizontal thumb wheel, USB-C",
        "patterns": [
            r"\bmx\s+master\s+3s\b",
            r"\bmx\s+master\s+3\b",
            r"\bmx\s+master\b",
            r"\blogitech\s+mx\s+master\b"
        ],
        "primary_keyword": "MX Master 3S"
    },
    {
        "id": "apple-magic-trackpad",
        "image": "/images/hardware/apple-magic-trackpad.jpg",
        "name": "Apple Magic Trackpad",
        "brand": "Apple",
        "category": "input",
        "price_tier": "$$",
        "tags": ["Glass Surface", "macOS Gestures", "Force Touch", "Zero Wrist Twist"],
        "specs": "Large edge-to-edge glass multi-touch surface, Force Touch haptic click, seamless macOS gesture control",
        "patterns": [
            r"\bmagic\s+trackpad\b",
            r"\bapple\s+trackpad\b"
        ],
        "primary_keyword": "Magic Trackpad"
    },
    {
        "id": "logitech-mx-vertical-lift",
        "image": "/images/hardware/logitech-mx-vertical-lift.jpg",
        "name": "Logitech Lift / MX Vertical",
        "brand": "Logitech",
        "category": "input",
        "price_tier": "$$",
        "tags": ["Vertical Ergonomic", "57-Degree Angle", "Carpal Relief", "SmartWheel"],
        "specs": "57-degree natural handshake angle to relieve wrist pronation, quiet clicks, textured grip",
        "patterns": [
            r"\blogitech\s+lift\b",
            r"\bmx\s+vertical\b",
            r"\blift\s+vertical\b",
            r"\blogitech\s+vertical\b"
        ],
        "primary_keyword": "Logitech Lift"
    },
    {
        "id": "kensington-slimblade-expert",
        "image": "/images/hardware/kensington-slimblade-expert.jpg",
        "name": "Kensington SlimBlade Pro / Expert Mouse",
        "brand": "Kensington",
        "category": "input",
        "price_tier": "$$",
        "tags": ["Large Trackball", "Dual Twist Scrolling", "Zero Arm Movement", "Stationary"],
        "specs": "55mm large optical trackball, twist-ball scrolling, ambidextrous design, wireless dual-mode",
        "patterns": [
            r"\bslimblade\b",
            r"\bkensington\s+slimblade\b",
            r"\bkensington\s+expert\b",
            r"\bexpert\s+mouse\b"
        ],
        "primary_keyword": "Kensington SlimBlade"
    },
    {
        "id": "logitech-mx-ergo",
        "image": "/images/hardware/logitech-mx-ergo.png",
        "name": "Logitech MX Ergo",
        "brand": "Logitech",
        "category": "input",
        "price_tier": "$$",
        "tags": ["Thumb Trackball", "Adjustable 20° Hinge", "Precision Mode", "Comfort Grip"],
        "specs": "Adjustable magnetic plate (0° or 20° tilt), thumb-operated trackball, precision button for cursor speed",
        "patterns": [
            r"\bmx\s+ergo\b",
            r"\blogitech\s+ergo\s+trackball\b"
        ],
        "primary_keyword": "MX Ergo"
    },

    # ==========================================
    # MONITORS
    # ==========================================
    {
        "id": "dell-ultrasharp-4k",
        "image": "/images/hardware/dell-ultrasharp-4k.png",
        "name": "Dell UltraSharp 4K (U2723QE / U3223QE)",
        "brand": "Dell",
        "category": "monitor",
        "price_tier": "$$$",
        "tags": ["IPS Black", "90W USB-C Hub", "2000:1 Contrast", "Built-in KVM"],
        "specs": "27\" or 32\" 4K (3840x2160) IPS Black panel, 98% DCI-P3, RJ45 Ethernet, built-in KVM and USB-C hub",
        "patterns": [
            r"\bu2723qe\b",
            r"\bu3223qe\b",
            r"\bdell\s+ultrasharp\b",
            r"\bultrasharp\s+4k\b",
            r"\bdell\s+u\d{4}\w*\b"
        ],
        "primary_keyword": "Dell UltraSharp"
    },
    {
        "id": "apple-studio-display",
        "image": "/images/hardware/apple-studio-display.jpg",
        "name": "Apple Studio Display 27\" 5K",
        "brand": "Apple",
        "category": "monitor",
        "price_tier": "$$$$",
        "tags": ["5K Retina 218 PPI", "600 Nits", "A13 Bionic", "6-Speaker Array"],
        "specs": "27-inch 5120x2880 5K Retina display, true 218 PPI for crisp macOS scaling, Center Stage 12MP camera",
        "patterns": [
            r"\bstudio\s+display\b",
            r"\bapple\s+studio\s+display\b"
        ],
        "primary_keyword": "Apple Studio Display"
    },
    {
        "id": "lg-c3-c4-oled-42",
        "image": "/images/hardware/lg-c3-c4-oled-42.jpg",
        "name": "LG OLED C3 / C4 (42\" / 48\")",
        "brand": "LG",
        "category": "monitor",
        "price_tier": "$$$",
        "tags": ["4K OLED", "Infinite Contrast", "120Hz/144Hz", "Developer Megascreen"],
        "specs": "Self-lit OLED evo panel, true black, 0.1ms response time, 4x HDMI 2.1, immersive desktop canvas",
        "patterns": [
            r"\blg\s+c3\b",
            r"\blg\s+c4\b",
            r"\blg\s+c2\b",
            r"\blg\s+oled\s+42\b",
            r"\boled\s+42\b"
        ],
        "primary_keyword": "LG OLED C3/C4"
    },
    {
        "id": "lg-ultrafine-5k-4k",
        "image": "/images/hardware/lg-ultrafine-5k-4k.jpg",
        "name": "LG UltraFine 5K (27MD5KL)",
        "brand": "LG",
        "category": "monitor",
        "price_tier": "$$$$",
        "tags": ["5K Thunderbolt 3", "macOS Native Controls", "218 PPI", "DCI-P3 99%"],
        "specs": "27-inch 5120x2880 IPS panel, Thunderbolt 3 single-cable connection, native macOS brightness/volume control",
        "patterns": [
            r"\bultrafine\s+5k\b",
            r"\blg\s+ultrafine\b"
        ],
        "primary_keyword": "LG UltraFine 5K"
    },
    {
        "id": "asus-proart-4k",
        "image": "/images/hardware/asus-proart-4k.png",
        "name": "ASUS ProArt Display (PA279CRV / PA329CRV)",
        "brand": "ASUS",
        "category": "monitor",
        "price_tier": "$$",
        "tags": ["Color Accurate", "Calman Verified", "96W USB-C", "Budget 4K Workhorse"],
        "specs": "4K UHD IPS panel, Delta E < 2 factory calibration, 96W USB-C Power Delivery, DisplayPort daisy-chain",
        "patterns": [
            r"\bproart\b",
            r"\basus\s+proart\b",
            r"\bpa279crv\b"
        ],
        "primary_keyword": "ASUS ProArt"
    },

    # ==========================================
    # CHAIRS & ERGONOMICS
    # ==========================================
    {
        "id": "herman-miller-aeron",
        "image": "/images/hardware/herman-miller-aeron.jpg",
        "name": "Herman Miller Aeron (Remastered)",
        "brand": "Herman Miller",
        "category": "furniture",
        "price_tier": "$$$$",
        "tags": ["Pellicle Mesh", "PostureFit SL", "Iconic Benchmark", "12-Year Warranty"],
        "specs": "8Z Pellicle breathable suspension mesh, dual PostureFit SL sacral/lumbar support, forward tilt, sizes A/B/C",
        "patterns": [
            r"\baeron\b",
            r"\bherman\s+miller\s+aeron\b",
            r"\bhm\s+aeron\b"
        ],
        "primary_keyword": "Herman Miller Aeron"
    },
    {
        "id": "herman-miller-embody",
        "image": "/images/hardware/herman-miller-embody.jpg",
        "name": "Herman Miller Embody (Logitech Edition)",
        "brand": "Herman Miller",
        "category": "furniture",
        "price_tier": "$$$$",
        "tags": ["Pixelated Support", "Dynamic Spine", "Active Sitting", "Upper Back Freedom"],
        "specs": "Matrix of pixels that automatically conforms to micro-movements, BackFit adjustment, copper cooling foam",
        "patterns": [
            r"\bherman\s+miller\s+embody\b",
            r"\blogitech\s+embody\b",
            r"\bembody\s+(chair|seat|gaming)\b",
            r"\bhm\s+embody\b"
        ],
        "primary_keyword": "Herman Miller Embody"
    },
    {
        "id": "steelcase-leap-v2",
        "image": "/images/hardware/steelcase-leap-v2.webp",
        "name": "Steelcase Leap V2",
        "brand": "Steelcase",
        "category": "furniture",
        "price_tier": "$$$$",
        "tags": ["LiveBack Technology", "4D Armrests", "Adjustable Lower Back Firmness", "Universal Comfort"],
        "specs": "LiveBack changes shape to support entire spine, natural glide system, legendary 4D multi-directional armrests",
        "patterns": [
            r"\bleap\s+v2\b",
            r"\bsteelcase\s+leap\b",
            r"\bsteelcase\s+leap\s+v2\b"
        ],
        "primary_keyword": "Steelcase Leap V2"
    },
    {
        "id": "steelcase-gesture",
        "image": "/images/hardware/steelcase-gesture.webp",
        "name": "Steelcase Gesture",
        "brand": "Steelcase",
        "category": "furniture",
        "price_tier": "$$$$",
        "tags": ["360° Rotating Arms", "Mobile Device Ergonomics", "Core Equalizer", "Flexible Perimeter"],
        "specs": "Designed for multi-device postures (laptop, phone, tablet), 360-degree rotating arms, contoured back",
        "patterns": [
            r"\bsteelcase\s+gesture\b",
            r"\bgesture\s+chair\b"
        ],
        "primary_keyword": "Steelcase Gesture"
    },
    {
        "id": "haworth-fern",
        "image": "/images/hardware/haworth-fern.jpg",
        "name": "Haworth Fern",
        "brand": "Haworth",
        "category": "furniture",
        "price_tier": "$$$$",
        "tags": ["Wave Suspension", "Frameless Back", "Deep Recline", "Edgeless Flexibility"],
        "specs": "Frond-inspired suspension structure without a rigid outer frame, 4-point active lumbar, edgeless comfort",
        "patterns": [
            r"\bhaworth\s+fern\b",
            r"\bfern\s+chair\b"
        ],
        "primary_keyword": "Haworth Fern"
    },

    # ==========================================
    # LAPTOPS
    # ==========================================
    {
        "id": "apple-macbook-pro-m-series",
        "image": "/images/hardware/apple-macbook-pro-m-series.png",
        "name": "Apple MacBook Pro 14\" / 16\" (M3 / M4 / M2 / M1)",
        "brand": "Apple",
        "category": "computer",
        "price_tier": "$$$$",
        "tags": ["Apple Silicon", "Liquid Retina XDR", "22h Battery", "Silent Dev Machine"],
        "specs": "Apple M-Series chips (M1/M2/M3/M4 Pro/Max), mini-LED 120Hz ProMotion screen, unified memory up to 128GB, quiet fans",
        "patterns": [
            r"\bmacbook\s+pro\s+m[1234]\b",
            r"\bm[1234]\s+macbook\s+pro\b",
            r"\bm[1234]\s+pro\b",
            r"\bm[1234]\s+max\b",
            r"\bmacbook\s+pro\s+(14|16)\b",
            r"\bapple\s+silicon\s+macbook\b"
        ],
        "primary_keyword": "MacBook Pro M"
    },
    {
        "id": "framework-laptop-13-16",
        "image": "/images/hardware/framework-laptop-13-16.webp",
        "name": "Framework Laptop 13 / 16",
        "brand": "Framework",
        "category": "computer",
        "price_tier": "$$$",
        "tags": ["Modular Repairable", "Right to Repair", "Swappable Expansion Cards", "Linux Champion"],
        "specs": "100% user-repairable with QR codes, modular USB-C/HDMI/Storage expansion bays, Intel Core Ultra or AMD Ryzen 7040/8040",
        "patterns": [
            r"\bframework\s+laptop\b",
            r"\bframework\s+13\b",
            r"\bframework\s+16\b",
            r"\bframework\s+(12|13|16)\b"
        ],
        "primary_keyword": "Framework Laptop"
    },
    {
        "id": "thinkpad-x1-carbon",
        "image": "/images/hardware/thinkpad-x1-carbon.jpg",
        "name": "Lenovo ThinkPad X1 Carbon (Gen 11 / 12)",
        "brand": "Lenovo",
        "category": "computer",
        "price_tier": "$$$$",
        "tags": ["TrackPoint Red Dot", "Carbon Fiber", "1.1kg Featherweight", "First-Class Linux"],
        "specs": "Ultralight carbon-fiber reinforced magnesium body, 2.8K OLED option, legendary ThinkPad keyboard, official Linux support",
        "patterns": [
            r"\bx1\s+carbon\b",
            r"\bthinkpad\s+x1\b",
            r"\bthinkpad\s+x1\s+carbon\b"
        ],
        "primary_keyword": "ThinkPad X1 Carbon"
    },
    {
        "id": "thinkpad-t-series",
        "image": "/images/hardware/thinkpad-t-series.jpg",
        "name": "Lenovo ThinkPad T14 / T14s (AMD / Intel)",
        "brand": "Lenovo",
        "category": "computer",
        "price_tier": "$$",
        "tags": ["Enterprise Workhorse", "Modular RAM (Gen 5)", "Durable Military-Spec", "Linux Native"],
        "specs": "Corporate standard workhorse, user-replaceable SODIMM modules (Gen 5), AMD Ryzen Pro APU, rugged Mil-SPEC durability",
        "patterns": [
            r"\bthinkpad\s+t14\b",
            r"\bthinkpad\s+t14s\b",
            r"\bt14s\b",
            r"\bt14\s+amd\b",
            r"\bthinkpad\s+t480\b"
        ],
        "primary_keyword": "ThinkPad T14"
    },
    {
        "id": "asus-rog-zephyrus-g14",
        "image": "/images/hardware/asus-rog-zephyrus-g14.png",
        "name": "ASUS ROG Zephyrus G14 (OLED)",
        "brand": "ASUS",
        "category": "computer",
        "price_tier": "$$$",
        "tags": ["OLED 120Hz", "AMD Ryzen + RTX", "CNC Aluminum", "Portable Powerhouse"],
        "specs": "14\" 3K 120Hz OLED, AMD Ryzen 9 + NVIDIA RTX 4070, unibody CNC aluminum, 1.5kg portable workstation",
        "patterns": [
            r"\bzephyrus\s+g14\b",
            r"\brog\s+zephyrus\b",
            r"\bg14\s+oled\b"
        ],
        "primary_keyword": "Zephyrus G14"
    },

    # ==========================================
    # AUDIO & HEADPHONES (耳机/音频)
    # ==========================================
    {
        "id": "sony-wh1000xm",
        "image": "/images/hardware/sony-wh1000xm.jpg",
        "name": "Sony WH-1000XM4 / XM5",
        "brand": "Sony",
        "category": "audio",
        "price_tier": "$$$",
        "tags": ["Industry-Leading ANC", "30h Battery Life", "Multipoint Bluetooth", "LDAC Hi-Res"],
        "specs": "Custom QN1 HD Noise Cancelling Processor, 30mm carbon composite drivers, 30-hour battery, speak-to-chat",
        "patterns": [
            r"\bwh[- ]?1000xm[45]\b",
            r"\bsony\s+1000xm[45]\b",
            r"\bsony\s+wh\s*1000\b"
        ],
        "primary_keyword": "Sony WH-1000XM"
    },
    {
        "id": "airpods-pro-max",
        "image": "/images/hardware/airpods-pro-max.jpg",
        "name": "Apple AirPods Pro (Gen 2) / Max",
        "brand": "Apple",
        "category": "audio",
        "price_tier": "$$$",
        "tags": ["Apple Ecosystem", "Adaptive Audio", "Transparency Mode", "H2 Silicon"],
        "specs": "Apple H2/H1 chip, best-in-class Transparency Mode, Personalized Spatial Audio with dynamic head tracking, USB-C case",
        "patterns": [
            r"\bairpods\s+pro\s*(2|gen\s*2)?\b",
            r"\bairpods\s+max\b",
            r"\bairpod\s+pro\b"
        ],
        "primary_keyword": "AirPods Pro"
    },
    {
        "id": "bose-quietcomfort",
        "image": "/images/hardware/bose-quietcomfort.jpg",
        "name": "Bose QuietComfort 45 / Ultra",
        "brand": "Bose",
        "category": "audio",
        "price_tier": "$$$",
        "tags": ["All-Day Ergonomic Fit", "Deep Noise Isolation", "Ultra-Lightweight", "Physical Buttons"],
        "specs": "Legendary all-day comfort, plush synthetic leather ear cushions, minimal clamp force, CustomTune audio calibration",
        "patterns": [
            r"\bbose\s+qc\s*(35|45|ultra)\b",
            r"\bquietcomfort\s*(35|45|ultra)\b",
            r"\bbose\s+quietcomfort\b"
        ],
        "primary_keyword": "Bose QuietComfort"
    },
    {
        "id": "sennheiser-hd600",
        "image": "/images/hardware/sennheiser-hd600.jpg",
        "name": "Sennheiser HD 600 / 650",
        "brand": "Sennheiser",
        "category": "audio",
        "price_tier": "$$$",
        "tags": ["Audiophile Standard", "Open-Back Acoustic", "Natural Vocal Timbre", "300 Ohm Dynamic"],
        "specs": "Open dynamic acoustic design, 300 ohm impedance, detachable OFC copper cable, legendary neutral frequency response",
        "patterns": [
            r"\bsennheiser\s+hd\s*6[05]0\b",
            r"\bhd\s*6[05]0\b",
            r"\bhd600\b",
            r"\bhd650\b"
        ],
        "primary_keyword": "Sennheiser HD 600"
    },
    {
        "id": "shure-sm7b-mv7",
        "image": "/images/hardware/shure-sm7b-mv7.jpg",
        "name": "Shure SM7B / MV7",
        "brand": "Shure",
        "category": "audio",
        "price_tier": "$$$",
        "tags": ["Broadcast Benchmark", "Cardioid Dynamic", "Air Suspension Shock", "Electromagnetic Shielding"],
        "specs": "Dynamic broadcast microphone, flat wide-range frequency response, bass rolloff and mid-range presence boost controls",
        "patterns": [
            r"\bshure\s+(sm7b|mv7[x]?)\b",
            r"\bsm7b\b",
            r"\bshure\s+sm\s*7\b",
            r"\bmv7\s+mic\b"
        ],
        "primary_keyword": "Shure SM7B"
    },

    # ==========================================
    # DESK & WORKSPACE ACCESSORIES (桌面配件/工效周边)
    # ==========================================
    {
        "id": "caldigit-ts4",
        "image": "/images/hardware/caldigit-ts4.jpg",
        "name": "CalDigit TS4 / TS3 Plus Thunderbolt Dock",
        "brand": "CalDigit",
        "category": "furniture",
        "price_tier": "$$$$",
        "tags": ["18-in-1 Ports", "Thunderbolt 4", "98W Power Delivery", "Single-Cable Setup"],
        "specs": "18 ports of connectivity, 98W host charging, 2.5GbE Ethernet, UHS-II SD card slot, dual 6K 60Hz display support",
        "patterns": [
            r"\bcaldigit\s+ts[34]\b",
            r"\bts4\s+dock\b",
            r"\bcaldigit\s+dock\b",
            r"\bts4\s+thunderbolt\b"
        ],
        "primary_keyword": "CalDigit TS4"
    },
    {
        "id": "benq-screenbar",
        "image": "/images/hardware/benq-screenbar.jpg",
        "name": "BenQ ScreenBar / Halo Monitor Light",
        "brand": "BenQ",
        "category": "furniture",
        "price_tier": "$$",
        "tags": ["Zero Screen Glare", "Asymmetrical Optics", "Auto-Dimming", "Desk Space Saver"],
        "specs": "Patented clamp fits curved and flat displays, asymmetrical optical design, ambient light sensor, wireless desktop dial (Halo)",
        "patterns": [
            r"\b(benq\s+)?screenbar(\s+halo|\s+plus)?\b",
            r"\bbenq\s+monitor\s+light\b"
        ],
        "primary_keyword": "BenQ ScreenBar"
    },
    {
        "id": "ergotron-lx",
        "image": "/images/hardware/ergotron-lx.jpg",
        "name": "Ergotron LX / HX Monitor Arm",
        "brand": "Ergotron",
        "category": "furniture",
        "price_tier": "$$$",
        "tags": ["Constant Force Tech", "Heavy-Duty Steel", "Smooth 360 Rotation", "10-Year Warranty"],
        "specs": "Constant Force lift and pivot technology, polished aluminum construction, holds up to 34\" displays (42\" with HX), integrated cable routing",
        "patterns": [
            r"\bergotron\s+(lx|hx)\b",
            r"\bergotron\s+arm\b",
            r"\bergotron\s+monitor\s+arm\b"
        ],
        "primary_keyword": "Ergotron LX"
    },
    {
        "id": "uplift-v2-fully",
        "image": "/images/hardware/uplift-v2-fully.png",
        "name": "Uplift V2 / Fully Jarvis Standing Desk",
        "brand": "Uplift",
        "category": "furniture",
        "price_tier": "$$$$",
        "tags": ["Dual Motor", "Anti-Collision", "Solid Wood Tops", "Rock-Solid Stability"],
        "specs": "Three-stage inverted legs, dual German motors, 355-lb lifting capacity, digital memory keypad, 15-year warranty",
        "patterns": [
            r"\buplift\s+v2\b",
            r"\buplift\s+desk\b",
            r"\bfully\s+jarvis\b",
            r"\bjarvis\s+standing\s+desk\b"
        ],
        "primary_keyword": "Uplift V2 Standing Desk"
    },

    # ==========================================
    # MINI PCS & HOMELAB (小主机/迷你服务器/单板机)
    # ==========================================
    {
        "id": "apple-mac-mini",
        "image": "/images/hardware/apple-mac-mini.png",
        "name": "Apple Mac mini (M-Series)",
        "brand": "Apple",
        "category": "computer",
        "price_tier": "$$$",
        "tags": ["Apple Silicon", "Whisper-Quiet", "Compact 5x5 Footprint", "Always-On Server"],
        "specs": "M2 / M4 / M4 Pro chips, unified memory architecture, 10GbE option, thermal architecture engineered for sustained high workloads",
        "patterns": [
            r"\bmac\s+mini\s*(m[1-4](\s+pro)?)?\b",
            r"\bm[1-4]\s+mac\s+mini\b",
            r"\bapple\s+mac\s+mini\b"
        ],
        "primary_keyword": "Mac mini"
    },
    {
        "id": "raspberry-pi-5",
        "image": "/images/hardware/raspberry-pi-5.jpg",
        "name": "Raspberry Pi 5 / 4",
        "brand": "Raspberry Pi",
        "category": "computer",
        "price_tier": "$",
        "tags": ["Single Board Computer", "PCIe 2.0 Interface", "GPIO Ecosystem", "Low Power Homelab"],
        "specs": "Broadcom BCM2712 quad-core Arm Cortex-A76 @ 2.4GHz, VideoCore VII GPU, single-lane PCIe 2.0 interface, dual 4Kp60 micro-HDMI",
        "patterns": [
            r"\braspberry\s+pi\s*[45]\b",
            r"\brpi\s*[45]\b",
            r"\braspberry\s+pi\s*5\b"
        ],
        "primary_keyword": "Raspberry Pi 5"
    },
    {
        "id": "intel-nuc",
        "image": "/images/hardware/intel-nuc.jpg",
        "name": "Intel NUC Mini PC",
        "brand": "Intel",
        "category": "computer",
        "price_tier": "$$",
        "tags": ["x86 Homelab Workhorse", "Dual NICs", "Proxmox / ESXi Ready", "Compact 4x4"],
        "specs": "Intel Core i5/i7 mobile processors, dual DDR4/DDR5 SO-DIMM slots, dual M.2 NVMe slots, ultra-compact form factor",
        "patterns": [
            r"\bintel\s+nuc\b",
            r"\bnuc\s+(mini\s+pc|box|kit|extreme|server)\b",
            r"\bnuc\s*1[123]\b"
        ],
        "primary_keyword": "Intel NUC"
    },
    {
        "id": "minisforum-beelink",
        "image": "/images/hardware/minisforum-beelink.jpg",
        "name": "Minisforum / Beelink Mini PC",
        "brand": "Minisforum",
        "category": "computer",
        "price_tier": "$$",
        "tags": ["AMD Ryzen Zen 4", "RDNA3 Radeon 780M", "Oculink eGPU", "High Value"],
        "specs": "AMD Ryzen 7/9 mobile APUs, dual 2.5GbE LAN, liquid metal cooling, dual PCIe 4.0 NVMe slots, compact CNC metal chassis",
        "patterns": [
            r"\bminisforum\b",
            r"\bbeelink\s+(mini\s+pc|ser[5-8]|eqr6|gtr)\b",
            r"\bum7[89]0\b"
        ],
        "primary_keyword": "Minisforum Mini PC"
    },

    # ==========================================
    # NETWORKING & STORAGE (网络与存储设备)
    # ==========================================
    {
        "id": "ubiquiti-unifi",
        "image": "/images/hardware/ubiquiti-unifi.png",
        "name": "Ubiquiti UniFi (Cloud Gateway / AP)",
        "brand": "Ubiquiti",
        "category": "network",
        "price_tier": "$$$",
        "tags": ["Enterprise SDN", "Cloud Gateway Ultra", "VLAN / IDS / IPS", "PoE WiFi 6/7"],
        "specs": "Centralized UniFi Network Controller, hardware deep packet inspection (DPI), high-throughput PoE access points, rackmount / desktop form factors",
        "patterns": [
            r"\bunifi\s+(dream\s+machine|udm|router|ap|protect|switch|cloud\s+gateway)\b",
            r"\bubiquiti\s+unifi\b",
            r"\bunifi\s+ap\b"
        ],
        "primary_keyword": "Ubiquiti UniFi"
    },
    {
        "id": "synology-nas",
        "image": "/images/hardware/synology-nas.jpg",
        "name": "Synology DiskStation (DS920+ / DS923+)",
        "brand": "Synology",
        "category": "network",
        "price_tier": "$$$",
        "tags": ["DSM Operating System", "Btrfs Snapshots", "Docker / Container Manager", "4-Bay RAID"],
        "specs": "4-drive bays, AMD Ryzen R1600 / Intel Celeron, ECC RAM expandable to 32GB, dual M.2 NVMe cache slots, DSM automated backup suite",
        "patterns": [
            r"\bsynology(\s+nas)?\b",
            r"\bdiskstation\b",
            r"\bds92[03]\+\b",
            r"\bds22[04]\+\b"
        ],
        "primary_keyword": "Synology NAS"
    }
,
    # ==========================================
    # MOBILE & TABLETS (手机与平板移动设备)
    # ==========================================
    {
        "id": "google-pixel",
        "image": "/images/hardware/google-pixel.jpg",
        "name": "Google Pixel 8 / 9 (GrapheneOS)",
        "brand": "Google",
        "category": "mobile",
        "price_tier": "7874$",
        "tags": ["GrapheneOS Hardened", "Titan M2 Security", "Zero Bloatware", "Pure Android"],
        "specs": "Google Tensor G3/G4 with Titan M2 security coprocessor, hardware security sandbox, officially recommended device for GrapheneOS",
        "patterns": [
            r"\bgoogle\s+pixel\b",
            r"\bpixel\s+[89]\b",
            r"\bgrapheneos\b",
            r"\bpixel\s+8\s*pro\b",
            r"\bpixel\s+9\s*pro\b"
        ],
        "primary_keyword": "Google Pixel"
    },
    {
        "id": "apple-iphone-pro",
        "image": "/images/hardware/apple-iphone-pro.jpg",
        "name": "Apple iPhone 15 Pro / 16 Pro",
        "brand": "Apple",
        "category": "mobile",
        "price_tier": "78747874",
        "tags": ["USB-C 10Gbps", "Titanium Frame", "A17/A18 Pro", "6-Year Support"],
        "specs": "Grade 5 Titanium enclosure, USB-C with 10Gbps transfer speeds, ProMotion 120Hz OLED, hardware-accelerated ray tracing, 6+ years iOS support",
        "patterns": [
            r"\biphone\s+(15|16)\s+pro\b",
            r"\biphone\s+1[56]\b",
            r"\biphone\s+pro\s+max\b"
        ],
        "primary_keyword": "iPhone Pro"
    },
    {
        "id": "apple-ipad-pro",
        "image": "/images/hardware/apple-ipad-pro.png",
        "name": "Apple iPad Pro (M-Series)",
        "brand": "Apple",
        "category": "mobile",
        "price_tier": "78747874",
        "tags": ["Ultra Retina XDR", "Apple M4 / M2", "Magic Keyboard", "Remote Dev Terminal"],
        "specs": "Tandem OLED Ultra Retina XDR display, Apple M2/M4 silicon, Thunderbolt port, paired with Magic Keyboard and SSH/Termius/Blink Shell for remote dev",
        "patterns": [
            r"\bipad\s+pro\b",
            r"\bm[124]\s+ipad\b",
            r"\bipad\s+pro\s+(11|13|12\.9)\b"
        ],
        "primary_keyword": "iPad Pro"
    },
    {
        "id": "remarkable-2",
        "image": "/images/hardware/remarkable-2.jpg",
        "name": "reMarkable 2 E-Ink Tablet",
        "brand": "reMarkable",
        "category": "mobile",
        "price_tier": "7874$",
        "tags": ["Distraction-Free", "Paper-Like Feel", "Linux Hackable", "Weeks Battery Life"],
        "specs": "10.3-inch monochrome digital paper display, 4.7mm ultrathin body, 21ms latency Canvas display, Linux-based Codex OS with SSH root access",
        "patterns": [
            r"\bremarkable\s*2\b",
            r"\bremarkable\s+tablet\b",
            r"\bremarkable\s+paper\b"
        ],
        "primary_keyword": "reMarkable 2"
    }
]
