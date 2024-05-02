import os
import zstandard as zstd

def pmtok_extract(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.bfres.zst'):
                zst_file_path = os.path.join(root, file)
                bfres_file_path = os.path.splitext(zst_file_path)[0]
                with open(zst_file_path, 'rb') as zst_file:
                    decomp = zstd.ZstdDecompressor()
                    with open(bfres_file_path, 'wb') as bfres_file:
                        decomp.copy_stream(zst_file, bfres_file)
                print(f"Extracted {zst_file_path} to {bfres_file_path}")
                os.remove(zst_file_path)
