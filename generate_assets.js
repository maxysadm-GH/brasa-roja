const sharp = require('sharp');
const path = require('path');
const fs = require('fs');

const BASE_DIR = __dirname;
const ASSETS_DIR = path.join(BASE_DIR, 'Assets');
const SOURCE_LOGO = path.join(BASE_DIR, 'Clean Files', 'Main_Logo_NBG.png');
const SOURCE_ICON = path.join(BASE_DIR, 'Clean Files', 'BR Icon NBG.png');

// Brand colors
const COLORS = {
  white: { r: 255, g: 255, b: 255 },
  cream: { r: 245, g: 239, b: 224 },      // #F5EFE0
  charcoal: { r: 45, g: 45, b: 45 },       // #2D2D2D
  black: { r: 0, g: 0, b: 0 },
  gold: { r: 201, g: 136, b: 43 },         // #C9882B
  red: { r: 198, g: 51, b: 51 },           // #C63333
};

async function ensureDir(dir) {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

async function createWithBackground(inputPath, outputPath, color, size = null) {
  let pipeline = sharp(inputPath);
  const metadata = await sharp(inputPath).metadata();

  const width = size || metadata.width;
  const height = size ? Math.round(size * metadata.height / metadata.width) : metadata.height;

  if (size) {
    pipeline = pipeline.resize(width, height, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } });
  }

  await pipeline
    .flatten({ background: color })
    .png()
    .toFile(outputPath);

  console.log(`Created: ${path.basename(outputPath)}`);
}

async function createTransparent(inputPath, outputPath, size = null) {
  let pipeline = sharp(inputPath);

  if (size) {
    pipeline = pipeline.resize(size, size, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } });
  }

  await pipeline.png().toFile(outputPath);
  console.log(`Created: ${path.basename(outputPath)}`);
}

async function createCircular(inputPath, outputPath, size) {
  const roundedCorners = Buffer.from(
    `<svg><circle cx="${size/2}" cy="${size/2}" r="${size/2}"/></svg>`
  );

  await sharp(inputPath)
    .resize(size, size, { fit: 'cover' })
    .composite([{ input: roundedCorners, blend: 'dest-in' }])
    .png()
    .toFile(outputPath);

  console.log(`Created: ${path.basename(outputPath)}`);
}

