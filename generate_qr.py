import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from PIL import Image

# ── CONFIG ──────────────────────────────────────────────────────────────────
# Replace this URL with wherever you host margaret_gitonga.html
# e.g. on GitHub Pages, a web server, Google Drive public link, etc.
# URL = "https://your-link-here.com/margaret_gitonga.html"
URL = "https://github.com/morismutuma/margaret-gitonga"


OUTPUT_FILE = "margaret_qr.png"

NAVY = (11, 31, 91)   # matches the card header colour
WHITE = (255, 255, 255)
# ─────────────────────────────────────────────────────────────────────────────

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high — allows logo overlay
    box_size=10,
    border=4,
)

qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    back_color=WHITE,
    fill_color=NAVY,
)

img.save(OUTPUT_FILE)
print(f"QR code saved → {OUTPUT_FILE}")
print(f"Scan it to open: {URL}")