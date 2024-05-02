import os
import zstandard as zstd

def pmtok_compress(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.bfres'):
                bfres_file_path = os.path.join(root, file)
                zst_file_path = bfres_file_path + '.zst'
                with open(bfres_file_path, 'rb') as bfres_file:
                    comp = zstd.ZstdCompressor()
                    with open(zst_file_path, 'wb') as zst_file:
                        comp.copy_stream(bfres_file, zst_file)
                print(f"Compressed {bfres_file_path} to {zst_file_path}")
                os.remove(bfres_file_path)
                print(f"Deleted {bfres_file_path}")