async function createPaddedSquare(inputPath, outputPath, size, padding = 0.1) {
  const innerSize = Math.round(size * (1 - padding * 2));
  const offset = Math.round(size * padding);

  const resized = await sharp(inputPath)
    .resize(innerSize, innerSize, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
    .toBuffer();

  await sharp({
    create: {
      width: size,
      height: size,
      channels: 4,
      background: { r: 0, g: 0, b: 0, alpha: 0 }
    }
  })
    .composite([{ input: resized, left: offset, top: offset }])
    .png()
    .toFile(outputPath);

  console.log(`Created: ${path.basename(outputPath)}`);
}

async function createSticker(inputPath, outputPath, diameterInches, dpi = 300) {
  const pixels = Math.round(diameterInches * dpi);
  await createCircular(inputPath, outputPath, pixels);
}

async function main() {
  console.log('=== Generating Brasa Roja Assets ===\n');

  // === LOGO_FULL ===
  console.log('--- Logo Full Variants ---');
  const logoFullDir = path.join(ASSETS_DIR, 'Logo_Full');
  await ensureDir(logoFullDir);

  await createTransparent(SOURCE_LOGO, path.join(logoFullDir, 'Logo_Transparent.png'));
  await createWithBackground(SOURCE_LOGO, path.join(logoFullDir, 'Logo_White_BG.png'), COLORS.white);
  await createWithBackground(SOURCE_LOGO, path.join(logoFullDir, 'Logo_Cream_BG.png'), COLORS.cream);
  await createWithBackground(SOURCE_LOGO, path.join(logoFullDir, 'Logo_Charcoal_BG.png'), COLORS.charcoal);
  await createWithBackground(SOURCE_LOGO, path.join(logoFullDir, 'Logo_Black_BG.png'), COLORS.black);

  // === LOGO_ICON ===
  console.log('\n--- Logo Icon Variants ---');
  const logoIconDir = path.join(ASSETS_DIR, 'Logo_Icon');
  await ensureDir(logoIconDir);

  await createTransparent(SOURCE_ICON, path.join(logoIconDir, 'Icon_Transparent.png'));
  await createWithBackground(SOURCE_ICON, path.join(logoIconDir, 'Icon_White_BG.png'), COLORS.white);
  await createWithBackground(SOURCE_ICON, path.join(logoIconDir, 'Icon_Cream_BG.png'), COLORS.cream);
  await createWithBackground(SOURCE_ICON, path.join(logoIconDir, 'Icon_Charcoal_BG.png'), COLORS.charcoal);
  await createWithBackground(SOURCE_ICON, path.join(logoIconDir, 'Icon_Black_BG.png'), COLORS.black);
  await createCircular(SOURCE_ICON, path.join(logoIconDir, 'Icon_Circle_512.png'), 512);
  await createCircular(SOURCE_ICON, path.join(logoIconDir, 'Icon_Circle_180.png'), 180);
  await createPaddedSquare(SOURCE_ICON, path.join(logoIconDir, 'Icon_Square_1024.png'), 1024);

  // === STICKERS (300dpi) ===
  console.log('\n--- Stickers (300dpi print-ready) ---');
  const stickersDir = path.join(ASSETS_DIR, 'Stickers');
  await ensureDir(stickersDir);

  // 3" diameter stickers with logo
  await createSticker(SOURCE_LOGO, path.join(stickersDir, 'Sticker_3in_Transparent.png'), 3, 300);

  // Create stickers with backgrounds
  const sticker3inSize = 3 * 300; // 900px
  const tempSticker = path.join(stickersDir, '_temp_sticker.png');

  // First resize the logo, then create circular versions with backgrounds
  await sharp(SOURCE_LOGO).resize(sticker3inSize, sticker3inSize, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 }}).png().toFile(tempSticker);

  for (const [name, color] of Object.entries({ White: COLORS.white, Cream: COLORS.cream, Charcoal: COLORS.charcoal, Black: COLORS.black })) {
    const roundedCorners = Buffer.from(`<svg><circle cx="${sticker3inSize/2}" cy="${sticker3inSize/2}" r="${sticker3inSize/2}"/></svg>`);
    await sharp(tempSticker)
      .flatten({ background: color })
      .composite([{ input: roundedCorners, blend: 'dest-in' }])
      .png()
      .toFile(path.join(stickersDir, `Sticker_3in_${name}.png`));
    console.log(`Created: Sticker_3in_${name}.png`);
  }

  // 2" icon stickers
  await createSticker(SOURCE_ICON, path.join(stickersDir, 'Sticker_Icon_2in.png'), 2, 300);
  // 1" icon stickers
  await createSticker(SOURCE_ICON, path.join(stickersDir, 'Sticker_Icon_1in.png'), 1, 300);

  // Cleanup temp file
  if (fs.existsSync(tempSticker)) fs.unlinkSync(tempSticker);

  // === APPAREL ===
  console.log('\n--- Apparel (Embroidery-optimized) ---');
  const apparelLightDir = path.join(ASSETS_DIR, 'Apparel', 'Light_Garment');
  const apparelDarkDir = path.join(ASSETS_DIR, 'Apparel', 'Dark_Garment');
  const apparelSimpleDir = path.join(ASSETS_DIR, 'Apparel', 'Simplified');
  await ensureDir(apparelLightDir);
  await ensureDir(apparelDarkDir);
  await ensureDir(apparelSimpleDir);

  // Light garment (dark logo on transparent)
  const logo35in = Math.round(3.5 * 300); // 1050px
  const icon25in = Math.round(2.5 * 300); // 750px

  await createTransparent(SOURCE_LOGO, path.join(apparelLightDir, 'Logo_3.5in.png'), logo35in);
  await createTransparent(SOURCE_ICON, path.join(apparelLightDir, 'Icon_2.5in.png'), icon25in);

  // Dark garment (same files, usage context differs)
  await createTransparent(SOURCE_LOGO, path.join(apparelDarkDir, 'Logo_3.5in.png'), logo35in);
  await createTransparent(SOURCE_ICON, path.join(apparelDarkDir, 'Icon_2.5in.png'), icon25in);

  // Simplified (smaller, for under 2" embroidery)
  const icon2in = Math.round(2 * 300); // 600px
  await createTransparent(SOURCE_ICON, path.join(apparelSimpleDir, 'Icon_Simple.png'), icon2in);

  // === PACKAGING ===
  console.log('\n--- Packaging (Print production) ---');
  const packagingDir = path.join(ASSETS_DIR, 'Packaging');
  await ensureDir(packagingDir);

  // High-res versions for print (300dpi)
  await createTransparent(SOURCE_LOGO, path.join(packagingDir, 'Logo_CMYK_300dpi.png'), 3000);
  await createTransparent(SOURCE_ICON, path.join(packagingDir, 'Icon_CMYK_300dpi.png'), 1500);

  // Black stamp version (for embossing)
  await sharp(SOURCE_ICON)
    .resize(600, 600, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
    .grayscale()
    .png()
    .toFile(path.join(packagingDir, 'Stamp_Icon_Black.png'));
  console.log('Created: Stamp_Icon_Black.png');

  // Gold foil version
  await sharp(SOURCE_LOGO)
    .resize(1500, 1500, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
    .png()
    .toFile(path.join(packagingDir, 'Foil_Logo_Gold.png'));
  console.log('Created: Foil_Logo_Gold.png');

  // === DIGITAL ===
  console.log('\n--- Digital (Web assets) ---');
  const digitalDir = path.join(ASSETS_DIR, 'Digital');
  await ensureDir(digitalDir);

  // Favicons
  await createPaddedSquare(SOURCE_ICON, path.join(digitalDir, 'Favicon_32.png'), 32, 0.1);
  await createPaddedSquare(SOURCE_ICON, path.join(digitalDir, 'Favicon_16.png'), 16, 0.1);

  // Apple Touch Icon
  await createPaddedSquare(SOURCE_ICON, path.join(digitalDir, 'Apple_Touch_180.png'), 180, 0.1);

  // OG Image (1200x630)
  const ogWidth = 1200;
  const ogHeight = 630;
  const logoHeight = Math.round(ogHeight * 0.6);

  const logoForOg = await sharp(SOURCE_LOGO)
    .resize({ height: logoHeight, fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
    .toBuffer();

  const logoMeta = await sharp(logoForOg).metadata();
  const leftOffset = Math.round((ogWidth - logoMeta.width) / 2);
  const topOffset = Math.round((ogHeight - logoMeta.height) / 2);

  await sharp({
    create: {
      width: ogWidth,
      height: ogHeight,
      channels: 4,
      background: COLORS.charcoal
    }
  })
    .composite([{ input: logoForOg, left: leftOffset, top: topOffset }])
    .png()
    .toFile(path.join(digitalDir, 'OG_Image_1200x630.png'));
  console.log('Created: OG_Image_1200x630.png');

  // Email Logo
  await createPaddedSquare(SOURCE_ICON, path.join(digitalDir, 'Email_Logo_80.png'), 80, 0.05);

  // Header Logo (200px wide)
  await sharp(SOURCE_LOGO)
    .resize(200, null, { fit: 'contain' })
    .png()
    .toFile(path.join(digitalDir, 'Header_Logo_200w.png'));
  console.log('Created: Header_Logo_200w.png');

  console.log('\n=== Asset Generation Complete! ===');
}

main().catch(console.error);
