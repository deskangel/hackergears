"""
download_hardware_images.py
Downloads authentic high-resolution product imagery for all 28 HackerGear hardware items
from official vendor CDNs and Wikimedia Commons.
"""

import os
import time
import urllib.request

IMAGE_SOURCES = {
    # Keyboards
    "kinesis-advantage": "https://upload.wikimedia.org/wikipedia/commons/6/63/Kinesis_Advantage_360_Wired.jpg",
    "zsa-moonlander": "https://assets.zsa.io/cdn-cgi/image/width=1200,quality=95,format=auto/images/@moonlander/legacy/2-two-halves.webp",
    "zsa-voyager": "https://assets.zsa.io/cdn-cgi/image/width=1200,quality=95,format=auto/images/@voyager/board/b-us-2.webp",
    "hhkb-professional": "https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b7/HHKB_Pro_Hybrid_Type-S.jpg/960px-HHKB_Pro_Hybrid_Type-S.jpg",
    "keychron-q-series": "https://www.keychron.com/cdn/shop/products/Keychron-Q1-75-percent-QMK-Custom-Mechanical-Keyboard-version-2-barebone-black.jpg",
    "ergodox-ez": "https://ergodox-ez.com/cdn-cgi/image/width=1200,quality=85,format=auto/images/home/home-01.webp",
    "glove80": "https://www.moergo.com/cdn/shop/files/Hero-3842x2000_1600x.jpg",
    "corne-split": "https://40s.wiki/boards/images/corne.jpg",

    # Mice & Trackballs
    "logitech-mx-master-3s": "https://thumb.wikimedia.org/wikipedia/commons/thumb/c/c8/Logitech_MX_Master_3S_HS04.jpg/960px-Logitech_MX_Master_3S_HS04.jpg",
    "apple-magic-trackpad": "https://thumb.wikimedia.org/wikipedia/commons/thumb/c/c3/Magic_Trackpad_2.jpg/960px-Magic_Trackpad_2.jpg",
    "logitech-mx-vertical-lift": "https://thumb.wikimedia.org/wikipedia/commons/thumb/7/79/Logitech_MX_Vertical_Ergonomic_Mouse.jpg/960px-Logitech_MX_Vertical_Ergonomic_Mouse.jpg",
    "kensington-slimblade-expert": "https://thumb.wikimedia.org/wikipedia/commons/thumb/6/6d/Kensington_Expert_Mouse_Wired_Trackball_64325.jpg/960px-Kensington_Expert_Mouse_Wired_Trackball_64325.jpg",
    "logitech-mx-ergo": "https://resource.logitech.com/w_800,c_limit,q_auto,f_webp/d_transparent.gif/content/dam/logitech/en/products/mice/mx-ergo/gallery/mx-ergo-gallery-01-new.png",

    # Monitors
    "dell-ultrasharp-4k": "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/peripherals/monitors/u-series/u2723qe/media-gallery/monitor-u2723qe-gallery-1.psd?fmt=png-alpha&pscan=auto&scl=1&hei=600&wid=800&qlt=100,1&resMode=sharp2&size=800,600&chrss=full",
    "apple-studio-display": "https://thumb.wikimedia.org/wikipedia/commons/thumb/6/6f/Studio_Display_%282022%29.jpg/960px-Studio_Display_%282022%29.jpg",
    "lg-c3-c4-oled-42": "https://media.us.lg.com/transform/ecomm-PDPGallery-1100x730/57e0f054-6064-4e24-b3b2-c0e80ccb2896/TV-OLED42C3PUA-gallery-01_5000x5000?io=transform:fill,width:800",
    "lg-ultrafine-5k-4k": "https://thumb.wikimedia.org/wikipedia/commons/thumb/4/4e/LG_UltraFine_5K_Display.jpg/960px-LG_UltraFine_5K_Display.jpg",
    "asus-proart-4k": "https://dlcdnwebimgs.asus.com/gain/28581920-41a9-4ea9-a94f-fd6a83eb57fd/w692",

    # Ergonomic Chairs
    "herman-miller-aeron": "https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d3/Aeron_Chair.jpg/960px-Aeron_Chair.jpg",
    "herman-miller-embody": "https://www.hermanmiller.com/content/dam/hmicom/page_assets/products/embody_chairs/mh_prd_ovw_embody_chairs.jpg",
    "steelcase-leap-v2": "https://images.steelcase.com/image/upload/c_fill,q_auto,f_auto,h_656,w_1166/v1673460708/22-0188221.jpg",
    "steelcase-gesture": "https://images.steelcase.com/image/upload/t_masthead_ow/q_auto,f_auto,h_656,w_1166/v1676576724/22-0188228_4x3-e1676576723437.jpg",
    "haworth-fern": "https://www.haworth.com/content/dam/haworth-com/global/products-na/seating/office-chairs/fern-office-chair/hero-carousel/fern-4-whitesweep-haworth.jpg",

    # Laptops
    "apple-macbook-pro-m-series": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/mac-macbook-pro-size-unselect-202610-gallery-1?wid=1200&hei=750&fmt=png-alpha",
    "framework-laptop-13-16": "https://static.frame.work/6ou8q6io9z68ecbjuc0se3qxxbiw",
    "thinkpad-x1-carbon": "https://thumb.wikimedia.org/wikipedia/commons/thumb/4/48/Lenovo_ThinkPad_X1_Carbon_Ultrabook.jpg/960px-Lenovo_ThinkPad_X1_Carbon_Ultrabook.jpg",
    "thinkpad-t-series": "https://thumb.wikimedia.org/wikipedia/commons/thumb/a/ac/ThinkPad_T14.jpg/960px-ThinkPad_T14.jpg",
    "asus-rog-zephyrus-g14": "https://dlcdnwebimgs.asus.com/gain/1596FF79-B299-49DE-8BCF-9ABD2C884429/w800"
}

def main():
    target_dir = os.path.join(os.path.dirname(__file__), "..", "public", "images", "hardware")
    os.makedirs(target_dir, exist_ok=True)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
    }

    print(f"Downloading {len(IMAGE_SOURCES)} product images to {target_dir}...")
    for item_id, url in IMAGE_SOURCES.items():
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read()
                mime = resp.headers.get_content_type()
                ext = 'jpg'
                if 'png' in mime or '.png' in url:
                    ext = 'png'
                elif 'webp' in mime or '.webp' in url:
                    ext = 'webp'
                out_path = os.path.join(target_dir, f"{item_id}.{ext}")
                with open(out_path, 'wb') as f:
                    f.write(content)
                print(f"[OK] {item_id} -> {os.path.basename(out_path)} ({len(content)} bytes)")
            time.sleep(0.3)
        except Exception as e:
            print(f"[FAIL] {item_id}: {e}")

if __name__ == "__main__":
    main()
