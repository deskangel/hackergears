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
        "category": "keyboard",
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
        "category": "keyboard",
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
        "category": "keyboard",
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
        "category": "keyboard",
        "price_tier": "$$$",
        "tags": ["Topre Electrostatic", "60% Minimalist", "Unix Control Key", "Cult Classic"],
        "specs": "Topre capacitive switches (45g), customized UNIX layout with Control next to 'A', Bluetooth & USB-C",
        "patterns": [
            r"\bhhkb\b",
            r"\bhappy\s+hacking\b",
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
        "category": "keyboard",
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
        "category": "keyboard",
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
        "category": "keyboard",
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
        "category": "keyboard",
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
        "category": "mouse",
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
        "category": "mouse",
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
        "category": "mouse",
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
        "category": "mouse",
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
        "image": "/images/hardware/logitech-mx-ergo.webp",
        "name": "Logitech MX Ergo",
        "brand": "Logitech",
        "category": "mouse",
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
        "category": "chair",
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
        "category": "chair",
        "price_tier": "$$$$",
        "tags": ["Pixelated Support", "Dynamic Spine", "Active Sitting", "Upper Back Freedom"],
        "specs": "Matrix of pixels that automatically conforms to micro-movements, BackFit adjustment, copper cooling foam",
        "patterns": [
            r"\bembody\b",
            r"\bherman\s+miller\s+embody\b",
            r"\blogitech\s+embody\b"
        ],
        "primary_keyword": "Herman Miller Embody"
    },
    {
        "id": "steelcase-leap-v2",
        "image": "/images/hardware/steelcase-leap-v2.webp",
        "name": "Steelcase Leap V2",
        "brand": "Steelcase",
        "category": "chair",
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
        "category": "chair",
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
        "category": "chair",
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
        "category": "laptop",
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
        "image": "/images/hardware/framework-laptop-13-16.jpg",
        "name": "Framework Laptop 13 / 16",
        "brand": "Framework",
        "category": "laptop",
        "price_tier": "$$$",
        "tags": ["Modular Repairable", "Right to Repair", "Swappable Expansion Cards", "Linux Champion"],
        "specs": "100% user-repairable with QR codes, modular USB-C/HDMI/Storage expansion bays, Intel Core Ultra or AMD Ryzen 7040/8040",
        "patterns": [
            r"\bframework\s+laptop\b",
            r"\bframework\s+13\b",
            r"\bframework\s+16\b",
            r"\bframework\b"
        ],
        "primary_keyword": "Framework Laptop"
    },
    {
        "id": "thinkpad-x1-carbon",
        "image": "/images/hardware/thinkpad-x1-carbon.jpg",
        "name": "Lenovo ThinkPad X1 Carbon (Gen 11 / 12)",
        "brand": "Lenovo",
        "category": "laptop",
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
        "category": "laptop",
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
        "category": "laptop",
        "price_tier": "$$$",
        "tags": ["OLED 120Hz", "AMD Ryzen + RTX", "CNC Aluminum", "Portable Powerhouse"],
        "specs": "14\" 3K 120Hz OLED, AMD Ryzen 9 + NVIDIA RTX 4070, unibody CNC aluminum, 1.5kg portable workstation",
        "patterns": [
            r"\bzephyrus\s+g14\b",
            r"\brog\s+zephyrus\b",
            r"\bg14\s+oled\b"
        ],
        "primary_keyword": "Zephyrus G14"
    }
]
